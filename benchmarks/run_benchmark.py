import time

def benchmark(name, fn):

    start = time.time()

    fn()

    end = time.time()

    duration = end - start

    print(f"{name}: {duration:.6f}s")

def sample():

    total = 0

    for i in range(1000000):
        total += i

benchmark("Sample Loop", sample)
