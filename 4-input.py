# the input statement takes input from the console

inp = input()  # takes input from the console and stores it in the variable inp

# input can also take a PROMPT (print something out to tell the user what to do before taking input)
# prints the string to the console then takes input
inp2 = input('Please enter a number: ')

# NOTE: input always returns a STRING

# example: pretend you type 3 to answer the below input statement
inp3 = input()  # inp3 would have a value of '3' (string with three in it)

# So if you multiplied inp3 by three, you would get three times the STRING
# i.e. 333

# to get the INT representation of the input, you have to convert the input to INT
inp4 = input()
# reassigning the variable (it overwrites it with the int version of '3')
inp4 = int(inp4)

# or if you prefer oneliners (like me)
inp4 = int(input())  # takes input and then converts it to int in the same line
