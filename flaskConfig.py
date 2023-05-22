# Import packages
## Import Basic Packages
import logging
## For Logging to file
logging.basicConfig(filename='../logs/wideavr-flaskRecord.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

## Import Services Server Packages
from flask import Flask, request, abort, jsonify, g, render_template, Response, redirect, url_for, flash
from flask_cors import CORS
import json

class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = 'the quick brown fox jumps over the lazy dog'

app = Flask(__name__)

cors = CORS(app)
app.config.from_object(__name__+'.ConfigClass')


# Error Handler
@app.errorhandler(400)
def bad_request(e):
    return json.dumps({"status" : "error",
                       "code" : 400,
                       "message" : "Bad request"})

@app.errorhandler(401)
def unauthorized(e):
    return json.dumps({"status" : "error",
                        "code" : 401,
                        "message" : "Unauthorized"})

@app.errorhandler(403)
def forbidden(e):
    return json.dumps({"status" : "error",
                       "code" : 403,
                       "message" : "Forbidden"})

@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"status" : "error",
                        "code" : 404,
                        "message" : "Not Found"})

@app.errorhandler(405)
def method_not_allowed(e):
    return json.dumps({"status" : "error",
                       "code" : 405,
                       "message" : "Method Not Allowed"})

@app.errorhandler(500)
def internal_server_error(e):
    return json.dumps({"status" : "error",
                       "code" : 500,
                       "message" : "Internal Server Error"})
# End of Error Handler