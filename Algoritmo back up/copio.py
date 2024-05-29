import os
import shutil
from os.path import getsize, getmtime

r_origen = "C:/Users/mateo/Desktop/archivo/"
r_destino = "C:/Users/mateo/Desktop/backup/"
backup_folder = "backup_folder"
class Backup:
    def __init__(self, destino=r_destino, origen=r_origen):
        print(f"Origen: {origen}")
        self.destino = destino
        self.origen = origen

    def backup(self):
        nuevo_directorio = os.path.join(self.destino, backup_folder)

        if os.path.exists(nuevo_directorio):
            print(f"El directorio de destino '{nuevo_directorio}' ya existe.")
            return
        
        shutil.copytree(self.origen, nuevo_directorio)
        
        print("Backup inicial completado")

    def listado_de_archivos(self, directorio):
        if os.listdir(directorio) == []:
            print("El directorio está vacío")
            return None
        return os.listdir(directorio)

    def backup_autoincrementado(self, ruta=backup_folder, ruta_destino=""):
        nuevo_directorio = os.path.join(self.destino, ruta)

        if ruta_destino == "":
            ruta_origen = self.origen
        else:
            ruta_origen = os.path.join(self.origen, ruta_destino)
        
        archivos = self.listado_de_archivos(ruta_origen)
        if archivos is None:
            return
        else:
            for archivo in archivos:
                origen_path = os.path.join(ruta_origen, archivo)
                destino_path = os.path.join(nuevo_directorio, archivo)
                
                if os.path.isdir(origen_path):
                    if not os.path.exists(destino_path):
                        shutil.copytree(origen_path, destino_path)
                        print(f"Carpeta '{archivo}' copiada completamente.")
                    else:
                        self.backup_autoincrementado( destino_path,origen_path)
                        print(f"ruta={ruta}/{archivo}, ruta_destino={ruta_destino}/{archivo}")
                        print(f"Carpeta '{archivo}' actualizada.")
                else:
                    self.actualizar_archivo(origen_path, destino_path)

    def actualizar_archivo(self, origen_path, destino_path):
        if not os.path.exists(destino_path):
            shutil.copy2(origen_path, destino_path)
            print(f"Archivo '{os.path.basename(origen_path)}' copiado nuevo.")
        else:
            if getmtime(origen_path) != getmtime(destino_path) or getsize(origen_path) != getsize(destino_path):
                shutil.copy2(origen_path, destino_path)
                print(f"Archivo '{os.path.basename(origen_path)}' actualizado.")
            else:
                print(f"Archivo '{os.path.basename(origen_path)}' no necesita ser actualizado.")