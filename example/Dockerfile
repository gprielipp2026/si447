FROM ubuntu

# everything runs as root
RUN apt update && \
    apt install -y apache2

RUN mkdir -p /var/run/apache2 /var/lock/apache2 /var/log/apache2

EXPOSE 8080

CMD ["apachectl", "-D", "FOREGROUND"]

