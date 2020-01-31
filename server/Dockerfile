FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip3.7 install --upgrade pip
RUN pip3.7 install -r requirements.txt
RUN python3.7 manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "server.wsgi:application"]
