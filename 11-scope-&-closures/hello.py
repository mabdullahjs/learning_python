# print("testing")


# scoping
# username = "mabdullah"
# def greetUser():
#     age = 21
#     print(username)

# greetUser()
# print(age) # x local variable




# #lexical scope

# # def outerFunc():
# #     username = "mabdullah"
# #     print(age) # not because of lexical scope
# #     def innerFunc():
# #         age = 21
# #         print(username)
# #     innerFunc()

# # outerFunc()




# # closure


# def outerFunc(num):
#     def innerFunc(x):
#         return x * 2
#     return innerFunc

# multiply = outerFunc(2)(3)
# print(multiply)