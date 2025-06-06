import time
# print("hello world")


# def wrapper(func):
#     def secondFunc():
#         print("decorator")
#         func()
    
#     return secondFunc

# @wrapper
# def greeting():
#     print("hello world")
#     return "testing"

# print(greeting())


# second example

# def wrapper(func):
#     def secondFunc():
#         print("decorator")
#         result = func()
#         return result
    
#     return secondFunc

# @wrapper
# def greeting():
#     print("hello world")
#     return "testing"

# print(greeting())




# def checkTime(func):
#     def wrapper(*args , **kwargs):
#         start_time = time.time()
#         result = func(*args , **kwargs)
#         end_time = time.time()
#         print(f"func name {func.__name__} ran in {end_time - start_time}")
#         return result

#     return wrapper


# @checkTime
# def greetingUser(username , age = 20):
#     time.sleep(3)
#     print(f"hello {username} with age {age}")


# greetingUser("abdullah" , age=21)



# def func_info(func):
#     def wrapper(*args , **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
#         result = func(*args , **kwargs)
#         print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return result
    
#     return wrapper

# @func_info
# def greetUser(username , age = 21):
#     return f"hello {username} with age {age}"

# print(greetUser("abdullah" , age=29))


# cache question


def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper




@cache
def time_taken_task(num1 , num2):
    time.sleep(1)
    return num1 + num2

print(time_taken_task(2 , 3))
print(time_taken_task(2 , 3))
print(time_taken_task(5 , 3))
print(time_taken_task(5 , 3))


