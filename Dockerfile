FROM python:3-onbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir /api_code
WORKDIR /api_code
ADD requirements.txt /api_code/
RUN pip install -r requirements.txt
ADD . /api_code/
