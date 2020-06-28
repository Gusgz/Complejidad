import tkinter as tkinter
class InterfazView:
    def __init__(self,model):
        self.model = model
        self.dibujar_escenario()
        self.dibujar_figuras()
        self.dibujar_menu_juego()

    def dibujar_escenario(self):
        canvas = tkinter.Canvas(self.model.root,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if self.model.escenario.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if self.model.escenario.matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)

    def dibujar_figura(self,f,c,matriz,color):
        canvas = tkinter.Canvas(self.model.root,width=90,height=90)
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
            self.dibujar_figura(0,i,self.model.figuras[i].matriz,self.model.figuras[i].color)

    def dibujar_menu_juego(self):
        def opcion_invertir(i):
            self.model.figuras[i].matriz = list(reversed(self.model.figuras[i].matriz))
            self.dibujar_figura(0,i,self.model.figuras[i].matriz,self.model.figuras[i].color)
        def opcion_rotar(i):
            matriz = []
            for f in range(len(self.model.figuras[i].matriz[0])):
                matriz.append([])
                for c in range(len(self.model.figuras[i].matriz)):
                    matriz[f].append(self.model.figuras[i].matriz[len(self.model.figuras[i].matriz)-1-c][f])
            self.model.figuras[i].matriz = matriz
            self.dibujar_figura(0,i,self.model.figuras[i].matriz,self.model.figuras[i].color)
        def opcion_insertar(x,y,i):
            self.model.escenario.insertar_figura(x,y,self.model.figuras[i])
            self.dibujar_escenario()
        def opcion_automatico(aux):
            #while(self.model.escenario.esta_completo()):
            for i in range(4):
                for j in range(4):
                    if self.model.escenario.se_puede_insertar(i,j,self.model.figuras[aux]) == True and self.model.escenario.primera_coordenada(self.model.figuras[aux]) == True:
                        self.model.escenario.insertar_figura(i,j,self.model.figuras[aux])
                        self.dibujar_escenario()
                        opcion_automatico(aux+1)
                    else:
                        opcion_rotar(aux)
        cont = 4
        # ID FIGURA
        etiqueta = tkinter.Label(self.model.root)
        etiqueta["text"] = "ID FIGURA"
        etiqueta.grid(row=cont,column=0)
        texto = tkinter.Entry(self.model.root,font="Calibri 12")
        texto.grid(row=cont,column=1,columnspan=2)
        cont += 1
        # OPCIONES ROTAR E INVERTIR
        botonRotar = tkinter.Button(self.model.root,text="ROTAR",command=lambda:opcion_rotar(int(texto.get())-1))
        botonRotar.grid(row=cont,column=1)
        botonInvertir = tkinter.Button(self.model.root,text="INVERTIR",command=lambda:opcion_invertir(int(texto.get())-1))
        botonInvertir.grid(row=cont,column=2)
        cont += 1
        # EN LA POSICIÓN X
        etiquetaX = tkinter.Label(self.model.root)
        etiquetaX["text"] = "X"
        etiquetaX.grid(row=cont,column=0)
        textoX = tkinter.Entry(self.model.root,font="Calibri 12")
        textoX.grid(row=cont,column=1,columnspan=2)
        cont += 1
        # EN LA POSICIÓN Y
        etiquetaY = tkinter.Label(self.model.root)
        etiquetaY["text"] = "Y"
        etiquetaY.grid(row=cont,column=0)
        textoY = tkinter.Entry(self.model.root,font="Calibri 12")
        textoY.grid(row=cont,column=1,columnspan=2)
        cont += 1
        # OPCIÓN INSERTAR
        botonInsertar = tkinter.Button(self.model.root,text="INSERTAR",command=lambda:opcion_insertar(int(textoX.get()),int(textoY.get()),int(texto.get())-1))
        botonInsertar.grid(row=cont,column=1,columnspan=2)
        cont += 1
        # AUTOMÁTICO
        botonAutomatico = tkinter.Button(self.model.root,text="AUTOMÁTICO",command=lambda:opcion_automatico(0))
        botonAutomatico.grid(row=cont,column=1,columnspan=2)




