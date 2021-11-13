def simple_add_while(num):
    result = 0
    while num > 0:
        result += num
        num -= 1
    return result

def simple_add_range(num):
    result = 0
    for i in range(num):
        result += i
    return result

    
def simple_addc_while(long num):
    cdef int result = 0
    while num > 0:
        result += num
        num -= 1
    return result

cdef long simple_addc_range(long num):
    cdef long i
    cdef long result = 0
    for i in range(0, num):
        result += i
    return result