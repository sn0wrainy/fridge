FROM python:3

ADD . /fridge
WORKDIR /fridge

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
