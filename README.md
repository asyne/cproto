## CProto

**CProto** is a Debugging Protocol client that supports Chrome, Chromium and Blink based browsers.

**CProto** provides you an advanced interface to interact with Headless Chrome instance from your Python code.
It's greatly useful for automated testing, debugging, profiling or even complicated page crawling.

*This project is under development. More updates are coming soon.*

### How does API look like?

**CProto** interface is fully compatible with [official Chrome Debugging Protocol API](https://chromedevtools.github.io/devtools-protocol/).

```python

from cproto import CProto

# Create CProto instance & connect to Chrome Headless over CDP
cp = CProto(host='127.0.0.1', port=9222)

# Navigate to https://github.com
cp.Page.navigate(url='https://github.com')

```

### Running Chrome Headless with Docker

While Chrome Headless mode is only available for Linux (MacOS coming soon), you could use [Docker](https://www.docker.com/) to run Headless mode on any major OS.

```sh
# Build Docker image for Chrome Headless:
$ docker build -t headless .

# Run Docker Chrome Headless mode container with port 9222 being proxied to the host machine:
$ docker run --rm -it --cap-add=SYS_ADMIN -p 9222:9222 headless

# That's all here. Chrome Debugging interface is now listening for connections.
# You could check it out by opening this link in your browser – http://localhost:9222.
```
