FROM ubuntu:latest
RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive

ADD . /hide
WORKDIR /hide

RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install -y python3.11 python3.11-dev
RUN apt-get install -y python3-pip
RUN unlink /usr/bin/python3
RUN ln -s /usr/bin/python3.11 /usr/bin/python3

RUN pip3 install aiohttp
RUN pip3 freeze > /hide/requirements.txt

RUN apt install -y git

EXPOSE 80
ENTRYPOINT ["/hide/entrypoint.sh"]
# CMD tail -f /dev/null
