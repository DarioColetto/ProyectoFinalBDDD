from tkinter import Entry, Frame, IntVar, Label, Spinbox, messagebox
from tkinter.ttk import Combobox
from GUI.components.windows.new_window import NewWindow
from models.categoria import Categoria
from models.cliente import Cliente
from GUI.components.widgets.Button import Button_
from models.producto import Producto
from repository.productoRepo import ProductoRepo



class CreateProductoWindow(NewWindow):

    

    def __init__(self, master, int_var:IntVar):
        super().__init__(master, "Agregar Producto")

        self.intvar = int_var
        
        #Frame
        self.frame=Frame(self, background="darkgoldenrod2")
        self.frame.pack(fill="both", padx=5, pady=5 , expand=True)
        
        #Nombre
        self.label_nombre=Label(self.frame ,text="Nombre", background="darkgoldenrod2", compound='right', padx=5 )
        self.label_nombre.grid(column=0, row=0, pady=3, sticky='e')      
        
        self.entry_nombre=Entry(self.frame )
        self.entry_nombre.grid(column=1, row=0)
        self.entry_nombre.focus()
        
        
        #Descripcion
        self.label_descripcion=Label(self.frame, text="Descripcion", background="darkgoldenrod2",   compound='right' ,padx=5 )
        self.label_descripcion.grid(column=0, row=1,pady=3, sticky='e')
        
        self.entry_descripcion=Entry(self.frame  )
        self.entry_descripcion.grid(column=1, row=1)
     
        #Categoria
        self.label_categoria=Label(self.frame , text="Categoria" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_categoria.grid(column=0, row=2, pady=3, sticky='e')
        
        self.entry_categoria=Combobox(self.frame, state='readonly', values= Categoria.list() )
        self.entry_categoria.grid(column=1, row=2)

        #Precio
        self.label_precio=Label(self.frame , text="Precio" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_precio.grid(column=0, row=3, pady=3, sticky='e')
        
        self.entry_precio=Entry(self.frame)
        self.entry_precio.insert(0, "0.0")
        self.entry_precio.grid(column=1, row=3)
       
        #stock

        self.label_stock=Label(self.frame , text="Stock" ,background="darkgoldenrod2",compound='right',padx=5 ,  )
        self.label_stock.grid(column=0, row=4, pady=3, sticky='e')

        self.entry_stock=Spinbox(self.frame, from_=1 , to=12 )
        self.entry_stock.grid(column=1, row=4)

        #Boton Agregar
        self.edit_btn=Button_(self.frame ,width=15 ,text="Agregar" ,compound='left', bg_color="darkgoldenrod2",padx=5 , command=self.save_data)
        self.edit_btn.grid(column=0, row=5,pady=5, sticky='w')

        #Boton Cerrar
        self.close_btn=Button_(self.frame, width=15, text="Close", compound='left', bg_color='DarkGoldenrod2',padx=5,  command=self.destroy )
        self.close_btn.grid(column=1, row=5, pady=5) 

        self.error_label=Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{''}")


    def save_data(self):
        
        try:
            self.error_label.destroy()
        except AttributeError:   # Ignora el error en caso que no existan.       
            pass
             
        finally:
            try:
                nombre = self.entry_nombre.get()
                descripcion = self.entry_descripcion.get()
                categoria = Categoria(self.entry_categoria.get()) 
                precio = float(self.entry_precio.get())  
                stock = int(self.entry_stock.get())
                
                producto = Producto(None,nombre=nombre ,descripcion=descripcion, categoria=categoria, precio=precio, stock=stock)
                ProductoRepo().create(producto)
                self.intvar.set(1)
                

                messagebox.showinfo(message=f"Producto:{nombre} creado exitosamente", title="Producto Creado")

                self.destroy()
        
            except ValueError as msg_error:
                    
                    self.error_label= Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{msg_error}")
                    self.error_label.pack(anchor="center")
        

        
    
        


