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
   listaIgualNombre = []
   for shpD in listaSHPD:
       if shpD.baseName==nombreUnico:
           listaIgualNombre.append(shpD.catalogPath)
   arcpy.Merge_management(listaIgualNombre,os.path.join(gdb,nombreUnico))