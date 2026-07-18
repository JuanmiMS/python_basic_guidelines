


name = input("What is your name? \n")
print(f"Hello {name}")

age = input("What is your age? \n")
print(f"Hello {name}, you are {age} years old, in 20 years you will be {int(age) + 20} years old")

country, city = input("Where are you from? (country, city) \n").split()
print(f"Hello {name}, you are from {city} in {country}")