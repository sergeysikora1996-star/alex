import re

with open('css/ukraine-theme.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    'body {\n  background-color: var(--bg-light);\n  background-image: radial-gradient(circle at top left, rgba(0,87,183,0.03) 0%, transparent 40%),\n                    radial-gradient(circle at bottom right, rgba(255,215,0,0.04) 0%, transparent 40%);\n  color: #1a202c;\n}',
    'body {\n  background-color: var(--bg-light);\n  background-image: radial-gradient(circle at top left, rgba(0,87,183,0.03) 0%, transparent 40%),\n                    radial-gradient(circle at bottom right, rgba(255,215,0,0.04) 0%, transparent 40%);\n  color: #1a202c;\n  overflow-x: hidden;\n}'
)

with open('css/ukraine-theme.css', 'w', encoding='utf-8') as f:
    f.write(css)
