import time

# Contar del 0 al 15
for i in range(16):
    binario = bin(i)[2:].zfill(4)  # convierte a binario, saca '0b' y rellena con ceros hasta 4 bits
    print(f"{i} -> {binario}")
    time.sleep(0.5)  # retardo de 0.5 segundos (se puede cambiar)
