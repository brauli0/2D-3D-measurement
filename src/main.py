#!/usr/bin/env python

__autor__ = "Braulio Mendez Agra"

import pygtk
pygtk.require('2.0')
import gtk
		
class Controller():
	def __init__(self):
		pass

	def change_screen(self, window, screen):
		if screen == 1:
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
			bbox.add(button)
			button = gtk.Button("Rectangle")
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Diamond")
			bbox.add(button)
			button = gtk.Button("Parallelogram")
			bbox.add(button)
			button = gtk.Button("Trapezoid")
			bbox.add(button)
			button = gtk.Button("Pentagon")
			bbox.add(button)
			vbox.pack_start(bbox)

			bbox = gtk.HButtonBox()
			bbox.set_border_width(5)
			bbox.set_layout(gtk.BUTTONBOX_SPREAD)
			bbox.set_spacing(30)

			button = gtk.Button("Hexagon")
			bbox.add(button)
			button = gtk.Button("Heptagon")
			bbox.add(button)
			button = gtk.Button("Octagon")
			bbox.add(button)
			button = gtk.Button("Decagon")
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

		elif screen == 2:
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
			entry = gtk.Entry(max=10)
			hbox.pack_start(entry)

			button = gtk.Button("Solve")
			vbox.pack_start(button, padding=10)

			label = gtk.Label("RESULT:  ")
			vbox.pack_start(label, padding=10)

		elif screen == 3:
			# TRIANGLE
			window.box = gtk.VBox()
			window.add(window.box)

			label = gtk.Label("TRIANGLE")
			window.box.add(label)
			
		else:
			print("Entrou aqui")

class main(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_resizable(False)
		self.set_title("2D&3D MEASUREMENT")
		self.set_border_width(18)

		self.connect("delete-event", gtk.main_quit)

		self.controller = Controller()
		self.controller.change_screen(self, 1)

		self.show_all()

	def on_circle_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, 2)
		self.show_all()

	def on_triangle_clicked(self, widget):
		self.remove(self.box)
		self.controller.change_screen(self, 3)
		self.show_all()

if __name__ == '__main__':
	main()
	gtk.main()
