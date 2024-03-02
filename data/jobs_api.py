import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates', static_folder="static")


@blueprint.route("/api/jobs", method=["GET"])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    temp = [item.to_dict() for item in jobs]
    return jsonify({"jobs": temp})


@blueprint.route("/api/jobs/<int:job_id>", method=["GET"])
def get_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({"error": "Bad request"})
    return jsonify({"job": job.to_dict()})