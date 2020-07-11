from concurrent.futures import ThreadPoolExecutor
import time
import threading

def task(interval):
    print("Processing in thread: {}", threading.current_thread())
    result = 0
    for i in range(5):
        result += i
        time.sleep(interval)
    print(result)
    print ("{} Done!", threading.current_thread())

def runTaskSyn():
    task(0.3)
    task(0.5)

def runTaskAsyn():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(task, 0.5)
        executor.submit(task, 0.3)
        executor.submit(task, 0.6)

runTaskAsyn()