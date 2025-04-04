import random

caracteres ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
longitud = int(input("introduzca el tamaño de la contraseña:"))
contraseña = ""

print(random.choice(caracteres))

for i in range (longitud):
   contraseña +=random.choice(caracteres)

   print("Tu nueva contraseña mas segura a sido generada:", contraseña)
