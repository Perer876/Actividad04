def factorial(numero:int):
    if numero >= 0:
        resultado = 1
        while numero > 0:
            resultado = resultado * numero
            numero -= 1
        return resultado
    else:
        return 'Indefinido'

print(factorial(-23))