FROM python:3.8-slim-buster
COPY . /code
WORKDIR /code
ENV FLASK_APP=calc.py
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "calc.py" ]
