import re

with open('css/ukraine-theme.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    'overflow: visible !important;\n}',
    'overflow: visible !important;\n  z-index: 10;\n}'
)

with open('css/ukraine-theme.css', 'w', encoding='utf-8') as f:
    f.write(css)
