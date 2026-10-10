import __main__
class DispensadorTurnos:
    def __init__(self):
        self.ultimo_turno_dato = 0
        self.turno_atendiendo = 0

    def tomar_turno(self) -> int:
        """
        Toma un turno para el pequeño banco e imprime en consola el estatus actual

        Return:
            int -> El ultimo turno dado
        """
        self.ultimo_turno_dato += 1
        pendientes = self.ultimo_turno_dato - self.turno_atendiendo
        print(f"Turno emitido: {self.ultimo_turno_dato} | Personas en espera: {pendientes}")
        return self.ultimo_turno_dato

    def llamar_siguiente(self) -> None:
        """Llama al siguiente turno"""
        if self.turno_atendiendo < self.ultimo_turno_dato:
            self.turno_atendiendo += 1
            print(f"-Llamando al turno: {self.turno_atendiendo}")
        else:
            print("No hay clientes espetando en la fila.")


def main() -> None:
    banco = DispensadorTurnos()

    banco.tomar_turno() # Juan  (turno 1)
    banco.tomar_turno() # Ana   (turno 2)
    banco.tomar_turno() # Messi (turno 3)

    banco.llamar_siguiente() # Juan
    banco.llamar_siguiente() # Ana

    banco.tomar_turno() # Pablo ( t4)

    banco.llamar_siguiente()
    banco.llamar_siguiente()

    banco.llamar_siguiente()


if __name__ == "__main__":
    main()
