FROM nginx:1.7
MAINTAINER Lukas Martinelli <me@lukasmartinelli.ch>

# install confd
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install curl && \
    curl -o /usr/bin/confd -L https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 && \
    chmod 755 /usr/bin/confd

# configure confd
RUN mkdir -p /etc/confd/{conf.d,templates}
COPY conf.d /etc/confd/conf.d
COPY templates /etc/confd/templates
COPY confd-watch /usr/local/bin/confd-watch
RUN chmod 755 /usr/local/bin/confd-watch

# purge nginx
RUN rm /etc/nginx/conf.d/*.conf

CMD /usr/local/bin/confd-watch
