from tkinter import Entry, Frame, IntVar, Label, StringVar, messagebox
from tkinter.ttk import Combobox
from GUI.components.widgets.Button import Button_
from GUI.components.windows.producto.create_producto_window import CreateProductoWindow
from GUI.components.windows.producto.update_producto_window import UpdateProductoWindow
from models.categoria import Categoria
from models.producto import Producto
from repository.productoRepo import ProductoRepo



class ProductoMenuBar(Frame):
    
    buttonWidth = 15
    producto:Producto
    bg_color="darkgoldenrod2"
    
    def __init__(self, master, int_var:IntVar):
        
        super().__init__(master, background=self.bg_color )
        self.pack(side='top', fill="both",  pady=5) 
        
        self.string_listener = StringVar(self, '') 
        self.int_var= int_var
        self.categoria_listener = StringVar(self)
        
        self.search_label=Label(self,width=20, background=self.bg_color ,text="Buscar")
        self.search_label.pack(side='left')

        self.entry_search=Entry(self, textvariable = self.string_listener , fg='grey20' )
        self.entry_search.pack(side='left')
        self.entry_search.focus()

        #Categoria
        self.label_categoria=Label(self , text="Categoria" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_categoria.pack(side='left')
        
        self.entry_categoria=Combobox(self, state='readonly',  textvariable= self.categoria_listener, values= Categoria.list() )
        self.entry_categoria.pack(side='left')
        
        
        
        self.add_btn=Button_(self,bg_color=self.bg_color, padx=10, text="Add",compound="left", width=self.buttonWidth, command = self.create_window )
        self.add_btn.pack(side='left')

       
        self.update_btn=Button_(self,text="Edit", bg_color=self.bg_color, padx=10 , compound="left" , width=self.buttonWidth ,command=self.update_window )
        self.update_btn.pack(side='left')

        
        self.delete_btn=Button_(self,text="Del",bg_color=self.bg_color, padx=10, compound="left" , width=self.buttonWidth, command=self.delete_window) 
        self.delete_btn.pack(side='left') 


        
        
        

    def text_changed(self, *arg): 

        
        print(" From child: ", self.string_listener.get() )
       
        self.string_listener.set( self.string_listener.get())

        #return self.string_listener.get()
        

            
            
    def update_window(self):
        UpdateProductoWindow(self, self.producto, self.int_var)
        
        
    def create_window(self):
        CreateProductoWindow(self, self.int_var)
    

    def delete_window(self):
        
        resp = messagebox.askyesno("Eliminar",  f"Desea elimnirar {self.producto.nombre}" )
        if resp:
            ProductoRepo().delete(self.producto.id_producto)
            self.int_var.set(self.producto.id_producto)

    def option_selected(self, *ars):
        
        print("algo paso!")
      