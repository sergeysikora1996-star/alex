import re

with open('css/instagram-business-a31ab8.webflow.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace(
    '  .mentor_image {\n    width: 88vw;',
    '  .mentor_image {\n    width: 75vw;'
)

css = css.replace(
    '  .mentor_image.is-size {\n    width: 85vw;',
    '  .mentor_image.is-size {\n    width: 72vw;'
)

css = css.replace(
    '  .mentor_image-wrap {\n    border-radius: 4.44vw;\n    position: absolute;\n    top: auto;\n    bottom: 0%;\n    left: auto;\n    right: -10vw;\n    overflow: hidden;\n  }',
    '  .mentor_image-wrap {\n    border-radius: 4.44vw;\n    position: absolute;\n    top: auto;\n    bottom: 0%;\n    left: auto;\n    right: -10vw;\n    overflow: hidden;\n    z-index: 1;\n  }'
)

with open('css/instagram-business-a31ab8.webflow.css', 'w', encoding='utf-8') as f:
    f.write(css)
