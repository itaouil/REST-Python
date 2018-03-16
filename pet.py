#!/usr/bin/python

# Modules
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the pet page."

@app.route("/list", methods=["GET"])
def petList():
    return "This will return the pet list."

@app.route("/update/<int:pet_id>", methods=["POST"])
def petUpdate(pet_id):
    return "This will update the a pet entry with ID: " + pet_id

@app.errorhandler(404)
def page_not_found(error):
    return "It seems like you entered the wrong url."
