#MenuTitle: Guideliner - add
# -*- coding: utf-8 -*-
__doc__="""
Delete all global guidelines from current master and add new ones stored in a list in this script.
"""

# list of global guides to add
# (x,y,angle)

globalGuidelines = [
(0,100,0),
(0,200,0),
(0,300,0),
(0,400,0),
(0,500,0),
(0,600,0),
(0,700,0),
(0,800,0),
(0,900,0),
(0,1000,0),
(400,400,15),
(400,400,30),
(400,400,45),
(400,400,60),
(400,400,75),
(400,400,90),
(400,400,105),
(400,400,120),
(400,400,135),
(400,400,150),
(400,400,165)
]

import GlyphsApp

font = Glyphs.font

font.disableUpdateInterface()

# delete guidelines
font.selectedFontMaster.guideLines = []

# add guidelines
for x,y,angle in globalGuidelines:
	guide = GSGuideLine()
	guide.position = (x,y)
	guide.angle = angle
	font.selectedFontMaster.guideLines.append(guide)

font.enableUpdateInterface()
