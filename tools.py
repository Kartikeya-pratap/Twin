import json
import os
try:
    import requests
    HAVE_REQUESTS = True
except Exception:
    requests = None
    HAVE_REQUESTS = False
try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*args, **kwargs):
        return None

# Try to import `types` from google.genai. If it's not installed (local/no-deps
# environment), provide a minimal shim so the app can run in fallback mode
# without raising ImportError.
try:
    from google.genai import types
except Exception:
    class _ShimTypes:
        class Type:
            STRING = "string"
            INTEGER = "integer"
            OBJECT = "object"

        class Schema:
            def __init__(self, type=None, description="", properties=None, required=None, **kwargs):
                self.type = type
                self.description = description
                self.properties = properties or {}
                self.required = required or []

        class FunctionDeclaration:
            def __init__(self, name, description, parameters=None):
                self.name = name
                self.description = description
                self.parameters = parameters

        class Tool:
            def __init__(self, function_declarations=None):
                self.function_declarations = function_declarations or []

        class Part:
            def __init__(self, text=None):
                self.text = text

            @staticmethod
            def from_function_response(name, response):
                return {"name": name, "response": response}

        class Content:
            def __init__(self, role, parts=None):
                self.role = role
                self.parts = parts or []

    types = _ShimTypes()

load_dotenv(override=True)

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

pushover_url = "https://api.pushover.net/1/messages.json"


def push(text):
    if not pushover_token or not pushover_user:
        print("Pushover credentials not configured; skipping push notification.", flush=True)
        return
    if not HAVE_REQUESTS:
        print("`requests` not installed; cannot send push notification.", flush=True)
        return
    try:
        requests.post(
            pushover_url,
            data={
                "token": pushover_token,
                "user": pushover_user,
                "message": text,
            },
            timeout=5,
        )
    except Exception as exc:
        print(f"Failed to send pushover notification: {exc}", flush=True)


def record_user_details(email, name="Name not provided", notes="not provided"):
    push(f"Recording interest from {name} with email {email} and notes {notes}")
    return "OK"


def record_unknown_question(question):
    push(f"Recording {question} asked that I couldn't answer")
    return "OK"


record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address of this user"},
            "name": {"type": "string", "description": "The user's name, if they provided it"},
            "notes": {
                "type": "string",
                "description": "Any additional info about the conversation that's worth recording to give context",
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The question that couldn't be answered"},
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json},
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}


def build_gemini_tools(tool_definitions):
    gemini_funcs = []
    for tool_def in tool_definitions:
        func_def = tool_def["function"]
        props = func_def["parameters"]["properties"]
        required = func_def["parameters"].get("required", [])

        gemini_props = {}
        for prop_name, prop_schema in props.items():
            prop_type = types.Type.STRING
            if prop_schema["type"] == "integer":
                prop_type = types.Type.INTEGER
            gemini_props[prop_name] = types.Schema(
                type=prop_type,
                description=prop_schema.get("description", ""),
            )

        gemini_funcs.append(
            types.FunctionDeclaration(
                name=func_def["name"],
                description=func_def["description"],
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties=gemini_props,
                    required=required,
                ),
            )
        )
    return [types.Tool(function_declarations=gemini_funcs)]


gemini_tools = build_gemini_tools(tools)


def handle_tool_calls(function_calls):
    results = []
    for call in function_calls:
        tool_name = call.name
        arguments = dict(call.args)
        print(f"Tool called: {tool_name}", flush=True)
        tool = tool_map.get(tool_name)
        result = tool(**arguments) if tool else "Unknown tool: " + tool_name
        response_dict = result if isinstance(result, dict) else {"result": result}
        results.append(types.Part.from_function_response(name=tool_name, response=response_dict))
    return results


def to_gemini_history(history):
    gemini_history = []
    for msg in history:
        if isinstance(msg, dict):
            role = msg.get("role")
            content = msg.get("content")
            if role == "assistant":
                role = "model"
            elif role == "system":
                continue
            if content is None:
                continue
            gemini_history.append(
                types.Content(role=role, parts=[types.Part(text=str(content))])
            )
        elif isinstance(msg, (tuple, list)) and len(msg) >= 2:
            user_content, assistant_content = msg[0], msg[1]
            if user_content is not None:
                gemini_history.append(
                    types.Content(role="user", parts=[types.Part(text=str(user_content))])
                )
            if assistant_content is not None:
                gemini_history.append(
                    types.Content(role="model", parts=[types.Part(text=str(assistant_content))])
                )
    return gemini_history
