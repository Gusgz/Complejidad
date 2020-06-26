import tkinter as tkinter
class InterfazView:
    def __init__(self,model):
        self.model = model

    def dibujar_figura(self,f,c,matriz,libre,ocupado):
        canvas = tkinter.Canvas(self.model.root,width=90,height=90)
        for i in range(3):
            x = i*30
            for j in range(3):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=libre)
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=ocupado)
        canvas.grid(row=f,column=c)
    
    def dibujar_escenario(self,f,c,matriz,libre,ocupado):
        canvas = tkinter.Canvas(self.model.root,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=libre)
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=ocupado)
        canvas.grid(row=f,column=c,columnspan=3)

    # ESTO DEBE ESTAR EN CONTROLLER
    
    # ___

    def dibujar_menu_juego(self,figuras):
        def invertir(figuras,aux):
            figuras[aux].model.matriz = list(reversed(figuras[aux].model.matriz))
            self.dibujar_figura(0,aux,figuras[aux].model.matriz,"white",figuras[aux].model.color)

        def rotar(figuras,aux):
            matriz = []
            for i in range(len(figuras[aux].model.matriz[0])):
                matriz.append([])
                for j in range(len(figuras[aux].model.matriz)):
                    matriz[i].append(figuras[aux].model.matriz[len(figuras[aux].model.matriz)-1-j][i])
            figuras[aux].model.matriz = matriz
            self.dibujar_figura(0,aux,figuras[aux].model.matriz,"white",figuras[aux].model.color)

        cont = 4
        # ID FIGURA
        etiqueta = tkinter.Label(self.model.root)
        etiqueta["text"] = "ID FIGURA"
        etiqueta.grid(row=cont,column=0)
        texto = tkinter.Entry(self.model.root,font="Calibri 12")
        texto.grid(row=cont,column=1,columnspan=2)
        cont += 1
        # OPCIONES ROTAR E INVERTIR
        botonRotar = tkinter.Button(self.model.root,text="ROTAR",command=lambda:rotar(figuras,int(texto.get())))
        botonRotar.grid(row=cont,column=1)
        botonInvertir = tkinter.Button(self.model.root,text="INVERTIR",command=lambda:invertir(figuras,int(texto.get())))
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
        botonInsertar = tkinter.Button(self.model.root,text="INSERTAR")
        botonInsertar.grid(row=cont,column=1,columnspan=2)




