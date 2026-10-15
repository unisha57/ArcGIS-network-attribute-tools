import arcpy

# =============================================================================
# Populate Polyline Start and End Attributes
#
# Description:
#     Matches the start and end vertices of polylines to coincident point
#     features and populates user-defined ID and Name fields.
#
# Inputs:
#     polyline_fc  : Polyline feature class
#     point_fc     : Point feature class
#
# Requirements:
#     Point features must exist at the start and end vertices of each polyline.
# =============================================================================

arcpy.env.overwriteOutput = True

# ---------------------------------------------------------------------------
# Input Feature Classes
# ---------------------------------------------------------------------------

polyline_fc = "Polyline_Features"
point_fc = "Point_Features"

# ---------------------------------------------------------------------------
# Point Feature Fields
# ---------------------------------------------------------------------------

point_id_field = "Point_ID"
point_name_field = "Point_Name"

# ---------------------------------------------------------------------------
# Polyline Feature Fields
# ---------------------------------------------------------------------------

start_id_field = "Start_Point_ID"
end_id_field = "End_Point_ID"

start_name_field = "Start_Point_Name"
end_name_field = "End_Point_Name"

# ---------------------------------------------------------------------------
# Build Point Lookup Dictionary
# Dictionary Structure:
#     {(X, Y): (Point_ID, Point_Name)}
# ---------------------------------------------------------------------------

point_dict = {}

with arcpy.da.SearchCursor(
    point_fc,
    ["SHAPE@XY", point_id_field, point_name_field]
) as cursor:

    for xy, point_id, point_name in cursor:
        point_dict[xy] = (point_id, point_name)

print(f"Loaded {len(point_dict)} point features.")

# ---------------------------------------------------------------------------
# Populate Start and End Attributes
# ---------------------------------------------------------------------------

update_fields = [
    "SHAPE@",
    start_id_field,
    end_id_field,
    start_name_field,
    end_name_field,
]

with arcpy.da.UpdateCursor(polyline_fc, update_fields) as cursor:

    for row in cursor:

        geometry = row[0]

        start_point = geometry.firstPoint
        end_point = geometry.lastPoint

        start_xy = (start_point.X, start_point.Y)
        end_xy = (end_point.X, end_point.Y)

        start_match = point_dict.get(start_xy)
        end_match = point_dict.get(end_xy)

        if start_match:
            row[1] = start_match[0]  # Start ID
            row[3] = start_match[1]  # Start Name

        if end_match:
            row[2] = end_match[0]    # End ID
            row[4] = end_match[1]    # End Name

        cursor.updateRow(row)

print("Start and end attributes populated successfully.")
