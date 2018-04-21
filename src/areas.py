#!/usr/bin/env python

PI = 3.14159265359

class Areas(object):
	def __init__(self):
		pass

	def circle(self, _, radiusEntry, label):
		radius = float(radiusEntry.get_text())
		result = radius**2 * PI
		label.set_text("RESULT:  " + str(result))