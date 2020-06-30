import model.Escenario as Escenario
import model.Figura as Figura
import model.Dado as Dado
import model.Interfaz as Interfaz
import model.Jugador as Jugador
import threading
import tkinter as tkinter

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

def cerrar_ventana(root):
    root.destroy()

def agregar_jugador(nombre,posicion,jugadores):
        jugador = Jugador.Jugador(nombre,posicion)
        print(nombre,posicion)
        jugadores.append(jugador)

def ventana_datos(root):
    root.withdraw()
    win = tkinter.Toplevel()
    jugadores = []
    # JUGADOR - NOMBRE
    fila = 0
    etiquetaTitulo = tkinter.Label(win)
    etiquetaTitulo["text"] = "INGRESE LOS JUGADORES"
    etiquetaTitulo.grid(row=fila,column=0,columnspan=2)
    fila += 1
    # JUGADOR - NOMBRE
    etiquetaNombre = tkinter.Label(win)
    etiquetaNombre["text"] = "NOMBRE"
    etiquetaNombre.grid(row=fila,column=0)
    textoNombre = tkinter.Entry(win,font="Calibri 12")
    textoNombre.grid(row=fila,column=1)
    fila += 1
    # JUGADOR - POSICIÓN
    etiquetaPosicion = tkinter.Label(win)
    etiquetaPosicion["text"] = "POSICION"
    etiquetaPosicion.grid(row=fila,column=0)
    textoPosicion = tkinter.Entry(win,font="Calibri 12")
    textoPosicion.grid(row=fila,column=1)
    fila += 1
    # AGREGAR
    botonAgregar = tkinter.Button(win,text="AGREGAR",command=lambda:agregar_jugador(textoNombre.get(),int(textoPosicion.get()),jugadores))
    botonAgregar.grid(row=fila,column=1)
    fila += 1
    # LISTO
    botonListo = tkinter.Button(win,text="LISTO",command=lambda:ventana_ubongo(root,win))
    botonListo.grid(row=fila,column=1)
    fila += 1

def ventana_ubongo(root):
    # falta agregar win de parametro
    #cerrar_ventana(win)
    root.deiconify()
    a = tkinter.Button(root,text="Empezar juego",command=lambda:ventana_juego(root))
    a.grid(row=0,column=0)

def ventana_juego(root):
    root.withdraw()
    win = tkinter.Toplevel()
    a = tkinter.Button(win,text="Juego terminado para jugador 1",command=lambda:ventana_ubongo(root,win))
    a.grid(row=0,column=0)

def run():
    root = tkinter.Tk()
    root.title("Ubongo")
    #ventana_datos(root)
    ventana_ubongo(root)
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
    
