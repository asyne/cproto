FROM ubuntu:latest

# Install utilities
RUN apt-get update --fix-missing && apt-get -y upgrade &&\
  apt-get install -y sudo curl wget unzip git python3 python3-pip

# Install Chrome for Ubuntu
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - &&\
  sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' &&\
  sudo apt-get update &&\
  sudo apt-get install -y google-chrome-stable

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
