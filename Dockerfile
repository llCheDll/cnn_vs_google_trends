FROM python:3

ENV PYHTONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r src/.meta/packages