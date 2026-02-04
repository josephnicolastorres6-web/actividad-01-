usuario=input("ingresa tu nombre de usuario: ")
contrraseña=input("ingresa tu contraseña: ")
if usuario == "admin" and contrraseña == "1234":
    print("acceso concedido")
else:
    print("usuario o contraseña incorrectos")