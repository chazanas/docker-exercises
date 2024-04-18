FROM python:3.12-slim

RUN mkdir project
RUN mkdir project/source
COPY ./source project/source
WORKDIR project/source

RUN pip install --upgrade pip
RUN pip install pandas

CMD ["python", "main.py"]