import os
import shutil

def generar_tabla_archivos(directorio):
    tabla = []
    for ruta, carpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            nombre, extension = os.path.splitext(archivo)
            print("nombre=",nombre)

            if extension.lower() in ['.rvt', '.nwd', '.nwc', '.nwf']:
                partes = nombre.split('_')
                #print("partes=", partes)
                if len(partes) >= 4:
                    patron = partes[2]
                    if patron == 'X':
                       patron = partes[1]
                       if patron not in tabla:
                        tabla.append(patron)

    return tabla

directorio_base = 'W:\\ControlDocumental\\01 RECIBIDA'
#tabla_generada = generar_tabla_archivos(directorio_base)
tabla_generada = ["ESP","T2C","T2M","VDT","MAS","T2E","ESO","T2D","T2F","T2X","ES6","CJV","GEN","T1A","T1M","ES1","T1X","P01","P02","PBB-T1M","CTR","HDG","LAN","PDI","SEL"]

# Imprimir la tabla construida
for item in tabla_generada:
    print(item)

patron = tabla_generada[23]

print("patron=",patron)

for ruta, carpetas, archivos in os.walk(directorio_base):
    #print("ruta:",ruta)
    #ruta: W:\ControlDocumental\01 RECIBIDA\2016\C-NP-0717-0576-16\REV - ACTUALIZADA\05-PROYECTO VIAL GENERAL\C-3
    
    ruta_lista = ruta.split('\\')
    if len(ruta_lista) > 4:
       carta = ruta_lista[4]
      
    if len(ruta_lista) > 3:
       anno = ruta_lista[3]
       ruta_nueva = "W:\\BIM\\" + patron + "\\" + anno
    
    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)
        #print("nombre=",nombre)

        if extension.lower() in ['.rvt', '.nwd', '.nwc', '.nwf']:
           partes = nombre.split('_')
           #print("partes=", partes)
           if len(partes) >= 4:
              if patron == partes[2] or patron == partes[1]:
                 print("Carta:",carta)
                 print("nombre:",nombre)
                 # Obtener el nuevo nombre del archivo
                 nuevo_nombre = f'{os.path.splitext(archivo)[0]}_{carta}{extension}'
                 # Ruta completa del archivo antiguo y nuevo
                 ruta_nombre_antigua = os.path.join(ruta, archivo)
                 ruta_nombre_nueva =   os.path.join(ruta_nueva, nuevo_nombre)  #E:\BIM\PDI\2016


                 # copiar el archivo
                 # os.copiar(archivo, ruta_nombre_nueva)

                 #import shutil

                 #carpeta_origen = r'C:\ruta\de\la\carpeta\A'
                 #carpeta_destino = r'C:\ruta\de\la\carpeta\B'
                 #nombre_archivo_origen = 'pepito.txt'
                 #nombre_archivo_destino = 'pepito.2023.txt'

                 #ruta_origen = carpeta_origen + '\\' + nombre_archivo_origen
                 #ruta_destino = carpeta_destino + '\\' + nombre_archivo_destino

                 #shutil.copy(ruta_origen, ruta_destino)


                 shutil.copy(ruta_nombre_antigua, ruta_nombre_nueva)
                 #print(f'Se ha renombrado "{archivo}" a "{nuevo_nombre}"')
                 print(f'Se ha copiado "{archivo}" a "{ruta_nombre_nueva}"')