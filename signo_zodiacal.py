def signo_zodiacal(dia:int, mes:int):
    if (dia >= 21 and dia <= 31 and mes == 3) or (dia >= 1 and dia <= 20 and mes == 4):
        return 'Aries'
    elif (dia >= 21 and dia <= 30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
        return 'Tauro'
    elif (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 21 and mes == 6):
        return 'Géminis'
    elif (dia >= 22 and dia <= 30 and mes == 6) or (dia >= 1 and dia <= 22 and mes == 7):
        return 'Cáncer'
    elif (dia >= 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 22 and mes == 8):
        return 'Leo'
    elif (dia >= 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 22 and mes == 9):
        return 'Virgo'
    elif (dia >= 23 and dia <= 30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
        return 'Libra'
    elif (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 22 and mes == 11):
        return 'Escorpio'
    elif (dia >= 23 and dia <= 30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
        return 'Sagitario'
    elif (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 20 and mes == 1):
        return 'Capricornio'
    elif (dia >= 21 and dia <= 31 and mes == 1) or (dia >= 1 and dia <= 18 and mes == 2):
        return 'Acuario'
    elif (dia >= 19 and dia <= 29 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
        return 'Piscis'
    else:
        return ''

while True:
    dia = int(input("Dia de nacimiento: ")) 
    mes = int(input("Mes de nacimiento: "))
    signo = signo_zodiacal(dia, mes)
    if signo == '':
        print("Fecha no valida, vueve a intentarlo")
    else:
        print("Tu signo zodiacal es ", signo)
        break
