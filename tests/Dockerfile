FROM phusion/baseimage:0.9.22

RUN apt install -y python3
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init"]

