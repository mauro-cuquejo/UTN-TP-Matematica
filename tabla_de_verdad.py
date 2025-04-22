LONG_COL = 37


def tabla_de_verdad():
    a = int(input("ingrese un numero binario: "))
    b = int(input("ingrese otro numero binario: "))
    if ((a < 0 or a > 1) or (b < 0 or b > 1)):
        print("numeros ingresados incorrectos")
        return
    # and
    resultados = []
    if (a and b):
        resultados.append([a, b, f"A AND B", "1"])
    else:
        resultados.append([a, b, f"A AND B", "0"])

    # or
    if (a or b):
        resultados.append([a, b, f"A OR B", "1"])
    else:
        resultados.append([a, b, f"A OR B", "0"])
    # not
    if (not a):
        resultados.append([a, b, f"NOT A", "1"])
    else:
        resultados.append([a, b, f"NOT A", "0"])
    if (not b):
        resultados.append([a, b, f"NOT B", "1"])
    else:
        resultados.append([a, b, f"NOT B", "0"])

    print("\nTabla de resultados:\n")
    print("-" * LONG_COL)
    print(f"| A | B | {'OPERACION':^11} | {'RESULTADO':^11} |")
    print("-" * LONG_COL)
    for a, b, op, res in resultados:
        print(f"| {a} | {b} | {op:<11} | {res:>11} |")
    print("-" * LONG_COL)


tabla_de_verdad()
