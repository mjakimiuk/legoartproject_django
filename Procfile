web: gunicorn lego_django.wsgi:application --log-file - --log-level debug
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
