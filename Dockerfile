FROM python:3.9.1-buster
WORKDIR /project
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "project/wsgi.py"]