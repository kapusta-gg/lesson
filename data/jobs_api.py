import flask
from flask import jsonify, request, make_response

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


@blueprint.route("/api/jobs", methods=['POST'])
def post_job():
    if not request.json:
        return make_response(jsonify({'Error': 'Empty request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        category=request.json['category'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({"OK": "Data commited"})
