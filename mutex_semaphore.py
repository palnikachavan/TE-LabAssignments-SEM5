from threading import Thread, Semaphore, Lock
import random
import time

buffer = []
buffer_size = int(input("Enter size of buffer :"))
empty = Semaphore(buffer_size)
full = Semaphore(0)
lock = Lock()

terminate = False  
def producer():
    global terminate
    while not terminate:
        item = random.randint(0, 100)
        
        if not terminate:
            empty.acquire()
        
        with lock:
            if not terminate:
                buffer.append(item)
                print(f"Produced: {item}    Buffer: {buffer}")
        
        full.release()
        time.sleep(random.uniform(0.2, 1))

def consumer():
    global terminate
    while not terminate:
        if not terminate:
            full.acquire()
        
        with lock:
            if buffer and not terminate:
                popped = buffer.pop(0)
                print(f"Consumed: {popped}    Buffer: {buffer}")
        
        empty.release()
        time.sleep(random.uniform(0.5, 1.5))

num_producers = int(input("Number of producers: "))
num_consumers = int(input("Number of consumers: "))


producers = [Thread(target=producer) for _ in range(num_producers)]
for p in producers:
    p.start()

consumers = [Thread(target=consumer) for _ in range(num_consumers)]
for c in consumers:
    c.start()


try:
    print("Running for 5 seconds...")
    time.sleep(5)
finally:
    terminate = True


for _ in range(buffer_size):
    empty.release()
for _ in range(buffer_size):
    full.release()

for p in producers:
    p.join()
for c in consumers:
    c.join()

print("All producers and consumers have finished.")
