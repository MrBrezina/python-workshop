#MenuTitle: Change sidebearings
# -*- coding: utf-8 -*-
__doc__="""
Increase/decrease sidebearings of selected glyphs by adding specific value.
"""

import GlyphsApp

changeLSB = 200
changeRSB = 200

font.disableUpdateInterface()

for layer in Glyphs.font.selectedLayers:
	thisGlyph = layer.parent
	thisGlyph.beginUndo()
	layer.LSB += changeLSB
	layer.width += changeRSB
	thisGlyph.endUndo()

font.enableUpdateInterface()
