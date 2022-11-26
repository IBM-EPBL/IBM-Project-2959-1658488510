From python:3.6
WORKDIR /app
ADD . /app
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install ibm_db
RUN python3 -m pip install bcrypt
RUN python3 -m pip install sendgrid
EXPOSE 5000
CMD ["python","app.py"]