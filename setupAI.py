##################################################################################
## 
## VERSION		:	0.0.1
## DATE			:	07Jan2016
##                				
## USAGE		:	Dockerfile to build scrapy in alpine linux
## Ref [1]		:	https://hub.docker.com/r/trcook/docker-scrapy/~/dockerfile/
## Ref [2]		:	https://github.com/shirk3y/scrapy-docker-alpine/blob/master/Dockerfile
##################################################################################

sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
yum update -y
yum install python-pip -y
yum install python-devel -y
yum install gcc gcc-devel -y
yum install libxml2 libxml2-devel -y
yum install libxslt libxslt-devel -y
yum install openssl openssl-devel -y
yum install libffi libffi-devel -y
pip install lxml
pip install scrapy	