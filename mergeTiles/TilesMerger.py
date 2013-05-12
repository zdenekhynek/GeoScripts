import os
import urllib

from PIL import Image

class TilesMerger:
	
	serverUrl = ""

	def __init__( self, serverUrl, customTilesFolder, finalTilesFolder ):
		self.serverUrl = serverUrl
		self.customTilesFolder = customTilesFolder
		self.finalTilesFolder = finalTilesFolder

	def getTiles( self, tilesDict ):
		for zoomLevel in tilesDict:
			tilesBounds = tilesDict[ zoomLevel ]
			
			#itirate over x
			xMin = tilesBounds[0]
			xMax = tilesBounds[1]
			xDif = xMax - xMin + 1
			
			for i in range( xDif ):
				
				x = xMin + i

				#itirate over y
				yMin = tilesBounds[2]
				yMax = tilesBounds[3]
				yDif = yMax - yMin + 1

				for q in range( yDif ):	
					y = yMin + q
					self.processTile( zoomLevel, x, y )

	def processTile( self, zoomLevel, x, y ):

		subFolderName = str( zoomLevel ) + "/" + str( x )
		ymax  = 1 << zoomLevel;
		y2 = ymax - y -1;
		
		imageName = str( y2 ) + ".jpg"

		#tiles from maptiler are ranked differently, need to do translation
		mapTilerImageName = str( y ) + ".png"

		#create base folder name, replace slashes
		baseFolderName = self.serverUrl
		baseFolderName = baseFolderName.replace( "/", "-" )

		#full path folder
		folderName = baseFolderName + "/" + subFolderName 

		#create folder if it doesn't exist
		if not os.path.exists( folderName ):
			os.makedirs( folderName )

		#grab existing or non-existing image
		imagePathOnDisk = folderName + "/" + imageName
		f = open( imagePathOnDisk, "wb" )
		
		#create url of image to get from server
		imageUrlOnServer = self.serverUrl + "/" + subFolderName + "/" + imageName

		#download image from server
		f.write( urllib.urlopen( imageUrlOnServer ).read() )
		f.close()

		#create paths to other folders
		customImagePath = self.customTilesFolder + "/" + subFolderName + "/" + mapTilerImageName
		finalImagePath = self.finalTilesFolder + "/" + subFolderName + "/" + imageName

		self.merge( imagePathOnDisk, customImagePath, finalImagePath )

	def merge( self, image1Path, image2Path, finalImagePath ):
		
		image1 = Image.open( image1Path )
		image2 = Image.open( image2Path )

		#create final image
		finalImage = Image.new( image1.mode, image1.size, "black")
		finalImage.paste( image1 )
		finalImage.paste( image1, (0,0), image2 )

		#check if final destination exists
		finalImageFolder = os.path.dirname( finalImagePath )
		if not os.path.exists( finalImageFolder ):
			os.makedirs( finalImageFolder )

		#save final image
		finalImage.save( finalImagePath, "JPEG" )
		print "Done saving finalimage to: " + finalImagePath




		



