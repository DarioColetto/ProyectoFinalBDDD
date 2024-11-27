from tkinter import Entry, Frame, IntVar, Label, StringVar
from GUI.components.widgets.Button import Button_

from GUI.components.windows.cliente.create_cliente_window import CreateClienteWindow
from GUI.components.windows.cliente.update_cliente_window import UpdateClienteWindow
from models.cliente import Cliente


class ClienteMenuBar(Frame):
    
    buttonWidth = 15
    cliente:Cliente
    bg_color="darkgoldenrod2"
    
    def __init__(self, master, int_var:IntVar, string_listener:StringVar ):
        
        super().__init__(master, background=self.bg_color )
        
        self.string_listener = string_listener
        self.int_var= int_var
        
        self.pack(side='top', fill="both",  pady=5) 


        # self.search_label_icon = search_icon()
        self.search_label=Label(self,width=20, background=self.bg_color ,text="Buscar")
        self.search_label.pack(side='left')

        self.entry_search=Entry(self, textvariable = self.string_listener , fg='grey20' )
        self.entry_search.pack(side='left')
        self.entry_search.focus()
        
        # self.add_btn_icon = add_icon()
        self.add_btn=Button_(self,bg_color=self.bg_color, padx=10, text="Add",compound="left", width=self.buttonWidth, command = self.create_window )
        self.add_btn.pack(side='left')

        # self.update_btn_icon = update_icon()
        self.update_btn=Button_(self,text="Edit", bg_color=self.bg_color, padx=10 , compound="left" , width=self.buttonWidth ,command=self.update_window )
        self.update_btn.pack(side='left')

        # self.delete_btn_icon = delete_icon()
        self.delete_btn=Button_(self,text="Del",bg_color=self.bg_color, padx=10, compound="left" , width=self.buttonWidth) #command=self.to_delete_window
        self.delete_btn.pack(side='left') 

        #TRACERS

        self.string_listener.trace_add("write", self.text_changed)
        
    
    def text_changed(self, *args): 
        
        entry_string = self.entry_search.get()

        print(entry_string)
        
        if entry_string:
            self.string_listener.set(entry_string)
            
            
    def update_window(self):
       
        self.updateWindow = UpdateClienteWindow(self, self.cliente, self.int_var)
        
        
    def create_window(self):
        return CreateClienteWindow(self )
    

    def setStringListener():
        pass