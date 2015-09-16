[![Build Status](https://travis-ci.org/nihalpd/DuJour.svg?branch=develop)](https://travis-ci.org/nihalpd/DuJour)
[![Coverage Status](https://coveralls.io/repos/nihalpd/DuJour/badge.svg?branch=develop&service=github)](https://coveralls.io/github/nihalpd/DuJour?branch=develop)
# DuJour

 "It's the soup of the day."

DuJour is a Web app designed to collect lunch orders around the office.



## Tech Stack
Django (1.8)
Python (3.4)
nginx
sqlite3


## Documentation
Django Documentation - https://docs.djangoproject.com/en/1.8/

Python Documentation - https://www.python.org/doc/

nginx Documentation - http://wiki.nginx.org/Main

sqlite Documentation - https://www.sqlite.org/docs.html


## Setting up dev environment
* Install Python
* Install virtualenvwrapper and create a virtualenv for this project:
```
pip install virtualenvwrapper
export WORKON_HOME=~/envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv dujour
```
* Change to this repo's directory
* Install dependencies: ```pip install -r requirements.txt```
* Create database: ```./manage.py migrate```
* Run server: ```./manage.py runserver```
