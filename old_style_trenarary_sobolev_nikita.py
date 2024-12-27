import dis

def foo():
    return 2 > 1 and 'a' or 'b'

dis.dis(foo)