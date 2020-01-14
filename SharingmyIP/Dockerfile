FROM python:alpine
WORKDIR /root
COPY . .
RUN pip3 install requests
RUN pip3 install bs4
ENTRYPOINT ["python3","script-sharingmyip.py"]
