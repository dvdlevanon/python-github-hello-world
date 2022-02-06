FROM python

ENV TEST_GITHUB_TOKEN=

WORKDIR /opt/python-github-hello-world

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD "uvicorn" "main:app" "--host" "0.0.0.0"
