from memory_profiler import profile


@profile
def ep_func():
    from math import log10
    print("Tetsting memory usage")
    print(log10(100))
    
ep_func()