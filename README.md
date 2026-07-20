---
title: twin
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---

Run locally (no billing required)
-------------------------------

To run the app locally without using cloud deploy or paid services, run:

```bash
python app.py
```

Notes:
- If you do not set `GEMINI_API_KEY` or `GOOGLE_API_KEY`, the app will run in a fallback mode and will not call the Gemini API (no billing).
- Avoid using `gradio deploy` or other cloud deploy commands if you want a free local run.
