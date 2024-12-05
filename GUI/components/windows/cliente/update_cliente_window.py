from tkinter import Entry, Frame, IntVar, Label, StringVar, messagebox
from models.cliente import Cliente
from GUI.components.windows.new_window import NewWindow
from GUI.components.widgets.Button import Button_
from repository.clienteRepo import ClienteRepo


class UpdateClienteWindow(NewWindow):

    def __init__(self, master, cliente:Cliente, int_var:IntVar):
        super().__init__(master, "Editar CLiente")

        self.cliente = cliente
        self.intvar = int_var

        #Frame
        self.frame=Frame(self, background="darkgoldenrod2")
        self.frame.pack(fill="both", padx=5, pady=5 , expand=True)
        
        #Nombre
        self.label_nombre=Label(self.frame ,text="Nombre", background="darkgoldenrod2", compound='right', padx=5 )
        self.label_nombre.grid(column=0, row=0, pady=3, sticky='e')      
        
        self.entry_nombre=Entry(self.frame )
        self.entry_nombre.insert(0, self.cliente.nombre)
        self.entry_nombre.grid(column=1, row=0)
        self.entry_nombre.focus()
        
        
        #Tel
        
        self.label_tel=Label(self.frame, text="Telefono", background="darkgoldenrod2",   compound='right' ,padx=5 )
        self.label_tel.grid(column=0, row=1,pady=3, sticky='e')
        
        self.entry_tel=Entry(self.frame  )
        self.entry_tel.insert(0, self.cliente.telefono)
        self.entry_tel.grid(column=1, row=1)
     
        #Mail
        self.label_mail=Label(self.frame , text="email" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_mail.grid(column=0, row=2, pady=3, sticky='e')
        
        self.entry_mail=Entry(self.frame  )
        self.entry_mail.insert(0, self.cliente.email)
        self.entry_mail.grid(column=1, row=2)
       
       #Direccion
        self.label_direccion=Label(self.frame , text="direccion" ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_direccion.grid(column=0, row=3, pady=3, sticky='e')
        
        self.entry_direccion=Entry(self.frame  )
        self.entry_direccion.insert(0, self.cliente.direccion)
        self.entry_direccion.grid(column=1, row=3)
       
        #Boton Save
        self.edit_btn=Button_(self.frame ,width=15 ,text="Save" ,compound='left', bg_color="darkgoldenrod2",padx=5 , command=self.save_data)
        self.edit_btn.grid(column=0, row=4,pady=5, sticky='w')

        #Boton Cerrar
        self.close_btn=Button_(self.frame, width=15, text="Close", compound='left', bg_color='DarkGoldenrod2',padx=5,  command=self.destroy )
        self.close_btn.grid(column=1, row=4, pady=5) 

        self.error_label=Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{''}")

    def save_data(self):

        
        if self.error_label:
             self.error_label.destroy()

        try:
            nombre = self.entry_nombre.get()
            tel = self.entry_tel.get()
            email = self.entry_mail.get()
            direccion = self.entry_direccion.get()
            
            cliente = Cliente(self.cliente.id_cliente, nombre, email, tel, direccion)
            

            ClienteRepo().update(cliente.id_cliente , cliente.toDict())
            self.intvar.set(self.cliente.id_cliente)

            messagebox.showinfo(message=f"Cliente:{nombre} Actualizado exitosamente", title="Actualizado")
            
            self.destroy()
                

           
       
        except ValueError as msg_error:
                
                self.error_label= Label(self, background='DarkGoldenrod2', fg="red" ,padx=5 ,compound="left", justify='center', text=f"{msg_error}")
                self.error_label.pack(anchor="center")


