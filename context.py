linkedin = ""
try:
    from pypdf import PdfReader

    try:
        reader = PdfReader("linkedin.pdf")
        for page in reader.pages:
            text = page.extract_text()
            if text:
                linkedin += text
    except Exception:
        print("Could not read linkedin.pdf; continuing without LinkedIn text", flush=True)
        linkedin = ""
except Exception:
    print("pypdf not installed; skipping linkedin.pdf parsing.", flush=True)
    linkedin = ""

try:
    with open("summary.txt", "r", encoding="utf-8") as f:
        summary = f.read()
except Exception:
    print("summary.txt not found or unreadable; using empty summary.", flush=True)
    summary = ""

SUMMARY_TEXT = summary.strip()
LINKEDIN_TEXT = linkedin.strip()

TWIN_SYSTEM_PROMPT = f"""

# Your role

You are a digital twin running on a website, chatting with visitors of the website.
You represent the person who's website you are on.
You answer questions related to their career, background, skills and experience.

Here are the details of the person you are representing:

{summary}

If asked, you explain clearly that you are an AI that is the digital twin of this person.

# Context

Here is a summary of the person's LinkedIn profile so that you can answer questions:

{linkedin}

# Rules

Engage with the user. Be professional and engaging, as if talking to a potential client or future employer who came across the website.
Only answer questions related to career, background, skills and experience.
If the user asks about something unrelated, then steer the conversation back to professional topics.

Always stay in character as the digital twin of the person you are representing. Represent the person.

If the user would like to get in touch, then ask for their email, and use your tool to record their email for follow-up.

IMPORTANT:
If you don't know the answer, use your tool to record the question, and then tell the user that you don't know. Never make up an answer.

Use styling (in markdown, no code blocks) to make the response more engaging and easy to read.
""".strip()


def build_fallback_reply(message, history=None):
    question = (message or "").strip().lower()
    if not question:
        return "I’m here to talk about my background, skills, and career interests. Ask me about my experience or projects."

    if any(term in question for term in ["email", "contact", "reach out", "connect", "hire"]):
        return "I’d be happy to connect. Please share your email and I’ll help capture your interest."

    if any(term in question for term in ["project", "building", "currently", "working on", "now"]):
        return "Right now I’m focused on building strong fundamentals in software engineering and AI while working on practical projects, hackathons, and fast-paced learning."

    if any(term in question for term in ["background", "experience", "about you", "who are you", "introduce"]):
        return (
            "I’m Kartikeya Pratap Singh Parihar, a first-year B.Tech student in Computer Science with AI & ML. "
            "I’m driven by learning quickly, solving problems from first principles, and turning ideas into practical projects."
        )

    if any(term in question for term in ["skill", "skills", "strength", "strong at"]):
        return "My strengths are fast learning, problem solving, AI/ML fundamentals, software engineering basics, and turning ideas into practical projects."

    return (
        "I’m here to talk about my background, experience, skills, and career interests. "
        "I can share more about my studies, projects, and goals—what would you like to know?"
    )
