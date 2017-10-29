# CProto

**CProto** is a Debugging Protocol client that supports Chrome, Chromium and Blink based browsers.

**CProto** provides you an advanced interface to interact with Chrome (or another supported browser) instance from your Python code.
It's greatly useful for automated testing, debugging, profiling or even complicated page crawling.

- [Getting Started](#getting-started)
- [API Docs](#api-docs)
- [Roadmap](#roadmap)
- [Chrome Headless](#chrome-headless)
- [Examples](#examples)

*This project is under development. More updates are coming soon.*

## Getting Started

#### Installing CProto

Python *2.7* or *3.3+* is required to install **CProto**.

Install the latest version using pip:

```sh
$ pip install cproto
```

#### Running Chrome in Debug mode

Option 1: [Run Chrome in Docker](#chrome-headless), also in Headless mode.

Option 2: Run Chrome on host machine:

```sh
# «chrome» should point to your installation of Chrome
chrome --remote-debugging-port=9222 "about:blank"

# If you haven't created alias for Chrome yet, you could set it on MacOS like that:
# For Chrome
alias chrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# For Chrome Canary
alias chrome-canary="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
# For Chromium
alias chromium="/Applications/Chromium.app/Contents/MacOS/Chromium"
```

## API Docs

[Chrome Debugging Protocol documentation.](https://chromedevtools.github.io/devtools-protocol/)

**CProto** complies to official Chrome Debugging Protocol, which implicates CProto's interface has the same API as Chrome Debugging Protocol. Consider this example:

```python
from cproto import CProto


# Print event's response and close CProto connection
def on_load(response):
    print(response)
    cp.close()


# Create CProto instance and connect to a browser over CDP
cp = CProto(host='127.0.0.1', port=9222)
# Enable Page domain events
cp.Page.enable()
# Adds Page callback that's fired after is loaded
cp.Page.loadEventFired = on_load
# Navigate browser to Github
cp.Page.navigate(url='https://github.com')
```

In this example [Page Domain API](https://chromedevtools.github.io/devtools-protocol/tot/Page/) was used to navigate to any arbitrary URL. There are a whole bunch of other methods and events available for each Domain, you could browse all of them on the CDP documentation website.

## Roadmap

- [x] Domains support
- [x] Methods support
- [x] Events support

Under consideration:
- Asynchronous I/O support using **asyncio**

## Headless Chrome in Docker

You could use [Docker](https://www.docker.com/) to run **CProto** with Chrome Headless mode on any major OS via *command line interface*.

```sh
# Clone the repository
$ git clone git@github.com:asyne/cproto.git

# Build Docker image for Chrome Headless
$ docker build -t chrome-headless cproto

# Run Docker Chrome Headless mode container with port 9222 being proxied to the host machine
$ docker run --rm -it --cap-add=SYS_ADMIN -p 9222:9222 chrome-headless

# That's all here. Chrome Debugging interface is now up and listening for connections.
# You could check it out by opening this link in your browser – http://localhost:9222.
```

## Examples

Check out [examples directory](https://github.com/asyne/cproto/tree/master/examples).

- [Take a Screenshot](https://github.com/asyne/cproto/blob/master/examples/screenshot.py)

*More examples are coming soon.*
