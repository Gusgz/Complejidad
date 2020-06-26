import view.InterfazView as InterfazView
class InterfazController:
    def __init__(self,model):
        self.model = model
        self.view = InterfazView.InterfazView(model)
    
    def ajustar_pantalla(self,x,y):
        self.model.root.geometry(str(x)+"x"+str(y))
        
    def run(self):
        self.model.root.mainloop()