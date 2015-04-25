#MenuTitle: Chopper
# -*- coding: utf-8 -*-
__doc__="""
Chop all contours in all selected layers into individual segments.
"""

import GlyphsApp

font = Glyphs.font

selectedLayers = font.selectedLayers

font.disableUpdateInterface()

for layer in selectedLayers:
	thisGlyph = layer.parent
	thisGlyph.beginUndo()

	tempPaths = []
	for path in layer.paths:
		for segment in path.segments:
			tempPath = GSPath()
			tempNodes = []
			for node in path.nodes:
				if node.position in segment:
					tempNodes.append(node)
			tempPath.nodes = tempNodes
			tempPath.segments = [segment]
			tempPaths.append(tempPath)

	layer.paths = tempPaths

	thisGlyph.endUndo()

font.enableUpdateInterface()
