FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y python3.8 python3-pip && \
    pip install pipenv

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

COPY . /app

WORKDIR /app

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
