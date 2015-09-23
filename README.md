[![Build Status](https://travis-ci.org/nihalpd/DuJour.svg?branch=develop)](https://travis-ci.org/nihalpd/DuJour)
[![Coverage Status](https://coveralls.io/repos/nihalpd/DuJour/badge.svg?branch=develop&service=github)](https://coveralls.io/github/nihalpd/DuJour?branch=develop)
# DuJour

 "It's the soup of the day."

DuJour is a Django web app designed to collect lunch orders around the office.

We're in early development so functionality is minimal for now.



## Tech Stack
* Django (1.8.4)
* Python (3.4.2)
* nginx
* sqlite3


## Documentation
Django Documentation - https://docs.djangoproject.com/en/1.8/

Python Documentation - https://www.python.org/doc/

nginx Documentation - http://wiki.nginx.org/Main

sqlite Documentation - https://www.sqlite.org/docs.html


## Setting up dev environment
* Install Python 3.4
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
