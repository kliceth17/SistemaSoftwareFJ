from excepciones.excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):

        try:
            if self.estado == "Confirmada":
                raise ReservaError("La reserva ya está confirmada")

            self.estado = "Confirmada"

        except ReservaError as e:
            raise ReservaError("Error al confirmar reserva") from e

    def cancelar(self):

        try:
            if self.estado == "Cancelada":
                raise ReservaError("La reserva ya está cancelada")

            self.estado = "Cancelada"

        finally:
            print("Proceso de cancelación finalizado")

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
