def conversor_a_decimal(binario):
    base = 2
    exponente = 0
    decimal = 0
    for digito in reversed(str(binario)):
        decimal += int(digito) * base ** exponente
        exponente += 1
    return decimal


def ejercicio():
    binario = input("ingrese un numero binario: ")
    for digito in binario:
        if int(digito) < 0 or int(digito) > 1:
            print("Ingresó un numero binario incorrecto")
            return
    print(conversor_a_decimal(binario))


ejercicio()
