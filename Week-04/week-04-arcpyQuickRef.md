# SOC 4650/5650: Week 04 `ArcPy` Quick Reference
#### Christopher Prener, PhD
#### 10 Feb 2017

---

## Basic Python
### Import modules
`import moduleName`

`import os`

### Change Working Directory
`os.chdir(filePath)`

### Get Drive Letter (Windows only)
`os.path.abspath(os.sep)`

### Assign Value to Variable
`varname = numValue`

`varname = "strValue"`

*Variables are used to store individual values in Python, for example `x = 2`.*

### Concatenate Strings

Two variables - `varname1 + varname2`

Variable and string - `varnme + 'stringText'`

---

### `ArcPy`
#### Set Map Document
`mxd = arcpy.mapping.MapDocument(filePath)`

*The `mxd` variable could be any name, but the norm within the `ArcPy` community is to use `mxd`. We'll follow this norm this semester. Many of the functions for `ArcPy` require this variable.*

#### Set Data Frame
`df = arcpy.mapping.ListDataFrames(mxd, "dataFrame")[0]`

*The `df` variable could be any name, but the norm within the `ArcPy` community is to use `df`. We'll follow this norm this semester. Many of the functions for `ArcPy` require this variable.*

#### Access All Layers in Table of Contents
`for lyr in arcpy.mapping.ListLayers(mxd, '', df):`

*This creates an array that stores all of the layer names in a specified data frame in the array `lyr`.*

#### Remove Layer
`arcpy.mapping.RemoveLayer(df, lyr)`

*When `lyr` is an array and not a single layer name, this will remove all layers in the array.*

#### Identify Layer
`layerVar = arcpy.mapping.Layer(filePath)`

*This function should be executed before adding a layer to the map.*

#### Add Layer to Map
`arcpy.mapping.AddLayer(df, layerVar, add_position)`

*This assumes that the layer reference has already been stored in a variable, as the week-04 files demonstrate. The `add_position` can be set as `"BOTTOM"`, `"TOP"`, and `"AUTO_ARRANGE"`.*

#### Change Layer Name
`lyr.name == "layer name"`

#### Query Layer
`lyr.definitionQuery = "attribute = val"`

*See ArGIS's [help site](http://desktop.arcgis.com/en/arcmap/10.3/map/working-with-layers/building-a-query-expression.htm#GUID-C05F4A2C-0CE4-4629-A36C-EBCB22E1B7C9) for details on constructions query expressions.*

