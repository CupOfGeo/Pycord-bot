FROM python:3.10-slim
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8080
CMD python small-flask-server.py
