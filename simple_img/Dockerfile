FROM python:3.12-slim

RUN pip install --upgrade pip
RUN pip install pandas

COPY ./ ./

CMD ["python", "main.py"]