FROM python:alpine3.7
COPY . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

