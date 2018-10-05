FROM python:3-alpine

WORKDIR /app
COPY . /app
COPY ./app/web/write_to_sys.py /app

RUN pip install --trusted-host pypi.python.org -r tests/requirements.txt

CMD ["python", "DefaultToUkTime.py"]