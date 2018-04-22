#!/usr/bin/env python

import math

class Volumes:
	def __init__(self):
		pass

	def sphere(self, _, radiusEntry, label):
		radius = float(radiusEntry.get_text())
		result = 4 * math.pi * radius**3 /3
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def spherical_zone(self, _, radius1Entry, radius2Entry, heightEntry, label):
		radius1 = float(radius1Entry.get_text())
		radius2 = float(radius2Entry.get_text())
		height = float(heightEntry.get_text())
		aux = height**2 + 3*radius1**2 + 3*radius2**2
		result = math.pi * height * aux / 6
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def tetrahedron(self, _, edgeEntry, label):
		result = math.sqrt(2) * float(edgeEntry.get_text())**3 / 12
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def cube(self, _, edgeEntry, label):
		result = float(edgeEntry.get_text())**3
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def cone(self, _, radiusEntry, heightEntry, label):
		radius = float(radiusEntry.get_text())
		height = float(heightEntry.get_text())
		result = math.pi * radius**2 * height / 3
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def cylinder(self, _, radiusEntry, heightEntry, label):
		radius = float(radiusEntry.get_text())
		height = float(heightEntry.get_text())
		result = math.pi * radius**2 * height
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def orthohedron(self, _, edge1Entry, edge2Entry, edge3Entry, label):
		result = float(edge1Entry.get_text()) * float(edge2Entry.get_text()) * float(edge3Entry.get_text())
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def octahedron(self, _, edgeEntry, label):
		edge = float(edgeEntry.get_text())
		result = math.sqrt(2) * edge**3 / 3
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def pyramid(self, _, areaEntry, heightEntry, label):
		result = float(areaEntry.get_text()) * float(heightEntry.get_text()) / 3
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def pyramid_trunk(self, _, area1Entry, area2Entry, heightEntry, label):
		area1 = float(area1Entry.get_text())
		area2 = float(area2Entry.get_text())
		height = float(heightEntry.get_text())
		aux = area1 + area2 + math.sqrt(area1*area2)
		result = height * aux / 3
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def prism(self, _, areaEntry, heightEntry, label):
		result = float(areaEntry.get_text()) * float(heightEntry.get_text())
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))

	def torus(self, _, greaterEntry, smallerEntry, label):
		greaterRadius = float(greaterEntry.get_text())
		smallerRadius = float(smallerEntry.get_text())
		result = 2 * math.pi**2 * greaterRadius * smallerRadius**2
		result = round(result, 3)
		label.set_text("RESULT:  " + str(result))