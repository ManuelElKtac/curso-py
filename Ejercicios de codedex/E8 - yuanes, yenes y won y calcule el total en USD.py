# input es par que el usuario ingrese un dato, pero hay que asignarle
# un valor o nombre al dato, como contraseña, nomnre, dinero, etc
YC = int(input("Cuantos Yuan Chino tienes?"))
YJ = int(input("Cuantos Yen Japoneces tiene?"))
WS = int(input("Cuantos Won Surcoreanos tienes?"))

yc1 = YC * 0.14
yj1 = YJ * 0.0074
ws1 = WS * 0.00077

print(yc1+yj1+ws1)
