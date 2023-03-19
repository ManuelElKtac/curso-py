# ((a*x)**2)+(b*x)+c=0
# x=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)

a = int(input("El primer numero es:"))
b = int(input("El segundo numero es:"))
c = int(input("El tercer numero es:"))

x = (-b - ((b**2) - (4*a*c))**(0.5)) / (2*a)

# no es necesario Y, en la resolicion lo demuentra, pero esta bien echo,
#  ya que en los 3 necesita que los numeros sean 2, 4 y -6
y = 0
y = ((a*(x**2))+(b*x)+c)

resultado = print(x)
