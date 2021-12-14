# CRIME INVESTIGATION

To run the application first run:

`docker-compose up -d`

Then execute:

`docker-compose exec -it <id of the container above> bash`

This will log you in to the docker container where the django application is up and running. What you want to do is run migrations and create a superuser to be able to log in to the admin panel. To accomplish that run following commands while you are inside the bash shell of the container created above:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

Now you should be able to log in on http://localhost:8000/admin by entering your username and password that you have set up by executing above command.
