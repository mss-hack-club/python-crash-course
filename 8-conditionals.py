# Conditionals (if statements) check certain conditions and do stuff based on whether they're true

# if condition:
#    do this

# NOTE: indenting is VERY important here. Any evenly indented set of code is a CODE BLOCK.
# In the case of if statements, the if statement will only
# execute the CODE BLOCK underneath it. Meaning, that if you
# want a line to be a part of the if statement, you need to tab
# it once underneath the if statement

# if statement - simple condition check

# checks if 3 < 4 (true)
if 3 < 4:
    print('3 is less than 4')

print('this statement will execute regardless of if the condition is true because it is OUTSIDE of the code block')

# elif - if the IF statement is not true, checks another condition

# checks if 4 < 3 (false)
if 4 < 3:
    print('this will not execute')
# else if the first condition is not true (it's not) checks this condition to see if it's true
elif 3 < 4:  # checks if 3 < 4 (true)
    print('this will execute because this is part of the elif which is true')

# else - if ALL ELSE FAILS (all ifs and elifs) runs the code in the else codeblock

# checks if 4 < 3 (false)
if 4 < 3:
    print('this will not execute')
# else if the first condition is not true (it's not) checks this condition to see if it's true
elif 5 < 3:  # checks if 5 < 3 (also false)
    print('this will NOT execute because this is part of the elif which is false')
# all other checks have failed, now we do the else
else:  # or else if all else fails
    print('this is the last resort, this executes because all the other checks failed')
