from tkinter import Tk
from tkinter import ttk

from GUI.components.windows.cliente.tree_view_cliente import ClienteView
from GUI.components.windows.ordenes.tree_view_ordenes import OrdenesView
from GUI.components.windows.producto.tree_view_producto import ProductoView

from .config_geometry import config_geometry




class MainWindow(Tk):
    
    
    def __init__(self):
        
        super().__init__()
        self.geometry(config_geometry(self, 1200, 800))
        self.config(background='DarkGoldenrod2', highlightthickness=4,
                    highlightbackground="grey15", highlightcolor="grey15"),
        self.resizable(True, True)
        self.minsize(550, 370)

        self.tabControl = ttk.Notebook(self) 
  
        self.tab1 = ttk.Frame(self.tabControl) 
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)  
        
        self.tabControl.add(self.tab1, text ='Clientes') 
        self.tabControl.add(self.tab2, text ='Productos') 
        self.tabControl.add(self.tab3, text ='Ordenes') 
        
        self.tabControl.pack(expand = 1, fill ="both") 

        self.clientesView = ClienteView(self.tab1)
        self.prductosView = ProductoView(self.tab2)
        self.ordenesView = OrdenesView(self.tab3)






         


