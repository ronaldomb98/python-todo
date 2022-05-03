# TODO Project
The idea for this project is set up a basic Python web application to excute TODO Actions

## Stack
- Python
- Flask
- SQL3

## Running locally
Create virtual env 
```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install -r requirements.txt
```

Export global environments
```
export FLASK_APP=main.py
export FLASK_ENV=development
```

Create Database
```
python3 ./database/init_db.py
```

Run project
```
flask run
```

## export Dependencies
Export dependencies
```
python3 -m pip freeze
```