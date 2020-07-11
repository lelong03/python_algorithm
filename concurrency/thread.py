import threading

def getThreadName():
    print("This is the current thread: {}".format(threading.current_thread()))

# Call with main thread
getThreadName()

# Call with defined thread
a_thread = threading.Thread(target=getThreadName)
a_thread.start()