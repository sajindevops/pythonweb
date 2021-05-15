FROM centos:7
ARG user
ARG pass
ARG server
MAINTAINER devops
RUN yum install -y https://repo.ius.io/ius-release-el7.rpm && \
yum install -y python36u python36u-libs python36u-devel python36u-pip mariadb-devel gcc
COPY requirements.txt /opt
RUN pip3 install -r /opt/requirements.txt
LABEL environment=prod \
      type=web
ENV DBUSER=${user}
ENV DBPASSWORD=${pass}
ENV DBSERVER=${server}
EXPOSE 9000
COPY maindir /opt/maindir
WORKDIR /opt/maindir
RUN chmod a+x start.sh
CMD ["/opt/maindir/start.sh"]