# Misión Órbita – Avance 1: Preparación de la misión

Simulador básico de exploración espacial en Python. En este primer avance se desarrollan
cuatro algoritmos independientes que calculan y verifican los recursos necesarios antes
de autorizar el lanzamiento de una misión.

Curso: SOFT-01 Principios de Programación 1 – Sección SCP0
Universidad CENFOTEC – C3-2026

Repositorio: https://github.com/MiguelVC95/PROYECTO--PREPARACI-N-DE-LA-MISI-N

## Integrantes
- Sharon Avila M
- Miguel Vargas
- Marcela Otarola

## Requisitos
- Python 3 instalado
- Visual Studio Code (recomendado)

## Descripción de los ejercicios

| Ejercicio | Archivo | Estructura de control | Propósito |
|---|---|---|---|
| 1. Cálculo de recursos | `ejercicio1_recursos.py` | Secuencial | Calcula combustible (ida, regreso, reserva y total), oxígeno, energía y provisiones |
| 2. Verificación de combustible | `ejercicio2_combustible.py` | Condicional simple | Calcula el combustible total y el adicional; advierte si el margen es menor que 10 |
| 3. Soporte para la tripulación | `ejercicio3_soporte_tripulacion.py` | Condicional doble | Verifica que el oxígeno **y** las provisiones sean suficientes |
| 4. Autorización de lanzamiento | `ejercicio4_autorizacion.py` | Condicional doble sin anidación | Autoriza solo si combustible (ida + regreso + reserva), oxígeno, energía y provisiones son suficientes |

## Estructura del repositorio

```text

PROYECTO--PREPARACI-N-DE-LA-MISI-N/ ├── README.md ├── avance1/ │ ├── ejercicio1_recursos.py │ ├── ejercicio2_combustible.py │ ├── ejercicio3_soporte_tripulacion.py │ └── ejercicio4_autorizacion.py └── documentacion/ └── avance1/ ├── [Avance1_MisionOrbita.pdf] ├── ejercicio1_recursos.drawio ├── ejercicio1_recursos.png ├── ejercicio2_combustible.drawio ├── ejercicio2_combustible.png ├── ejercicio3_soporte_tripulacion.drawio ├── ejercicio3_soporte_tripulacion.png ├── ejercicio4_autorizacion.drawio └── ejercicio4_autorizacion.png

## Ejecución

### Requisitos
- Python 3 instalado ([python.org](https://www.python.org/downloads/)).
- Visual Studio Code (recomendado).
- No se requieren librerías externas: los programas usan solo la consola.

### 1. Obtener el código

**Opción A – Clonar con Git:**

```bash

git clone https://github.com/MiguelVC95/PROYECTO--PREPARACI-N-DE-LA-MISI-N.git 
cd PROYECTO--PREPARACI-N-DE-LA-MISI-N

**Opción B – Descargar ZIP:** botón **Code → Download ZIP** y descomprimir.
La carpeta se llamará `PROYECTO--PREPARACI-N-DE-LA-MISI-N-main`.

### 2. Ejecutar los programas

Desde la carpeta raíz del repositorio:

**Windows (PowerShell o CMD):**

```powershell

python avance1\ejercicio1_recursos.py python avance1\ejercicio2_combustible.py python avance1\ejercicio3_soporte_tripulacion.py python avance1\ejercicio4_autorizacion.py

> Si `python` no se reconoce, usar `py` en su lugar.

**macOS / Linux:**

```bash

python3 avance1/ejercicio1_recursos.py python3 avance1/ejercicio2_combustible.py python3 avance1/ejercicio3_soporte_tripulacion.py python3 avance1/ejercicio4_autorizacion.py

**Desde Visual Studio Code:** abrir la carpeta del repositorio (**Archivo → Abrir carpeta**),
abrir el archivo `.py` deseado y presionar **▷ Run Python File**.

Cada programa solicita los datos en consola. Se deben ingresar **números enteros positivos**
(excepto el nombre de la misión en el ejercicio 1).

### 3. Prueba rápida (casos documentados)

| Programa | Datos de entrada | Resultado esperado |
|---|---|---|
| Ejercicio 1 | Explorador I, 3, 5 | Total combustible = 90; Oxígeno = 35; Energía = 35; Provisiones = 18 |
| Ejercicio 2 | 95, 40, 40 | Total = 90; Adicional = 5; muestra advertencia |
| Ejercicio 3 | 35, 35, 18, 18 | "La nave posee recursos suficientes para la tripulación." |
| Ejercicio 4 | 50, 40, 40, 50, 35, 40, 35, 25, 18 | "Lanzamiento no autorizado. La misión debe ser revisada." (solo alcanza para llegar) |

Los casos de prueba completos (exitosos, límite y de fallo) están en el PDF de documentación.

---

## Documentación

Toda la documentación del Avance 1 se encuentra en [`documentacion/avance1/`](documentacion/avance1/).

| Contenido | Archivo |
|---|---|
| Informe completo (portada, tablas de variables, diagramas, casos de prueba y capturas) | [Avance1_MisionOrbita.pdf](documentacion/avance1/Avance1_MisionOrbita.pdf) |
| Diagrama Ejercicio 1 – Recursos | [PNG](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaRecursos.drawio.png) · [drawio](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaRecursos.drawio) |
| Diagrama Ejercicio 2 – Combustible | [PNG](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaCombustible.drawio.png) · [drawio](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaCombustible.drawio) |
| Diagrama Ejercicio 3 – Soporte tripulación | [PNG](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaSoporteTripulacion.drawio.png) · [drawio](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaSoporteTripulacion.drawio) |
| Diagrama Ejercicio 4 – Autorización | [PNG](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaAutorizacion.drawio.png) · [drawio](PROYECTO--PREPARACI-N-DE-LA-MISI-N/DiagramaAutorizacion.drawio) |

- El **PDF** es el documento oficial de la entrega.
- Los archivos **.png** son los diagramas exportados para lectura.
- Los archivos **.drawio** son editables: se abren en [app.diagrams.net](https://app.diagrams.net)
  con **Archivo → Abrir desde → Dispositivo**.

---

## Restricciones técnicas cumplidas

- Solo consola para entrada y salida, con variables simples y enteros positivos.
- Sin ciclos, listas, tuplas, diccionarios ni colecciones.
- Sin funciones `def`, sin librerías ni `import`, sin archivos, JSON ni POO.
- Constantes en MAYÚSCULAS declaradas al inicio de cada archivo (sin números mágicos).
- Variables en `snake_case`, indentación de 4 espacios y encabezado completo en cada archivo.
- Código elaborado en Visual Studio Code como archivos `.py` independientes.

---

## Reglas principales de la misión

- El combustible total siempre incluye **ida + regreso + reserva de 10 unidades**.
- Una misión con combustible suficiente **solo para llegar** no se autoriza, porque la tripulación quedaría varada.
- El viaje de regreso dura la misma cantidad de días que el de ida.



