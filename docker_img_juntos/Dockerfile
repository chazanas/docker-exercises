FROM python:3.12-slim

RUN pip install --upgrade pip
RUN pip install pandas

RUN mkdir project
RUN mkdir project/source
COPY ./source project/source
WORKDIR project/source

CMD ["python", "main.py"]