###
# Casting in Python
###


print(type("100"))
print(int("100"))
print(type(int("100")))

print(2 + int("100"))
print(3.14)
print(int(3.14))
print(int(2.5))


print(bool(3)) #true
print(bool(0)) #false
print(bool(-1)) #true
print(bool("")) #false
print(bool("Hello")) #true
print(bool([])) #false
print(bool([1, 2, 3])) #true

#round redondea al par más cercano, si es impar redondea hacia arriba
print(round(3.5))
print(round(3.14))
print(round(2.5))