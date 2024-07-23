import fastapi
import uvicorn
import time
import pydantic
import threading
import datetime


test_storage = []
current_time = datetime.datetime.now()
current_time -= datetime.timedelta(microseconds=current_time.microsecond)


class TimerSerializer(pydantic.BaseModel):
    seconds: int

    class Meta:
        from_attributes = True


def set_timer_function(seconds):
    global current_time
    target_time = current_time
    target_time += datetime.timedelta(seconds=seconds)
    test_storage.append(target_time)


def queue_listener():
    while True:
        global test_storage
        global current_time
        test_storage.sort()
        time.sleep(1)
        current_time.second += 1
        if current_time in test_storage:
            print("Сработал")


app = fastapi.FastAPI()


@app.post("/set-timer", response_model=TimerSerializer)
async def set_timer(timer: TimerSerializer):
    set_timer_function(seconds=timer.seconds)
    return TimerSerializer(seconds=timer.seconds)


api_thread = threading.Thread(
    target=uvicorn.run, kwargs={"app": app, "host": "0.0.0.0", "port": 3001}
)

queue_listener_thread = threading.Thread(target=queue_listener)
api_thread.run()
queue_listener_thread.run()
queue_listener_thread.join()
api_thread.join()
