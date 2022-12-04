FROM python:3.10

WORKDIR /micahbot

COPY src/* /micahbot

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "micahbot.py" ]