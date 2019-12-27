# project/server/main/views.py


import redis
from rq import Queue, Connection
from flask import render_template, Blueprint, jsonify, request, current_app

from project.server.main.tasks import detect
from deepgeo import ProcessorFactory

main_blueprint = Blueprint("main", __name__,)


@main_blueprint.route("/", methods=["GET"])
def home():
    models = current_app.engine.get_added_model()
    return render_template("main/home.html",models=models)

@main_blueprint.route("/task", methods=["POST","GET"])
def run_task():
    # print("Posted Data : {}".format(data))
    task_type = request.form["uri"]
    model_name = request.form["model_name"]
    file_type = request.form["file_type"]
#    print(file_type)
#    print(model_name)
#    print(task_type)
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        processor = ProcessorFactory.create(engine=current_app.engine,type_name=file_type)
        task = q.enqueue(detect,processor=processor,alias_model_name=model_name,url=task_type)
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id()
            }
        }    
    return jsonify(response_object), 202
   


@main_blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    with Connection(redis.from_url(current_app.config["REDIS_URL"])):
        q = Queue()
        task = q.fetch_job(task_id)
        q_len = len(q)
    if task:
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
                "message": "Task queued at {} {}jobs queued".format(task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S'),q_len)
            },
        }
    else:
        response_object = {"status": "error"}
    return jsonify(response_object)

