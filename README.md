# UrbanAI RESTful API Server
  - implementation using flask with redis rq worker 
  - you can see deepgeo_task in web

## Requirements
  - redis-server
  - redis worker
  - Deepgeo
## Usage
  - you must have to do two steps
```bash
  # Server run
  python manage.py run -h 0.0.0.0 -p
  # redis RQ Worker run
  python manage.py run_worker
```
## **Deepgeo lib will be changed**
  - when [deepgeoconvert repositorty](https://github.com/rdj94/deepgeoconvert) updated

### Reference
  - [flask-redis-queue](https://github.com/mjhea0/flask-redis-queue) 
  
## How to use UrbanAI RESTful API

### Add image detection task API
- GET API for adding task

 http://your_urbanai_rest_server_url/task?key1=value1&key2=value2&key3=value3...
 
 |key  | value |
| ------------- | ------------- |
| url  | {http://*, file://*}  |
| file_type  | {iamge, video} |
| model_name | {mscoco_maskrcnn, road_damage, mscoco_yolo } |
 
- Return value 

 ex: {"data":{"task_id":"886b8916-9785-4e71-b4a4-f1551c67a4a6"},"status":"add task success"}
 
- GET API for detection result

http://your_urbanai_rest_server_url/tasks/${taskID}


### examples of Image Detection GET API 
- GET API for adding image detection

  http://djr.urbanai.net/task?url=http://infolab.kunsan.ac.kr:8080/files/attach/images/675/386/002/1c4398adf662ce8b38b2de4b250987af.jpg&model_name=mscoco_maskrcnn&file_type=image
  
- will return the task id. 
  
  {"data":{"task_id":"886b8916-9785-4e71-b4a4-f1551c67a4a6"},"status":"add task success"}
  
- Get the detection result

  http://djr.urbanai.net/tasks/886b8916-9785-4e71-b4a4-f1551c67a4a6
  
### examples of video Detection GET API 
- GET API for adding video detection

http://djr.urbanai.net/task?url=http://urbanai.net/data/media/20190524_133559_NF.mp4&model_name=mscoco_maskrcnn&file_type=video

- will return the task id. 

{"data":{"task_id":"7fd0662d-a8a3-4988-a9cc-4f062f1e8bbc"},"status":"add task success"}

- Get the detection result

  http://djr.urbanai.net/tasks/7fd0662d-a8a3-4988-a9cc-4f062f1e8bbc
  
- Not finished yet

{"data":{"message":"Task queued at Fri, 03 Jan 2020 07:49:15 0 jobs queued","task_id":"a88a2227-a068-49fd-ab90-5f6c6519d2d0","task_result":null,"task_status":"failed"},"status":"success"}

- Finished successfully

 {"data":{"message":"Task queued at Fri, 03 Jan 2020 07:49:15 0 jobs queued","task_id":"a88a2227-a068-49fd-ab90-5f6c6519d2d0","task_result":null,"task_status":"failed"},"status":"success"}
  
  

# Deplolying DeepGeo Docker 
  - 연구실 nas의 postgeomedia_deepgeo_api_docker의 docker에는 현 저장소의 파일과 Deepgeo library가 site-package에 설치되어있습니다.
  - 경로는 /home/DeepGeoAPI입니다.
  - 실행은 flask와 redis rq worker를 둘다 해주셔야합니다.
  - 업로드된 이미지의 python버전은 3.6.5이며 alias를 따로 설정하지않아 실행은 꼭 둘다 해주셔야합니다. 이 경우 터미널 탭을 2개로 실행 해야 할 것입니다.
      1. python3.6 manage.py run -h 0.0.0.0 
      2. python3.6 manage.py run_worker
  - flask Server의 기본 PortNumber는 5000 입니다. 따라서 host에서 image를 이용하여 container를 생성할때 5000번에 대한 포트 포워딩을 해주셔야합니다.
  - flask Server의 PortNumber와 ip는 Server 실행시 -p option을 통해 지정할수있습니다. 
      1. python3.6 manage.py run -h 0.0.0.0 -p 80 
  - Port 설정 명령어는 p입니다.
    1. docker run --privileged -p (hostPortNumber):5432 -p (hostPortNumber):5000 --name=(alias_name) -d -e container=docker -v /sys/fs/cgroup:/sys/fs/cgroup:ro ayasofi/pg_cuda:api /usr/sbin/init
  - host의 portnumber를 통해 container로 포트 포워딩시 각각의 Portnumber는 열려있어야합니다.
# Usage
  - 정상적으로 flask server 및 redis rq worker를 실행 하셨다면 포트 포워딩 때 설정한 Host IP:portnumber를 Web을 통해 간단한 task 뷰를 확인할수 있습니다.
  - UI 설정 및 URL 입력후 Submit Button을 클릭시 redis Queue에 task가 등록되며 task들은 1초마다 status를 반환합니다.(ui를 통한 request가 task status를 1초마다 볼 수 없습니다.)
  - 이때 taskID는 output data를 조회할수 있는 key입니다.
  - 현재 API Method는 2개입니다.
    1. file 다운로드 및 예측 태스크 등록 /task?url=(file_url)&model_name=(alias_model_name)&file_type=(image or video)
    2. 위의 ( 및 ) 는 실제 들어가지않습니다. 또한 task 등록 성공시 task_id와 태스크 등록 성공 여부를 반환합니다.
    3. queue에 등록한 task들의 상태 및 예측 결과값 조회 /tasks/task_id
    4. Output는 image와 video 각각 Geojson AppendixC와 AppendixD의 format을 따릅니다.
    
## Environment  postgresql11 in ( postgis, pl/python3u pl/java) cuda 9.0 and set cudnn (v7.4.2)
### image Based on  nvidia/cuda:9.0-devel-centos7 
- Make sure you have installed the **NVIDIA driver and Docker 19.03 for your Linux distribution Note that you do not need to install the CUDA toolkit on the host, but the driver needs to be installed**
- **install nvidia-docker or docker version > =19.03**
- **If you're docker version < 19.03  you must have to do install nvidia-driver and cuda in your host**
## **Usage**  
- **Postgresql default portNumber=5432 and to solve D-Bus-Error See the command below.**
    - when you open add serveral port number docker run -p (hostportNumber):5432 -p (hostportNumbert):portnumber
- **docker run --privileged -p (hostPortNumber):5432 --name=(custom) -d -e container=docker -v /sys/fs/cgroup:/sys/fs/cgroup:ro ayasofi/pg_cuda:latest /usr/sbin/init**
- **nvidia-docker run --privileged -p (hostPortNumber):5432 --name=(custom) -d -e container=docker -v /sys/fs/cgroup:/sys/fs/cgroup:ro ayasofi/pg_cuda:latest /usr/sbin/init**
### **allocate GPU device Test nvidia-smi with the latest official CUDA image**
-  docker run --gpus all nvidia/cuda:9.0-base nvidia-smi
### **Start a GPU enabled container on two GPUs**
- docker run --gpus 2 nvidia/cuda:9.0-base nvidia-smi
### **Starting a GPU enabled container on specific GPUs**
- docker run --gpus '"device=1,2"' nvidia/cuda:9.0-base nvidia-smi
- docker run --gpus '"device=UUID-ABCDEF,1"' nvidia/cuda:9.0-base nvidia-smi
### **Specifying a capability (graphics, compute, ...) for my container**
### **Note this is rarely if ever used this way**
- docker run --gpus all,capabilities=utility nvidia/cuda:9.0-base nvidia-smi

## Issue
- **when postgresql can't connect using pgadmin  please restart service** 
  - **docker exec -it  containner_name /bin/bash** 
 -  **systemctl restart postgresql-11.service**
- **docker run --privilleged option acquire all Capabilities from host then when you run this option it can't devide your gpus**
-  I really want to know how to solve this problem maybe it can solve when you create container --add each Capabilities option 
-  I don't try to that please announce to me try this process

### If you are korean Please Read read this posts these are explain how to use Docker in your system 
-  [StartGuide](https://subicura.com/2017/02/10/docker-guide-for-beginners-create-image-and-deploy.html)
-  [Change saved Data path](https://yookeun.github.io/docker/2018/10/29/docker-change/)
-  [Explain how to mount new partition](http://blog.naver.com/PostView.nhn?blogId=pcgun70&logNo=221112204338&parentCategoryNo=&categoryNo=20&viewDate=&isShowPopularPosts=false&from=postView)
- [firewalld installed in your containner if you want change rule see this post](https://www.lesstif.com/pages/viewpage.action?pageId=43844015)

