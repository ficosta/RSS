FROM 3.8.0a2-alpine3.9

ADD src:/src

RUN pip instal -R requirements.txt

CMD [ "python", "./my_script.py" ]