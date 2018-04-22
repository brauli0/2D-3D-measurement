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

	def cylinder(self, _, radiusEntry, heightEntry, label):
		pass

	def orthohedron(self, _, edge1Entry, edge2Entry, edge3Entry, label):
		pass

	def octahedron(self, _, edgeEntry, label):
		pass

	def pyramid(self, _, areaEntry, heightEntry, label):
		pass

	def pyramid_trunk(self, _, area1Entry, area2Entry, heightEntry, label):
		pass

	def prism(self, _, areaEntry, heightEntry, label):
		pass

	def torus(self, _, greaterEntry, smallerEntry, labelResult):
		pass