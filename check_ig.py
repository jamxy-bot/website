with open('index.html', encoding='utf-8') as f:
    h = f.read()

import re
matches = re.finditer(r'href="https?://(?:www\.)?instagram\.com/[^"]+"', h)
for m in matches:
    print(m.group(0))
