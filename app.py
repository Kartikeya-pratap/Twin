import os

try:
    from google import genai
    from google.genai import types
    HAVE_GENAI = True
except Exception:
    genai = None
    types = None
    HAVE_GENAI = False
    print("google-genai not installed — running in fallback mode.", flush=True)

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
    print("gradio not installed; run: pip install -r requirements.txt", flush=True)

load_dotenv(override=True)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
API_KEY    = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if API_KEY and HAVE_GENAI:
    gemini_client = genai.Client(api_key=API_KEY)
else:
    gemini_client = None
    if not API_KEY:
        print("No API key found — running in offline fallback mode.", flush=True)

QUOTA_HINTS   = ("RESOURCE_EXHAUSTED", "429", "QUOTA", "RATE_LIMIT")
UNAVAIL_HINTS = ("UNAVAILABLE", "TEMPORARILY UNAVAILABLE", "HIGH DEMAND")


def is_gemini_problem(exc):
    text = str(exc).upper()
    return any(h in text for h in QUOTA_HINTS + UNAVAIL_HINTS)


def chat(message, history):
    if not gemini_client:
        return build_fallback_reply(message, history)
    try:
        session = gemini_client.chats.create(
            model=MODEL_NAME,
            history=to_gemini_history(history),
            config=types.GenerateContentConfig(
                system_instruction=TWIN_SYSTEM_PROMPT,
                tools=gemini_tools,
            ),
        )
        response = session.send_message(message)
        while response.function_calls:
            results  = handle_tool_calls(response.function_calls)
            response = session.send_message(results)
        return response.text
    except Exception as exc:
        print(f"Gemini error: {exc}", flush=True)
        if is_gemini_problem(exc):
            record_unknown_question(message)
        return build_fallback_reply(message, history)


if __name__ == "__main__":
    if gr is None:
        print("Cannot launch — gradio not installed.", flush=True)
    else:
        port = int(os.environ.get("PORT", 7860))

        theme = gr.themes.Base(
            primary_hue="violet",
            secondary_hue="cyan",
            neutral_hue="slate",
            font=(gr.themes.GoogleFont("Inter"),),
            font_mono=(gr.themes.GoogleFont("JetBrains Mono"),),
        )

        chatbot = gr.Chatbot(
            show_label=False,
            height=460,
            placeholder="Ask me about my background, skills, or projects...",
        )

        textbox = gr.Textbox(
            placeholder="Type your question here...",
            container=False,
            scale=7,
        )

        demo = gr.ChatInterface(
            fn=chat,
            chatbot=chatbot,
            textbox=textbox,
            examples=EXAMPLES,
            title="Digital Twin",
            description="Ask me anything about my background, skills, and career.",
        )

        demo.launch(
            theme=theme,
            css=CSS,
            js=JS,
            server_name="0.0.0.0",
            server_port=port,
            share=False,
            debug=False,
        )