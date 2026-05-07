import time

def benchmark(name, fn):

    start = time.time()

    fn()

    end = time.time()

    print(
        f"{name}: "
        f"{end - start:.6f}s"
    )

def loop():

    total = 0

    for i in range(1000000):
        total += i

benchmark("Million Loop", loop)
