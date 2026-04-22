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













