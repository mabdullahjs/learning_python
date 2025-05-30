# print('loops in python');

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positiveNum = []

# for x in numbers:
#     if x > 0:
#         positiveNum.append(x)

# # print(len(positiveNum))
# print(positiveNum)


# num = [2,4,6,8,10,12,16,18]
# sum = 0
# for x in num:
#     sum += x

# print(sum)


# num = 5

# for x in range(1 , 11):
#     print(f'{num} * {x} = {num*x}') if x!= 5 else None


# factorial number
# num = 10
# fac = 1
# while num > 0:
#     print(num)
#     fac = fac * num
#     num = num - 1


# print(fac)


# userInput = int(input("enter any num between 1 to 10 ==> "))
# print(userInput)


# while True:
#     if userInput < 10 and userInput > 0:
#         print("correct")
#         break
#     else:
#         userInput = int(input("enter any num between 1 to 10"))

# print('testing ')


list = [1,2,3,4,5,6]

# for i in list:
#     print(i)

I = iter(list)
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

