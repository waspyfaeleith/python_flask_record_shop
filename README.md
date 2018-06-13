# Python Flask Record Shop

Record Store web app implemented in Python with Flask, connecting to a PostgreSQL database

You will need to have python3 and PostgreSQL installed.

You will also need to install psycopg2 (the Python PostgreSQL driver) and Flask(a lightweight web framework for Python)

To install:

```
$ pip3 install psycopg2
$ pip3 install Flask
```

You will also need to create a PostgreSQL database called `record_store`:

```
$ createdb record_store
```

To set up the tables:

```
$ psql -d record_store -f record_store.sql
```

To run the app:
```
$ python3 app.py
```

OR

```
$ FLASK_APP=app.py flask run
```

To see the app running open a web browser and go to `http://localhost:5000/`
