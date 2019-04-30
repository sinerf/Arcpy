import arcpy
field=r"C:\Student\DatosPracticaPhyton\32044"
des=arcpy.Describe(field)
for children in des.children:
    print(children.catalogPath)