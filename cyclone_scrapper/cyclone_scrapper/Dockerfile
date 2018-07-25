FROM ubuntu
MAINTAINER Ritesh Kumar Agrahari <ritesh.nus>



RUN apt-get update -y

# Install system dependencies
RUN apt-get install -y autoconf \
                       build-essential \
                       curl \
                       git \
                       vim-tiny

# Python dependencies
RUN apt-get install -y python \
                       python-dev \
                       python-distribute \
                       python-pip \
                       ipython

# Scrapy dependencies
RUN apt-get install -y libffi-dev \
                       libssl-dev \
                       libtool \
                       libxml2 \
                       libxml2-dev \
                       libxslt1.1 

# Add the dependencies to the container and install the python dependencies
RUN pip install scrapy
RUN pip install pymysql
RUN pip install sqlalchemy

RUN mkdir cyclone_scrapper
COPY . cyclone_scrapper/ 
WORKDIR cyclone_scrapper/

RUN scrapy crawl cyclone_scrapper