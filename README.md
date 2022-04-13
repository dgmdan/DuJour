# DuJour

 "It's the soup of the day."

DuJour is a Django web app designed to collect lunch orders around the office.


## Tech Stack
* Django (3.2 LTS)
* Python (3.8)
* nginx
* sqlite3


## Documentation
Django Documentation - https://docs.djangoproject.com/en/1.8/

Python Documentation - https://www.python.org/doc/

nginx Documentation - http://wiki.nginx.org/Main

sqlite Documentation - https://www.sqlite.org/docs.html


## Setting up dev environment
* Install Python 3.7
* Create a venv for this project.
On Windows:

Add to your PATH: ```C:\Python34\Tools\Scripts;C:\PythonEnvs\DuJour```

Then run this in a command prompt:
```
mkdir C:\PythonEnvs
./pyvenv.py C:\PythonEnvs\DuJour
```
Now whenever you want to use this venv, run ```C:\PythonEnvs\dujour\Scripts\activate.bat``` in your command prompt. Any PIP installs/uninstall you run will be local to this venv.

Linux users: figure it out yourself and put the commands here!

For Ubuntu, one thing you'll have to do is install these packages:
```
sudo apt-get install python3-dev freetds-dev
```
* Change to this repo's directory
* Install dependencies: ```pip install -r requirements.txt```
* Create database: ```./manage.py migrate```
* Run server: ```./manage.py runserver```
