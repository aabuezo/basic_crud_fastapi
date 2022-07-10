# Simple CRUD with fastapi and MySQL

Based on the course of FastAPI from Ashutosh Pawar in udemy.

To get this project up and running, you first need to download this repo and create a virtual environment:
```
$ virtualenv venv
$ source venv/bin/activate
```

Then install required packages:
```
$ pip install -r requirements.txt
```

Complete example.ini and docker-compose.yml with your personal preferred data. Rename example.ini to config.ini.
Then, you can execute the following commands to get a MySQL DB from docker:
```
$ cd config
config$ docker-compose up
```

To run the API, execute the following command from this directory:
```
$ python -m uvicorn main:app
```