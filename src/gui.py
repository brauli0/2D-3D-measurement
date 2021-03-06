#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from areas import Areas
from volumes import Volumes

class Interface():
	def __init__(self):
		pass

	def change_screen(self, window, screen, areas, volumes):
		if screen == "main_menu":
			window.box = gtk.VBox()
			window.add(window.box)
			
			frame = gtk.Frame("Areas")
			frame.set_label_align(0.5, 0.5)
			window.box.pack_start(frame, padding=10)

			vbox = gtk.VBox()
			vbox.set_border_width(10)
			frame.add(vbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Circle")
			button.connect("clicked", window.on_circle_clicked)
			bbox.add(button)
			button = gtk.Button("Triangle")
			button.connect("clicked", window.on_triangle_clicked)
			bbox.add(button)
			button = gtk.Button("Square")
			button.connect("clicked", window.on_square_clicked)
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Rectangle")
			button.connect("clicked", window.on_rectangle_clicked)
			bbox.add(button)
			button = gtk.Button("Rhombus")
			button.connect("clicked", window.on_rhombus_clicked)
			bbox.add(button)
			button = gtk.Button("Parallelogram")
			button.connect("clicked", window.on_parallelogram_clicked)
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Trapezoid")
			button.connect("clicked", window.on_trapezoid_clicked)
			bbox.add(button)
			button = gtk.Button("Regular polygon")
			button.connect("clicked", window.on_polygon_clicked)
			bbox.add(button)
			vbox.pack_start(bbox)



			frame = gtk.Frame("Volumes")
			frame.set_label_align(0.5, 0.5)
			window.box.pack_start(frame, padding=10)

			vbox = gtk.VBox()
			vbox.set_border_width(10)
			frame.add(vbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Sphere")
			button.connect("clicked", window.on_sphere_clicked)
			bbox.add(button)
			button = gtk.Button("Spherical zone")
			button.connect("clicked", window.on_spherical_clicked)
			bbox.add(button)
			button = gtk.Button("Tetrahedron")
			button.connect("clicked", window.on_tetrahedron_clicked)
			bbox.add(button)
			button = gtk.Button("Cube")
			button.connect("clicked", window.on_cube_clicked)
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Cone")
			button.connect("clicked", window.on_cone_clicked)
			bbox.add(button)
			button = gtk.Button("Cylinder")
			button.connect("clicked", window.on_cylinder_clicked)
			bbox.add(button)
			button = gtk.Button("Orthohedron")
			button.connect("clicked", window.on_orthohedron_clicked)
			bbox.add(button)
			button = gtk.Button("Octahedron")
			button.connect("clicked", window.on_octahedron_clicked)
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Pyramid")
			button.connect("clicked", window.on_pyramid_clicked)
			bbox.add(button)
			button = gtk.Button("Pyramid trunk")
			button.connect("clicked", window.on_pyramid_trunk_clicked)
			bbox.add(button)
			button = gtk.Button("Prism")
			button.connect("clicked", window.on_prism_clicked)
			bbox.add(button)
			button = gtk.Button("Torus")
			button.connect("clicked", window.on_torus_clicked)
			bbox.add(button)
			vbox.pack_start(bbox)

		elif screen == "circle":
			# CIRCLE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("CIRCLE AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Radius:  ")
			hbox.pack_start(label)
			radiusEntry = gtk.Entry(max=10)
			hbox.pack_start(radiusEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.circle, radiusEntry, labelResult)

		elif screen == "triangle":
			# TRIANGLE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("TRIANGLE AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base:  ")
			hbox.pack_start(label)
			baseEntry = gtk.Entry(max=10)
			hbox.pack_start(baseEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.triangle, baseEntry, heightEntry, labelResult)

		elif screen == "square":
			# SQUARE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("SQUARE AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Side:  ")
			hbox.pack_start(label)
			sideEntry = gtk.Entry(max=10)
			hbox.pack_start(sideEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.square, sideEntry, labelResult)

		elif screen == "rectangle":
			# RECTANGLE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("RECTANGLE AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base:  ")
			hbox.pack_start(label)
			baseEntry = gtk.Entry(max=10)
			hbox.pack_start(baseEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.rectangle, baseEntry, heightEntry, labelResult)

		elif screen == "rhombus":
			# RHOMBUS
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("RHOMBUS AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Diagonal 1:  ")
			hbox.pack_start(label)
			diag1Entry = gtk.Entry(max=10)
			hbox.pack_start(diag1Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Diagonal 2:  ")
			hbox.pack_start(label)
			diag2Entry = gtk.Entry(max=10)
			hbox.pack_start(diag2Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.rhombus, diag1Entry, diag2Entry, labelResult)

		elif screen == "parallelogram":
			# PARALLELOGRAM
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("PARALLELOGRAM AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base:  ")
			hbox.pack_start(label)
			baseEntry = gtk.Entry(max=10)
			hbox.pack_start(baseEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.parallelogram, baseEntry, heightEntry, labelResult)

		elif screen == "trapezoid":
			# TRAPEZOID
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("TRAPEZOID AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base 1:  ")
			hbox.pack_start(label)
			base1Entry = gtk.Entry(max=10)
			hbox.pack_start(base1Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base 2:  ")
			hbox.pack_start(label)
			base2Entry = gtk.Entry(max=10)
			hbox.pack_start(base2Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.trapezoid, base1Entry, base2Entry, heightEntry, labelResult)

		elif screen == "polygon":
			# REGULAR POLYGON
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("REGULAR POLYGON AREA")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Number of sides:  ")
			hbox.pack_start(label)
			numberEntry = gtk.Entry(max=10)
			hbox.pack_start(numberEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Side length:  ")
			hbox.pack_start(label)
			sideEntry = gtk.Entry(max=10)
			hbox.pack_start(sideEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", areas.polygon, numberEntry, sideEntry, labelResult)

		# VOLUMES
		elif screen == "sphere":
			# SPHERE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("SPHERE VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Radius:  ")
			hbox.pack_start(label)
			radiusEntry = gtk.Entry(max=10)
			hbox.pack_start(radiusEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.sphere, radiusEntry, labelResult)

		elif screen == "spherical":
			# SPHERICAL
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("SPHERICAL ZONE VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Radius 1:  ")
			hbox.pack_start(label)
			radius1Entry = gtk.Entry(max=10)
			hbox.pack_start(radius1Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Radius 2:  ")
			hbox.pack_start(label)
			radius2Entry = gtk.Entry(max=10)
			hbox.pack_start(radius2Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.spherical_zone, radius1Entry, radius2Entry, heightEntry, labelResult)

		elif screen == "tetrahedron":
			# TETRAHEDRON
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("REGULAR TETRAHEDRON VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Edge:  ")
			hbox.pack_start(label)
			edgeEntry = gtk.Entry(max=10)
			hbox.pack_start(edgeEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.tetrahedron, edgeEntry, labelResult)

		elif screen == "cube":
			# CUBE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("CUBE VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Edge:  ")
			hbox.pack_start(label)
			edgeEntry = gtk.Entry(max=10)
			hbox.pack_start(edgeEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.cube, edgeEntry, labelResult)

		elif screen == "cone":
			# CONE
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("CONE VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base radius:  ")
			hbox.pack_start(label)
			radiusEntry = gtk.Entry(max=10)
			hbox.pack_start(radiusEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.cone, radiusEntry, heightEntry, labelResult)

		elif screen == "cylinder":
			# CYLINDER
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("CYLINDER VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base radius:  ")
			hbox.pack_start(label)
			radiusEntry = gtk.Entry(max=10)
			hbox.pack_start(radiusEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.cylinder, radiusEntry, heightEntry, labelResult)

		elif screen == "orthohedron":
			# ORTHOHEDRON
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("ORTHOHEDRON VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Edge 1:  ")
			hbox.pack_start(label)
			edge1Entry = gtk.Entry(max=10)
			hbox.pack_start(edge1Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Edge 2:  ")
			hbox.pack_start(label)
			edge2Entry = gtk.Entry(max=10)
			hbox.pack_start(edge2Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Edge 3:  ")
			hbox.pack_start(label)
			edge3Entry = gtk.Entry(max=10)
			hbox.pack_start(edge3Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.orthohedron, edge1Entry, edge2Entry, edge3Entry, labelResult)


		elif screen == "octahedron":
			# OCTAHEDRON
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("OCTAHEDRON VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Edge:  ")
			hbox.pack_start(label)
			edgeEntry = gtk.Entry(max=10)
			hbox.pack_start(edgeEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.octahedron, edgeEntry, labelResult)

		elif screen == "pyramid":
			# PYRAMID
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("PYRAMID VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base area:  ")
			hbox.pack_start(label)
			areaEntry = gtk.Entry(max=10)
			hbox.pack_start(areaEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.pyramid, areaEntry, heightEntry, labelResult)

		elif screen == "pyramid_trunk":
			# PYRAMID TRUNK
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("PYRAMID TRUNK VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Area 1:  ")
			hbox.pack_start(label)
			area1Entry = gtk.Entry(max=10)
			hbox.pack_start(area1Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Area 2:  ")
			hbox.pack_start(label)
			area2Entry = gtk.Entry(max=10)
			hbox.pack_start(area2Entry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.pyramid_trunk, area1Entry, area2Entry, heightEntry, labelResult)

		elif screen == "prism":
			# PRISM
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("PRISM VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Base area:  ")
			hbox.pack_start(label)
			areaEntry = gtk.Entry(max=10)
			hbox.pack_start(areaEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Height:  ")
			hbox.pack_start(label)
			heightEntry = gtk.Entry(max=10)
			hbox.pack_start(heightEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.prism, areaEntry, heightEntry, labelResult)

		elif screen == "torus":
			# TORUS
			window.box = gtk.VBox()
			window.add(window.box)

			hbox = gtk.HBox()
			window.box.pack_start(hbox, padding=10)

			vbox = gtk.VBox()
			hbox.pack_start(vbox, padding=30)

			label = gtk.Label("TORUS VOLUME")
			vbox.pack_start(label, padding=10)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Greater radius:  ")
			hbox.pack_start(label)
			greaterEntry = gtk.Entry(max=10)
			hbox.pack_start(greaterEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			label = gtk.Label("Smaller radius:  ")
			hbox.pack_start(label)
			smallerEntry = gtk.Entry(max=10)
			hbox.pack_start(smallerEntry)

			hbox = gtk.HBox()
			vbox.pack_start(hbox, padding=10)
			button = gtk.Button("BACK")
			button.connect("clicked", window.on_back_clicked)
			hbox.pack_start(button, padding=5)
			button = gtk.Button("SOLVE")
			hbox.pack_start(button, padding=5)

			labelResult = gtk.Label("RESULT: -")
			vbox.pack_start(labelResult, padding=10)

			button.connect("clicked", volumes.torus, greaterEntry, smallerEntry, labelResult)