from datetime import datetime
from tkinter import IntVar, StringVar
from tkinter.ttk import Treeview, Scrollbar
from GUI.components.widgets.ordenes_menubar import OrdenMenuBar
from models.orden import Orden
from models.ordenDTO import OrdenDTO
from ...ttk_styles import TreeViewStyle
from repository.ordenRepo import OrdenRepo

class OrdenesView(Treeview):

   
    def __init__(self, master):


        columns_ids = ['#1','#2','#3', '#4', '#5']
        columns_names = ["Orden Id","Cliente","Producto", "Fecha", "Cantidad"]
        super().__init__(master, columns=columns_ids ,show="headings", selectmode='browse')
        
        self.pack(side='left', fill='both', expand=True)
        self.string_listener = StringVar(self)
        self.int_var = IntVar(self)

        self.widgetFrame = OrdenMenuBar(self)
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
        self.widgetFrame.string_listener_id.trace_add("write", self.refresh_by_search_id)
        self.widgetFrame.string_listener_name.trace_add("write", self.refresh_by_search_name)
        self.widgetFrame.int_var.trace_add("write", self.refresh_view)

        #BIndings
        self.bind('<ButtonRelease-1>', self.get_selected_item) 
        self.bind('<KeyRelease>', self.keyReleased)


    def load_data(self,  *arg):
        
        rows = OrdenRepo().get_all()
        self.insert_rows(rows)

    def insert_rows(self, rows:list[OrdenDTO]):
            
         for row in rows:
            self.insert("", "end", text=row, values=(row.id_orden ,row.cliente, row.producto, row.fecha, row.cantidad))    

    def get_selected_item(self,  *arg):

        try:
            row = self.item(self.selection())
            values =  row["values"] 
            print(values)

            date_object = datetime.strptime(values[3], '%Y-%m-%d') .date()    

            self.orden = OrdenDTO(
                id_orden= int(values[0]),
                cliente= values[1],
                producto= values[2],
                fecha =  date_object,
                cantidad= int(values[4])
            )

            self.widgetFrame.orden = self.orden
        except IndexError:
            print("Selecciona un item.") 
         
        
    def refresh_view(self,  *arg):

        self.clean_view()
        self.load_data()

    def refresh_by_search_id(self, *args):

        value =  self.widgetFrame.string_listener_id.get()
        
        if value.isdigit():

            self.clean_view()
            row = OrdenRepo().get(int( value))
            if row:
                self.insert("", "end", text=row, values=(row.id_orden ,row.cliente, row.producto, row.fecha, row.cantidad))    
        else:
            self.clean_view()
            rows = OrdenRepo().get_all()
            self.insert_rows(rows)


    def refresh_by_search_name(self, *args):

        value =  self.widgetFrame.string_listener_name.get()
        
        if len(value) > 3: 
            self.clean_view()
            rows = OrdenRepo().getByName(value)
            if rows:
                self.insert_rows(rows)
        else:
            self.clean_view()
            rows = OrdenRepo().get_all()
            self.insert_rows(rows)                                
             

    def clean_view(self):
        for child in self.get_children():
            self.delete(child)
    

    def keyReleased(self, event):
        print(event.keysym) 
        key = event.keysym    
        if key == "Up" or key == "Down":
            self.get_selected_item()  


