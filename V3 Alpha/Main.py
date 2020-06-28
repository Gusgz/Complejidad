import model.Escenario as Escenario
import model.Figura as Figura
import model.Dado as Dado
import model.Interfaz as Interfaz
import threading
import tkinter as tk

def generar_escenario():
    escenario = Escenario.Escenario()
    id = escenario.generar()
    return id,escenario

def generar_figuras(id):
    figuras = []
    for i in range(3):
        figura = Figura.Figura()
        figura.generar(id)
        figuras.append(figura)
    return figuras

def lanzar_dado(escenarioId,figuras):
    dado = Dado.Dado()
    dado.lanzar(escenarioId,figuras)

def init_juego():
    escenarioId, escenario = generar_escenario()
    figuras = generar_figuras(escenarioId)
    lanzar_dado(escenarioId,figuras)
    return escenario,figuras

def juego(root):
    root.withdraw()
    win = tk.Toplevel()
    escenario,figuras = init_juego()
    interfaz = Interfaz.Interfaz(win,escenario,figuras)
    interfaz.dibujar_figuras()
    interfaz.dibujar_escenario()
    interfaz.dibujar_menu_juego()
    a = tk.Button(win,text="regresar",command=lambda:volver(win,root))
    a.grid(row=0,column=4)
    interfaz.iniciar()

def volver(win,root):
    root.deiconify()
    win.destroy()

def run():

    root = tk.Tk()
    root.geometry("200x200")
    root.title("UBONGO")
    a = tk.Button(root,text="Este boton me lleva al juego",command=lambda:juego(root))
    a.grid(row=0,column=0)
    root.mainloop()
    #
    '''escenario,figuras = init_juego()
    interfaz = Interfaz.Interfaz(escenario,figuras)
    interfaz.dibujar_figuras()
    interfaz.dibujar_escenario()
    interfaz.dibujar_menu_juego()
    interfaz.iniciar()'''

if __name__ == "__main__":
    run()
    
