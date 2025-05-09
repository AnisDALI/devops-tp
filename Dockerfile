FROM python:3.9

COPY hello-devops/ /app
WORKDIR /app

RUN pip install -r requirements.txt && pip install flake8 pytest

CMD ["pytest"]
