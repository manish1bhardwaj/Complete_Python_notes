letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
Name = input("Enter your Name :")
Date = input("Enter Date :")
print(f"Dear {Name},You are selected! {Date}") # Output : Enter your Name :MAnish Enter Date :2 Dear MAnish,You are selected! 2

# or

print(letter.replace("<|Name|>","Manish Bhardwaj").replace("<|Date|>","2-July-2024"))
''' Output : 
Dear Manish Bhardwaj,
You are selected!
2-July-2024'''