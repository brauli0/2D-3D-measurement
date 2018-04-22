#!/usr/bin/env python

__autor__ = "Braulio Mendez Agra"

import pygtk
pygtk.require('2.0')
import gtk
from areas import Areas

class Controller():
	def __init__(self):
		pass

	def change_screen(self, window, screen, areas):
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

			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
			bbox.add(button)
			button = gtk.Button("volume")
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

class main(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_resizable(False)
		self.set_title("2D&3D MEASUREMENT")
		self.set_border_width(18)

		self.connect("delete-event", gtk.main_quit)

		self.areas = Areas()
		self.controller = Controller()
		self.controller.change_screen(self, "main_menu", self.areas)

		self.show_all()

	def on_back_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "main_menu", self.areas)
		self.show_all()

	def on_circle_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "circle", self.areas)
		self.show_all()

	def on_triangle_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "triangle", self.areas)
		self.show_all()

	def on_square_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "square", self.areas)
		self.show_all()

	def on_rectangle_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "rectangle", self.areas)
		self.show_all()

	def on_rhombus_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "rhombus", self.areas)
		self.show_all()

	def on_parallelogram_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "parallelogram", self.areas)
		self.show_all()

	def on_trapezoid_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "trapezoid", self.areas)
		self.show_all()

	def on_polygon_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, "polygon", self.areas)
		self.show_all()

if __name__ == '__main__':
	main()
	gtk.main()
