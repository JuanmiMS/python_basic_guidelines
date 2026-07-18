print("Conditional Statements")


nota: int = 4
if nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

edad = 18
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")
else:
    print("No puede conducir")


num = input("Introduce un número: ")
if num == str(17) or num == str(18):
    print("Tienes 17 o 18 años")

estudiante = True
if not estudiante:
    print("No eres estudiante")