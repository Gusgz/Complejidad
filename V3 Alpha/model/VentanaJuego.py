import tkinter as tkinter
import time
class VentanaJuego:
    def __init__(self,root,escenario,figuras):
        self.id = 0 # ID DE LA FIGURA ACTUAL SELECCIONADA
        self.root = root
        self.escenario = escenario
        self.figuras = figuras

    def iniciar(self):
        self.root.mainloop()

    def finalizar(self):
        self.root.destroy()

    def dibujar_figura(self,f,c,matriz,color):
        canvas = tkinter.Canvas(self.root,width=90,height=90)
        for i in range(3):
            x = i*30
            for j in range(3):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=color)
        canvas.grid(row=f,column=c)

    def dibujar_figuras(self):
        for i in range(3):
            self.dibujar_figura(0,i,self.figuras[i].matriz,self.figuras[i].color)
    
    def dibujar_escenario(self):
        canvas = tkinter.Canvas(self.root,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if self.escenario.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if self.escenario.matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)

    def dibujar_escenario_con_figura(self,m,color):
        canvas = tkinter.Canvas(self.root,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if self.escenario.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if self.escenario.matriz[j][i] == 1:
                    if m[j][i] == 1:
                        canvas.create_rectangle(x,y,x+30,y+30,fill=color)
                    else:
                        canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)


    def opcion_invertir(self):
        self.figuras[self.id].invertir()
        self.dibujar_figura(0,self.id,self.figuras[self.id].matriz,self.figuras[self.id].color)

    def opcion_rotar(self):
        self.figuras[self.id].rotar()
        self.dibujar_figura(0,self.id,self.figuras[self.id].matriz,self.figuras[self.id].color)

    def opcion_insertar(self,x,y):
        if self.escenario.se_puede_insertar_figura(x,y,self.figuras[self.id]) and self.id < 3:
            m, color = self.escenario.insertar_figura(x,y,self.figuras[self.id])
            self.dibujar_escenario_con_figura(m,color)
            self.id += 1
            if self.id == 3:
                self.finalizar()

    def avanzar_coordenada(self,x,y):
        nx = x + 1
        ny = y
        if nx > 3:
            nx = 0
            ny += 1
        return nx,ny
                

    def insertar_figura_automatica(self,x,y):
        cont = 0
        for aux in range(100):
            if self.escenario.se_puede_insertar_figura(x,y,self.figuras[self.id]):
                #
                print("insertó",self.id)
                m, color = self.escenario.insertar_figura(x,y,self.figuras[self.id])
                self.dibujar_escenario_con_figura(m,color)
                time.sleep(3)
                #
                self.id += 1
                if self.id > 3:
                    self.id = 0
                #
                x,y = self.avanzar_coordenada(x,y)
            else:
                self.opcion_rotar()
                cont += 1
                if cont == 4:
                    self.opcion_invertir()
                    print("modo espejo...")
                if cont == 8:
                    print("nueva figura...")
                    self.id += 1
                    cont = 0
            x,y = self.avanzar_coordenada(x,y)
            if y == 4:
                print("FAIL")
                break
        print("FIN DEL BUCLE")


    def opcion_automatico(self):
        self.id = 0
        self.insertar_figura_automatica(0,0)

    def dibujar_menu_juego(self):
        fila = 4
        # SOLICITAR X
        etiquetaX = tkinter.Label(self.root)
        etiquetaX["text"] = "X"
        etiquetaX.grid(row=fila,column=0)
        textoX = tkinter.Entry(self.root,font="Calibri 12")
        textoX.grid(row=fila,column=1,columnspan=2)
        fila += 1
        # SOLICITAR Y
        etiquetaY = tkinter.Label(self.root)
        etiquetaY["text"] = "Y"
        etiquetaY.grid(row=fila,column=0)
        textoY = tkinter.Entry(self.root,font="Calibri 12")
        textoY.grid(row=fila,column=1,columnspan=2)
        fila += 1
        # OPCION ROTAR
        botonRotar = tkinter.Button(self.root,text="ROTAR",command=self.opcion_rotar)
        botonRotar.grid(row=fila,column=0)
        # OPCIÓN INVERTIR
        botonInvertir = tkinter.Button(self.root,text="INVERTIR",command=self.opcion_invertir)
        botonInvertir.grid(row=fila,column=1)
        # OPCIÓN INSERTAR
        botonInsertar = tkinter.Button(self.root,text="INSERTAR",command=lambda:self.opcion_insertar(int(textoX.get()),int(textoY.get())))
        botonInsertar.grid(row=fila,column=2)
        fila += 1
        # AUTOMÁTICO
        botonAutomatico = tkinter.Button(self.root,text="AUTOMATICO",command=self.opcion_automatico)
        botonAutomatico.grid(row=fila,column=0,columnspan=3)
        fila += 1
