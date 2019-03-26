FROM python:3.8.0a2-alpine3.9

COPY src /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD [ "python", "./rss_download.py" ]