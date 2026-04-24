# PARCIAL DE SISTEMAS DIGITALES | SEGUNDO CORTE 

Elaborado por: Karol Vanessa Rojas Gil

Docente: Diego Alejandro Barragan Vargas

------------------------
# PARTE CONCEPTUAL 

**- ¿Cuál es la diferencia entre un latch y un flip flop?**

| **Característica** | **Latch** | **Flip-Flop** |
|--------------------|-----------|---------------|
| Sensibilidad | Nivel (activo mientras la señal esté activa) | Flanco (actúa solo en el borde de subida o bajada del reloj) |
| Sincronización | Asíncrono | Síncrono |
| Estabilidad | Menos estable, propenso a glitches | Más estable y predecible |
| Uso típico | Circuitos simples, registros transparentes | Registros, contadores, memorias |

**- ¿Cuáles son los diferentes tipos de latch y flip flops?**

**Latch:**

**Latch SR (Set-Reset):** Tiene dos entradas S y R. S=1 pone la salida en 1, R= 1 la pone en 0. Estado prohibido: S=1 y R=1 simultáneamente.

**Latch D (Data):** Tiene una entrada D y una habilitación E. Cuando E=1, la salida sigue a D. Cuando E= 0, mantiene el último valor. Elimina el estado prohibido del SR.

**Latch JK:** Mejora del SR. Cuando J=1 y K=1 la salida conmuta (toggle). No tiene estado prohibido.

**Flip-Flop:**

**FF-SR:** Igual al latch SR pero disparado por flanco de reloj. Tiene estado prohibido con S=R=1.

**FF-D:** Captura el valor de D en cada flanco de reloj. Es el más usado para registros de almacenamiento.

**FF-JK:** El más versátil. J activa, K desactiva, J=K=1 conmuta. No tiene estado prohibido.

**FF-T (Toggle):** Tiene una sola entrada T. Si T=1 en cada flanco el estado conmuta. Si T =0 mantiene su valor. Se usa en contadores.

**- ¿Cuál es la diferencia entre un multiplexor y un demultiplexor?**

| **Característica** | **Multiplexor (MUX)** | **Demultiplexor (DEMUX)** |
|--------------------|-----------------------|---------------------------|
| Función | Selecciona una de N entradas y la envía a una salida | Toma una entrada y la dirige a una de N salidas |
| Entradas de datos | Múltiples | Una |
| Salidas | Una | Múltiples |
| Analogía | Muchos canales → un cable | Un cable → muchos canales |

**Multiplexor de 8 entradas**

Tiene 8 entradas de datos (I0–I7), 3 líneas de selección (S0, S1, S2) y 1 salida Y.  
Las 3 líneas de selección permiten 2³ = 8 combinaciones, seleccionando cada una de las 8 entradas, como se ve a continuación:

```
S2 S1 S0  | Salida Y
----------|----------
0  0  0   |    I0
0  0  1   |    I1
0  1  0   |    I2
0  1  1   |    I3
1  0  0   |    I4
1  0  1   |    I5
1  1  0   |    I6
1  1  1   |    I7
```

Ecuación de salida: `Y = S2'S1'S0'·I0 + S2'S1'S0·I1 + ... + S2·S1·S0·I7`

**Demultiplexor de 8 salidas**

Tiene 1 entrada de datos (D), 3 líneas de selección (S0, S1, S2) y 8 salidas (Y0–Y7).  
Dirige la entrada D hacia la salida seleccionada; las demás salidas quedan en 0, como se ve a continuación:

```
S2 S1 S0  | Salida activa
----------|---------------
0  0  0   |    Y0 = D
0  0  1   |    Y1 = D
0  1  0   |    Y2 = D
0  1  1   |    Y3 = D
1  0  0   |    Y4 = D
1  0  1   |    Y5 = D
1  1  0   |    Y6 = D
1  1  1   |    Y7 = D
```

**- ¿Qué es un sumador completo, un sumador medio y circuitos secuenciales?**

**Sumador medio:** suma dos bits (A y B) y produce dos salidas
- **Suma (S):** S = A XOR B
- **Acarreo (C):** C = A AND B

No puede procesar el acarreo de una operación anterior. Es la unidad más básica de suma binaria.

```
A | B | Suma | Acarreo
0 | 0 |  0   |   0
0 | 1 |  1   |   0
1 | 0 |  1   |   0
1 | 1 |  0   |   1
```

**Sumador Completo:** suma tres bits: A, B y un acarreo de entrada (Cin)
- **Suma (S):** S = A XOR B XOR Cin
- **Acarreo de salida (Cout):** Cout = (A AND B) OR (Cin AND (A XOR B))

Es la base para construir sumadores de N bits encadenando varios Full Adders.

```
A | B | Cin | Suma | Cout
0 | 0 |  0  |  0   |  0
0 | 0 |  1  |  1   |  0
0 | 1 |  0  |  1   |  0
0 | 1 |  1  |  0   |  1
1 | 0 |  0  |  1   |  0
1 | 0 |  1  |  0   |  1
1 | 1 |  0  |  0   |  1
1 | 1 |  1  |  1   |  1
```

**Circuitos Secuenciales:** a diferencia de los combinacionales, los circuitos secuenciales tienen memoria: su salida depende de las entradas actuales Y del estado previo almacenado. Requieren un elemento de memoria (flip-flop) y generalmente una señal de reloj. Ejemplos: contadores, registros de desplazamiento, máquinas de estados.

**- ¿Qué es un mapa de karnaugh? ¿Para qué sirve?**

El mapa de Karnaugh es una herramienta gráfica para simplificar funciones booleanas sin necesidad de aplicar álgebra manualmente. Organiza la tabla de verdad en una cuadrícula donde las celdas adyacentes difieren en exactamente un bit (código Gray).

**¿Para qué sirve?**
- Minimizar el número de compuertas necesarias en un circuito
- Obtener la expresión booleana más simple (SOP o POS)
- Reducir costo y complejidad del hardware

**Reglas de agrupación:**
- Los grupos deben ser de tamaño potencia de 2: 1, 2, 4, 8 celdas
- Solo se agrupan celdas con valor 1
- Los grupos pueden ser adyacentes horizontal, vertical y en los bordes (wrap-around)
- Mientras más grande el grupo, más variables se eliminan

-------------------

# PARTE DE DISEÑO

**Ecuacion utilizada para el dibujo del circuito y tabla de verdad (2a):** <img width="910" height="114" alt="image" src="https://github.com/user-attachments/assets/407a41a4-c211-4b85-b716-bc2c405258cd" />

**Dibujo:** <img width="810" height="334" alt="image" src="https://github.com/user-attachments/assets/55b08d91-a0c3-4978-a750-d63b7067f2be" />

**Tabla de verdad:**

| **A** | **B** | **C** | **D** | **B̄** | **ĀB̄** | **BD** | **C+BD** | **(C+BD)+ĀB̄** | **AB̄** | **X** |
|---|---|---|---|----|----|-----|------|-----------|-----|-----------------|
| 0 | 0 | 0 | 0 |  1 |  1 |  0  |  0   |     1     |  0  |        0        |
| 0 | 0 | 0 | 1 |  1 |  1 |  0  |  0   |     1     |  0  |        0        |
| 0 | 0 | 1 | 0 |  1 |  1 |  0  |  1   |     1     |  0  |        0        |
| 0 | 0 | 1 | 1 |  1 |  1 |  0  |  1   |     1     |  0  |        0        |
| 0 | 1 | 0 | 0 |  0 |  0 |  0  |  0   |     0     |  0  |        0        |
| 0 | 1 | 0 | 1 |  0 |  0 |  1  |  1   |     1     |  0  |        0        |
| 0 | 1 | 1 | 0 |  0 |  0 |  0  |  1   |     1     |  0  |        0        |
| 0 | 1 | 1 | 1 |  0 |  0 |  1  |  1   |     1     |  0  |        0        |
| 1 | 0 | 0 | 0 |  1 |  0 |  0  |  0   |     0     |  1  |        0        |
| 1 | 0 | 0 | 1 |  1 |  0 |  0  |  0   |     0     |  1  |        0        |
| 1 | 0 | 1 | 0 |  1 |  0 |  0  |  1   |     1     |  1  |        1        |
| 1 | 0 | 1 | 1 |  1 |  0 |  0  |  1   |     1     |  1  |        1        |
| 1 | 1 | 0 | 0 |  0 |  0 |  0  |  0   |     0     |  0  |        0        |
| 1 | 1 | 0 | 1 |  0 |  0 |  1  |  1   |     1     |  0  |        0        |
| 1 | 1 | 1 | 0 |  0 |  0 |  0  |  1   |     1     |  0  |        0        |
| 1 | 1 | 1 | 1 |  0 |  0 |  1  |  1   |     1     |  0  |        0        |

**Simplificación:**

```
Cuando C = 0 → X = 0 (el factor C al final anula todo)
Cuando C = 1 → C + BD = 1, entonces:
  X = AB̄(1 + ĀB̄) · 1 = AB̄
Resultado simplificado: X = AB̄C
```

**Resultado:**

X = 1 únicamente cuando A = 1, B = 0, C = 1 (mintérminos 10 y 11)  
Expresión mínima: **X = AB̄C**

<img width="810" height="334" alt="image" src="https://github.com/user-attachments/assets/53a99551-1849-4169-8910-22719347d559" />

---------------

**Ecuacion utilizada para el dibujo del circuito y tabla de verdad (2b):** <img width="910" height="114" alt="image" src="https://github.com/user-attachments/assets/38721302-67d6-47c9-a2e0-f72aea35b444" />

**Dibujo:** <img width="810" height="334" alt="Captura de pantalla 2026-04-23 203236" src="https://github.com/user-attachments/assets/5d69c2e5-e2ba-42e7-b106-007c4e378f58" />

**Explicación:**

```
1. Se distribuye:

A B̄ C · BD = 0  (porque B · B̄ = 0)  
A B̄ C · CDE = A B̄ C D E  

Entonces:

X = A B̄ C D E + AC  

2. Se factoriza:

X = AC (1 + B̄ D E)

3. Propiedad booleana:

1 + cualquier cosa = 1  

Resultado:

X = AC
```

**Tabla de verdad**

| **A** | **B** | **C** | **D** | **E** | **X** |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 |


**Resultado:**

X = 1 únicamente cuando:

- A = 1  
- C = 1  

(No depende de B, D, ni E)


**Mintérminos:**

Los valores donde X = 1 corresponden a:

m(20, 21, 22, 23, 28, 29, 30, 31)

**Expresión mínima:** X = AC




