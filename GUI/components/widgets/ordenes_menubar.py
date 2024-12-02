from tkinter import Entry, Frame, IntVar, Label, StringVar, messagebox
from GUI.components.widgets.Button import Button_

from GUI.components.windows.ordenes.create_orden import CreateOrdenWindow
from models.orden import Orden
from models.ordenDTO import OrdenDTO
from repository.ordenRepo import OrdenRepo


class OrdenMenuBar(Frame):
    
    buttonWidth = 15
    orden:OrdenDTO
    bg_color="darkgoldenrod2"
    
    def __init__(self, master ):
        
        super().__init__(master, background=self.bg_color )
        
        self.string_listener_id = StringVar(self, '')
        self.string_listener_name = StringVar(self, '')  
        self.int_var =  IntVar(self, 0)
        
        self.pack(side='top', fill="both",  pady=5) 

        self.search_label_id=Label(self,width=20, background=self.bg_color ,text="Buscar por ID")
        self.search_label_id.pack(side='left')

        self.entry_search_id=Entry(self, textvariable = self.string_listener_id , fg='grey20' )
        self.entry_search_id.pack(side='left')
        

        self.search_label_name=Label(self,width=20, background=self.bg_color ,text="Buscar por cliente")
        self.search_label_name.pack(side='left')

        self.entry_search_name=Entry(self, textvariable = self.string_listener_name , fg='grey20' )
        self.entry_search_name.pack(side='left')
        
        

        self.add_btn=Button_(self,bg_color=self.bg_color, padx=10, text="Add",compound="left", width=self.buttonWidth, command = self.create_window )
        self.add_btn.pack(side='left')


        self.update_btn=Button_(self,text="Edit", bg_color=self.bg_color, padx=10 , compound="left" , width=self.buttonWidth ,command=self.update_window )
        self.update_btn.pack(side='left')


        self.delete_btn=Button_(self,text="Del",bg_color=self.bg_color, padx=10, compound="left" , width=self.buttonWidth) #command=self.to_delete_window
        self.delete_btn.pack(side='left') 

        #TRACERS

        self.string_listener_id.trace_add("write", self.entry_id_text_changed)
        self.string_listener_name.trace_add("write", self.entry_name_text_changed)
        
    
    def entry_id_text_changed(self, *args): 
        entry_string =  self.entry_search_id.get()
        print(entry_string)
        if entry_string:
            self.string_listener_id.set(entry_string)
    
    def entry_name_text_changed(self, *args): 
        entry_string =  self.entry_search_name.get()
        print(entry_string)
        if entry_string:
            self.string_listener_name.set(entry_string)
                      
            
    def update_window(self):
       
        #UpdateOrdenWindow(self, self.orden, self.int_var)
        pass
        
    def create_window(self):
        CreateOrdenWindow(self, self.int_var )
    

    def delete_window(self):
        
        resp = messagebox.askyesno("Eliminar",  f"Desea elimnirar {self.orden.id_orden}" )
        if resp:
            OrdenRepo().delete(self.orden.id_orden)
            self.int_var.set(self.orden.id_orden)
        