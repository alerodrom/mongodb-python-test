 FROM python:3.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 COPY docker-entrypoint.sh /docker-entrypoint.sh
 RUN chmod +x /docker-entrypoint.sh
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/

 ENTRYPOINT ["/docker-entrypoint.sh"]