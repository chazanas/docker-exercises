FROM python:3.12-slim

RUN pip install --upgrade pip
RUN pip install django

RUN mkdir project
RUN mkdir project/src
COPY src project/src
WORKDIR project/src

CMD ["python", "manage.py", "runserver"]