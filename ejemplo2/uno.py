

class Equipo:

    def __init__(self):
        self.nombre = "Demo"
        self.jugadores = 22
        self.ciudad = "Loja"

    def agregar_nombre(self, n):
        self.agregar_nombre = n


    def agregar_ciudad(self, n):
        self.ciudad = n

    def obtener_nombre(self):
        return self.nombre

    def obtener_jugadores(self):
        return self.jugadores

    def obtener_ciudad(self):
        return self.ciudad
    
    def presentar(self):
        return "%s-%s-%s" % (self.obtener_nombre(), self.obtener_ciudad(), 
                self.obtener_jugadores())
