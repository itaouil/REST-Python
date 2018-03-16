#!/usr/bin/python

# Modules
from flask import Flask
from modules.db import Database
from modules.pet import Pet

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

    # Return list of pets
    # TODO: Convert to JSON
    return pet_list

@app.route("/update/<int:pet_id>", methods=["POST"])
def petUpdate(pet_id, pet):
    """
        Updates a particular pet
        entry with the given ID.

        Arguments:
            int: Pet's ID
            Pet: Pet object (with new values)
    """
    # Create database connection
    connection = Database()

    # Fetch pets in the database
    connection.update(pet_id, pet)

@app.errorhandler(404)
def page_not_found(error):
    """
        Returns an empty JSON in
        case of wrong route being
        accessed.

        Returns:
            JSON: Empty JSON response
    """
    return "It seems like you entered the wrong url."
