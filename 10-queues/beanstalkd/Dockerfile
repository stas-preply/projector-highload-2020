FROM alpine:3.13.1

WORKDIR /project

COPY ./binlog ./binlog

RUN apk add --no-cache wget make alpine-sdk
RUN wget https://github.com/beanstalkd/beanstalkd/archive/master.zip \
    && unzip master \
    && mv ./beanstalkd-master/* ./ \
    && rm -rf beanstalkd-master \
    && rm -rf master.zip \
    && make


# Uncomment the line below according to the way you want to launch the beanstalkd.
# -b saves messages on disc.
#CMD ["./beanstalkd", "-b", "/project/binlog"]
CMD ["./beanstalkd"]