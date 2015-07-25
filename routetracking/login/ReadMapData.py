
def ReadMap(Filename="Data.xls",Location_Column=1,Latitude_Column=2,Longitude_Column=3,Elevation_Column=4,Marker_Text_Column=5,Loc="Loc",Lat="Lat",Lng="Lng",Elv="Elv",Mrkr="Mrkr"):

	import xlrd

	GeoRouteData={}

	Excel=xlrd.open_workbook(Filename)
	TotalSheets=Excel.nsheets

	for SheetNumber in range(0,TotalSheets):

		Sheet=Excel.sheet_by_index(SheetNumber)
		LastRow=Sheet.nrows
		LastCol=Sheet.ncols
		RouteData={}
				
		for Row in range(1,LastRow):
			for Col in range(1,LastCol):
				Location=str(Sheet.row_values(Row)[Location_Column])
				Latitude=str(Sheet.row_values(Row)[Latitude_Column])
				Longitude=str(Sheet.row_values(Row)[Longitude_Column])
				Elevation=str(Sheet.row_values(Row)[Elevation_Column])
				Marker_Text=str(Sheet.row_values(Row)[Marker_Text_Column])

				LocationDetails={Lat:Latitude,Lng:Longitude,Elv:Elevation,Mrkr:Marker_Text}
				RouteData[str(Location)]=LocationDetails
				GeoRouteData[str(SheetNumber)]=RouteData

	return GeoRouteData


#GeoRouteData=ReadMap("MapCoordinates.xls")
#
#
#for Sheet in GeoRouteData.keys():
#	L0=GeoRouteData[Sheet]
#	for Location in L0.keys():
#		L1=L0[Location]
#		for key1 in L1.keys():
#			print "Sheet Number : => " + Sheet + " Location : => " + Location	
#			print key1 + " : => " + L1[key1]
