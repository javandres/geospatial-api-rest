FROM ubuntu:16.04

LABEL Llactalab -Universida de Cuenca - "jgarcia@ubicacuenca.com"

RUN apt -y update &&\
    apt -y install python3 python3-pip

RUN python3 -m pip install --upgrade pip

RUN apt -y update &&\
    apt install -y nginx supervisor

#install all python modules
ADD requirements.txt /
RUN pip3 install --upgrade pip && \
    python3 -m pip install -r requirements.txt

# nginx 
RUN rm /etc/nginx/sites-enabled/default
ADD ./src/nginx_flask_proxy.conf /etc/nginx/sites-enabled/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# supervisor log
RUN mkdir -p /var/log/supervisor

ENTRYPOINT ["/usr/bin/supervisord"]
