from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        self.horas = horas

    def calcular_costo(self, impuesto=0):
        return (self.precio_base * self.horas) + impuesto

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)

        if dias <= 0:
            raise ValueError("Los días deben ser mayores a cero")

        self.dias = dias

    def calcular_costo(self, descuento=0):
        total = self.precio_base * self.dias
        return total - descuento

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, nivel):
        super().__init__(nombre, precio_base)
        self.nivel = nivel

    def calcular_costo(self, extra=0):
        return self.precio_base + extra

    def descripcion(self):
        return f"Asesoría especializada nivel {self.nivel}"
