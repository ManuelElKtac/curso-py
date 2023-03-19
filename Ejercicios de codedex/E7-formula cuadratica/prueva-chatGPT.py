a = int(input("El primer numero es:"))
b = int(input("El segundo numero es:"))
c = int(input("El tercer numero es:"))

# Calcula el discriminante
discriminante = b**2 - 4*a*c

# Calcula las soluciones
if discriminante >= 0:
    x1 = (-b + (discriminante)**(0.5)) / (2*a)
    x2 = (-b - (discriminante)**(0.5)) / (2*a)
else:
    x1 = (-b + (abs(discriminante))**(0.5)*1j) / (2*a)
    x2 = (-b - (abs(discriminante))**(0.5)*1j) / (2*a)

# Imprime las soluciones
print("x1 =", x1)
print("x2 =", x2)
