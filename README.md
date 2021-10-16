# djangoDB_flights
# Commands used in database django apps

#Migration = database
#After a model is created in models.py, run this command to make a migration commade for django or apply new changes
python manage.py makemigrations
#To apply:
python manage.py migrate

#Open console to run python commands on the project
python manage.py shell

##Python commands for sql

#Insert data to db
from <app>.models import <class>
f = <class>(<members>)
f.save()

#Select all
<class>.objects.all()
