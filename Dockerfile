FROM 3.8.0a2-alpine3.9

ADD src:/src
ADD requirements.txt:requirements.txt

RUN pip instal -R requirements.txt

CHDIR src

CMD [ "python", "./rss_download.py" ]