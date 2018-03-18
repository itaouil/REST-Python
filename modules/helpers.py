#!/usr/bin/python

import json

def createResponse(app, status, data):
    return app.response_class (
               status = status,
               response = json.dumps(data, indent=4, default=str),
               mimetype = 'application/json'
           )
