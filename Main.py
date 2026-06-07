#Este es el archivo principal
import csv

#Primera funcion calcula los puntos de cada equipo
def CalcularPuntos(Equipos):
    for Equipo,datos in Equipos.items():
       Puntos = (datos["ganados"] *3) + (datos["empatados"])
       Equipos[Equipo]["puntos"] = Puntos;
       
       Diferencia = (datos["goles_favor"]) - (datos["goles_contra"])
       Equipos[Equipo]["diferencia_goles"] = Diferencia;

#Segunda Funcion ordena los equipos con base a sus puntos de mayor a menor
def liderTabla (Equipos):
    CopiaEquipos = Equipos.copy()
    EquiposFinales = {}

    while len(CopiaEquipos) > 0:
       EquipoMayor = None
       Puntosmax = 0
       for equipo, dato in CopiaEquipos.items():
          if dato["puntos"] > Puntosmax:
             Puntosmax = dato["puntos"]
             EquipoMayor = equipo
       EquiposFinales[EquipoMayor] = CopiaEquipos[EquipoMayor]
       del CopiaEquipos[EquipoMayor]
    return EquiposFinales


dictEquipos = {}
#lectura y gurdado de datos del archivo de entrada
with open("input/Equipos_Entrada.csv", "r") as Equipos:
    lector = csv.DictReader(Equipos)

    for fila in lector:
     dictEquipos[fila["equipo"]] = {
     "ganados": int(fila["ganados"]),
     "empatados": int(fila["empatados"]),
     "perdidos": int(fila["perdidos"]),
     "goles_favor": int(fila["goles_favor"]),
     "goles_contra": int(fila["goles_contra"])
     }

CalcularPuntos(dictEquipos)
#El diccionario final con todos los datos actualizados y ordenados
EquiposFinales = liderTabla(dictEquipos)
#lee el diccionario final por consola
"""
for llave,valor in EquiposFinales.items():
   print(llave, end=" | ")
   for llave2, valor2 in valor.items():
      print(llave2,valor2, end=" ")
   print()"""

columnas = ["equipo", "ganados", "empatados", "perdidos", "goles_favor", "goles_contra", "puntos", "diferencia_goles"]
#escribe el diccionario final en un archivo csv
with open("output/Equipos_salida", "w", newline="") as archivo_csv:
   escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)
   escritor.writeheader()
   for equipo, datos in EquiposFinales.items():
      fila = datos.copy()
      fila["equipo"] = equipo
      escritor.writerow(fila)