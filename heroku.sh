#!/bin/bash
git add -A .
git commit -m "modificaciones en Heroku"
git push heroku master

# heroku run python manage.py migrate --settings=config.settings-heroku
# heroku run python manage.py createsuperuser --settings=config.settings-heroku
# heroku run python manage.py makemigrations --settings=config.settings-heroku
# heroku run python manage.py migrate --settings=config.settings-heroku