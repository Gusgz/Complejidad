import view.JugadorView as jv
class JugadorController:
    def __init__(self,jugador):
        self.model = jugador
        self.view = jv.JugadorView(jugador)
