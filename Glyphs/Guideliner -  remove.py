#MenuTitle: Guideliner - remove
# -*- coding: utf-8 -*-
__doc__="""
Delete all global guidelines.
"""

import GlyphsApp

font = Glyphs.font

font.disableUpdateInterface()

# delete all global guidelines
font.selectedFontMaster.guideLines = []

font.enableUpdateInterface()
