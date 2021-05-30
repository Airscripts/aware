source airenv/bin/activate
python3 manage.py runserver 0.0.0.0:8080
su - postgres
psql
\du
\q
https://medium.com/@hdsingh13/deploying-django-app-on-heroku-with-postgres-as-backend-b2f3194e8a43