FROM python:3.5

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /workdir
ADD . /workdir

CMD ["pytest"]
