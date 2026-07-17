import random
caracteres = (
    "QWERTYUIOPASDFGHJKLZXCVBNM"
    "qwertyuiopasdfghjklzxcvbnm"
    "1234567890"
    "!#$%&/()=?¿°ñÑ"
)
longitud = int(input("Ingresar logitud de la contraseña "))
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)
    
contrasena = "".join(random.choice(caracteres) for i in range(longitud))
print(contraseña, contrasena)