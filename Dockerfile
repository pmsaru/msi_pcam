FROM python:3.8
WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt

COPY ./run.sh /
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
