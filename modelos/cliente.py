from modelos.entidad import Entidad

class Cliente(Entidad):

    def __init__(self, nombre, correo):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"
