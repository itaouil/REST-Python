#!/usr/bin/python

# Modules
import json
from modules import *
from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, request, jsonify

# Create flask object
app = Flask(__name__)
Swagger(app)

@app.route("/list", methods=["GET"])
@swag_from('./specs/list.yml')
def listPets():
    """
        Fetches all entries from
        the database and returns
        them in JSON format.

        Returns:
            JSON: List of pets
    """
    # Create database connection
    connection = Database()

    # Fetch pets in the database
    pet_list = connection.list()

    # Return data if these present
    # otherwise return empty JSON
    if pet_list:
        return createResponse(app, 200, pet_list)
    else:
        return createResponse(app, 404, "{}")

@app.route("/add", methods=["POST"])
@swag_from('./specs/add.yml')
def addPet():
    """
        Fetches all entries from
        the database and returns
        them in JSON format.

        Returns:
            JSON: List of pets
    """
    if request.method == "POST":
        # Parse incoming data into JSON
        data = request.get_json()

        # Get JSON fields
        name     = data['name']
        gender   = data['gender']
        species  = data['species']
        birthday = data['birthday']

        # Build Pet object
        pet = Pet(name, gender, species, birthday)

        # Create database connection
        connection = Database()

        # Fetch pets in the database
        result = connection.add(pet)

        return createResponse(app, 201, "{sucess: True}") if result else createResponse(app, 404, "{sucess: False}")
    else:
        return createResponse(app, "{}")

@app.route("/update", methods=["POST"])
@swag_from('./specs/update.yml')
def updatePet():
    """
        Updates a particular pet
        entry with the given ID.

        Arguments:
            Pet: Pet object
    """
    if request.method == "POST":
        # Parse incoming data into JSON
        data = request.get_json()

        # Get JSON fields
        id       = data['id']
        name     = data['name']
        gender   = data['gender']
        species  = data['species']
        birthday = data['birthday']

        print(id, name, gender, species, birthday)

        # Build Pet object
        pet = Pet(name, gender, species, birthday)

        # Create database connection
        connection = Database()

        # Fetch pets in the database
        result = connection.update(id, pet)

        return createResponse(app, 201, "{sucess: True}") if result else createResponse(app, 404, "{sucess: False}")

@app.errorhandler(404)
def page_not_found(error):
    """
        Returns an empty JSON in
        case of wrong route being
        accessed.

        Returns:
            JSON: Empty JSON response
    """
    return createResponse(app, 404, "{sucess: False, msg: 'It seems like you entered the wrong url.'}")
