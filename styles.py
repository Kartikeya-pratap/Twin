"""Styling constants for the digital twin Gradio app."""

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap');

:root {
  --bg:        #0e1117;
  --surface:   #181c27;
  --surface2:  #1e2436;
  --border:    #2a3044;
  --border-hi: #3d4a66;
  --text:      #e8eaf0;
  --muted:     #7a8299;
  --accent:    #6c63ff;
  --accent-hi: #8b84ff;
  --teal:      #3ecfcf;
  --r:         8px;
  --r-sm:      5px;
}

body:not(.dark) {
  --bg:        #f0f2f8;
  --surface:   #ffffff;
  --surface2:  #e9ebf4;
  --border:    #d0d4e8;
  --border-hi: #b0b8d4;
  --text:      #1a1e2e;
  --muted:     #6a7090;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--bg) !important; }

.gradio-container {
  background:  var(--bg) !important;
  color:       var(--text) !important;
  font-family: 'Inter', system-ui, sans-serif !important;
  max-width:   860px !important;
  margin:      0 auto !important;
  padding:     36px 24px 56px !important;
  width:       100% !important;
}
.gradio-container * { box-sizing: border-box; min-width: 0; }

.gradio-container h1 {
  font-size:   24px !important;
  font-weight: 700 !important;
  color:       var(--text) !important;
  margin:      0 0 4px !important;
  padding:     0 !important;
  border:      none !important;
  background:  none !important;
  text-align:  left !important;
}
.gradio-container h1::after {
  content:    '';
  display:    block;
  width:      36px;
  height:     3px;
  background: var(--accent);
  border-radius: 2px;
  margin-top: 8px;
}

.block, .form {
  background: transparent !important;
  box-shadow: none !important;
  border:     none !important;
}

.chatbot, .chatbot.block {
  background:    var(--surface) !important;
  border:        1px solid var(--border) !important;
  border-radius: var(--r) !important;
  min-height:    440px !important;
  box-shadow:    0 4px 32px rgba(0,0,0,0.28) !important;
}

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container { display: none !important; }

.message-row,
.message-wrap,
.bubble-wrap {
  background: transparent !important;
  border:     none !important;
  box-shadow: none !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border:        none !important;
  box-shadow:    none !important;
  border-radius: var(--r-sm) !important;
  padding:       10px 14px !important;
  font-size:     14px !important;
  line-height:   1.65 !important;
}

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {
  background: var(--teal) !important;
  color:      #0e1117 !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  background:  var(--surface2) !important;
  color:       var(--text) !important;
  border-left: 3px solid var(--accent) !important;
}

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

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p {
  font-size:   14px !important;
  line-height: 1.65 !important;
  margin:      0 0 8px !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child { margin-bottom: 0 !important; }

.message-row .message a,
.message-row .bubble a { color: var(--accent-hi) !important; text-decoration: underline; }

textarea, input[type="text"] {
  background:    var(--surface) !important;
  border:        1px solid var(--border) !important;
  border-radius: var(--r-sm) !important;
  color:         var(--text) !important;
  font-family:   'Inter', system-ui, sans-serif !important;
  font-size:     14px !important;
  padding:       12px 16px !important;
  min-height:    48px !important;
  transition:    border-color 0.15s, box-shadow 0.15s;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--accent) !important;
  outline:      none !important;
  box-shadow:   0 0 0 2px rgba(108,99,255,0.2) !important;
}
textarea::placeholder, input::placeholder { color: var(--muted) !important; }

button {
  font-family:     'JetBrains Mono', monospace !important;
  font-size:       11px !important;
  font-weight:     600 !important;
  letter-spacing:  0.08em !important;
  text-transform:  uppercase !important;
  border:          1px solid var(--border) !important;
  border-radius:   var(--r-sm) !important;
  background:      transparent !important;
  color:           var(--text) !important;
  padding:         0 18px !important;
  min-height:      48px !important;
  cursor:          pointer;
  display:         inline-flex !important;
  align-items:     center !important;
  justify-content: center !important;
  transition:      border-color 0.15s, color 0.15s, background 0.15s;
}
button:hover {
  border-color: var(--accent) !important;
  color:        var(--accent) !important;
  background:   rgba(108,99,255,0.07) !important;
}

button.primary, button[variant="primary"], button.submit,
button.submit-button, .submit-button, button.lg.primary {
  background:   var(--accent) !important;
  border-color: var(--accent) !important;
  color:        #fff !important;
}
button.primary:hover, button.submit:hover,
.submit-button:hover, button.lg.primary:hover {
  background:   var(--accent-hi) !important;
  border-color: var(--accent-hi) !important;
  color:        #fff !important;
}
button.submit svg, .submit-button svg,
button.primary svg, button[variant="primary"] svg {
  width: 18px !important; height: 18px !important; color: #fff !important;
}

.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding:    0 !important;
  margin-top: 16px !important;
}
.examples table, .examples-table { background: transparent !important; border: none !important; }

.examples button, .example, [data-testid="examples"] button {
  background:     var(--surface) !important;
  border:         1px solid var(--border) !important;
  border-radius:  var(--r-sm) !important;
  color:          var(--muted) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family:    'Inter', system-ui, sans-serif !important;
  font-size:      13px !important;
  font-weight:    400 !important;
  padding:        9px 14px !important;
  min-height:     0 !important;
  align-self:     auto !important;
  display:        inline-block !important;
  transition:     border-color 0.15s, color 0.15s;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--teal) !important;
  color:        var(--teal) !important;
  background:   rgba(62,207,207,0.05) !important;
}

.icon-button, .chatbot .icon-button {
  background: transparent !important;
  border:     none !important;
  color:      var(--muted) !important;
  min-height: 0 !important;
  padding:    4px !important;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color: var(--accent) !important; background: transparent !important;
}

::-webkit-scrollbar       { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border-hi); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

::selection { background: var(--accent); color: #fff; }

@media (max-width: 640px) {
  .gradio-container { padding: 20px 14px 40px !important; }
  .gradio-container h1 { font-size: 20px !important; }
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