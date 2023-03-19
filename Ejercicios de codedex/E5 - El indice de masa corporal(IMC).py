"""Python también puede realizar exponenciación como 2³ o 10².

En matemáticas escritas, podríamos ver un exponente como un número de superíndice (como arriba), pero escribir números de superíndice no siempre es fácil en los teclados modernos. Dado que la exponenciación es muy similar a la multiplicación, Python usa la notación .**

score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32
"""
# Indice de masa corporal (IMC)
# Se calcula tomando el peso (masa) de un individuo en kilogramos y dividiéndolo por
# el cuadrado de su altura en metros.

M = 45
A = 1.70

IMC = M/(A**2)
print(IMC)  # IMC = 15.570934256055365
