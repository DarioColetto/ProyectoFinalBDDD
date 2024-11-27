from tkinter import IntVar, StringVar
from tkinter.ttk import Treeview, Scrollbar
from GUI.components.widgets.prducto_menubar import ProductoMenuBar
from models.categoria import Categoria
from models.producto import Producto
from repository.productoRepo import ProductoRepo
from ...ttk_styles import TreeViewStyle


class ProductoView(Treeview):

    repo = ProductoRepo()
    

    def __init__(self, master):
          
        columns_ids = ['#1','#2','#3', '#4', '#5', '#6']
        columns_names = ["Id","Nombre","Descripcion", "Categoria", "Precio", "Stock"]
        
        super().__init__(master, columns=columns_ids ,show="headings", selectmode='browse')
        
        self.pack(side='left', fill='both', expand=True)

        self.string_listener = StringVar(self)
        self.int_var = IntVar(self)
        
        self.widgetFrame = ProductoMenuBar(self, self.int_var, self.string_listener)
        self.widgetFrame.pack(side='bottom')
        self.pack(side='left', fill='both', expand=True)

        #STYLES
        self.style= TreeViewStyle(self)

        #ScrollBar Widet
        self.scroll_bar =Scrollbar(self ,orient="vertical",command=self.yview)
        self.scroll_bar.pack(side='right', fill='y')
        self.configure(yscrollcommand=self.scroll_bar.set)  
        
 
       #Configuracion de Titulos y Columnas
        for i in range(len(columns_ids)):
            self.heading(columns_ids[i], text=columns_names[i])
            self.column(columns_ids[i] ,width=160, stretch=True)
        
        #INICIALIZA DATA
        self.load_data()

        #Solo muesra las columnas indicadas por el '#ID'
        self.config(displaycolumns=['#1', '#2','#3', '#4', '#5', '#6' ]) 

        self.bind('<ButtonRelease-1>', self.get_selected_item) #Cambia el estado de los botones Edit y Delet

        #TRACERS

        self.string_listener.trace_add("write", self.refresh_view)
        self.int_var.trace_add("write", self.refresh_view)

    def load_data(self,  *arg):
        
        rows = ProductoRepo().get_all()
        self.insert_rows(rows)

    def insert_rows(self, rows:list[Producto]):
         
        for row in rows:
            self.insert("", "end", text=row, values= (row.id_producto, row.nombre, row.descripcion, row.categoria.value, row.precio, row.stock))    

    def get_selected_item(self,  *arg):
        
        row = self.item(self.selection())
        values =  row["values"] 

        self.producto = Producto(
            id_producto= values[0],
            nombre= values[1],
            descripcion= values[2],
            categoria = Categoria(values[3]),
            precio=float (values[4]),
            stock= int(values[5])

        )

        self.widgetFrame.producto = self.producto
         
        
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