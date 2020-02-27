FROM ubuntu:bionic

# python3 - utf8 local
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get -qq update && apt install -y shelltestrunner \
    software-properties-common
RUN apt-get -qq update && apt install -y software-properties-common \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt install -y python3.8 python3-pip
RUN pip3 install pipenv

COPY . .
RUN pipenv install
CMD shelltest -D DOMAIN=nginx-auth-jwt:8080 -D PREFIX=/ auth.test
