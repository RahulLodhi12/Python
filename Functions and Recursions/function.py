def percent(marks): # function definition
    return (sum(marks)/500)*100

    
marks1 = [45,67,87,66,96]
percentage1 = percent(marks1) # function call

marks2 = [65,77,87,37,93]
percentage2 = percent(marks2) # function call

print(percentage1, percentage2)