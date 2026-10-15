# ArcGIS-network-attribute-tools
ArcPy tool that automatically matches polyline start and end vertices to point features and populates ID and name attributes in ArcGIS Pro.

Populate Polyline Endpoint Attributes:
An ArcPy utility for ArcGIS Pro that automatically identifies the start and end points of polyline features and populates user-defined attribute fields using connected point features.

Overview:
Many GIS workflows involve networks where line features connect to point features. Examples include:
  Stream networks,
  Drainage systems,
  Utility networks,
  Pipeline networks,
  Transportation networks,
  Fiber or communication networks.
This script identifies the first and last vertex of each polyline, matches them to coincident point features, and populates start/end ID and name fields.

Features:
  Extracts start and end vertices from polyline features,
  Matches vertices to point features using coordinates,
  Populates start point attributes,
  Populates end point attributes,
  Updates multiple attribute fields automatically,
  Works with any network-like GIS dataset.

  Inputs:
    Polyline Feature,
    Point Feature containing Start_Point_ID, End_Point_ID, Start_Point_Name, End_Point_Name.

Requirements:
  ArcGIS Pro,
  ArcPy,
  Python 3.x (ArcGIS Pro environment).
  
Limitations:
  Point features must exist at the exact start and end coordinates of the polyline.
  Coordinate systems should match between datasets.
  Does not currently support spatial tolerance matching.
  
Future Enhancements:
  User-defined search tolerance,
  Nearest-point matching,
  Support for multipart polylines,
  ArcGIS Pro toolbox interface (.pyt).
  
Author:
  Unisha Ghimire.

    
