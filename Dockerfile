FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["python", "server/app.py"]
