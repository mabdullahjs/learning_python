# print('hello list')

fruits = ["apple" , "banana" , "orange" , "mango" , "watermelon"]
# print(fruits[1])
# print(fruits[-1])

# print(fruits[1: 4])

# fruits[1] = "changed banana"
# fruits[1: 1] = ["test" , "test"]
# print(fruits)

# # Empty list
# my_list = []

# # List with integers
# numbers = [1, 2, 3, 4, 5]

# # Mixed data types
# mixed = [1, "hello", 3.14, True]

# # Nested list
# nested = [1, [2, 3], [4, 5]]



# fruits[1] = "orange"     # Change element
# fruits.append("grape")   # Add at the end
# fruits.insert(1, "kiwi") # Insert at index
# fruits.remove("apple")   # Remove by value
# fruits.pop()             # Remove last element


# len(fruits)               # Length
# sorted(fruits)            # Returns sorted list
# fruits.sort()             # Sorts the list in place
# fruits.reverse()          # Reverses the list in place
# fruits.index("orange")    # Index of element
# print("banana" in fruits )       # Membership check




# for item in fruits:
#     print(item , end=("-"))



#  Lists Are Mutable

# a = [1 , 2]
# b = a

# b[0] = "changed"
# print(a)


# but if we have to give another reference

# a = [1 , 2]
# b = a.copy()

# b[0] = "changed"
# print(a)




square = [x ** 2 for x in range(11)]
print(square)
cube = [x ** 3 for x in range(11)]
print(cube)