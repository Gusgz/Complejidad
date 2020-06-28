import model.Interfaz as Interfaz
import view.InterfazView as InterfazView
class InterfazController:
    def __init__(self,escenario,figuras):
        self.model = Interfaz.Interfaz(escenario,figuras)
        self.view = InterfazView.InterfazView(self.model)
        self.run()
    
    def ajustar_pantalla(self,x,y):
        self.model.root.geometry(str(x)+"x"+str(y))
        
    def run(self):
        self.model.root.mainloop()