import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


browser_protocol = 'https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/browser_protocol.json'
js_protocol = 'https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/js_protocol.json'

browser = json.loads(urlopen(browser_protocol).read())
js = json.loads(urlopen(js_protocol).read())

browser['domains'] += js['domains']
protocol = json.dumps(browser, indent=4)

with open('cproto/resources/protocol.json', 'w') as f:
    f.write(protocol)
