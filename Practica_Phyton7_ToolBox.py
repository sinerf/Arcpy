import arcpy
import os
arcpy.env.overwriteOutput=True
def Unir_Por_Nombre(gdb, dir):
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
if __name__ == "__main__":
    Unir_Por_Nombre(arcpy.GetParameterAsText(0),arcpy.GetParameterAsText(1))