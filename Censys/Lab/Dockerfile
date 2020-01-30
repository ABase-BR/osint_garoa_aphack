FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install censys
ENTRYPOINT ["python3","script-censys.py"]
