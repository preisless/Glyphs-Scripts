#MenuTitle: Close open paths
"""Close all paths in visible layers of selected glyphs."""

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

def process( thisLayer ):
	pathCount = 0
	
	for thisPath in thisLayer.paths:
		if not thisPath.closed:
			thisPath.closed = True
			pathCount += 1
	
	return pathCount

Font.disableUpdateInterface()

print "Closing paths in %i glyphs:" % len( selectedLayers )

for thisLayer in selectedLayers:
	print "-- %s: closed %i path(s)." % ( thisLayer.parent.name, process( thisLayer ) )

Font.enableUpdateInterface()

