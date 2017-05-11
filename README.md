## CProto

**CProto** is a Debugging Protocol client that supports Chrome, Chromium and Blink based browsers.
CProto provides you an advanced interface to interact with Headless Chrome instance from your Python code.
It's greatly useful for automated testing, debugging, profiling or even complicated page crawling.

*This project is under development. More updates are coming soon.*

### How does API look like?

CProto interface will be fully compatible with official Chrome Debugging Protocol API.
[API Docs](https://chromedevtools.github.io/devtools-protocol/).

```python

from cproto import CProto

# Create CProto instance & connect to Chrome Headless over CDP
cp = CProto(host='127.0.0.1', port=9222)

# Navigate to https://github.com
cp.Page.navigate(url='https://github.com')

```
