# **REST-Python**

## Installs

Please install flask, flasgger and PyMySQL for the application to run (preferably on your set virtual environment):

```Python
pip install Flask-API && pip install flask-swagger && pip install PyMySQL
```

Clone the repo on your machine:

```Python
cd <your-directory> && git clone https://github.com/itaouil/REST-Python.git
```

## Database model (dump)

A database dump is provided in the dumps folder, create a mysql user using the terminal and run the following command in your terminal to dump the sql content locally on your machine:

```MySQL
mysql -u root -p -h localhost <database_name> < SQLModel.sql
```

## Run

Now that you have installed the required modules, you can run the application by doing the following:

```Python
export FLASK_APP=app.py
flask run
```

The application is now running on port 5000 (by default) and you can access the endpoints. To access the spec of the API access the following URL:

**http://localhost:5000/apidocs/**

## TODO

I spent around 4/5 hours on the task, mostly researching about swagger and how to integrate it into the API, hence there are quite a lot of improvements I would made if this was a production service, mainly:

1. Input validation (maybe using endpoint specs)
2. Handle database exception
3. Write better unit/integration tests (I was limited on the time because of other projects so I mainly used    postman for this one)
4. Better API implementation (maybe using blueprints in FLASK)
