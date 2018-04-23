#!/usr/bin/env python

__autor__ = "Braulio Mendez Agra"

import pygtk
pygtk.require('2.0')
import gtk
from gui import Interface
from areas import Areas
from volumes import Volumes

class main(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)
		self.set_resizable(False)
		self.set_title("2D&3D MEASUREMENT")
		self.set_border_width(18)

		self.connect("delete-event", gtk.main_quit)

		self.areas = Areas()
		self.volumes = Volumes()
		self.interface = Interface()
		self.interface.change_screen(self, "main_menu", self.areas, self.volumes)

		self.show_all()

	def on_back_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "main_menu", self.areas, self.volumes)
		self.show_all()

	def on_circle_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "circle", self.areas, self.volumes)
		self.show_all()

	def on_triangle_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "triangle", self.areas, self.volumes)
		self.show_all()

	def on_square_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "square", self.areas, self.volumes)
		self.show_all()

	def on_rectangle_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "rectangle", self.areas, self.volumes)
		self.show_all()

	def on_rhombus_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "rhombus", self.areas, self.volumes)
		self.show_all()

	def on_parallelogram_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "parallelogram", self.areas, self.volumes)
		self.show_all()

	def on_trapezoid_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "trapezoid", self.areas, self.volumes)
		self.show_all()

	def on_polygon_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "polygon", self.areas, self.volumes)
		self.show_all()

	def on_sphere_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "sphere", self.areas, self.volumes)
		self.show_all()

	def on_spherical_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "spherical", self.areas, self.volumes)
		self.show_all()

	def on_tetrahedron_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "tetrahedron", self.areas, self.volumes)
		self.show_all()

	def on_cube_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "cube", self.areas, self.volumes)
		self.show_all()

	def on_cone_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "cone", self.areas, self.volumes)
		self.show_all()

	def on_cylinder_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "cylinder", self.areas, self.volumes)
		self.show_all()

	def on_orthohedron_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "orthohedron", self.areas, self.volumes)
		self.show_all()

	def on_octahedron_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "octahedron", self.areas, self.volumes)
		self.show_all()

	def on_pyramid_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "pyramid", self.areas, self.volumes)
		self.show_all()

	def on_pyramid_trunk_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "pyramid_trunk", self.areas, self.volumes)
		self.show_all()

	def on_prism_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "prism", self.areas, self.volumes)
		self.show_all()

	def on_torus_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_screen(self, "torus", self.areas, self.volumes)
		self.show_all()

if __name__ == '__main__':
	main()
	gtk.main()
