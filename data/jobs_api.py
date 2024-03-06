import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates', static_folder="static")

@blueprint.route("/api/jobs", methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    temp = [item.to_dict(only=("team_leader", "job", "work_size", "collaborators", "is_finished")) for item in jobs]
    return jsonify({"jobs": temp})


@blueprint.route("/api/jobs/<int:job_id>", methods=['GET'])
def get_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({"Error": "Data not found"})
    return jsonify({"job": job.to_dict(only=("team_leader", "job", "work_size", "collaborators", "is_finished"))})

