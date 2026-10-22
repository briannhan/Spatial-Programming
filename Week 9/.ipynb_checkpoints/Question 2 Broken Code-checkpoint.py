# Import needed modules
import arcpy

# Set the workspace and allow overwrites
arcpy.env.workspace = # ADD FILEPATH, THIS IS NOT AN ERROR!!!

# Create a Describe object
desc = arcpy.Describe("Bangladesh_Hospitals")

# The code continues if the feature class is a shapefile
if desc.dataType == "ShapeFile":
    
    # These two variables will be used to construct SQL queries 
    amenity1 = "hospital"
    amenity2 = "pharmacy"
    
    # Create a new feature class that contains only pharmacies from the original
    pharmFeature = "Bangladesh_Pharmacies"
    whereClause = "amenity = '{0}'".format(amenity1)
    arcpy.analysis.Select("Bangladesh_Hospitals",pharmfeature,whereClause)
    
    # Same again but for the point locations of hospitals only
    hospFeature = "Bangladesh_Hosp_Only"
    whereClause = "amenity == '{0}'".format(amenity2)
    arcpy.analysis.Select("Bangladesh_Hospitals",hospFeature,whereClause)

# The else condition catches the application of a feature class that does
# not contain a shapefile
else
    print("Please check the data type of the downloaded folder and try again.")

