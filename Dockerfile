FROM python:alpine3.17
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5000
ENTRYPOINT [ "python", "./src/app.py" ]