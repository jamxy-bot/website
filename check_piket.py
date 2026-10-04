with open('index.html', encoding='utf-8') as f:
    h = f.read()

import re
piket = re.search(r'<section id="piket".*?</section>', h, re.DOTALL)
if piket:
    print(piket.group(0))
