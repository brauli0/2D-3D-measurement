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
		
class Interface():
	def __init__(self):
		pass

	def change_box(self, window, events, screen):
		if screen == 1:
			window.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
			window.add(window.box)
			window.box.set_margin_top(50)
			window.box.set_margin_right(200)
			window.box.set_margin_left(200)
			window.box.set_margin_bottom(50)
			buttonArea = Gtk.Button(label="Button 1")
			buttonArea.connect("clicked", window.on_button1_clicked)
			window.box.add(buttonArea)
		elif screen == 2:
			window.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
			window.add(window.box)
			window.box.set_margin_top(50)
			window.box.set_margin_right(200)
			window.box.set_margin_left(200)
			window.box.set_margin_bottom(50)
			buttonArea = Gtk.Button(label="Button 2")
			buttonArea.connect("clicked", window.on_button2_clicked)
			window.box.add(buttonArea)
		else:
			print("Entrou aquí")

class main(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="2D&3D MEASUREMENT")
		self.set_resizable(False)

		self.events = Events()
		#self.connect("delete-event", events.on_exit_clicked)
		self.connect("delete-event", Gtk.main_quit)

		self.interface = Interface()
		self.interface.change_box(self, self.events, 1)

		self.show_all()

	def on_button1_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_box(self, self.events, 2)
		self.show_all()

	def on_button2_clicked(self, widget):
		self.remove(self.box)
		self.interface.change_box(self, self.events, 1)
		self.show_all()

if __name__ == '__main__':
	main()
	Gtk.main()
