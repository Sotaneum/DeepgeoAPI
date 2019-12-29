#-*- coding:utf-8 -*-

from flask import Flask, url_for

app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

@app.route("/task/url=<url>/model_name=<model_name>/file_type=<file_type>", methods=["GET"])
def get_task(url,model_name,file_type):
    pass
    # with Connection(redis.from_url(current_app.config["REDIS_URL"])):
    #     q = Queue()
    #     processor = ProcessorFactory.create(engine=current_app.engine,type_name=file_type)
    #     task = q.enqueue(detect,processor=processor,alias_model_name=model_name,url=url)
    #     response_object = {
    #         "status": "success",
    #         "data": {
    #             "task_id": task.get_id()
    #         }
    #     }    
    # return jsonify(response_object), 202



with app.test_request_context():
    # print(url_for('get_task'))
    print(url_for('index')) # index 함수과 연관된 URL 출력
    print(url_for('login')) # login 함수와 연관된 URL 출력
    print(url_for('get_task',url='https://.jpg',model_name='alias_name',file_type='image'))
# login 함수와 연관된 URL을 출력하되 next라는 변수에는 '/' 값을 대입할 것
# 값이 없으므로 쿼리 인자로 URL에 덧붙여 출력된다
    print (url_for('profile', username='John Doe'))
# profile 함수와 연관된 URL을 출력하되 username라는 변수에는 'John Doe'를 대입할 것