# Ejercicios de Razonamiento Lógico para POO en Python

## Ejercicio 1: El Sistema de Turnos de un Banco

Un banco pequeño atiende a sus clientes por orden de llegada entregando un número de turno consecutivo (comenzando en el número 1). El sistema debe ser capaz de emitir nuevos turnos y llamar al siguiente cliente en la fila para atenderlo.

Tareas:

    Diseña una clase DispensadorTurnos.

    Mantén el registro del número de turno actual y de cuántos clientes quedan pendientes por atender.

    Si un cajero intenta llamar a un cliente pero la fila está vacía, el sistema debe indicar que no hay nadie esperando.

## Ejercicio 2: Reproductor de Música Simple

Una aplicación de música en streaming tiene una lista de canciones guardadas. El reproductor debe poder agregar canciones, pasar a la siguiente pista de la lista y mostrar qué canción está sonando en ese instante.

Tareas:

    Diseña la clase Reproductor.

    Administra la lista de nombres de canciones y un índice que indique la posición de la canción actual.

    Si el reproductor llega al final de la lista de canciones y el usuario pide avanzar, debe volver a empezar desde la primera canción (reproducción en bucle).


## Ejercicio 3: Control de Clave de Seguridad (Caja Fuerte)


Una caja fuerte digital se configura inicialmente con una clave numérica secreta de 4 dígitos y empieza estando bloqueada. Para desbloquearla, el usuario debe ingresar la clave correcta. Si se equivoca 3 veces consecutivas, el sistema se bloquea por seguridad y rechaza cualquier intento posterior.

Tareas:

    Crea la clase CajaFuerte que reciba la clave_secreta en su creación.

    Guarda el estado de si está abierta/cerrada, cuántos intentos fallidos van y si el sistema está bloqueado por seguridad.

    Crea un método desbloquear(clave) y otro bloquear().