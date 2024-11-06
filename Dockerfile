FROM python:3.12.3

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . . 

CMD ["python", "auth_service/manage.py", "runserver", "0.0.0.0:8000"]