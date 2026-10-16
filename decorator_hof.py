# higher order functions
'''
arr = [2,4,6,8,10]

def divide(val):
    return val // 2

res = list(map(divide, arr))

print(res)
'''
# decorator
'''
def announce(func):
    def wrapper(*args, **kwargs):
        print("Message 1")
        result = func(*args, **kwargs)
        print("Message 2")
        return result

    return wrapper

@announce
def multiply(a, b):
    print("Inside")
    return a * b

result = multiply(3, 4)
print(result)
'''