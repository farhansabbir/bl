FROM python:3.10

WORKDIR /app/
COPY requirements add.py /app/
EXPOSE 3000

#RUN apt update
RUN python -m venv venv
RUN pip install -r requirements
RUN . /app/venv/bin/./activate
ENTRYPOINT [ "python", "add.py" ]

