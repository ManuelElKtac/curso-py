curso = "Ultimate \"Python\""

r"""
se puede usar comillas simples para separar las commillas y
 las comillas simples, pero tamben se puede usar \ que se usa para que la
 litra despues de \ no se cuente como codigo 
"""
# al utilizar el prefijo "r" antes de una cadena de texto, se indica a Python
#  que se trata de una "cadena cruda" o "raw string", lo que significa que
# cualquier carácter especial dentro de la cadena se debe interpretar de forma
#  literal, sin procesar secuencias de escape. Hola

# comentario
# \" = permite uqe se imprima "
# \' = permite uqe se imprima '
# \\ = permite uqe se imprima \
# \n = toma el sring que viene despues de \ y lo pasa a una nueva linea


print(curso)

cursi = "Ultimate 'Python'"
print(cursi)

cursi = "Ultimate \n\"Python\" "
print(cursi)
