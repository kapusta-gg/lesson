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


@blueprint.route("/api/jobs", method=["POST"])
def create_job():
    if not request.json:
        return jsonify({"error": "No json file"})
    if not all([key in request.json for key in ["team_leader", "job", "work_size", "collaborators"]]):
        return jsonify({"error": "No keys"})
    db_sess = db_session.create_session()
    job = Jobs(
        id=request.json["id"],
        team_leader=request.json["team_leader "],
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"],
        start_date=request.json["start_date"],
        end_date=request.json["end_date"],
        is_finished=request.json["is_finished"]
    )

    db_sess.add(job)
    db_sess.commit()
    return jsonify({"ok": "Everything is ok"})