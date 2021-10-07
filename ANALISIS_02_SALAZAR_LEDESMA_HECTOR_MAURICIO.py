import csv


exp_imp = []

with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for linea in lector:
        exp_imp.append(linea)

#Funcion que recibe una lista, la filtra y regresa una lista
#con la cantidad de veces que se repiten sus elementos

def filtro(lista):
    sin_rep = []
    cantidad = []
    for item in lista:
        if item not in sin_rep:
            sin_rep.append(item)
    for elemento in sin_rep:
        cantidad.append((elemento,lista.count(elemento)))
    return cantidad

#Funcion que filtra y obtiene solo valores sin repetir

def filtra(lista): 
    sin_rep = []
    for i in range(len(lista)):
        if lista[i][0] not in sin_rep:
            sin_rep.append(lista[i][0])
    return sin_rep

#Funcion que suma por los valores deseados

def suma_total(lista_total,filtrada):
    
    valores_totales = []
    
    for i in range(len(filtrada)):
        valores_por_pais = []
        for j in range(len(lista_total)):
            if filtrada[i] == lista_total[j][0]:
                valores_por_pais.append(int(lista_total[j][1]))
        valores_totales.append((filtrada[i],sum(valores_por_pais)))
    return valores_totales

#Funcion que ordena los elementos de una lista por el segundo elemento
def ordena(lista):
    lista_ordenada = sorted(lista, key = lambda x: x[1], reverse = True)

    return lista_ordenada

"""
Rutas más demandadas
"""
#Obtenemos una lista de tuplas donde el primer elemento de nuestra tupla es el pais origen y la segunda
#es el pais destino

rutas_exportacion = []
rutas_importacion = []

for i in range(len(exp_imp)) : 
    if exp_imp[i]["direction"] == "Exports": 
        rutas_exportacion.insert(i, (exp_imp[i]["direction"],exp_imp[i]["origin"],exp_imp[i]["destination"]))
    else:
        rutas_importacion.insert(i, (exp_imp[i]["direction"],exp_imp[i]["origin"],exp_imp[i]["destination"]))
#Numero de veces que se repiten las rutas
cantidad_exportacion = filtro(rutas_exportacion)
cantidad_importacion = filtro(rutas_importacion)

lista_ordenada_exp = ordena(cantidad_exportacion)
lista_ordenada_imp = ordena(cantidad_importacion)


print("Estas son las 10 rutas más demandadas de importación y exportación \n")
print("Exportacion")

for i in range(10):
    print(lista_ordenada_exp[i][0][0],lista_ordenada_exp[i][0][1],"-",lista_ordenada_exp[i][0][2],lista_ordenada_exp[i][1])

print("\n")
print("Importacion")    
for i in range(10):
    print(lista_ordenada_imp[i][0][0],lista_ordenada_imp[i][0][1],"-",lista_ordenada_imp[i][0][2],lista_ordenada_imp[i][1])

#Creamos un archivo csv donde guardamos la información

with open("rutas_exp.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(lista_ordenada_exp)

with open("rutas_imp.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(lista_ordenada_imp)
    
"""
Medios de transporte mejor valorados
"""

medios_exp = []
medios_imp = []

for i in range(len(exp_imp)) : 
    if exp_imp[i]["direction"] == "Exports": 
        medios_exp.insert(i, [exp_imp[i]["transport_mode"],exp_imp[i]["total_value"]])
    else:
        medios_imp.insert(i, [exp_imp[i]["transport_mode"],exp_imp[i]["total_value"]])

#Listas filtradas de los medios de importacion y exportacion, donde sólo se encuentran los cuatro medios disponibles
medios_exp_filt = filtra(medios_exp)
medios_imp_filt = filtra(medios_imp)
#Listas que contienen el total de exportaciones por cada medio
total_medios_exp = suma_total(medios_exp,medios_exp_filt)
total_medios_imp = suma_total(medios_imp,medios_imp_filt)
#Listas ordenadas de mayor cantidad monetaria a menor
ordena_exp = ordena(total_medios_exp)
ordena_imp = ordena(total_medios_imp)


print("Estas son los 3 medios más demandadas de importación y exportación \n")
print("Exportacion")

for i in range(3):
    print(ordena_exp[i][0],ordena_exp[i][1])

print("\n")
print("Importacion")    
for i in range(3):
    print(ordena_imp[i][0],ordena_imp[i][1])
    

with open("medios_exp.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(ordena_exp)

with open("medios_imp.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(ordena_imp)

"""
Valor total de importaciones y exportaciones
"""
"""
Total de exportaciones e importaciones
"""

total_exp = []
total_imp = []

for i in range(len(exp_imp)) : 
    if exp_imp[i]["direction"] == "Exports": 
        total_exp.insert(i, int(exp_imp[i]["total_value"]))
    else:
        total_imp.insert(i,int(exp_imp[i]["total_value"]))
 
#Variables que obtienen el total monetario de exportacion e importacion respectivamente       
totale = sum(total_exp)
totali = sum(total_imp)
        
paises_exp = []
paises_imp = []

for i in range(len(exp_imp)): 
    if exp_imp[i]["direction"] == "Exports": 
        paises_exp.insert(i, [exp_imp[i]["origin"],exp_imp[i]["total_value"]])
    else:
        paises_imp.insert(i, [exp_imp[i]["destination"],exp_imp[i]["total_value"]])
 
#Lista que contiene a los paises exportadores e importadores  
paises_exp_filt = filtra(paises_exp)
paises_imp_filt = filtra(paises_imp)

#Listas que contienen el total de exportaciones e importaciones por pais  
total_exportaciones = suma_total(paises_exp,paises_exp_filt)
total_importaciones = suma_total(paises_imp,paises_imp_filt)
#Lista que contiene total de exportaciones e importaciones, 
#asi como el porcentaje que representan
porcentaje_exp = []
porcentaje_imp = []

for i in range(len(total_exportaciones)):
    
    porcentaje_exp.insert(i, (total_exportaciones[i][0],
                              total_exportaciones[i][1],
                              (int(total_exportaciones[i][1]) * 100 ) / totale))
for i in range(len(total_importaciones)):
    
    porcentaje_imp.insert(i, (total_importaciones[i][0],
                              total_importaciones[i][1],
                              (int(total_importaciones[i][1]) * 100 ) / totali))
#lista ordenada
porcentaje_e = ordena(porcentaje_exp)
porcentaje_i = ordena(porcentaje_imp)

print("\n")
print("Estas son los paises con mayores exportaciones e importaciones, su valor monetario, y su porcentaje")
print("\n")
print("Exportacion")

for i in range(len(porcentaje_e)):
    print(porcentaje_e[i][0],porcentaje_e[i][1],porcentaje_e[i][2])

print("\n")
print("Importacion")    
for j in range(len(porcentaje_i)):
    print(porcentaje_i[j][0],porcentaje_i[j][1],porcentaje_i[j][2])
    
with open("porcentaje_exp.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(porcentaje_e)

with open("porcentaje_imp.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(porcentaje_i)
