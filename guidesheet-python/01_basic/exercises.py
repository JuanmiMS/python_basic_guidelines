###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

question = input("Cuál es tu nombre y tu ciudad? \n").split()
print(f"Nombre {question[0]},\n Ciudad {question[1]}")
### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print(f"Variable a: {a}, Tipo: {type(a)}")
print(f"Variable b: {b}, Tipo: {type(b)}")
print(f"Variable c: {c}, Tipo: {type(c)}")
print(f"Variable d: {d}, Tipo: {type(d)}")
print(f"Variable e: {e}, Tipo: {type(e)}")

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
entero = int(cadena)
float = float(entero)
print(f"Cadena: {cadena}, Entero: {entero}, Float: {float}")

float_2 = 3.99
entero_2 = int(float_2)
print(f"Float: {float_2}, Entero: {entero_2}")
### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

nombre = "Juanmi"
edad = 30
altura = 1.80
print("Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros") #Sin f-string
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

# "Hola! Me llamo Juanmi y tengo 30 años, mido 1.80 metros"

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi_rounded = round(3.14159)
print(f"PI redondeado: {pi_rounded}")
print(f"División entera: {pi_rounded // 2}")
print(f"Resultado: {pi_rounded // 2 == 1}")
