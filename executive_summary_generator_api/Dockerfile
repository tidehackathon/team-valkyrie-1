FROM python:3.9-slim-buster

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "service:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]