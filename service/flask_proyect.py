from flask import Flask, request, jsonify, flash, redirect, url_for
from flask_cors import CORS
import logging
import gunicorn

from controler import *

import pdb

app = Flask(__name__)
CORS(app)


@app.route("/")
def welcome():
    """
    This function returns information about the API.

    Args:
        None

    Returns:
        HTML text with a link to the API documentation.
    """
    return """<!DOCTYPE html>
              <html>
              <head>
              <title>ALeRCE Cats Service</title>
              </head>
              <body>
              <h3>Welcome to the Cats Service</h3>
              <p>Documentation can be found
              <a href="https://alerceapi.readthedocs.io/en/latest/catshtm.html">
              here</a>.</p>
              </body>
              </html>"""


@app.route("/conesearch")
def conesearch():
    """
    This function returns the cone search result, it uses an auxiliary
    function to generate the result.

    Args:
        A Request

    Returns:
        The JSON representation of the cone search result for a single catalog.
    """
    return controller_conesearch(request)


@app.route("/conesearch_all")
def conesearch_all():
    """
    This function returns the result of running a cone search over all
    available catalogs. It uses the 'conesearch' function to generate this
    results.

    Args:
        A request

    Returns:
        The JSON representation of the cone search results for all catalogs.
    """
    return controller_conesearch_all(request)


@app.route("/crossmatch")
def crossmatch():
    """
    This function returns the result of running a crossmatch over one catalog.
    It uses an auxiliary function to compute the results.

    Args:
        A request
    Returns:
        The JSON representation of the crossmatch result.
    """
    return controller_crossmatch(request)



@app.route("/crossmatch_all")
def crossmatch_all():
    """
    This function returns the crossmatch result for all catalogs.

    Args:
        A request
    Returns:
        The JSON representation of the crossmatch result for all catalogs.
    """
    return controller_crossmatch_all()





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5001")