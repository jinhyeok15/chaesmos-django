FROM python:3.9

WORKDIR /

# Add code
ADD ./chaesmos /srv/chaesmos

# Install application requirements
ADD ./config/requirements.txt /srv/chaesmos/

RUN apt-get update
RUN apt-get install -y libpq-dev python-dev
RUN pip3 install -r /srv/chaesmos/requirements.txt

# Add start script
ADD ./config/start.sh /

# Add uWSGI config
ADD ./config/django-uwsgi.ini /etc/uwsgi/django-uwsgi.ini

# Create django user, will own the Django app. This is needed
# because we defined this, in the uwsgi.ini file
RUN adduser --no-create-home --disabled-login --group --system django
RUN chown -R django:django /srv/chaesmos

# Execute start script
CMD ["./start.sh"]
