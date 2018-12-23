FROM python:3.6.4

WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
EXPOSE 8888
CMD ["python", "dummyapp.py"]