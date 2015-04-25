#MenuTitle: Change sidebearings (with dialogue)
# -*- coding: utf-8 -*-
__doc__="""
Increase/decrease sidebearings of selected glyphs by adding specific value.
"""

# based on Rainer Erich Scheichelbauer’s script Change Metrics by Percentage

import vanilla
import GlyphsApp

class ChangeSidebearings(object):
	def __init__(self):
		self.w = vanilla.FloatingWindow((200, 120), "Change sidebearings of selected layers", autosaveName="com.pythonworkshop.ChangeSidebearings.mainwindow")

		self.w.text_LSB = vanilla.TextBox((15, 12+2, 90, 14), "Change LSB by", sizeStyle='small')
		self.w.LSB = vanilla.EditText((105, 12, -15, 15+3), "10.0", sizeStyle = 'small')

		self.w.text_RSB = vanilla.TextBox((15, 42+2, 90, 14), "Change RSB by", sizeStyle='small')
		self.w.RSB = vanilla.EditText((105, 42, -15, 15+3), "10.0", sizeStyle = 'small')

		self.w.runButton = vanilla.Button((15, 82-1, -15, 19), "Change", sizeStyle='small', callback=self.ChangeSidebearingsMain)

		self.w.setDefaultButton(self.w.runButton)

		try:
			self.LoadPreferences()
		except:
			pass

		self.w.open()

	def SavePreferences(self, sender):
		try:
			Glyphs.defaults["com.pythonworkshop.ChangeSidebearings.LSB"] = self.w.LSB.get()
			Glyphs.defaults["com.pythonworkshop.ChangeSidebearings.RSB"] = self.w.RSB.get()
		except:
			return False

		return True

	def LoadPreferences(self):
		try:
			self.w.LSB.set(Glyphs.defaults["com.pythonworkshop.ChangeSidebearings.LSB"])
			self.w.RSB.set(Glyphs.defaults["com.pythonworkshop.ChangeSidebearings.RSB"])
		except:
			return False

		return True

	def ChangeSidebearingsMain(self, sender):
		selectedLayers = Glyphs.font.selectedLayers

		changeLSB = int(self.w.LSB.get())
		changeRSB = int(self.w.RSB.get())

		if changeLSB:
			for layer in selectedLayers:
				layer.LSB += changeLSB

		if changeRSB:
			for layer in selectedLayers:
				layer.RSB += changeRSB

		if not self.SavePreferences(self):
			print "Note: could not write preferences."


ChangeSidebearings()
