FROM python:3-alpine
MAINTAINER Enedir, Alex e Guilherme

ARG BUILD_DATE
ARG VCS_REF

# Set labels (see https://microbadger.com/labels)
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/alexjravila/JogoBaixoWebAPI"


RUN mkdir -p /usr/src/www
WORKDIR /usr/src/www

COPY requirements.txt /usr/src/www/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/www

# Expose the Flask port
EXPOSE 5000

CMD [ "python", "run.py" ]