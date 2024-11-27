from tkinter.ttk import Treeview, Scrollbar
from models.orden import Orden
from ...ttk_styles import TreeViewStyle
from repository.ordenRepo import OrdenRepo

class OrdenesView(Treeview):

    repo = OrdenRepo()

    def __init__(self, master):

        

        columns_ids = ['#1','#2','#3', '#4', '#5']
        columns_names = ["Id","Id cliente","Id Producto", "Fecha", "Cantidad"]
        
        super().__init__(master, columns=columns_ids ,show="headings", selectmode='browse')
        
        self.pack(side='left', fill='both', expand=True)

        #STYLES
        self.style= TreeViewStyle(self)

        #ScrollBar Widet
        self.scroll_bar =Scrollbar(self ,orient="vertical",command=self.yview)
        self.scroll_bar.pack(side='right', fill='y')
        self.configure(yscrollcommand=self.scroll_bar.set)  
        
 
       
        for i in range(len(columns_ids)):
            self.heading(columns_ids[i], text=columns_names[i])
            self.column(columns_ids[i] ,width=160, stretch=True)
        
        
        self.load_data()


        self.config(displaycolumns=['#1', '#2','#3', '#4', '#5' ]) #Solo muesra las columnas indicadas por el '#ID'

        #self.bind('<ButtonRelease-1>', self.get_selected_item) #Cambia el estado de los botones Edit y Delet

        #TRACERS

        # common.string_listener.trace_add("write", self.refresh_view)
        # common.added.trace_add("write", self.refresh_view)

    def load_data(self,  *arg):
        
        rows = self.repo.get_all()
        self.insert_rows(rows)

    def insert_rows(self, rows:list[Orden]):
            
         for row in rows:
            self.insert("", "end", text=row, values=(row.id_orden ,row.id_cliente, row.id_producto, row.fecha, row.cantidad))    

    # def get_selected_item(self,  *arg):
        
    #     row = self.item(self.selection())
    #     common.id_ = row["values"][0] 
        
    #     print(common.id_)
         
        
    # def refresh_view(self,  *arg):

    #     if common.string_listener:
    #         self.clean_view()
    #         self.refresh_by_search()
    #         self.focus_row()
        
    #     else:
    #         self.clean_view()
    #         self.load_data()    
             


    # def refresh_by_search(self, *args):

    #     rows = Repository().get_by_query(common.string_listener.get())
    #     self.insert_rows(rows)
    #     self.focus_row()            


    # def clean_view(self):
            
    #         for child in self.get_children():
    #             self.delete(child)


    # def insert_rows(self, rows:list):
            
    #      for row in rows:
    #         self.insert("", "end", text=row[1], values= row)


    # def focus_row(self):
    #     """Algoritmo para reenfocar"""
        
    #     children_ids = [x for x in self.get_children()] #Da todos los Id de los campos Ej.. ['I012', 'I013', 'I014', 'I015', 'I016', 'I017'...]
    #     items=[self.item(item) for item in children_ids] #Da todos los items que tiene el child_ID
        
    #     for x in range(len(children_ids)):
    #         if items[x]["values"][0] == common.id_:
    #             self.focus(children_ids[x])   
    #             self.selection_set(children_ids[x])
    #             break