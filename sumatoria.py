def factorial(numero:int):
    resultado = 1
    while numero > 0:
        resultado = resultado * numero
        numero -= 1
    return resultado

print(factorial(23))