#!/usr/bin/env python

import math

class Volumes:
	def __init__(self):
		pass

	def sphere(self, _, radiusEntry, label):
		radius = float(radiusEntry.get_text())
		result = 4 * math.pi * radius**3 /3
		label.set_text("RESULT:  " + str(result))

	def spherical_zone(self, _, radius1Entry, radius2Entry, heightEntry, label):
		pass

	def tetrahedron(self, _, edgeEntry, label):
		pass

	def cube(self, _, edgeEntry, label):
		result = float(edgeEntry.get_text())**3
		label.set_text("RESULT:  " + str(result))

	def cone(self, _, radiusEntry, heightEntry, label):
		pass

	