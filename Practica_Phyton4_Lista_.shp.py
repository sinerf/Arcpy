import arcpy
dir=r"C:\Student\DatosPracticaPhyton"
desDir=arcpy.Describe(dir)
listaSHPD=[]
for hijosDir in desDir.children:
    for nietosDir in hijosDir.children:
        if nietosDir.name[-4:]==r".shp":
            listaSHPD.append(nietosDir)
for D in listaSHPD:
    print(D.catalogPath)
