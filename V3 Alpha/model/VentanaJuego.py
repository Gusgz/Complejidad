import tkinter as tkinter
import time
import random
from os import system
class VentanaJuego:
    def __init__(self,root,escenario,figuras):
        self.id = 0 # ID DE LA FIGURA ACTUAL SELECCIONADA
        self.root = root
        self.escenario = escenario
        self.figuras = figuras
        self.matriz_original = self.escenario.matriz
        self.memoria = []
        self.cache_id = [0,1,2]

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

    def ins_auto(self,x,y,nivel):
        if self.id > 2:
            self.id = 0
        if self.escenario.esta_completo():
            print("SI")
            return True
        if nivel == 0:
            return False
        for i in range(24):
            ya_testeado = False
            for i in range(len(self.lista)):
                if self.lista[i].id == self.figuras[self.id].id and self.lista[i].estado == self.figuras[self.id].estado and self.lista[i].invertido == self.figuras[self.id].invertido and nivel == 3:
                    ya_testeado = True
            if self.escenario.se_puede_insertar_figura(x,y,self.figuras[self.id]) and ya_testeado == False:
                if nivel == 36:
                    print("guardando figura inicial del bucle...")
                    self.lista.append(self.figuras[self.id])
                    #self.lista.append(self.figuras[self.id].matriz)
                m, color = self.escenario.insertar_figura(x,y,self.figuras[self.id])
                self.dibujar_escenario_con_figura(m,color)
                print("insertando figura",self.id)
                time.sleep(2)
                self.id += 1
                break
            else:
                if i%8 == 0:
                    self.id += 1
                if i%4 == 0:
                    if self.id > 2:
                        self.id = 0
                    self.opcion_invertir()
                    self.figuras[self.id].invertido = True
                if self.id > 2:
                    self.id = 0
                self.opcion_rotar()
                self.figuras[self.id].estado += 1
                if self.figuras[self.id].estado > 3:
                    self.figuras[self.id].estado = 0
        x,y = self.avanzar_coordenada(x,y)
        return self.ins_auto(x,y,nivel-1)

    # NUEVO
    def buscar_en_memoria(self,id):
        for i in range(len(self.memoria)):
            if id == self.memoria[i]:
                return True
        return False

    def siguiente_figura(self):
        self.id += 1
        if self.id > 2:
            self.id = 0

    def ins_figura_auto_V2(self,x,y,n):
        #time.sleep(1)
        #self.reiniciar_figuras()
        #print("probrando insercción en coordenada",x,y)
        for aux in range(3):
            #print("\tFIGURA",self.id)
            time.sleep(1)
            for aux2 in range(2):
                for i in range(4):
                    #print("\t"+str(i))
                    #time.sleep(1)
                    if self.escenario.se_puede_insertar_figura(x,y,self.figuras[self.id]):
                        #print("\t(+) insertando figura",self.id)
                        m, color = self.escenario.insertar_figura(x,y,self.figuras[self.id])
                        self.dibujar_escenario_con_figura(m,color)
                        self.siguiente_figura()
                        #time.sleep(1)
                        return True # SE INSERTÓ LA FIGURA
                    self.opcion_rotar()
                    #time.sleep(1)
                self.opcion_invertir()
                #print("\tinvertir")
            self.siguiente_figura()
        return False # NO SE INSERTÓ LA FIGURA
    
    def re_V2(self,x,y,n):
        #print("FIGURAS POR INSERTAR",n,"/3")
        if y == 4:
            return False
        if self.ins_figura_auto_V2(x,y,n):
            n -= 1
            if self.escenario.esta_completo():
                return True
        x += 1
        if x > 3:
            x = 0
            y += 1
        return self.re_V2(x,y,n)
        
    def reiniciar_escenario(self):
        self.escenario.generar_id()

    def reiniciar_figuras(self):
        for i in range(3):
            self.figuras[i].generar(self.figuras[i].id)

    def opcion_automatico_anterior(self):
        self.id = 0
        intentos = 0
        #system("cls")
        while intentos < 10:
            '''print("--------------------")
            print("Intento(s)",intentos)'''
            print(intentos)
            if self.re_V2(0,0,3):
                #print("bien")
                #time.sleep(3)
                return
            self.reiniciar_escenario()
            intentos += 1
            '''print("--------------------")
            system("cls")'''
        #print("prueba finalizada")
        
        #time.sleep(3)
        #self.escenario.generar_id()
    
    def buscar_en_memoria_bt(self,_id,_inv,_rot,_nivel):
        for id,inv,rot,nivel in self.memoria:
            if id == _id and inv == _inv and rot == _rot and nivel != _nivel:
                return True
        return False

    def buscar_en_memoria_bt_V2(self,matriz,n):
        for i in range(len(self.memoria)):
            if matriz == self.memoria[i] and n == 3:
                return True
        return False

    def siguiente_figura_bt(self,lista,i):
        if len(lista) != 0:
            if i == len(lista):
                i = 0
            self.id = lista[i]

    def ins_figura_para_bt(self,x,y):
        for fig in range(3):
            for inv in range(2):
                for rot in range(4):
                    if self.escenario.se_puede_insertar_figura(x,y,self.figuras[self.id]):
                        m, color = self.escenario.insertar_figura(x,y,self.figuras[self.id])
                        self.dibujar_escenario_con_figura(m,color)
                        '''print("(+) insertando figura",self.id)
                        time.sleep(1)'''
                        self.siguiente_figura()
                        return True
                    self.figuras[self.id].rotar()
                self.figuras[self.id].invertir()
            self.siguiente_figura()
        return False

    def func_bt(self,x,y):
        if y == 4:
            return False
        if self.ins_figura_para_bt(x,y):
            if self.escenario.esta_completo():
                return True
        x,y = self.avanzar_coordenada(x,y)
        #print("avanzar a coordenada",x,y)
        #time.sleep(1)
        return self.func_bt(x,y)



    def opcion_automatico(self):
        self.id = 0
        intentos = 0
        while intentos < 10000:
            system("cls")
            print("intentos",intentos)
            #print("nuevo intento..",intentos)
            if self.func_bt(0,0):
                break
            self.escenario.generar_id()
            self.figuras[0].rotar()
            self.figuras[1].rotar()
            self.figuras[2].rotar()
            #self.reiniciar_figuras()
            intentos += 1
        print("fin")


    # NUEVO
    
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
