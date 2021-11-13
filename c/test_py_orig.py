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