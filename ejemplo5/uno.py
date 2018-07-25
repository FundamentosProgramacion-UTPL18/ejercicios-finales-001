

class Equipo:

    def __init__(self):
        self.nombre = "Demo"
        self.jugadores = []
        self.ciudad = "Loja"

    def agregar_nombre(self, n):
        self.agregar_nombre = n


    def agregar_jugadores(self, lista):
        self.jugadores = [1,2,3]
    
    def agregar_ciudad(self, n):
        self.ciudad = n

    def obtener_nombre(self):
        return self.nombre

    def obtener_jugadores(self):
        return self.jugadores

    def obtener_ciudad(self):
        return self.ciudad

    def obtener_promedio_jugadores(self):
        return self.jugadores
    
    def presentar(self):
        return "%s-%s-Promedio-edad de jugadores %s" % (self.obtener_nombre(), self.obtener_ciudad(), 
                self.obtener_promedio_jugadores())
