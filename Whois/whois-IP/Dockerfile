FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install requests
ENTRYPOINT ["python3","whois-ip.py"]
