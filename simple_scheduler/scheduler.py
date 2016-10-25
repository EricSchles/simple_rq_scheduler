from redis import Redis
from rq import Queue
from datetime import datetime
import time

def f():
    print("start")

def schedule(start_time=datetime.now(),func=f,args=tuple(),interval=5,repeat=10):
    q = Queue(connection=Redis())
    current_time = start_time
    if repeat==float('Inf'):
        while True:
            q.enqueue(func,args=args)
            time.sleep(interval)
    else:
        for i in range(repeat):
            q.enqueue(func,args=args)
            time.sleep(interval)
    
