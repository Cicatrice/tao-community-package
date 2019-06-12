FROM ubuntu:bionic
RUN apt update
ENV TZ=Europe/Luxembourg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt install -y phing git libswitch-perl libdatetime-perl imagemagick php-fpm php-apcu php-mysql php-pgsql php-redis php-curl php-redis php-gd php-imagick php-mbstring php-zip php-fdomdocument phing mysql-client postgresql-client redis-tools apache2
RUN apt install -y supervisor openssh-server
ADD tao-community*deb  /releases/
RUN dpkg -i /releases/tao-community*deb
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/php /var/run/sshd /var/log/supervisor
RUN a2dissite 000-default

### Enable SSH access for debugging
RUN echo 'root:tao' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

EXPOSE 22 80
CMD ["/usr/bin/supervisord"]
