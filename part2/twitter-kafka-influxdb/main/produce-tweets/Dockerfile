FROM python:3.8-alpine3.11
LABEL maintainer="Ravi Byakod rbyakod@gmail.com"

RUN apk update && apk add build-base
RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /produce-tweets
COPY . .

RUN pip install -r requirements.txt

# EXPOSE 8000
# HEALTHCHECK CMD xxx

CMD ["python", "run.py"]