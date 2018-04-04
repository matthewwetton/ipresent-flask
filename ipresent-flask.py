#!/usr/bin/env python

# Title       : ipresent-flask
# Filename    : ipresent-flask.sh
# Version     : 1.0
# Created     : 2018-04-04
# Modified    : 2018-04-04
# Author      : Matthew Wetton
# Description : A basic flask application, part of project ipresent. 
#
# Code souce 2018-04-04 "http://flask.pocoo.org/docs/0.12/quickstart/"
#

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
