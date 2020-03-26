FROM ubuntu:19.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update 
RUN apt-get install -y git-core python curl
RUN apt-get install -y python-subprocess32 python-tk
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN python -m pip install matplotlib pandas
RUN git clone https://github.com/kwraight/textCharacter.git

CMD "bash"
