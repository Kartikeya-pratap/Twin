"""Styling constants for the digital twin Gradio app."""

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

:root {
  --bg:       #0a0a0a;
  --surface:  #111111;
  --surface2: #1a1a1a;
  --border:   #222222;
  --text:     #ededed;
  --muted:    #666666;
  --accent:   #ffffff;
  --user-bg:  #1a1a1a;
  --bot-bg:   #111111;
}

body:not(.dark) {
  --bg:       #fafafa;
  --surface:  #ffffff;
  --surface2: #f4f4f4;
  --border:   #e5e5e5;
  --text:     #111111;
  --muted:    #888888;
  --accent:   #111111;
  --user-bg:  #f0f0f0;
  --bot-bg:   #ffffff;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--bg) !important; }

.gradio-container {
  background:  var(--bg) !important;
  color:       var(--text) !important;
  font-family: 'Inter', system-ui, sans-serif !important;
  max-width:   780px !important;
  margin:      0 auto !important;
  padding:     48px 28px 64px !important;
  width:       100% !important;
}
.gradio-container * { box-sizing: border-box; min-width: 0; }

/* ── Title ── */
.gradio-container h1 {
  font-size:      20px !important;
  font-weight:    500 !important;
  letter-spacing: -0.01em !important;
  color:          var(--text) !important;
  margin:         0 0 6px !important;
  padding:        0 !important;
  border:         none !important;
  background:     none !important;
  text-align:     left !important;
}

/* ── Description ── */
.gradio-container .prose p {
  font-size:   13px !important;
  color:       var(--muted) !important;
  margin:      0 0 28px !important;
  font-weight: 400 !important;
}

/* ── Blocks ── */
.block, .form {
  background: transparent !important;
  box-shadow: none !important;
  border:     none !important;
}

/* ── Chatbot frame ── */
.chatbot, .chatbot.block {
  background:    var(--surface) !important;
  border:        1px solid var(--border) !important;
  border-radius: 8px !important;
  min-height:    460px !important;
  box-shadow:    none !important;
}
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container { display: none !important; }

.chatbot .placeholder,
.chatbot .placeholder * {
  color:     var(--muted) !important;
  font-size: 13px !important;
}

/* ── Message wrappers ── */
.message-row,
.message-wrap,
.bubble-wrap {
  background: transparent !important;
  border:     none !important;
  box-shadow: none !important;
}

/* ── Base bubble ── */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border:        none !important;
  box-shadow:    none !important;
  border-radius: 6px !important;
  padding:       10px 14px !important;
  font-size:     14px !important;
  line-height:   1.7 !important;
  font-weight:   400 !important;
}

/* ── User bubble ── */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {
  background: var(--user-bg) !important;
  color:      var(--text) !important;
}

/* ── Assistant bubble ── */
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  background:  var(--bot-bg) !important;
  color:       var(--text) !important;
  border-left: 2px solid var(--border) !important;
}

/* Strip double border from nested bubbles */
.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble {
  border-left: none !important;
}

/* ── Paragraphs inside bubbles ── */
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p {
  font-size:   14px !important;
  line-height: 1.7 !important;
  margin:      0 0 8px !important;
  color:       inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child { margin-bottom: 0 !important; }

.message-row .message a,
.message-row .bubble a {
  color:           var(--text) !important;
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* ── Input ── */
textarea, input[type="text"] {
  background:    var(--surface) !important;
  border:        1px solid var(--border) !important;
  border-radius: 6px !important;
  color:         var(--text) !important;
  font-family:   'Inter', system-ui, sans-serif !important;
  font-size:     14px !important;
  font-weight:   400 !important;
  padding:       12px 16px !important;
  min-height:    48px !important;
  transition:    border-color 0.15s;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--text) !important;
  outline:      none !important;
  box-shadow:   none !important;
}
textarea::placeholder, input::placeholder {
  color:       var(--muted) !important;
  font-weight: 400 !important;
}

/* ── Buttons ── */
button {
  font-family:     'Inter', system-ui, sans-serif !important;
  font-size:       13px !important;
  font-weight:     500 !important;
  letter-spacing:  0 !important;
  text-transform:  none !important;
  border:          1px solid var(--border) !important;
  border-radius:   6px !important;
  background:      transparent !important;
  color:           var(--muted) !important;
  padding:         0 16px !important;
  min-height:      48px !important;
  cursor:          pointer;
  display:         inline-flex !important;
  align-items:     center !important;
  justify-content: center !important;
  transition:      color 0.15s, border-color 0.15s;
}
button:hover {
  color:        var(--text) !important;
  border-color: var(--text) !important;
  background:   transparent !important;
}

/* Primary button */
button.primary, button[variant="primary"],
button.submit, button.submit-button,
.submit-button, button.lg.primary {
  background:   var(--text) !important;
  border-color: var(--text) !important;
  color:        var(--bg) !important;
}
button.primary:hover, button.submit:hover,
.submit-button:hover, button.lg.primary:hover {
  background:   var(--muted) !important;
  border-color: var(--muted) !important;
  color:        var(--bg) !important;
}
button.submit svg, .submit-button svg,
button.primary svg, button[variant="primary"] svg {
  width:  17px !important;
  height: 17px !important;
  color:  var(--bg) !important;
}

/* ── Example chips ── */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding:    0 !important;
  margin-top: 16px !important;
}
.examples table, .examples-table {
  background: transparent !important;
  border:     none !important;
}
.examples button, .example, [data-testid="examples"] button {
  background:     transparent !important;
  border:         1px solid var(--border) !important;
  border-radius:  6px !important;
  color:          var(--muted) !important;
  font-family:    'Inter', system-ui, sans-serif !important;
  font-size:      13px !important;
  font-weight:    400 !important;
  padding:        8px 14px !important;
  text-align:     left !important;
  min-height:     0 !important;
  align-self:     auto !important;
  display:        inline-block !important;
  transition:     color 0.15s, border-color 0.15s;
}
.examples button:hover, .example:hover,
[data-testid="examples"] button:hover {
  color:        var(--text) !important;
  border-color: var(--text) !important;
  background:   transparent !important;
}

/* ── Icon buttons ── */
.icon-button, .chatbot .icon-button {
  background: transparent !important;
  border:     none !important;
  color:      var(--border) !important;
  min-height: 0 !important;
  padding:    4px !important;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color:      var(--muted) !important;
  background: transparent !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar       { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }

::selection { background: var(--text); color: var(--bg); }

@media (max-width: 640px) {
  .gradio-container { padding: 24px 16px 48px !important; }
  .gradio-container h1 { font-size: 18px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusLast = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusLast, 400);

  const watch = (area) => {
    if (area.dataset.watched) return;
    area.dataset.watched = '1';
    let prev = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const now = area.disabled || area.readOnly;
      if (prev && !now) setTimeout(focusLast, 100);
      prev = now;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watch);
  setTimeout(scan, 600);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""