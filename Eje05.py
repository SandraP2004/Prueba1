# Cargarmeos el raster como referencia, a un no se carga amemoria
capa1 = QgsVectorLayer("C:/Users/Nahum/Desktop/SGZ_gis/denue202211/denue_inegi_06_.shp")
capa2 = QgsVectorLayer("C:/Users/Nahum/Desktop/SGZ_gis/MAGE06-2016/conjunto de datos/06fm.shp")
miorto = QgsRasterLayer("C:/Users/Nahum/Desktop/SGZ_gis/CEM_V3_20170619_R15_E06_TIF/Colima_r15m.tif")
# Validar o preguntar si el raster es valido
miorto.isValid()
# Podemos obtener altura y ancho de la orto para saber sus filas y columnas
print("El numero de filas y columnas es: ", miorto.height(), '-',miorto.width())
print(miorto.extent())
ext = miorto.extent()
print (ext)
# obtendremos 
# <QgsRectangle: 534952 2149246, 540848 2156224>
print("Las coordenadas minimas y maximas de la imagen son:\n", ext.xMinimum(), ext.yMinimum(), ext.xMaximum(),ext.yMaximum())
QgsProject.instance().addMapLayer(miorto)
QgsProject.instance().addMapLayer(capa1)
QgsProject.instance().addMapLayer(capa2)
#La ultima linea agrega al visor la imagen, cuando claramente desde antes sin cargar ya podiamos 
#trabajar con la imagen


