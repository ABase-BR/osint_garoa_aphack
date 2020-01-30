FROM python:3-slim-stretch
RUN pip3 install yandex-search
WORKDIR /root
ADD . .
ENTRYPOINT ["python3","yandex-site.py"]
