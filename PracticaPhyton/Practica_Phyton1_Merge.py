import arcpy
import os
arcpy.env.overwriteOutput=True
tf=r"C:\Student\DatosPracticaPhyton\32044\BTN25_ETRS_BCN0201L_CUR_NIV_line.shp"
jf=r"C:\Student\DatosPracticaPhyton\32045\BTN25_ETRS_BCN0201L_CUR_NIV_line.shp"
gdb=r"C:\Student\Proyectos\Phyton\Phyton.gdb"
of=r"BTN25_ETRS_BCN0201L_CUR_NIV_line_Merge"
arcpy.Merge_management([tf,jf],os.path.join(gdb,of))