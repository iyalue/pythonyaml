FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir Flask

COPY script.py .

CMD [ "python", "./script.py" ]
