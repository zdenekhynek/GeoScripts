import sys
from TilesMerger import TilesMerger

if len( sys.argv ) != 4:
	sys.exit( "Need three arguments" )

server = sys.argv[ 1 ] 
customTilesFolder = sys.argv[ 2 ] 
outputFolder = sys.argv[ 3 ] 

tilesDict = { 
			  10: [ 507, 507, 685, 685 ],
			  11: [ 1015, 1015, 1370, 1370 ],
			  12: [ 2030, 2031, 2740, 2740 ],
			  13: [ 4061, 4062, 5480, 5481 ],
			  14: [ 8123, 8124, 10961, 10962 ],
			  15: [ 16247, 16249, 21922, 21924 ]
			}

merger = TilesMerger( server, customTilesFolder, outputFolder )
merger.getTiles( tilesDict )
