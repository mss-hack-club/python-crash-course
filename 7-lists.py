# lists store LISTS of items (any items, take your pick)

a = []  # this is how to make an EMPTY list
b = [1, 2, 3, 4]  # this is how to make a list with STUFF INSIDE IT ALREADY

# ACCESS SPECIFIC ELEMENT OF THE LIST - just like strings

print(b[0])  # prints first element of b
print(b[1])  # prints second element of b
print(b[2])  # prints third element of b

# common list operations - append, insert, remove

# APPEND - adds the element to the END of the list

b.append(4)  # adds 4 to the END of b
print(b)

# b is now: [1, 2, 3, 4, 4]

# INSERT - inserts a given item into the list at a certain INDEX

b.insert(2, 7)  # inserts the element 7 into the list at index 2
print(b)

# b is now: [1, 2, 7, 3, 4, 4]

# remove - removes the given element from the list

b.remove(7)  # removes 7 from the list
print(b)

# b is now: [1, 2, 3, 4, 4]
