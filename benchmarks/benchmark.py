import time

def benchmark(fn):

    start = time.time()
    fn()
    end = time.time()

    print(f"Execution time: {end - start:.6f}s")

def sample():
    sum(range(1000000))

benchmark(sample)
