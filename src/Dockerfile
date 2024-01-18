FROM python:3

EXPOSE 8000

WORKDIR /usr/study/src
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .