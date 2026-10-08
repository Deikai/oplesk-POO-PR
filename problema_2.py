class Reproductor:
    def __init__(self):
        self.canciones = []
        self.indice_actual = 0

    def agregar_canciones(self, titulo: str) -> None:
        self.canciones.append(titulo)
        print(f"🎵 Canción agregada: {titulo}")

    def reproducir(self) -> None:
        if not self.canciones:
            print("La lista de reproducción esta vacía.")
            return

        cancion = self.canciones[self.indice_actual]
        print(f"Sonando ahora: `{cancion}` (Pista {self.indice_actual + 1} de {len(self.canciones)})")

    def siguiente(self) -> None:
        if not self.canciones:
            print("No hay canciones para reproducir.")
            return

        # Incrementar y volver a 0 si se llego al final
        self.indice_actual = (self.indice_actual + 1) % len(self.canciones)
        self.reproducir()

        
def main() -> None:
    mi_mp3 = Reproductor()

    mi_mp3.agregar_canciones("Bohemian Rhapsody")
    mi_mp3.agregar_canciones("Asereje de las ketchup")
    mi_mp3.agregar_canciones("Billie Jean")

    print("\n\n--- Reprodución ---")
    mi_mp3.reproducir() # 1
    mi_mp3.siguiente() # 2
    mi_mp3.siguiente() # 3
    mi_mp3.siguiente() # volver 1
    mi_mp3.siguiente() # 2


if __name__ == "__main__":
    main()