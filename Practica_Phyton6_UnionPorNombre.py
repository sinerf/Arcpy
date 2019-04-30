import arcpy
import os
arcpy.env.overwriteOutput=True
gdb=r"C:\Student\Proyectos\Phyton\Phyton.gdb"
dir=r"C:\Student\DatosPracticaPhyton"
desDir=arcpy.Describe(dir)
listaSHPD=[]
listaNombres=[]
for hijosDir in desDir.children:
   for nietosDir in hijosDir.children:
       if nietosDir.name[-4:]==r".shp":
           listaSHPD.append(nietosDir)
           listaNombres.append(nietosDir.baseName)
ListaNombresUnicos=set(listaNombres)
for nombreUnico in ListaNombresUnicos:
   listaIgualNombrePuntos = []
   listaIgualNombreLineas = []
   listaIgualNombreArea = []
   for shpD in listaSHPD:
       if shpD.baseName==nombreUnico and shpD.dataElementType=='Point':
           listaIgualNombrePuntos.append(shpD.catalogPath)
       if shpD.baseName == nombreUnico and shpD.dataElementType == 'Polyline':
           listaIgualNombreLineas.append(shpD.catalogPath)
       if shpD.baseName == nombreUnico and shpD.dataElementType == 'Shape':
           listaIgualNombreArea.append(shpD.catalogPath)
   arcpy.Merge_management(listaIgualNombrePuntos,os.path.join(gdb,nombreUnico+'Puntos'))
   arcpy.Merge_management(listaIgualNombreLineas, os.path.join(gdb, nombreUnico+'Lineas'))
   arcpy.Merge_management(listaIgualNombreArea, os.path.join(gdb, nombreUnico+'Areas'))