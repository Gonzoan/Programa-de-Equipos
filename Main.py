#Este es el archivo principal
import csv
dictEquipos = {}
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
for llave,valor in dictEquipos.items():
   print(llave, end=" | ")
   for llave2, valor2 in valor.items():
      print(valor2, end=" ")
   print()


#Primera funcion
def CalcularPuntos(Equipos):
    print("hola")

#Segunda Funcion
def liderTabla (Equipos):
    print("hola")

