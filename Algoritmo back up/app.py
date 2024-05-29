
from copio import Backup
menu_Status = True

r_origen = "C:/Users/mateo/Desktop/archivo/"
r_destino = "C:/Users/mateo/Desktop/backup/"
backup_folder = "backup_folder"



while menu_Status:
    print("1. Backup inicial")
    print("2. Backup autoincrementado")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        backup = Backup()
        backup.backup()
    elif opcion == "2":
        backup = Backup()
        backup.backup_autoincrementado()
    elif opcion == "3":
        menu_Status = False
    else:
        print("Opción no válida")
