from tkinter import Entry, Frame, IntVar, Label, StringVar, messagebox
from GUI.components.widgets.Button import Button_

from GUI.components.windows.cliente.create_cliente_window import CreateClienteWindow
from GUI.components.windows.cliente.update_cliente_window import UpdateClienteWindow
from models.cliente import Cliente
from repository.clienteRepo import ClienteRepo



class ClienteMenuBar(Frame):
    
    buttonWidth = 15
    cliente:Cliente
    bg_color="darkgoldenrod2"
    
    def __init__(self, master ):
        
        super().__init__(master, background=self.bg_color )
        self.pack(side='top', fill="both",  pady=5) 
       
        self.string_listener = StringVar(self, '') 
        self.int_var =  IntVar(self, 0)
        
        self.search_label=Label(self,width=20, background=self.bg_color ,text="Buscar")
        self.search_label.pack(side='left')

        self.entry_search=Entry(self, textvariable = self.string_listener , fg='grey20' )
        self.entry_search.pack(side='left')
        self.entry_search.focus()
        
        self.add_btn=Button_(self,bg_color=self.bg_color, padx=10, text="Add",compound="left", width=self.buttonWidth, command = self.create_window )
        self.add_btn.pack(side='left')

        self.update_btn=Button_(self,text="Edit", bg_color=self.bg_color, padx=10 , compound="left" , width=self.buttonWidth ,command=self.update_window )
        self.update_btn.pack(side='left')

        self.delete_btn=Button_(self,text="Del",bg_color=self.bg_color, padx=10, compound="left" , width=self.buttonWidth, command=self.delete_window) 
        self.delete_btn.pack(side='left') 

        #TRACERS

        self.string_listener.trace_add("write", self.text_changed)
        
    
    def text_changed(self, *args): 
        
        entry_string = self.entry_search.get()

        print(entry_string)
        
        if entry_string:
            self.string_listener.set(entry_string)
            
            
    def update_window(self):
       
        UpdateClienteWindow(self, self.cliente, self.int_var)
        
        
    def create_window(self):
        CreateClienteWindow(self, self.int_var)
    

    def delete_window(self):
        
        resp = messagebox.askyesno("Eliminar",  f"Desea elimnirar {self.cliente.nombre}" )
        if resp:
            result = ClienteRepo().delete(self.cliente.id_cliente)
            if result:
                messagebox.showinfo("Eliminado", message= f"cliente {self.cliente.nombre} eliminado.")
                self.int_var.set(self.cliente.id_cliente)
            else:
                messagebox.showinfo("Eliminado", message= "No se puede eliminar el cliente, tiene ordenes asociadas.")