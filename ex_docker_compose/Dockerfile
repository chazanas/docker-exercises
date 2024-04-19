FROM python:3.12-slim

RUN pip install --upgrade pip
RUN pip install django

RUN mkdir project
RUN mkdir project/app
COPY source project/app
WORKDIR project/app

CMD ["python", "manage.py", "runserver"]