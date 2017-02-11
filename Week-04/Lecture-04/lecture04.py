# ==========================================================================
#
# LECTURE 04 PYTHON EXAMPLES
#
# ==========================================================================
#
# SOC 4650/5650: Intro to GIS
# Christopher Prener, PhD
# Created: 09 Feb 2017
# Updated: 10 Feb 2017
#
# Filename: lecture04.py
#
# Description:
#   This script illustrates techniques for setting the working directory
#   and ArcPy environment using functions, setting and using relative
#   file paths using variables, importing and ordering layers in the
#   table of contents, enabling and modifying labels, executing sql
#   queries, and renaming layers.
#
# Assumptions:
#   Course file structure is in place where SOC5650 is in the root
#   directory, a .mxd file named Lecture-04-Py.mxd is saved in the Week-04
#   lecture directory. Data should be saved in the ExampleData directory.
#
# Dependencies: os module, arcpy module
#
# ==========================================================================

# INITIAL SET-UP

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### import modules
import arcpy
import os

### set working directory to root directory of drive
os.chdir(os.path.abspath(os.sep))

### set arcpy environment to root directory of drive
arcpy.env.workspace = os.path.abspath(os.sep)

### set path variable for assignment directory
workDir = "SOC5650/Lectures/Week-04/"

### set path variable to data directories
data1 = "SOC5650/Data/ExampleData/Shapefiles/"
data2 = "SOC5650/Data/ExampleData/PublicSafety.gdb/"

### set map variables
mxd = arcpy.mapping.MapDocument(workDir + 'Lecture-04-Py.mxd')
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]

# ==========================================================================

# EDIT MAP DOCUMENTS

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### delete current layers in map

for lyr in arcpy.mapping.ListLayers(mxd, '', df):
    arcpy.mapping.RemoveLayer(df, lyr)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### add city boundary to map document

boundaryShp = arcpy.mapping.Layer(data1 + 'STL_BOUNDARY_City.shp')
arcpy.mapping.AddLayer(df, boundaryShp, "BOTTOM")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### add major bodies of water to map document

hydroShp = arcpy.mapping.Layer(data1 + 'STL_HYDRO_MajorBodies.shp')
arcpy.mapping.AddLayer(df, hydroShp, "TOP")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### add major fire stations to map document

fireFC = arcpy.mapping.Layer(data2 + 'STL_PUBLICSAFETY_FireStations')
arcpy.mapping.AddLayer(df, fireFC, "TOP")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

### edit fire stations layer

for lyr in arcpy.mapping.ListLayers(mxd, '', df):
    if lyr.name == "STL_PUBLICSAFETY_FireStations":

        # label fire stations
        lyr.supports("LABELCLASSES")
        lyr.showLabels = True
        lyr.labelClasses[0].expression = '"Station " & ' + "[stationID]"

        # execute sql query for stations in Battalion 6
        lyr.definitionQuery = "battalion = 6"

        # rename layer to reflect queried data
        lyr.name == "Battalion 6"

# ==========================================================================

# FINAL STEPS

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# save map document
mxd.save()

# export pdf
arcpy.mapping.ExportToPDF(mxd, "output.pdf")

# clean up environment
del mxd
