import os
try:
    from google import genai
    from google.genai import types
    from google.genai.errors import ClientError
    HAVE_GENAI = True
except Exception:
    genai = None
    types = None
    ClientError = Exception
    HAVE_GENAI = False
    print(
        "google-genai package not installed — running in fallback mode (no API calls).",
        flush=True,
    )
from context import TWIN_SYSTEM_PROMPT, build_fallback_reply
from tools import gemini_tools, handle_tool_calls, record_unknown_question, to_gemini_history
from styles import CSS, JS, EXAMPLES
try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*args, **kwargs):
        return None
try:
    import gradio as gr
except Exception:
    gr = None
    print(
        "gradio not installed; to run the UI install gradio or run `pip install -r requirements.txt`.",
        flush=True,
    )

load_dotenv(override=True)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if API_KEY:
    gemini_client = genai.Client(api_key=API_KEY)
else:
    gemini_client = None
    print(
        "No GEMINI_API_KEY / GOOGLE_API_KEY found — running in offline fallback mode.",
        flush=True,
    )

QUOTA_ERROR_HINTS = ("RESOURCE_EXHAUSTED", "429", "quota", "RATE_LIMIT")
UNAVAILABLE_HINTS = ("UNAVAILABLE", "temporarily unavailable", "high demand")


def is_gemini_problem(exc):
    exc_text = str(exc).upper()
    return any(hint in exc_text for hint in QUOTA_ERROR_HINTS + UNAVAILABLE_HINTS)


def chat(message, history):
    if not gemini_client:
        return build_fallback_reply(message, history)

    try:
        chat_session = gemini_client.chats.create(
            model=MODEL_NAME,
            history=to_gemini_history(history),
            config=types.GenerateContentConfig(
                system_instruction=TWIN_SYSTEM_PROMPT,
                tools=gemini_tools,
            ),
        )
        response = chat_session.send_message(message)
        while response.function_calls:
            tool_results = handle_tool_calls(response.function_calls)
            response = chat_session.send_message(tool_results)
        return response.text
    except Exception as exc:
        print(f"Gemini call failed: {exc}", flush=True)
        if is_gemini_problem(exc):
            record_unknown_question(message)
        return build_fallback_reply(message, history)


if __name__ == "__main__":
    if gr is None:
        print("Cannot start Gradio UI because `gradio` is not installed.", flush=True)
        print("Install dependencies with: pip install -r requirements.txt", flush=True)
    else:
        gr.ChatInterface(
            chat,
            examples=EXAMPLES,
            title="Digital Twin",
            description="Talk to my AI twin about my career",
            chatbot=gr.Chatbot(show_label=False),
        ).launch(css=CSS, js=JS, theme=gr.themes.Base())
