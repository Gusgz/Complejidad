import model.Escenario as Escenario
import model.Figura as Figura
import model.Dado as Dado
import model.Jugador as Jugador
import model.VentanaJuego as VentanaJuego
import model.VentanaUbongo as VentanaUbongo
import model.Tablero as Tablero
import Util.Dijkstra as Dijkstra
import threading
import tkinter as tkinter
import math
import heapq

jugadores = []
def generar_escenario():
    escenario = Escenario.Escenario()
    escenario.generar()
    return escenario

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
    escenario = generar_escenario()
    figuras = generar_figuras(escenario.id)
    lanzar_dado(escenario.id,figuras)
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

def listar_jugadores(nombre,posicion):
    global jugadores
    jugador=Jugador.Jugador(nombre,posicion)
    print(nombre,posicion) 
    jugadores.append(jugador) 

def ventana_datos(root):
    #withdraw para cerrar
    root.withdraw()
    #win para abrir la ventana
    win = tkinter.Toplevel()
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
    botonAgregar = tkinter.Button(win,text="AGREGAR",command=lambda:listar_jugadores(textoNombre.get(),int(textoPosicion.get())))
    botonAgregar.grid(row=fila,column=1)
    
    fila += 1
    # LISTO
    botonListo = tkinter.Button(win,text="LISTO",command=lambda:ventana_ubongo(root,win))
    botonListo.grid(row=fila,column=1)
    fila += 1

def bellmanFord(G,start):
    n = len(G)
    d =[math.inf]*n
    p =[None]*n
    d[start]=0
    # LA SOLUCIÓN SE VA A ENCONTRAR MAX HASTA V - 1
    for _ in range(n-1):
        # POR CADA VÉRTICE EN EL GRAFO
        for u in range(n):
          # POR CADA VALOR (V,W) EN EL GRAFO
            for v,w in G[u]:
              # SI LA DISTANCIA ACTUAL ES MENOR
                if d[v]>d[u]+w:
                    d[v]=d[u]+w
                    p[v]=u
        for u in range(n):
            for v,w in G[u]:
                if d[v]>d[u]+w:
                    print("oh noo, ciclo negativo")
                    return
    return p, d

def ventana_ubongo(root,win):
    # falta agregar win de parametro
    cerrar_ventana(win)
    root.deiconify()
    ###
    tablero = Tablero.Tablero()
    tablero.generar_gemas()
    lista = tablero.generar_conexiones()
    #lista = tablero.grafo.generar_lista()
    #tablero.grafo.imprimir_grafo()
    G =[[(1,1),(2,2),(3,8)],
    [(4,3)],
    [(4,3),(5,8),(3,5)],
    [(5,12)],
    [(5,4)],
    []]
    #p, d = bellmanFord(lista,0)
    #print(p)
    #print(d)
    #tablero.grafo.imprimir_grafo()
    '''
    for v,w in lista[0]:
        print(tablero.grafo.colores[v])
        ####'''
    #tablero.generar_conexiones()
    #lista = tablero.grafo.obtener_lista_adyacencia()
    #print(tablero.grafo.vertices)
    #tablero.grafo.imprimir_grafo()
    ubongo = VentanaUbongo.VentanaUbongo(root,tablero)
    ubongo.dibujar_tablero()
    ubongo.dibujar_jugadores(jugadores)
    ubongo.iniciar()

    #a = tkinter.Button(root,text="Empezar juego",command=lambda:ventana_juego(root))
    #a.grid(row=0,column=0)

def ventana_juego(root):
    root.withdraw()
    win = tkinter.Toplevel()
    a = tkinter.Button(win,text="Juego terminado para jugador 1",command=lambda:ventana_ubongo(root,win))
    a.grid(row=0,column=0)

def run():
    root = tkinter.Tk()
    root.title("Ubongo")
    ventana_datos(root)
    #ventana_ubongo(root)
    #
    '''escenario,figuras = init_juego()
    interfaz = VentanaJuego.VentanaJuego(root,escenario,figuras)
    interfaz.dibujar_figuras()
    interfaz.dibujar_escenario()
    interfaz.dibujar_menu_juego()
    interfaz.iniciar()'''
    root.mainloop()

if __name__ == "__main__":
    run()
