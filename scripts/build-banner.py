"""Wrap the original animated GIF with a greeting and locally embedded icons."""
from pathlib import Path
import base64
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
def data(path, mime):
    return f'data:{mime};base64,' + base64.b64encode((root / path).read_bytes()).decode()

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
<title id="title">Good to meet you!</title>
<desc id="desc">Animated banner with Node.js, TypeScript, JavaScript, then Vue.js and React icons.</desc>
<image width="1200" height="400" preserveAspectRatio="xMidYMid slice" xlink:href="{data('assets/banner.gif', 'image/gif')}"/>
<rect width="1200" height="400" fill="#10291e" opacity=".35"/>
<rect x="365" y="99" width="470" height="202" rx="24" fill="#173d2b" opacity=".85"/>
<text x="600" y="168" text-anchor="middle" fill="#f7f0d5" font-family="Arial, Helvetica, sans-serif" font-size="42" font-weight="700">Good to meet you!</text>
<path d="M574 191h52" stroke="#e9bd55" stroke-width="3" stroke-linecap="round"/>
<image x="428" y="218" width="184" height="56" xlink:href="{data('assets/icons/backend.svg', 'image/svg+xml')}"/>
<image x="644" y="218" width="120" height="56" xlink:href="{data('assets/icons/frontend.svg', 'image/svg+xml')}"/>
</svg>'''
ET.fromstring(svg)
(root / 'assets/profile-banner.svg').write_text(svg)
print('Built self-contained banner SVG.')
