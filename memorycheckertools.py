
import tracemalloc #1
from memory_profiler import profile #2
tracemalloc.start()#1
@profile #2
def loo():
    i=0
    while i < 1:
        i=i+0.00001*1.2**1.3
        print(i)
    return i
l = loo()
print(tracemalloc.get_traced_memory())#1 (achter functie call)
tracemalloc.stop()#1
print(l)


