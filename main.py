from modelos.cliente import Cliente
from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva

import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

clientes = []
reservas = []

print("\n===== SISTEMA SOFTWARE FJ =====\n")

# OPERACIÓN 1
try:
    cliente1 = Cliente("Karol", "karol@gmail.com")
    clientes.append(cliente1)
    print(cliente1.mostrar_info())

except Exception as e:
    logging.error(e)

# OPERACIÓN 2
try:
    cliente2 = Cliente("", "correo@gmail.com")
    clientes.append(cliente2)

except Exception as e:
    print("Error:", e)
    logging.error(e)

# OPERACIÓN 3
try:
    cliente3 = Cliente("Ana", "correo_invalido")
    clientes.append(cliente3)

except Exception as e:
    print("Error:", e)
    logging.error(e)

# OPERACIÓN 4
try:
    servicio1 = ReservaSala("Sala VIP", 50000, 3)
    print(servicio1.descripcion())

except Exception as e:
    logging.error(e)

# OPERACIÓN 5
try:
    servicio2 = AlquilerEquipo("Portátil Gamer", 80000, 2)
    print(servicio2.descripcion())

except Exception as e:
    logging.error(e)

# OPERACIÓN 6
try:
    servicio3 = AsesoriaEspecializada("IA Empresarial", 120000, "Avanzado")
    print(servicio3.descripcion())

except Exception as e:
    logging.error(e)

# OPERACIÓN 7
try:
    servicio_error = ReservaSala("Sala pequeña", -1000, 2)

except Exception as e:
    print("Error:", e)
    logging.error(e)

# OPERACIÓN 8
try:
    reserva1 = Reserva(cliente1, servicio1)
    reserva1.confirmar()
    reservas.append(reserva1)

    print(reserva1.mostrar_reserva())

except Exception as e:
    print("Error:", e)
    logging.error(e)

# OPERACIÓN 9
try:
    reserva1.confirmar()

except Exception as e:
    print("Error:", e)
    logging.error(e)

# OPERACIÓN 10
try:
    reserva1.cancelar()
    print(reserva1.mostrar_reserva())

except Exception as e:
    print("Error:", e)
    logging.error(e)

print("\nSistema ejecutado correctamente")
