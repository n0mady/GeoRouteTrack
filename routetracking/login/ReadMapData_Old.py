
def ReadMap(Filename="Data.xls",Location_Column=1,Latitude_Column=2,Longitude_Column=3,Elevation_Column=4,Marker_Text_Column=5,Loc="Loc",Lat="Lat",Lng="Lng",Elv="Elv",Mrkr="Mrkr"):
	""" Module to Read the Map Coordinates from the Excel Sheet """

	import xlrd

	GeoRouteData={}

	Excel=xlrd.open_workbook(Filename)

	Sheet=Excel.sheet_by_index(0)

	LastRow=Sheet.nrows
	LastCol=Sheet.ncols


	for Row in range(1,LastRow):
		for Col in range(1,LastCol):
			
			Location=str(Sheet.row_values(Row)[Location_Column])
			Latitude=str(Sheet.row_values(Row)[Latitude_Column])
			Longitude=str(Sheet.row_values(Row)[Longitude_Column])
			Elevation=str(Sheet.row_values(Row)[Elevation_Column])
			Marker_Text=str(Sheet.row_values(Row)[Marker_Text_Column])

			GeoRouteData[Location]={Lat:Latitude,Lng:Longitude,Elv:Elevation,Mrkr:Marker_Text}

	return GeoRouteData
