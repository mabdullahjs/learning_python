# print('hello functions')

# def cubeRoot(num):
#     return num ** 3

# print(cubeRoot(4))


# def greetUser(name,age):
#     return f"hello {name} with age {age}"

# print(greetUser("abdullah" , 21))


# def combine(val1, val2):
#     if isinstance(val1, str) and isinstance(val2, str):
#         return f"string concatenation {val1} {val2}"
#     elif isinstance(val1, int) and isinstance(val2, int):
#         return f"sum {val1 + val2}"
#     else:
#         return "please give same type"


# print(combine("hello", "abc"))
# print(combine(20, 30))
# print(combine(29, "abc"))



# def cal(num):
#     return num ** 2, num ** 3

# sq , cube = cal(2)
# print(sq , cube)




# def optional(mess="No message provided."):
#     return mess

# print(optional("testing"))




# checkeven = lambda x : x % 2 == 0
# print(checkeven(3))



# def flexible (*args):
#     return sum(args) # args return tuple

# print(flexible(2,3,4,5,6))



# def flexible(name , age):
#         print(f"{name} => {age}")

# flexible(name = "abdullah" , age = 21)

# def flexible(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key} => {value}")

# flexible(name = "abdullah" , age = 21)



# using **kwargs is good when you dont know how many argument will pass


# evenList = []
# def limitEven(num):
#     for val in range(1 , num + 1):
#         if val % 2 == 0:
#             evenList.append(val)
    
#     return evenList

# print(limitEven(100))



# def limitEven(num):
#     for num in range(2 , num + 1 , 2):
#         yield num


# print(limitEven(10))

# for num in limitEven(10):
#     print(num)




def recursion(n):
    if(n == 0):
        return 0
    else:
        return n + recursion(n - 1)
    

print(recursion(10))