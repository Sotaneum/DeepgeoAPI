# project/server/main/tasks.py


import time


def detect(processor,alias_model_name:str,url:str):    
    start = time.time()
    processor.read(uri=url)
    processor.detect(alias_model_name)
    processor.locate()
    end = time.time()
    time_elapsed = end - start
    print(f"Time elapsed: {time_elapsed} ms")
    return processor.get_json()

def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
