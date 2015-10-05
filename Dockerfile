FROM ubuntu:15.04

MAINTAINER John Erwin  "joerwin69@gmail.com"

RUN apt-get update && apt-get -y install python-pip nginx

RUN mkdir -p /opt/shortUrl
ADD requirements.txt /opt/shortUrl/requirements.txt
ADD app /opt/shortUrl/app
ADD run.py /opt/shortUrl/run.py
ADD initialize.py /opt/shortUrl/initialize.py
ADD global_config /opt/shortUrl/global_config
ADD configs/short_url /etc/nginx/sites-available/short_url
RUN pip install -r /opt/shortUrl/requirements.txt
WORKDIR /opt/shortUrl
RUN python initialize.py

EXPOSE 8080

RUN ln -s /etc/nginx/sites-available/short_url /etc/nginx/sites-enabled/short_url


CMD ["python", "/opt/shortUrl/run.py"]
#ENTRYPOINT ["python", "/opt/shortUrl/run.py"]


