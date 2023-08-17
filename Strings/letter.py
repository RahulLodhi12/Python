letter = '''Dear <|Name|>,
Greeting from GreyMatter Tech., I am happy to inform you about your selection 
You are selected!
Have great day ahead!
Thanks and regards
Walter White
Date: <|Date|>'''

name = input("Enter your name ")
date = input("Enter date ")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)
