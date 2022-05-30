web: gunicorn quizapp.wsgi.py --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
