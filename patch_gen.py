import re

font_link = (
    '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans'
    ':wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">'
)

with open(r'd:\PF Ass\pf-assistant-legal\generator.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the <link rel="stylesheet" href=...css/style.css... with new block
old_pattern = r'  <link rel="stylesheet" href="\{rel\}css/style\.css(?:\?v=\d+)?">(\s*  <link rel="icon")'
new_block = (
    '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  ' + font_link + '\n'
    '  <link rel="stylesheet" href="{rel}css/style.css?v=5">\n'
    r'\1'
)

new_c, n = re.subn(old_pattern, new_block, c)
print(f"Replacements made: {n}")

if n == 0:
    # Show context
    idx = c.find('css/style.css')
    print("Not found. Context:", repr(c[max(0,idx-30):idx+120]))
else:
    with open(r'd:\PF Ass\pf-assistant-legal\generator.py', 'w', encoding='utf-8') as f:
        f.write(new_c)
    print("generator.py updated successfully!")
