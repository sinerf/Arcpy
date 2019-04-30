import arcpy
arcpy.env.overwriteOutput=True
dir=r"C:\Student\DatosPracticaPhyton"
desDir=arcpy.Describe(dir)
listaSHPD=[]
for hijosDir in desDir.children:
    for nietosDir in hijosDir.children:
        if nietosDir.name[-4:]==r".shp":
            listaSHPD.append(nietosDir)
listaNombres=[]
for shpDN in listaSHPD:
    listaNombres.append(shpDN.baseName)
ListaNombresUnicos=set(listaNombres)
print(ListaNombresUnicos)
print(len(listaNombres))
print(len(ListaNombresUnicos))