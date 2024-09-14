import string
import time

# Crear una lista con todas las letras del abecedario en mayúsculas
abecedario = list(string.ascii_uppercase)

# Solicitar el nombre del usuario
nombre_input = input("INGRESE EL NOMBRE: ")
nombre = nombre_input.upper()

# Variable para almacenar el resultado final
final = ""

# Procesar cada letra del nombre ingresado
for letra_nombre in nombre:
    if letra_nombre == " ":  # Si es un espacio, simplemente agregarlo
        final += " "
        #print(" ")
        continue

    # Iterar sobre el abecedario hasta alcanzar la letra correspondiente
    for letra_abc in abecedario:
        print(final + letra_abc, end="\r")  # Mostrar la letra que se va alcanzando
        time.sleep(0.1)  # Añadir una pequeña pausa para mostrar el progreso
        
        if letra_abc == letra_nombre:  # Cuando se alcanza la letra, se agrega al resultado
            final += letra_abc
            break

# Mostrar el re