#!/usr/bin/python

import json

def createResponse(app, data):
    return app.response_class (
               status = 200,
               response = json.dumps(data, indent=4, default=str),
               mimetype = 'application/json'
           )
