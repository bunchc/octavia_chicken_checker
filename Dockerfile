FROM python:3
LABEL maintainer="Cody Bunch <cody.bunch@rackspace.com>"

ENV PS1="\[\e[0;33m\]|> occ <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /src
COPY . /src
RUN mkdir -p /etc/openstack 
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py install
WORKDIR /

CMD ["occ"]
