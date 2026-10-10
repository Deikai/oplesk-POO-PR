# 🐍 Ejercicios de Programación Orientada a Objetos

Ejercicios de lógica y modelado de objetos usando Python. Cada consigna presenta una situación y una lista de requisitos para guiar la resolución.

## 📚 Índice

1. [Sistema de turnos de un banco](#1-sistema-de-turnos-de-un-banco)
2. [Reproductor de música simple](#2-reproductor-de-música-simple)
3. [Control de clave de seguridad](#3-control-de-clave-de-seguridad)
4. [Áreas de figuras geométricas](#4-áreas-de-figuras-geométricas)
5. [Envío de notificaciones](#5-envío-de-notificaciones)

---

## 1. Sistema de turnos de un banco

### Situación

Un banco pequeño atiende a sus clientes por orden de llegada y entrega números de turno consecutivos, comenzando por el 1. El sistema debe permitir emitir nuevos turnos y llamar al siguiente cliente.

### Requisitos

- [ ] Diseñar una clase `DispensadorTurnos`.
- [ ] Llevar el registro del último número de turno y de cuántos clientes quedan pendientes.
- [ ] Al llamar a un cliente cuando la fila está vacía, indicar que no hay nadie esperando.

**Script:** [`hack_1.py`](hack_1.py)

---

## 2. Reproductor de música simple

### Situación

Una aplicación de música guarda una lista de canciones. El reproductor debe permitir agregar canciones, avanzar a la siguiente pista y mostrar cuál está sonando.

### Requisitos

- [ ] Diseñar la clase `Reproductor`.
- [ ] Administrar la lista de canciones y la posición de la canción actual.
- [ ] Al avanzar desde la última canción, volver a la primera.

**Script:** [`hack_2.py`](hack_2.py)

---

## 3. Control de clave de seguridad

### Situación

Una caja fuerte digital se configura con una clave numérica secreta de cuatro dígitos y comienza bloqueada. El usuario debe ingresar la clave correcta para abrirla. Después de tres intentos fallidos consecutivos, el sistema se bloquea por seguridad y rechaza cualquier intento posterior.

### Requisitos

- [ ] Crear la clase `CajaFuerte`, que reciba la clave secreta al crearse.
- [ ] Llevar el estado de la caja (abierta o cerrada), la cantidad de intentos fallidos y si el sistema está bloqueado por seguridad.
- [ ] Crear un método `desbloquear(clave)`.
- [ ] Crear un método `bloquear()`.

---

## 4. Áreas de figuras geométricas

### Situación

Un programa de dibujo guarda figuras de distintos tipos, por ejemplo, círculos y rectángulos. Se necesita mostrar el nombre y el área de cada figura guardada.

### Requisitos

- [ ] Crear las clases necesarias para representar círculos y rectángulos, recibiendo sus medidas al crearlos.
- [ ] Permitir que cada figura informe su área.
- [ ] Guardar varias figuras en una misma colección y recorrerla para mostrar la información de cada una.

---

## 5. Envío de notificaciones

### Situación

Una aplicación debe enviar mensajes a sus usuarios por distintos medios, como correo electrónico y mensaje de texto. Cada medio presenta el mensaje de una manera diferente, pero la aplicación debe poder enviar todas las notificaciones pendientes.

### Requisitos

- [ ] Crear las clases necesarias para representar los distintos medios de envío. Cada notificación debe guardar el destinatario y el texto del mensaje.
- [ ] Implementar en cada medio la acción de enviar, mostrando en consola el destinatario y el mensaje con un formato adecuado.
- [ ] Guardar notificaciones de distintos medios en una misma colección y enviarlas recorriéndola.
