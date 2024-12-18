from datetime import date
from tkinter import Entry, Frame, IntVar, Label, Spinbox, messagebox
from GUI.components.windows.new_window import NewWindow
from models.orden import Orden
from GUI.components.widgets.Button import Button_
from repository.clienteRepo import ClienteRepo
from repository.ordenRepo import OrdenRepo
from repository.productoRepo import ProductoRepo



class CreateOrdenWindow(NewWindow):


    def __init__(self, master, int_var:IntVar):
        super().__init__(master, "Agregar Orden")

        self.intvar = int_var
        
        #Frame
        self.frame=Frame(self, background="darkgoldenrod2")
        self.frame.pack(fill="both", padx=5, pady=5 , expand=True)

        self.label_idCliente=Label(self.frame, text="Id Cliente", background="darkgoldenrod2",   compound='right' ,padx=5 )
        self.label_idCliente.grid(column=0, row=1,pady=3, sticky='e')
        
        self.entry_idCliente=Entry(self.frame  )
        self.entry_idCliente.grid(column=1, row=1)
        

        self.label_producto=Label(self.frame, text="Producto", background="darkgoldenrod2",   compound='right' ,padx=5 )
        self.label_producto.grid(column=0, row=2,pady=3, sticky='e')
        
        self.entry_producto=Entry(self.frame  )
        self.entry_producto.grid(column=1, row=2)

        self.label_cantidad=Label(self.frame , text="Cantidad" ,background="darkgoldenrod2",compound='right',padx=5 ,  )
        self.label_cantidad.grid(column=0, row=3, pady=3, sticky='e')
     
        self.entry_cantidad=Spinbox(self.frame, from_=0 , to=12)
        self.entry_cantidad.grid(column=1, row=3)
        

       
        #Boton Agregar
        self.edit_btn=Button_(self.frame ,width=15 ,text="Agregar" ,compound='left', bg_color="darkgoldenrod2",padx=5 , command=self.save_data)
        self.edit_btn.grid(column=0, row=4,pady=5, sticky='w')

        #Boton Cerrar
        self.close_btn=Button_(self.frame, width=15, text="Close", compound='left', bg_color='DarkGoldenrod2',padx=5,  command=self.destroy )
        self.close_btn.grid(column=1, row=4, pady=5) 

        self.error_label=Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{''}")


    def save_data(self):
        
        try:
            self.error_label.destroy()
        except AttributeError:   # Ignora el error en caso que no existan.       
            pass
             
        finally:
            try:
                
                id_cliente = int(self.entry_idCliente.get())
                nombre_producto = self.entry_producto.get()
                cantidad = int(self.entry_cantidad.get())
                fecha = date.today()

                producto =  ProductoRepo().getOneByName(nombre_producto)

                stock = ProductoRepo().getStockByName(nombre_producto)[0]
                
                if not None: 
                    stock= int(stock )

                if not ClienteRepo().get(id_cliente):
                    messagebox.showerror("Cliente inexistente" , "El cliente no se encuentra guardado.")

                elif not producto:   
                    messagebox.showerror("Producto inexistente" , "El producto no se encuentra.")
                
                elif stock < cantidad:
                    messagebox.showerror("Stock insuficiente" , "No hay stock.")

                else:
                     
                    orden = Orden(None, id_cliente,producto.id_producto, fecha, cantidad )
                    id_orden = OrdenRepo().create(orden)
                    resp = messagebox.askyesno("Crear orden ?", 
                                        message=f"""Desea crear Orden: 
                                                    
                                                    Producto: {nombre_producto}
                                                    Cantidad: {cantidad}
                                                    Fecha: {fecha}
                    """)
                    if resp:
                        messagebox.showinfo(message=f"Orden {id_orden} creada", title="Orden") 
                        self.intvar.set(1)
                        self.destroy()
        
            except ValueError as msg_error:
                    
                    self.error_label= Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{msg_error}")
                    self.error_label.pack(anchor="center")
        

        
    
        


