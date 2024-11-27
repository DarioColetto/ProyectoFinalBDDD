from tkinter import IntVar, StringVar
from tkinter.ttk import Treeview, Scrollbar
from GUI.components.ttk_styles import TreeViewStyle
from GUI.components.widgets.cliente_menubar import ClienteMenuBar
from models.cliente import Cliente
from repository.clienteRepo import ClienteRepo


class ClienteView(Treeview):


    cliente:Cliente

    def __init__(self, master):
        
        columns_ids = ['#1','#2','#3', '#4', '#5']
        columns_names = ["Id","Nombre","Email", "Teléfono", "Direccion"]
        super().__init__(master, columns=columns_ids ,show="headings", selectmode='browse')
        self.pack(side='left', fill='both', expand=True)
        
        self.string_listener = StringVar(self)
        self.int_var = IntVar(self)
        
        self.widgetFrame = ClienteMenuBar(self, self.int_var, self.string_listener)
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
        self.bind('<ButtonRelease-1>', self.get_selected_item) #Cambia el estado de los botones Edit y Delet

        #TRACERS

        self.string_listener.trace_add("read", self.refresh_view)
        self.int_var.trace_add("write", self.refresh_view)


        

    def load_data(self,  *arg):
        
        rows = ClienteRepo().get_all()
        self.insert_rows(rows)

    def insert_rows(self, rows:list[Cliente]):
         
        for row in rows:
            self.insert("", "end", text=row, values= (row.id_cliente, row.nombre, row.email, row.telefono,  row.direccion))

    def get_selected_item(self,  *arg):
        
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
        
        
         
        
    def refresh_view(self,  *arg):

        print(self.int_var.get())

        self.clean_view()
        self.load_data()    
             


    # def refresh_by_search(self, *args):

    #     rows = Repository().get_by_query(common.string_listener.get())
    #     self.insert_rows(rows)
    #     self.focus_row()            


    def clean_view(self):
        print("cleaning")
        for child in self.get_children():
            self.delete(child)





    # def focus_row(self):
    #     """Algoritmo para reenfocar"""
        
    #     children_ids = [x for x in self.get_children()] #Da todos los Id de los campos Ej.. ['I012', 'I013', 'I014', 'I015', 'I016', 'I017'...]
    #     items=[self.item(item) for item in children_ids] #Da todos los items que tiene el child_ID
        
    #     for x in range(len(children_ids)):
    #         if items[x]["values"][0] == common.id_:
    #             self.focus(children_ids[x])   
    #             self.selection_set(children_ids[x])
    #             break