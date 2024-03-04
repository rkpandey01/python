import multiprocessing
import time
import os

num_processors = os.cpu_count()
print(f"Number of processors: {num_processors}")

def worker(n):
    print(f"Working on task {n}")
    time.sleep(1)
    return n * n

# Create a pool of 3 processes
with multiprocessing.Pool(processes=3) as pool:
    # Submit tasks to the pool
    result1 = pool.apply_async(worker, (1,))
    result2 = pool.apply_async(worker, (2,))
    result3 = pool.apply_async(worker, (3,))

    # Get the results of the completed tasks
    print(result1.get())
    print(result2.get())
    print(result3.get())

