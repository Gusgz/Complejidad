import tkinter as tk
class Interfaz:

    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root,width=500,height=300,bg='white')
        self.canvas.pack
        self.canvas.create_rectangle(10, 100, 200, 200, width=5, fill='red')
        self.root.mainloop()
    
    def dibujar_figuras(self):
        self.canvas.create_line(10,10,80,80)
    
    def mainloop(self):
        self.root.mainloop()

