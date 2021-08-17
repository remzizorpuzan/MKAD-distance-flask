FROM python:3.9.6

LABEL key="remzizorpuzan@outlook.com"

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

CMD [ "python", "./__init__.py" ]