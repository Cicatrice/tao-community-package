FROM fedora:latest
RUN dnf update -y
RUN dnf install -y phing git php-fpm php-apcu php-mysqlnd php-pgsql php-redis php-curl php-redis php-gd php-imagick php-mbstring php-zip mariadb httpd
RUN dnf install -y ImageMagick supervisor openssh-server
ADD tao-community*rpm  /releases/
RUN dnf install -y /releases/tao-community*rpm
RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisord.d/supervisord.conf

### Enable SSH access for debugging
RUN /usr/bin/ssh-keygen -A
RUN echo 'root:tao' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

EXPOSE 22 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]
