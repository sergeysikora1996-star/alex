import re

with open('css/ukraine-theme.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    '.plan_card, .bonuses_card, .faq_card, .mentor_card, .make-step_card {\n  background-color: var(--card-bg) !important;\n  border-radius: 20px !important;\n  border: 1px solid rgba(0, 87, 183, 0.1) !important;\n  box-shadow: 0 10px 35px rgba(0, 87, 183, 0.05), 0 2px 10px rgba(0, 0, 0, 0.02) !important;\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n  position: relative;\n  overflow: hidden;\n}',
    '.plan_card, .bonuses_card, .faq_card, .make-step_card {\n  background-color: var(--card-bg) !important;\n  border-radius: 20px !important;\n  border: 1px solid rgba(0, 87, 183, 0.1) !important;\n  box-shadow: 0 10px 35px rgba(0, 87, 183, 0.05), 0 2px 10px rgba(0, 0, 0, 0.02) !important;\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n  position: relative;\n  overflow: hidden;\n}\n\n.mentor_card {\n  background-color: var(--card-bg) !important;\n  border-radius: 20px !important;\n  border: 1px solid rgba(0, 87, 183, 0.1) !important;\n  box-shadow: 0 10px 35px rgba(0, 87, 183, 0.05), 0 2px 10px rgba(0, 0, 0, 0.02) !important;\n  transition: transform 0.3s ease, box-shadow 0.3s ease;\n  position: relative;\n  overflow: visible !important;\n}'
)

css = css.replace(
    '.plan_card::before, .bonuses_card::before, .mentor_card::before, .make-step_card::before {\n  content: "";\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 6px;\n  background: linear-gradient(90deg, var(--ua-blue) 0%, var(--ua-yellow) 100%);\n}',
    '.plan_card::before, .bonuses_card::before, .mentor_card::before, .make-step_card::before {\n  content: "";\n  position: absolute;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 6px;\n  background: linear-gradient(90deg, var(--ua-blue) 0%, var(--ua-yellow) 100%);\n  border-top-left-radius: 20px;\n  border-top-right-radius: 20px;\n}'
)

with open('css/ukraine-theme.css', 'w', encoding='utf-8') as f:
    f.write(css)
