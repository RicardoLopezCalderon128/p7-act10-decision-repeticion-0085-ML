# Ricardo Lopez NC = 0085
print("Ricardo Lopez NC = 0085")

# ----------------------------------------
print("1 Python Conditions")
print("ejemplo 1")
numero = 15
if numero > 0:
    print("El número es positivo")

print("ejemplo 2")
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
    print("Ya puedes votar.")


# ----------------------------------------
print("2 Python If...Elif")
print("ejemplo 1")
score = 75
if score >= 90:
    print("Nota: A")
elif score >= 80:
    print("Nota: B")
elif score >= 70:
    print("Nota: C")

print("ejemplo 2")
edad = 25
if edad < 13:
    print("Eres un niño")
elif edad < 20:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")


# ----------------------------------------
print("Python If...Else")
print("ejemplo 1")
a = 200
b = 33
if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")

print("ejemplo 2")
conectado = False
if conectado:
    print("¡Bienvenido de vuelta!")
else:
    print("Por favor, inicia sesión.")


# ----------------------------------------
print("Python For Loops")
print("ejemplo 1")
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)

print("ejemplo 2")
for i in range(5):
    print("Repetición número:", i)


# ----------------------------------------
print("Python While Loops")
print("ejemplo 1")
i = 1
while i < 6:
    print(i)
    i += 1

print("ejemplo 2")
i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1


# ----------------------------------------
print("programa hecho por Lopez Ricardo NC = 0085")
