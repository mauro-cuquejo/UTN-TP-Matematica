# PARTE 1 algortimos
import math


def funcionF(x):
    if (x >= 2):
        y = math.sqrt(x - 2)
        return str(y)
    else:
        raise Exception("En F, La variable debe ser mayor o igual a 2")


def funcionG(x):
    if (x != 0):
        y = 1 / x
        return y
    else:
        raise Exception("En G, la variable X debe ser distinta de 0")


def funcionCompuesta(x):
    try:
        return funcionF(funcionG(x))
    except Exception as e:
        return str(e) + " - En FoG, la variable debe ser mayor a 0 y menor o igual que 0.5"


# PARTE 2: Logica matematica
'''
Entonces:
Df = x >= 2
Dg = x != 0
Dfog = ?

acá no es tan sencillo de ver, pero para obtener el dominio de la función compuesta,
sabemos que para poder aplicar F(G(x)), en G(x) se debe cumplir que x pertenezca a Dg y G(x), a Df

Pensamos entonces en las proposiciónes lógicas:
A(x) => x != 0, que es lo mismo que decir x < 0 + x > 0
B(x) => x >= 2, que es lo mismo que decirm x > 2 + x = 2
C(x) = A(x) . B(A(x))

C(x) = (x > 0) + (x < 0) . (1 / x) > 2 + (1 / x) = 2

Si (1 / x) >= 2:
    => (1 / x) - 2 >= 0
    => (1 - 2x) / x >= 0
    Ahora tenemos que buscar los puntos criticos de esta ecuación:
        => para el numerador:
            => 1 - 2x >= 0
            => -2x >= -1

            acá como divido ambos lados por un número negativo, cambia el signo
            => x <= -1 / -2
            => x <= 1 / 2

            Esto sería que los valores mayores a 1/2, rompen a la función.
            En este caso, podríamos tomar los valores x < 1 / 2 + x = 1 / 2


        => para el denominador:
            x = 0
            Esto sería que 0, rompe a la funcion
            en este caso, los valores que podemos tomar son los que sean distintos de cero, que ya vimos que eran x < 0 + x > 0

        Tomamos los puntos criticos y verificamos en donde se cumple la función:

        x < 0                 | x > 0 . x < 1 / 2     | x = 1/2            | x > 1/2
        (1 / -2) - 2 >= 0     | (1 / (1/3)) - 2 >= 0  |(1 / x) - 2 >= 0    | (1 / 2) - 2 >= 0
        -(5 / 2) >= 0 (falso) | 1 >= 0 (verdadero)    | 0 >= 0 (verdadero) | -3 / 2 >= 0 (falso)

        vemos que los valores en donde se cumple la función son (x > 0 . x < 1 / 2) + (x = 1/2)
        (x > 0 . x < 1 / 2) + (x = 1/2)

        Como C implica A porque x = 1/2 es > 0, podemos decir que C = A.C
        (A . B) + A.C

        A.[(1.B) + C]
        A.(B + C)
        Quedando:
        (x > 0) . [(x < 1/2) + (x = 1/2)]

        Esto sólo lo hice para que se viera como cuando se calcula el dominio de FoG(x) y después sea un poco más sencillo optimizar


        Entonces:
            C(x) = [(x > 0) + (x < 0)] + Los puntos críticos que obtuvimos para que se cumpla que B(A(x))
            => C(x) = [(x > 0) + (x < 0)] . [(x > 0) . [(x < 1/2) + (x = 1/2)]]

            si pensamos en C(x) como un conjunto de miniterminos, en donde:
            M1 = (x > 0)
            M2 = (x < 0)
            M3 = (x < 1/2)
            M4 = (x = 1/2)

            queda:
            C(x) = (M1 + M2) . [M1.(M3 + M4)]

            Aplicamos asociativa:
            C(x) = [(M1 + M2).M1] . (M3 + M4)
            Aplicamos distributiva:
            C(x) = [(M1.M1) + (M1.M2)] . (M3 + M4)
            Aplicamos ley de identidad
            C(x) =  [M1 + (M1.M2)] . (M3 + M4)
            Aplicamos ley de absorcion
            C(x) = M1.(1 + M2) . (M3 + M4)
            C(x) = M1 . (M3 + M4)

'''
# PARTE 3 Tabla de verdad y FND y mapa de karnaugh
'''
        Entonces, C(x) = (x > 0) . [(x < 1/2) + (x = 1/2)]

        de estos valores, armando una tabla podemos definir que

        | x > 0  | x < 1/2 | x = 1/2 | [(x < 1/2) + (x = 1/2)] | (x > 0) . [(x < 1/2) + (x = 1/2)] |
        |   0    |   0     |    0    |            0            |          0                        |
        |   0    |   0     |    1    |            1            |          0                        |
        |   0    |   1     |    0    |            1            |          0                        |
        |   0    |   1     |    1    |            1            |          0                        |
        |   1    |   0     |    0    |            0            |          0                        |
        |   1    |   0     |    1    |            0            |          1                        |
        |   1    |   1     |    0    |            1            |          1                        |
        |   1    |   1     |    1    |            1            |          1                        |

        Que si partieramos de esta tabla, nuestra funcion booleana seria:

        F(A,B,C)= (A⋅!B⋅C) + (A⋅B⋅C) + (A⋅B⋅!C)

        Y aplicando mapa de karnaugh, tendriamos algo asi cómo:

       |    \ C | 0 | 1 |
       |AB   \  |   |   |
       |-----------------
       |00      |   |   |
       |01      |   |   |
       |10      |   | 1 |
       |11      | 1 | 1 |

        Tomamos este grupo

        |    \ C | 0 | 1 |
        |AB   \  |   |   |
        |-----------------
        |11      | 1 | 1 |

        y este grupo

        |    \ C | 0 | 1 |
        |AB   \  |   |   |
        |-----------------
        |10      |   | 1 |
        |11      |   | 1 |

        Nos queda:
        F(A,B,C) = A.B + A.C

        Si sacamos factor comun A, llegamos al resultado original.

        F(A,B,C) = A . (B + C)


        Ahora, podemos ajustar la condición de la función compuesta y deberíamos obtener el mismo resultado

'''

# PARTE 1 (2) : Como queda la funcion despues de los calculos


def funcionCompuesta2(x):
    if (x > 0) and (x < 0.5 or x == 0.5):
        y = math.sqrt((1/x) - 2)
        return y
    else:
        return "En FoG, la variable debe ser mayor a 0 y menor o igual que 0.5"


print("x < 0")
print(funcionCompuesta(-1))
print(funcionCompuesta2(-1))
print("x == 0")
print(funcionCompuesta(0))
print(funcionCompuesta2(0))
print("x > 0 y x < 0.5")
print(funcionCompuesta(0.2))
print(funcionCompuesta2(0.2))
print("x == 0.5")
print(funcionCompuesta(0.5))
print(funcionCompuesta2(0.5))
print("x > 0.5")
print(funcionCompuesta(1))
print(funcionCompuesta2(1))


# PARTE 5 Binario. Proceso de conversion del resultado a binario.
def convertir_a_binario(numero):
    resto = numero
    numero_binario = []
    while (numero >= 2):
        resto = numero % 2
        numero = numero // 2
        numero_binario.append(str(resto))
    numero_binario.append(str(numero))
    numero_binario.reverse()
    return "".join(numero_binario)


numero_a_validar = funcionCompuesta2(0.001)
print(
    f"el int de {numero_a_validar} es {int(numero_a_validar)}")
print(convertir_a_binario(int(numero_a_validar)))
