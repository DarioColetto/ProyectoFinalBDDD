from tkinter import Toplevel
from .config_geometry import config_geometry



class NewWindow(Toplevel):
        def __init__(self, master,win_tilte, *arg, **kwargs):
            super().__init__(master,*arg, **kwargs)
            self.geometry(config_geometry(self, 600,600))
            self.config(background='DarkGoldenrod2', highlightthickness=4, highlightbackground="grey15", highlightcolor="grey15")      
            self.title = win_tilte
                  


