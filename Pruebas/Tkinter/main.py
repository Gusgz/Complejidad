import tkinter as tk



def run():

    def func(nombre):
        etiqueta["text"] = nombre

    ventana = tk.Tk()
    ventana.geometry("400x300")
    ventana.title("Ubongo")
    #ventana.configure(width=1000,height=500)
    #
    #texto = tk.Entry(ventana,font="Calibri 18")
    #texto.grid(row=0,column=0)
    #texto.pack() 
    #
    #boton = tk.Button(ventana,text="Boton",width=10,height=5,command = lambda: func(texto.get()))
    #boton.place(x=0,y=0)
    #boton.grid(row=1,column=0)
    #boton.pack(side=tk.LEFT)
    #
    #etiqueta =tk.Label(ventana)
    #etiqueta.grid(row=2,column=0)
    #etiqueta.pack()

    #canvas
    c = tk.Canvas(ventana,width=90,height=90)
    c.create_rectangle(0, 0, 30, 30, fill="blue")
    c.create_rectangle(30, 0, 60, 30, fill="blue")
    c.create_rectangle(60, 0, 90, 30, fill="blue")
    c.create_rectangle(0, 0, 30, 30, fill="blue")
    c.create_rectangle(0, 30, 30, 60, fill="blue")
    c.create_rectangle(0, 60, 30, 90, fill="blue")
    c.grid(row=0,column=0)
    #c.delete("all")

    ventana.mainloop()

if __name__ == "__main__":
    run()