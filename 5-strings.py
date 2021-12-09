# this document contains useful stuff for strings

a = "this is a string"  # make a string variable
b = "this is another string"  # make another string variable

# CONCATENATION (you can put strings together using +)
c = a + " " + b
print(c)  # prints the new combo of strings

# CHARACTER ACCESS: You can access a specific character of a string using its index (in Python everything is 0-indexed)
print(a[0])  # prints first character of i
print(a[1])  # prints second character of i
print(a[5])  # prints sixth character of i


# LENGTH: you can find the length of a string (or any iterable) using len()
# prints the length of the string (how many characters it has including space)
print(len(c))

# FIND - find a character by index
# finds the first occurence of character i in the string a and stores the INDEX
d = a.find('i')
print(d)  # prints the first index of the character 'i' in the string a
