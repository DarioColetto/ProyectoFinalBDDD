from tkinter import Entry, Frame, IntVar, Label, Spinbox, StringVar, messagebox
from tkinter.ttk import Combobox
from models.categoria import Categoria
from models.producto import Producto
from GUI.components.windows.new_window import NewWindow
from GUI.components.widgets.Button import Button_
from repository.productoRepo import ProductoRepo


class UpdateProductoWindow(NewWindow):

    def __init__(self, master, producto:Producto, int_var:IntVar):
        super().__init__(master, "Editar Producto")

        self.producto = producto
        self.intvar = int_var

        #Frame
        self.frame=Frame(self, background="darkgoldenrod2")
        self.frame.pack(fill="both", padx=5, pady=5 , expand=True)
        
        #Nombre
        self.label_nombre=Label(self.frame ,text="Nombre", background="darkgoldenrod2", compound='right', padx=5 )
        self.label_nombre.grid(column=0, row=0, pady=3, sticky='e')      
        
        self.entry_nombre=Entry(self.frame )
        self.entry_nombre.insert(0, self.producto.nombre)
        self.entry_nombre.grid(column=1, row=0)
        self.entry_nombre.focus()
        
        
        #Descripcion
        self.label_descripcion=Label(self.frame, text="Descripcion", background="darkgoldenrod2",   compound='right' ,padx=5 )
        self.label_descripcion.grid(column=0, row=1,pady=3, sticky='e')
        
        self.entry_descripcion=Entry(self.frame)
        self.entry_descripcion.insert(0, self.producto.descripcion)
        self.entry_descripcion.grid(column=1, row=1)
     
        #Mail
        self.label_categoria=Label(self.frame , text="Categoria" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_categoria.grid(column=0, row=2, pady=3, sticky='e')
        
        self.entry_categoria=Combobox(self.frame, state='readonly', values= Categoria.list() )
        self.entry_categoria.set(self.producto.categoria.value)
        self.entry_categoria.grid(column=1, row=2)
       
       #Precio
        self.label_precio=Label(self.frame , text="Precio" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_precio.grid(column=0, row=3, pady=3, sticky='e')
        
        self.entry_precio=Entry(self.frame)
        self.entry_precio.insert(0, self.producto.precio)
        self.entry_precio.grid(column=1, row=3)

        #stock

        self.label_stock=Label(self.frame , text="Stock" ,background="darkgoldenrod2",compound='right',padx=5 ,  )
        self.label_stock.grid(column=0, row=4, pady=3, sticky='e')


        my_var= StringVar(self)
        my_var.set(self.producto.stock)
        self.entry_stock=Spinbox(self.frame, from_=0 , to=1000 , textvariable= my_var)
        self.entry_stock.grid(column=1, row=4)
       
        #Boton Save
        self.edit_btn=Button_(self.frame ,width=15 ,text="Save" ,compound='left', bg_color="darkgoldenrod2",padx=5 , command=self.save_data)
        self.edit_btn.grid(column=0, row=5,pady=5, sticky='w')

        #Boton Cerrar
        self.close_btn=Button_(self.frame, width=15, text="Close", compound='left', bg_color='DarkGoldenrod2',padx=5,  command=self.destroy )
        self.close_btn.grid(column=1, row=5, pady=5) 

        self.error_label=Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{''}")

    def save_data(self):

        
        if self.error_label:
             self.error_label.destroy()

        try:
            nombre = self.entry_nombre.get()
            descripcion = self.entry_descripcion.get()
            categoria = Categoria(self.entry_categoria.get()) 
            precio = float(self.entry_precio.get())  
            stock = int(self.entry_stock.get())
                
            producto = Producto(self.producto.id_producto,nombre=nombre ,descripcion=descripcion, categoria=categoria, precio=precio, stock=stock)
            

            ProductoRepo().update(producto.id_producto , producto.toDict())
            self.intvar.set(self.producto.id_producto)

            messagebox.showinfo(message=f"Producto:{nombre} Actualizado", title="Producto Actualizado")
            
            self.destroy()
                

           
       
        except ValueError as msg_error:
                
                self.error_label= Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{msg_error}")
                self.error_label.pack(anchor="center")


