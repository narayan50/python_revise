import threading
import time

def worker(name):
    print("thread is running---------------")
    print(f"Thread {name}: starting")
    time.sleep(9)
    print(f"Thread {name}: finishing")
    time.sleep(6)
    print("thread is completed and terminated------------")
# Create threads
t1= threading.Thread(target=worker, args=("sam",))
print("runnable-------------------------------------------")
t2= threading.Thread(target=worker, args=("john",))

# Start threads
t1.start()
t2.start()
# Wait for both threads to complete
t1.join()
print("")
t2.join()
print("-----------main thread executed---------")