def factorial(numero:int):
    if numero >= 0:
        resultado = 1
        while numero > 0:
            resultado = resultado * numero
            numero -= 1
        return resultado
    else:
        return 'Indefinido'

def miSumatoria(limite:int, primer_valor_de_n:int = 0):
    n = primer_valor_de_n
    e = 0
    while n < limite:
        e += 1/factorial(n)
        n = n + 1
    return e

print("Mientras mayor sea el limite, mayor la presicion al calcular el número e y el tiempo de ejecución")
limite = int(input('Limite: '))
print('EL valor de e es: ', miSumatoria(limite))
