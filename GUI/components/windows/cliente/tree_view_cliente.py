from tkinter import IntVar, StringVar
from tkinter.ttk import Treeview, Scrollbar
from GUI.components.ttk_styles import TreeViewStyle
from GUI.components.widgets.cliente_menubar import ClienteMenuBar
from models.cliente import Cliente
from repository.clienteRepo import ClienteRepo


class ClienteView(Treeview):


    def __init__(self, master):
        
        columns_ids = ['#1','#2','#3', '#4', '#5']
        columns_names = ["Id","Nombre","Email", "Teléfono", "Direccion"]
        super().__init__(master, columns=columns_ids ,show="headings", selectmode='browse')
        self.pack(side='left', fill='both', expand=True)
        
        self.string_listener = StringVar(self)
        self.int_var = IntVar(self)
        
        self.widgetFrame = ClienteMenuBar(self)
        self.widgetFrame.pack(side='bottom')
       

        #STYLES
        self.style= TreeViewStyle(self)

        #ScrollBar Widet
        self.scroll_bar =Scrollbar(self ,orient="vertical",command=self.yview)
        self.scroll_bar.pack(side='right', fill='y')
        self.configure(yscrollcommand=self.scroll_bar.set)  
        
 
       
        for i in range(len(columns_ids)):
            self.heading(columns_ids[i], text=columns_names[i])
            self.column(columns_ids[i] ,width=160, stretch=True)
        
        self.config(displaycolumns=['#1', '#2','#3', '#4', '#5' ]) #Solo muesra las columnas indicadas por el '#ID'
        
        
        self.load_data()
        

        #TRACERS
        self.widgetFrame.string_listener.trace_add("write", self.refresh_by_search)
        self.widgetFrame.int_var.trace_add("write", self.refresh_view)

        #BIndings
        self.bind('<ButtonRelease-1>', self.get_selected_item) 
        self.bind('<KeyRelease>', self.keyReleased)

    def load_data(self,  *arg):
        
        rows = ClienteRepo().get_all()
        self.insert_rows(rows)

    def insert_rows(self, rows:list[Cliente]):
         
        for row in rows:
            self.insert("", "end", text=row, values= (row.id_cliente, row.nombre, row.email, row.telefono,  row.direccion))

    def get_selected_item(self,  *arg):

        try:
            row = self.item(self.selection())
            values =  row["values"] 
        
            row = self.item(self.selection())
            values =  row["values"] 

            self.cliente = Cliente(
                id_cliente= values[0],
                nombre= values[1],
                email=values[2],
                telefono= str(values[3]),
                direccion=values[4]

            )

        
            self.widgetFrame.cliente =  self.cliente 
        except IndexError:
            print("Selecciona un item.") 
        
         
        
    def refresh_view(self,  *arg):

        self.clean_view()
        self.load_data()    
             


    def refresh_by_search(self, *args):

        nombre =  self.widgetFrame.string_listener.get()
        if nombre:
            self.clean_view()
            rows = ClienteRepo().getByNombre(nombre)
            self.insert_rows(rows)
        else:
            self.clean_view()
            rows = ClienteRepo().get_all()
            self.insert_rows(rows)              


    def clean_view(self):
        print("cleaning")
        for child in self.get_children():
            self.delete(child)


    def keyReleased(self, event):
        print(event.keysym) 
        key = event.keysym    
        if key == "Up" or key == "Down":
            self.get_selected_item()    


