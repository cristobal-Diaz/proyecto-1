import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class dialog():


    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./window.iu")
    
        self.dialog = self.builder.get_object("dialog")

        self.boton = self.builder.get_object("boton")
        self.boton.connect("clicked", self.dialog.destroy)

        self.dialog.show_all()


if __name__ == "__main__":
    MainWindow()
    Gtk.main()