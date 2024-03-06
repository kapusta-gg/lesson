import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates', static_folder="static")

