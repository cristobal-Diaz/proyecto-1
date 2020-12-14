import pandas
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import hipotesis_1
import hipotesis_2
import pregunta_3
import pregunta_4
import pregunta_5
import dialog 

class Mainwindows():
    
    #metodo constructor
    def __init__(self):
        #abrir ventana principal
        self.builder = Gtk.Builder()
        self.builder.add_from_file("./window.ui")
        self.window = self.builder.get_object("window")
        self.window.connect("destroy", Gtk.main_quit)
        #boton ventana secundaria
        self.btn = self.builder.get_object("btn")
        self.btn.connect("clicked", self.desarrollador)
        #label
        self.label = self.builder.get_object("label")
        #gtk treeview = tree
        self.tree = self.builder.get_object("tree")
        self.tree.connect("cursor-changed", self.cambio)
        #combobox text 
        self.combobox_text = self.builder.get_object("combobox_text")
        self.combobox_text.set_entry_text_column(0)
        #listado de preguntas que van en el combobox text
        preguntas = ["¿El numero de muertos es mayor al número de recuperados?",
                    "Comparacion en los indices de obesidad entre LATAM - EEUU",
                    "Cuales son los 5 pa ́ıses que tienen m ́as habitantes con obesidad?",
                    "Cuales son los 5 paıses que tienen más habitantes con obesidad y que ademas los que mas muertes tienen?",
                    "¿Los paı́ses que tienen mayor consumo de alcohol son los paı́ses que más contagios confirmados tienen?"]
        
        for index in lista:

            self.combobox_text.append_text(index)

        self.comboboxtext.connect("changed", self.combobox)

        self.window.show_all


def combobox(self, cmb=None):

        if self.tree.get_columns():
            for column in self.tree.get_columns():
                self.tree.remove_column(column)
 
        it = self.combobox_text.get_active()
        if it == 0:
            self.dataframe = hipotesis_1.main()
        elif it == 1:
            self.dataframe = hipotesis_2.main()
        elif it == 2:
            self.dataframe = pregunta_3.main()
        elif it == 3:
            self.dataframe = pregunta_4.main()
        elif it == 4:
            self.dataframe = pregunta_5.main()


def abre_dialogo(self, btn=None):
    #se abre programa de la desarrollador.
    dialog.main()
    

if __name__ == "__main__":
    Mainwindows()
    Gtk.main()

