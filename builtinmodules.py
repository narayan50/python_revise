import math

print("value of pi is :--" ,math.pi)
print("squaare root of 25 is :--" ,math.sqrt(25))
print("floor of 23.8 is :--",math.floor(23.8))
print("ceil of 23.8 is :--" ,math.ceil(23.8))
print("round of 23.8 is :--",round(23.8))


#

num= math.sqrt(25)
print(type(num))


from threading import Thread
import time

def task1():
    i = 0
    while True:
        print("Task-1 running:", i)
        i += 1
        time.sleep(2)

def task2():
    j = 100
    while True:
        print("Task-2 running:", j)
        j += 10
        time.sleep(1)

# create threads
t1 = Thread(target=task1)
t2 = Thread(target=task2)

# start threads
t1.start()
t2.start()
