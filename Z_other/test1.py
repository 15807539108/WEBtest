import threading
import time

def fun_timer():
    print("1")
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()

fun_timer()

time.sleep(5)
timer.cancel()



