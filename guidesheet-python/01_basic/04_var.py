my_name = "Juanmi"


print(f"Hello {my_name}")

age = 30
print(f"Hello {my_name}, you are {age} years old")  

age = 31
print(f"Hello {my_name}, you are {age} years old")

CONSTANT = 3.14 #constant

is_active: bool = True #boolean
is_active = 42 #Error when typecheck in VSCode is active
print(is_active) #prints 42, but is_active is not a boolean anymore


age_typed = "error" #Error even declared after assigning it
age_typed: int = 30
