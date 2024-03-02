import flask
from flask import jsonify

from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates', static_folder="static")


@blueprint.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    temp = [item.to_dict() for item in jobs]
    return jsonify({"jobs": temp})