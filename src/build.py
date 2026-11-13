"""Baut PubQuiz.html: bettet Schriften und Logo in src/src.html ein.
Aufruf (im Projektordner): python3 src/build.py
"""
import re, base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, 'assets')
OUT = os.path.join(HERE, '..', 'PubQuiz.html')

css = open(os.path.join(A, 'fonts', 'fonts.css'), encoding='utf-8').read()
blocks = re.findall(r'/\* (latin(?:-ext)?) \*/\s*@font-face\s*\{(.*?)\}', css, re.S)
seen, faces = set(), []
for sub, body in blocks:
    fam = re.search(r"font-family: '([^']+)'", body).group(1)
    url = re.search(r'url\((https://[^)]+)\)', body).group(1)
    ur = re.search(r'unicode-range: ([^;]+);', body).group(1)
    if (fam, sub) in seen:
        continue
    seen.add((fam, sub))
    data = open(os.path.join(A, 'fonts', url.rsplit('/', 1)[1]), 'rb').read()
    b = base64.b64encode(data).decode()
    faces.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:100 900;font-display:swap;"
                 f"src:url(data:font/woff2;base64,{b}) format('woff2');unicode-range:{ur}}}")
logo = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(A, 'logo.webp'), 'rb').read()).decode()
html = open(os.path.join(HERE, 'src.html'), encoding='utf-8').read()
html = html.replace('{{FONTS}}', '\n'.join(faces)).replace('{{LOGO}}', logo)
open(OUT, 'w', encoding='utf-8').write(html)
print('geschrieben:', os.path.normpath(OUT), len(html), 'Bytes')
