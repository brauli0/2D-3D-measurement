#!/usr/bin/env python3

__autor__ = "Braulio Méndez Agra"

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Events:
	def __init__(self):
		pass

	def on_exit_clicked(self, widget, x = None):
		dialog = Gtk.Dialog("Do you want to exit?", widget.get_toplevel(), Gtk.DialogFlags.DESTROY_WITH_PARENT, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
		dialog.set_resizable(False)
		box = dialog.get_content_area()
		box.set_margin_top(18)
		box.set_margin_right(18)
		box.set_margin_left(18)
		box.set_margin_bottom(18)
		box.show_all()
		answer = dialog.run()
		dialog.destroy()
		if answer == Gtk.ResponseType.OK:
			Gtk.main_quit()
			return False
		else:
			return True

	def on_buttonArea_clicked(self, widget):
		print("Area")

	def on_buttonVolume_clicked(self, widget):
		print("Volume")
		

class Interface(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="2D&3D MEASUREMENT")
		self.set_resizable(False)

		events = Events()
		self.connect("delete-event", events.on_exit_clicked)

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
		self.add(box)
		box.set_margin_top(50)
		box.set_margin_right(200)
		box.set_margin_left(200)
		box.set_margin_bottom(50)
		buttonArea = Gtk.Button(label="Area")
		buttonArea.connect("clicked", events.on_buttonArea_clicked)
		box.add(buttonArea)
		buttonVolume = Gtk.Button(label="Volume")
		buttonVolume.connect("clicked", events.on_buttonVolume_clicked)
		box.add(buttonVolume)

		self.show_all()

if __name__ == '__main__':
	window = Interface()
	Gtk.main()
