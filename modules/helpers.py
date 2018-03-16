#!/usr/bin/python

import json

def createResponse(app, data):
    return app.response_class (
               status = 200,
               response = json.dumps(data),
               mimetype = 'application/json'
           )
