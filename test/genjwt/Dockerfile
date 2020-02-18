FROM debian:buster

RUN apt-get -qq update && apt-get install -y shelltestrunner pipenv

COPY . .
RUN pipenv install
CMD shelltest -D DOMAIN=nginx-subrequest-auth-jwt:8080 -D PREFIX=/ auth.test
