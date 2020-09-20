FROM python:3.7

MAINTAINER dingya tunogya@qq.com

ENV PYTHONUNBUFFERED 1

RUN echo \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\
    > /etc/apt/sources.list

RUN mkdir /Blockchain

WORKDIR /Blockchain

RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD requirements.txt /Blockchain/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

ADD . /Blockchain/