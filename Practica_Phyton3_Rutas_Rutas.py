import arcpy
dir=r"C:\Student\DatosPracticaPhyton"
desDir=arcpy.Describe(dir)
for hijosDir in desDir.children:
    print(hijosDir.catalogPath)
    for nietosDir in hijosDir.children:
        print(nietosDir.catalogPath)