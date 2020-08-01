FROM python:3.8-alpine

RUN pip install requests

WORKDIR /app
ENV PATH=/app/bin:$PATH

ADD config.json .
ADD ./bin ./bin
ADD ./src ./src

ENTRYPOINT ["bin/teams-msg"]
