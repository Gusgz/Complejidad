import tkinter as tkinter
class VentanaUbongo:
    def __init__(self,root,tablero):
        self.root = root
        self.tablero = tablero
    
    def iniciar(self):
        self.root.mainloop()

    def finalizar(self):
        self.root.destroy()
