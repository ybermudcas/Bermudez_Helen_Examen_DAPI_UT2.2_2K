datos = {}

while True:
    hora = input("A qué hora ha pasado el corredor?")
    punto_kolimétrico = input("En qué kilometro se encontraba?")
    carrera = bool(input("Si el corredor terminó la carrera escribir True, si el corredor no terminó escribir False"))

    datos[hora] = punto_kolimétrico

    if carrera == True:
        print("El corredor a las", datos.keys, "estaba en el km", punto_kolimétrico)

    else:
        print()