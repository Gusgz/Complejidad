import model.Jugador as Jugador
import model.Tablero as Tablero
import model.InterfazCanvas as InterfazCanvas
import model.Escenario as Escenario
import model.Figura as Figura
import model.Dado as Dado
import tkinter as tk
from tkinter import messagebox
import random as rand
import time
import threading
from os import system
empezar = False
tiempo = 0
puntaje = 0
jugador_id = 0
juegos = 0
class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.jugadores = []
        self.canvas = InterfazCanvas.InterfazCanvas(self.root)
        self.id = 0
        self.figuras = []

    def init_win_datos(self):
        self.root.withdraw()
        win = tk.Toplevel()
        #
        def agregar_jugador(nombre,posicion):
            jugador = Jugador.Jugador()
            jugador.nombre = nombre
            jugador.posicion = posicion
            if(len(self.jugadores)<2):
              self.jugadores.append(jugador)
            else:
              messagebox.showerror(title='Limite de jugadores superado',message='No pueden haber mas de 2 jugadores!')
        def agregar_bot():
            jugador = Jugador.Jugador()
            jugador.nombre = "bot"
            jugador.posicion = rand.randint(1,3)
            jugador.bot = True
            if(len(self.jugadores)<2):
              self.jugadores.append(jugador)
            else:
              messagebox.showerror(title='Limite de jugadores superado',message='No pueden haber mas de 2 jugadores!')
        def siguiente():
            win.destroy()
            self.init_win_tablero()
        #
        lblTitulo = tk.Label(win)
        lblTitulo["text"] = "UBONGO - Participantes"
        lblTitulo.grid(row=0,column=0)
        #
        lblNombre = tk.Label(win)
        lblNombre["text"] = "Nombre"
        lblNombre.grid(row=1,column=0)
        txtNombre = tk.Entry(win,font="Calibri 12")
        txtNombre.grid(row=2,column=0)
        #
        lblPosicion = tk.Label(win)
        lblPosicion["text"] = "Posición"
        lblPosicion.grid(row=3,column=0)
        txtPosicion = tk.Entry(win,font="Calibri 12")
        txtPosicion.grid(row=4,column=0)
        #
        btnAgregarJugador = tk.Button(win,text="Agregar Jugador",command=lambda:agregar_jugador(txtNombre.get(),int(txtPosicion.get())))
        btnAgregarJugador.grid(row=5,column=0)
        #
        btnAgregarBot = tk.Button(win,text="Agregar Bot",command=agregar_bot)
        btnAgregarBot.grid(row=6,column=0)
        #
        btnSiguiente = tk.Button(win,text="Siguiente",command=siguiente)
        btnSiguiente.grid(row=7,column=0)
        pass

    def init_win_tablero(self):
        self.root.deiconify()
        self.root.geometry("800x600")
        # --- FRAME 2
        frame2 = tk.Frame(self.root)
        frame2.place(x=240,y=20,width=200,height=200)
        frame2.config(bg="lightblue")
        # --- TABLERO
        tablero = Tablero.Tablero()
        tablero.generar_gemas()
        tablero.generar_conexiones()
        tablero.dibujar(frame2)
        # --- MÉTODOS DE POSICIONES
        def mover(jug,jug2):
            global juegos
            tablero.dibujar_con_posicion(frame2,jug,jug2,juegos)
            juegos+=1
            pass
        def actualizar_posicion():
            global juegos
            if juegos%2 == 0:
                if self.jugadores[0].posicion == self.jugadores[1].posicion:
                    self.jugadores[0].posicion += 1
                if self.jugadores[0].posicion > 3:
                    self.jugadores[0].posicion = 0
                mover(self.jugadores[0],self.jugadores[1])
        actualizar_posicion()
        # --- FRAME 1
        frame1 = tk.Frame(self.root)
        frame1.place(x=20,y=20,width=200,height=200)
        # --- LABEL JUGADORES
        for i in range(len(self.jugadores)):
                lblNombre = tk.Label(frame1)
                lblNombre["text"] = self.jugadores[i].nombre + " pos:" + str(self.jugadores[i].posicion) +" pts:" + str(self.jugadores[i].puntos)
                lblNombre.grid(row=i,column=0,sticky="w")
                #lblNombre.place(x=20,y=20*(i*2+1))
        # --- BTN JUGADOR 1
        btnJugador1 = tk.Button(frame1,text="Jugar",command=lambda:self.init_win_puzzle(0))
        btnJugador1.grid(row=0,column=1,sticky="w")
        # --- BTN JUGADOR 1
        btnJugador2 = tk.Button(frame1,text="Jugar",command=lambda:self.init_win_puzzle(1))
        btnJugador2.grid(row=1,column=1,sticky="w")
        # --- LBL SELECCIONAR POS
        lblSeleccionarPos = tk.Label(frame1)
        lblSeleccionarPos["text"] = "Jugador 1"
        lblSeleccionarPos.grid(row=2,column=0,sticky="w")
        # --- TXT POS
        txtSeleccionarPos = tk.Entry(frame1,font="Calibri 8")
        txtSeleccionarPos.grid(row=3,column=0,sticky="w")
        # --- BTN CAMBIAR POS
        btnSeleccionarPos = tk.Button(frame1,text="Cambiar",command=lambda:mover(0,1))
        btnSeleccionarPos.grid(row=3,column=1,sticky="w")
        # --- LBL SELECCIONAR POS 2
        lblSeleccionarPos2 = tk.Label(frame1)
        lblSeleccionarPos2["text"] = "Jugador 2"
        lblSeleccionarPos2.grid(row=4,column=0,sticky="w")
        # --- TXT POS 2
        txtSeleccionarPos2 = tk.Entry(frame1,font="Calibri 8")
        txtSeleccionarPos2.grid(row=5,column=0,sticky="w")
        # --- BTN CAMBIAR POS 2
        btnSeleccionarPos2 = tk.Button(frame1,text="Cambiar",command=lambda:mover(1,3))
        btnSeleccionarPos2.grid(row=5,column=1,sticky="w")
        # --- JUGADOR 1
        cadena1 = ""
        for i in range(5):
            cadena1 += self.jugadores[0].gemas[i] + " "
        lblJugador1Gemas = tk.Label(frame1,font="Calibri 8")
        lblJugador1Gemas["text"] = cadena1
        lblJugador1Gemas.grid(row=6,column=0,sticky="w")
        # --- JUGADOR 2
        cadena2 = ""
        for i in range(5):
            cadena2 += self.jugadores[1].gemas[i] + " "
        lblJugador2Gemas = tk.Label(frame1,font="Calibri 8")
        lblJugador2Gemas["text"] = cadena2
        lblJugador2Gemas.grid(row=7,column=0,sticky="w")
        pass

    def init_win_puzzle(self,jugadorId):
        global empezar
        global juegos
        global jugador_id
        self.id = 0
        jugador_id = jugadorId
        
        if juegos <= 12:
            # --- VALORES INICIALES
            self.root.withdraw()
            win = tk.Toplevel()
            def cronometro():
                global tiempo
                global puntaje
                tiempo = 0
                while tiempo < 100:
                    tiempo += 1
                    time.sleep(1)
                    #print("Tiempo restante",tiempo,"/ 30 seg")
                    pass
                if not dado.escenario.esta_completo():
                    messagebox.showerror(title='Tiempo acabo',message='No completaste el puzzle a tiempo!')
                    puntaje = tiempo
                    self.jugadores[jugadorId].puntos += tiempo
                    win.destroy()
                    self.init_win_tablero()
            thread = threading.Thread(target=cronometro)
            # SE GENERAN LAS CLASES ESCENARIO, FIGURA Y DADO
            escenario = Escenario.Escenario()
            figuras = []
            for i in range(3):
                figura = Figura.Figura()
                figuras.append(figura)
            dado = Dado.Dado(escenario,figuras)
            dado.lanzar()
            self.figuras = dado.figuras
            def dibujar_escenario_figuras():
                for i in range(3):
                    dado.figuras[i].dibujar(win,0,i)
                dado.escenario.dibujar(win)
            dibujar_escenario_figuras()
            # --- MÉTODOS PARA LAS OPCIONES
            def opcion_invertir():
                figuras[self.id].invertir()
                figuras[self.id].dibujar(win,0,self.id)
            def opcion_rotar():
                figuras[self.id].rotar()
                figuras[self.id].dibujar(win,0,self.id)
            def opcion_insertar(x,y):
                global juegos
                if escenario.se_puede_insertar_figura(x,y,figuras[self.id]) and self.id < 3 and empezar:
                    m,color = escenario.insertar_figura(x,y,figuras[self.id])
                    escenario.dibujar_con_figura(win,m,color)
                    self.id += 1
                    if self.id == 3:
                        self.id = 0
                        #messagebox.showinfo(title='Puzzle completado!',message='Tu turno ha finalizado')
                        result = messagebox.askquestion("Si = avanzar, No = retroceder")
                        if result != "no":
                            self.jugadores[jugador_id].posicion += 1
                            if self.jugadores[jugador_id].posicion > 3:
                                self.jugadores[jugador_id].posicion = 0
                        else:
                            self.jugadores[jugador_id].posicion -= 1
                            if self.jugadores[jugador_id].posicion < 0:
                                self.jugadores[jugador_id].posicion = 3
                        juegos += 1
                        win.destroy()
                        self.init_win_tablero()
                pass
            def opcion_reiniciar():
                if dado.escenario.id == 1:
                    dado.escenario.matriz = [
                        [1,0,0,0],
                        [1,0,0,0],
                        [0,0,0,0],
                        [1,1,0,0]
                    ]
                if dado.escenario.id == 2:
                    dado.escenario.matriz = [
                        [0,0,0,1],
                        [0,0,0,0],
                        [0,0,0,0],
                        [0,1,1,1]
                    ]
                dibujar_escenario_figuras()
                self.id = 0
                pass
            def opcion_empezar():
                global empezar
                self.id = 0
                if empezar == False:
                    empezar = True
                    thread.start()
            def avanzar_coordenada(x,y):
                nx = x + 1
                ny = y
                if nx > 3:
                    nx = 0
                    ny += 1
                return nx,ny
            def siguiente_figura():
                self.id += 1
                if self.id > 2:
                    self.id = 0
            def ins_figura_para_bt(x,y):
                for fig in range(3):
                    for inv in range(2):
                        for rot in range(4):
                            if dado.escenario.se_puede_insertar_figura(x,y,dado.figuras[self.id]):
                                m, color = dado.escenario.insertar_figura(x,y,dado.figuras[self.id])
                                dado.escena100o.dibujar_con_figura(win,m,color)
                                
                                siguiente_figura()
                                return True
                            dado.figuras[self.id].rotar()
                        dado.figuras[self.id].invertir()
                    siguiente_figura()
                return False

            def func_bt(x,y):
                if y == 4:
                    return False
                if ins_figura_para_100(x,y):
                    if dado.escenario.esta_completo():
                        return True
                    
                x,y = avanzar_coordenada(x,y)
                #print("avanzar a coordenada",x,y)
                #time.sleep(1)
                return func_bt(x,y)

            def opcion_automatico():
                self.id = 0
                intentos = 0
                while intentos < 10000:
                    system("cls")
                    print("intentos",intentos)
                    #print("nuevo intento..",intentos)
                    if func_bt(0,0):
                        break
                    dado.escenario.generar_id(dado.escenario.id)
                    dado.figuras[0].rotar()
                    dado.figuras[1].rotar()
                    dado.figuras[2].rotar()
                    #self.reiniciar_figuras()
                    intentos += 1
                print("fin")
            # --- SOLICITAR X
            fila = 4
            etiquetaX = tk.Label(win)
            etiquetaX["text"] = "X"
            etiquetaX.grid(row=fila,column=0)
            textoX = tk.Entry(win,font="Calibri 12")
            textoX.grid(row=fila,column=1,columnspan=2)
            fila += 1
            # --- SOLICITAR Y
            etiquetaY = tk.Label(win)
            etiquetaY["text"] = "Y"
            etiquetaY.grid(row=fila,column=0)
            textoY = tk.Entry(win,font="Calibri 12")
            textoY.grid(row=fila,column=1,columnspan=2)
            fila += 1
            # --- OPCION ROTAR
            botonRotar = tk.Button(win,text="ROTAR",command=opcion_rotar)
            botonRotar.grid(row=fila,column=0)
            # --- OPCIÓN INVERTIR
            botonInvertir = tk.Button(win,text="INVERTIR",command=opcion_invertir)
            botonInvertir.grid(row=fila,column=1)
            # --- OPCIÓN INSERTAR
            start = time.perf_counter()
            botonInsertar = tk.Button(win,text="INSERTAR",command=lambda:opcion_insertar(int(textoX.get()),int(textoY.get())))
            botonInsertar.grid(row=fila,column=2)
            fila += 1
            # --- OPCIÓN REINICIAR
            btnReiniciar = tk.Button(win,text="REINICIAR",command=opcion_reiniciar)
            btnReiniciar.grid(row=fila,column=2)
            fila += 1
            #
            # --- OPCIÓN EMPEZAR
            btnEmpezar = tk.Button(win,text="EMPEZAR",command=opcion_empezar)
            btnEmpezar.grid(row=fila,column=2)
            fila += 1
            #
            # --- OPCIÓN AUTOMATICA
            btnAutomatico = tk.Button(win,text="AUTOMATICO",command=opcion_automatico)
            btnAutomatico.grid(row=fila,column=2)
            fila += 1
            #
            juegos += 1
        pass

    def run(self):
        self.root.mainloop()