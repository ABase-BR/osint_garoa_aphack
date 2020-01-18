FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install shodan
ENTRYPOINT ["python3","shodan-recon.py"]
