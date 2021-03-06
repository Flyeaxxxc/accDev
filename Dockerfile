FROM python:3.9

RUN pip install --upgrade pip \
	&& mkdir /app

RUN pip freeze > requirements.txt

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/bot.py
