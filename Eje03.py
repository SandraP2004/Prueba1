# Programa que lista los identifidores espaciales de una capa
# paso 1) cargar una capa en QGIS
# paso 2) ejecutar lo siguiente en la consola de Python
capa = iface.activeLayer()
# Lo que se hace a continuación es obtener el nombre de la capa + UUID
print(capa.id())
#Para obtener la extensión de la capa, es necesario usar el método extensión () de la clase QgsMapLayer:
print(capa.extent().toString())
#Para saber cuántos registros o elementos espaciales contienen el vector, use lo siguiente:
print(capa.featureCount())
#Como vimos anteriormente, los vectores pueden obtenerse de diferentes fuentes, cada uno
#con sus propias capacidades y limitaciones. Para descubrir la capacidad de "capa", use el siguiente método:
print(capa.capabilitiesString())

#Para obtener el contenedor de encabezados para "capa", utilizamos el siguiente código:
encabezado = capa.fields()
print(encabezado)

#Aquí, el encabezado almacenará una instancia de campos. Podemos usar métodos de campos para agregar o
#eliminar columnas, obtener el índice de la columna por nombre con indexFromName u obtener un campo específico
#utilizando su índice con el siguiente código:
campo_0 = encabezado[0]
print (campo_0)
#Cada campo tiene sus métodos para obtener el nombre de la columna con name(), obtener su tipo con type()
#y typeName(), y también obtiene su  precision () si es numérico.

# Lo anteior puede servir como para hacer algo de
print("Cuantas columnas hay", encabezado.count())
print("Existe la columna 4?", encabezado.exists(4))
print("Existe la columna llamada 'CVEGEO' ?", encabezado.indexFromName('clee'))
print("Existe la columna llamada 'POB1' ?", encabezado.indexFromName('POB1'))
print("Columna 0 tiene el nombre", encabezado[0].name())

for columna in encabezado:
    print("Nombre: ", columna.name())
    print("Tipo: ", columna.typeName())
    print("Precision: ", columna.precision())