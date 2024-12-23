from memory_profiler import profile

@profile
def ep_func():
    import math
    print("Tetsting memory usage")
    print(math.log10(100))
    
    
ep_func()