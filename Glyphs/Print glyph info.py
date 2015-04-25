#MenuTitle: Print glyph info

__doc__ = """
Prints name, unicode, LSB, RSB, and width for all selected glyphs
"""

import GlyphsApp

print "name | unicode | LSB | RSB | width"

for layer in Glyphs.font.selectedLayers:
	print "%s | %s | %d | %d | %d" % (layer.parent.name, layer.parent.unicode, layer.LSB, layer.RSB, layer.width)
