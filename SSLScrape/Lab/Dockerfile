FROM python:2.7.17-stretch

WORKDIR /root
ADD . .
RUN pip install python-masscan
RUN pip install ndg-httpsclient
RUN pip install requests
RUN apt-get update
RUN apt-get install masscan -y

ENTRYPOINT ["python","sslScrape.py"]
