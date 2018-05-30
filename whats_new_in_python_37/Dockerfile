FROM python:3.7-rc-stretch

ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir jupyter ipdb

VOLUME /data

WORKDIR /data

EXPOSE 8888

ENTRYPOINT jupyter notebook --ip=0.0.0.0 --allow-root --no-browser
