#!/usr/bin/python

# Modules
import json
from modules import *
from flask import Flask, jsonify

# Create flask object
app = Flask(__name__)

@app.route("/list", methods=["GET"])
def petList():
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
        return createResponse(app, pet_list)
    else:
        return createResponse(app, "{}")

@app.route("/update/<int:pet_id>", methods=["POST"])
def petUpdate(pet_id):
    """
        Updates a particular pet
        entry with the given ID.

        Arguments:
            int: Pet's ID
            Pet: Pet object
    """
    if request.method == "POST":
        # Parse incoming data into JSON
        data = request.get_json()

        # Get JSON fields
        name = data['name']
        gender = data['gender']
        species = data['species']
        birthday = data['birthday']

        # Build Pet object
        pet = Pet(name, gender, species, birthday)

        # Create database connection
        connection = Database()

        # Fetch pets in the database
        connection.update(pet_id, pet)

    else:
        return createResponse(app, "{}")

@app.errorhandler(404)
def page_not_found(error):
    """
        Returns an empty JSON in
        case of wrong route being
        accessed.

        Returns:
            JSON: Empty JSON response
    """
    return jsonify("It seems like you entered the wrong url.")
