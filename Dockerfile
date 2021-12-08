FROM python:3.10.0-slim

COPY . /testsrc
WORKDIR /testsrc
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "test.py" ]