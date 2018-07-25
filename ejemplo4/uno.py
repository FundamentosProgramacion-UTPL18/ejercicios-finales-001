

class Equipo:

    def __init__(self):
        self.nombre = ""
        self.ciudad = ""
        self.jugadores = []

    def agregar_nombre(self, n):
        pass

    def agregar_ciudad(self, n):
        pass

    def agregar_jugadores(self, n):
        self.jugadores = n

    def obtener_nombre(self):
        return self.nombre

    def obtener_jugadores(self):
        return self.jugadores

    def obtener_ciudad(self):
        return self.ciudad
    
    def presentar(self):
        return "%s-%s-%s" % (self.obtener_nombre(), self.obtener_ciudad(), 
                self.obtener_jugadores())
