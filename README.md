# aws-cli-docker

# aws-cli in docker
* Modified using as base: https://hub.docker.com/r/mesosphere/aws-cli

* docker pull eshnil2000/mesosphere-aws-boto3-cli-pandas

* or build on your own using dockerfile
* nano ~/.bash_profile
```
export AWS_ACCESS_KEY_ID="xxx"
export AWS_SECRET_ACCESS_KEY="xxx"
export AWS_DEFAULT_REGION="us-west-1"

alias aws='docker run --rm -t $(tty &>/dev/null && echo "-i") -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" -e "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" -e "AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}" -v "$(pwd):/project" mesosphere/aws-cli'
```
source ~/.bash_profile

To call manually, and override aws executable entrypoint: 
```
docker run -it --entrypoint "/bin/sh" --rm -v ~/Nilesh/aws/aws_project/:/project -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" -e "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" -e "AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}" mesosphere/aws-cli
```
to build own dockerfile:
```
docker build -t mesosphere/aws-cli .
```
====Dockerfile====
```
FROM python:3-alpine
RUN apk -v --update add \
        python3 \
        py-pip \
        groff \
        less \
        mailcap \
        py3-numpy \
        build-base \
        && \
    pip3 install --upgrade boto3 awscli s3cmd==2.0.1 python-magic pandas logger sensible && \
    apk -v --purge del py-pip  && \
    rm /var/cache/apk/*
VOLUME /root/.aws
VOLUME /project
WORKDIR /project
ENTRYPOINT ["aws"]
```
docker volumes on Mac:
```
screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
cd /var/lib/docker/volumes
```
to exit screen: Ctrl a+k

* To run test.py, execute from inside the container:
```python3.7 test.py 
```
* or 
```./test.py
