edad = int(input("ingresa tu edad: "))
ciudadano = input("¿Eres ciudadano? (si/no): ")

if edad >= 18 and ciudadano.lower() == "si":
    print("Eres elegible para votar.")
else:
    print("No eres elegible para votar.")