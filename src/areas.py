#!/usr/bin/env python

import math

class Areas:
	def __init__(self):
		pass

	def circle(self, _, radiusEntry, label):
		radius = float(radiusEntry.get_text())
		result = radius**2 * math.pi
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def triangle(self, _, baseEntry, heightEntry, label):
		result = float(baseEntry.get_text()) * float(heightEntry.get_text()) / 2
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def square(self, _, sideEntry, label):
		result = float(sideEntry.get_text())**2
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def rectangle(self, _, baseEntry, heightEntry, label):
		result = float(baseEntry.get_text()) * float(heightEntry.get_text())
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def rhombus(self, _, diag1Entry, diag2Entry, label):
		result = float(diag1Entry.get_text()) * float(diag2Entry.get_text()) / 2
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def parallelogram(self, _, baseEntry, heightEntry, label):
		result = float(baseEntry.get_text()) * float(heightEntry.get_text())
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def trapezoid(self, _, base1Entry, base2Entry, heightEntry, label):
		result = (float(base1Entry.get_text()) + float(base2Entry.get_text())) / 2 * float(heightEntry.get_text())
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def polygon(self, _, numberEntry, sideEntry,  label):
		angle = 360 / float(numberEntry.get_text())
		halfAngle = angle / 2
		halfSide = float(sideEntry.get_text()) / 2
		apothem = halfSide / math.tan(halfAngle * math.pi / 180)
		perimeter = float(numberEntry.get_text()) * float(sideEntry.get_text())
		result = apothem * perimeter / 2
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))