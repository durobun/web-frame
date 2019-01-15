# pull official base image 
FROM python:3.7-alpine 

MAINTAINER juskim <tojskim72@gmail.com>

# set environment varibles 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

# set work directory 
WORKDIR /usr/src/aweb 

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

#install djangorestframework
RUN pip install djangorestframework \
    && pip install markdown \
    && pip install django-filter

# install dependencies 
RUN pip install --upgrade pip 
RUN pip install pipenv 
COPY ./Pipfile /usr/src/aweb/Pipfile 
RUN pipenv install --skip-lock --system --dev 

# copy entrypoint.sh 
COPY ./entrypoint.sh /usr/src/aweb/entrypoint.sh

RUN chmod 755 /usr/src/aweb/entrypoint.sh

# copy project 
COPY . /usr/src/aweb/ 

# run entrypoint.sh 
ENTRYPOINT ["/usr/src/aweb/entrypoint.sh"] 