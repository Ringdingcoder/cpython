import time
import itertools

import threading

THREADS = 3

last_time = [None] * THREADS

def mytime(f):
    t = time.time()
    r = f()
    print "Elapsed:", time.time() - t
    return r

def sieve():
    """Sieve of Eratosthenes, yield each prime in sequence."""
    yield 2
    D = {}
    q = 3
    while True:
        p = D.pop(q, 0)
        if p:
            x = q + p
            while x in D: x += p
            D[x] = p
        else:
            yield q
            D[q*q] = 2*q
        q += 2

def take(n, iterable):
    return list(itertools.islice(iterable, n))


def calc_thread(arg):
    while True:
        t = time.time()
        take(50000, sieve())
        last_time[arg] = time.time() - t

ts = [threading.Thread(target=calc_thread, args=(x,), prio=x) for x in range(THREADS)]
for t in ts:
    t.setDaemon(True)
    t.start()

while True:
    print "\t".join(map(str, last_time))
    time.sleep(0.5)
