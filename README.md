# CProto

**CProto** is a Debugging Protocol client that supports Chrome, Chromium and Blink based browsers.

**CProto** provides you an advanced interface to interact with Headless Chrome instance from your Python code.
It's greatly useful for automated testing, debugging, profiling or even complicated page crawling.

- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Chrome Headless](#chrome-headless)
- [Examples](#examples)

*This project is under development. More updates are coming soon.*

## Getting Started

Python *2.7* or *3.3+* is required to install **CProto**.

Install the latest version using pip:

```sh
$ pip install cproto
```

## Documentation

[Chrome Debugging Protocol documentation.](https://chromedevtools.github.io/devtools-protocol/)

**CProto** complies to official Chrome Debugging Protocol, which implicates CProto's interface has the same API as Chrome Debugging Protocol. Consider this example:

```python
from cproto import CProto

# Create CProto instance and connect to Chrome over CDP
cp = CProto(host='127.0.0.1', port=9222)

# Use Page to navigate to github.com.
cp.Page.navigate(url='https://github.com')

```

As you see, [Page Domain API](https://chromedevtools.github.io/devtools-protocol/tot/Page/) could be used to navigate any arbitrary URL (github in this case). There are a whole bunch of other methods and events available for each Domain, so you could browse all of them in the CDP documentation.

## Chrome Headless

While Chrome Headless mode is only available for Linux (MacOS coming soon), you could use [Docker](https://www.docker.com/) to run Headless mode on any major OS.

```sh
# Build Docker image for Chrome Headless:
$ docker build -t headless .

# Run Docker Chrome Headless mode container with port 9222 being proxied to the host machine:
$ docker run --rm -it --cap-add=SYS_ADMIN -p 9222:9222 headless

# That's all here. Chrome Debugging interface is now listening for connections.
# You could check it out by opening this link in your browser – http://localhost:9222.
```


## Examples

*Examples are coming soon.*
