GeoScripts
==========


mergeTiles

Simple script to download Open Street tiles and merge them with set of custom tiles prepared using the MapTiler software.

Parameters:
serverUrl - address of the Open Street server ( or else ) to download tiles from
customTilesFolder - name of the folder with custom tiles
finalTilesFolder - name of the folder to store merged tiles

Sample usage from command line:
python mergeTiles.py  http://otile4.mqcdn.com/tiles/1.0.0/osm customTiles finalTiles
