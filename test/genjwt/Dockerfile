FROM ubuntu:bionic

RUN apt-get -qq update && apt install -y shelltestrunner \
    software-properties-common
RUN apt-get -qq update && apt install -y software-properties-common \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt install -y python3.8
RUN pip install pipenv

COPY . .
RUN pipenv install
CMD shelltest -D DOMAIN=nginx-auth-jwt:8080 -D PREFIX=/ auth.test
