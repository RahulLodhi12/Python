a = 22

if (a>22):
    print("Greater")
elif (a==22):
    print("Equal")
else:
    print("Lesser") # else is optional

print("Done")

# elif clause
'''
if (condition1):
    #code
elif (condition 2):
    #code
elif (condition 2):
    #code
….
else:
    #code    '''
# The above ladder will stop once a condition in an if or elif is met.


# Important Notes:
# There can be any number of elif statements.
# Last else is executed only if all the conditions inside elifs fail.