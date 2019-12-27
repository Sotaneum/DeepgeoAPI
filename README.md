# Deepgeo API 
  - implementation using flask with redis rq worker 
  - you can see deepgeo_task in web

## requirements
  - redis-server
  - redis worker
  - Deepgeo
## Usage
  - you must have to do two steps
```bash
  # Server run
  python manage.py run -h 0.0.0.0 -p
  # redis RQ Wokrer run
  python manage.py run_worker
```
## **Deepgeo lib will be changed**
  - when [deepgeoconvert repositorty](https://github.com/rdj94/deepgeoconvert) updated

# Reference
  - [flask-redis-queue](https://github.com/mjhea0/flask-redis-queue) 
