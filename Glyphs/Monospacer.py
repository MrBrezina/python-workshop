#MenuTitle: Monospacer
# -*- coding: utf-8 -*-
__doc__="""
Extend width of all selected glyphs while increasing RSB and LSB equally.
"""

import GlyphsApp

font = Glyphs.font
selectedLayers = font.selectedLayers

font.disableUpdateInterface()

newWidth = 610

for layer in selectedLayers:
	thisGlyph = layer.parent
	thisGlyph.beginUndo()
	layer.LSB += float(newWidth - layer.width) / 2
	# no need to set RSB if width is set
	layer.width = newWidth
	thisGlyph.endUndo()

font.enableUpdateInterface()
