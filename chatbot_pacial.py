import pyttsx3
import re
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def hablar(texto):
    try:
        engine.say(texto)
        engine.runAndWait()
    except Exception:
        pass

respuestas = [

    ["hola", "Hola! Soy DigiBot, un asistente de Sistemas Digitales creado por Karol Rojas. Puedo explicarte compuertas logicas, semiconductores, algebra de Boole y mucho mas. En que te puedo ayudar?"],
    ["buenas", "Buenas! Soy DigiBot, un asistente de Sistemas Digitales creado por Karol Rojas. Puedo explicarte compuertas logicas, semiconductores, algebra de Boole y mucho mas. En que te puedo ayudar?."],
    ["quien eres", "Soy DigiBot, un asistente de Sistemas Digitales creado por Karol Rojas. Puedo explicarte compuertas logicas, semiconductores, algebra de Boole y mucho mas. En que te puedo ayudar?"],
    ["gracias", "Con gusto! Si tienes mas preguntas, aqui estoy."],
    ["adios", "Hasta luego! Espero haberte ayudado."],
    ["chao", "Chao! Fue un placer."],
    ["salir", "Hasta luego!"],
    ["que es and", "La compuerta AND produce 1 SOLO cuando TODAS sus entradas son 1. Tabla: 0·0=0, 0·1=0, 1·0=0, 1·1=1."],
    ["compuerta and", "La compuerta AND produce 1 SOLO cuando TODAS sus entradas son 1. Tabla: 0·0=0, 0·1=0, 1·0=0, 1·1=1."],
    ["que es or", "La compuerta OR produce 1 cuando AL MENOS UNA entrada es 1. Tabla: 0+0=0, 0+1=1, 1+0=1, 1+1=1."],
    ["compuerta or", "La compuerta OR produce 1 cuando AL MENOS UNA entrada es 1. Tabla: 0+0=0, 0+1=1, 1+0=1, 1+1=1."],
    ["que es not", "La compuerta NOT invierte la entrada. Si entra 0 sale 1, si entra 1 sale 0. Tambien se llama inversor."],
    ["que es nand", "La compuerta NAND es AND seguida de NOT. Su salida es 0 SOLO cuando todas las entradas son 1. Es compuerta universal."],
    ["que es nor", "La compuerta NOR es OR seguida de NOT. Su salida es 1 SOLO cuando todas las entradas son 0. Es compuerta universal."],
    ["que es xor", "La compuerta XOR produce 1 cuando las entradas son DIFERENTES. Tabla: 0 xor 0=0, 0 xor 1=1, 1 xor 0=1, 1 xor 1=0."],
    ["que es xnor", "La compuerta XNOR produce 1 cuando las entradas son IGUALES. Es el complemento de XOR."],
    ["compuerta universal", "Las compuertas universales son NAND y NOR. Con cualquiera de ellas se puede construir cualquier otra compuerta logica."],
    ["diferencia latch flip flop", "El Latch es sensible al NIVEL de la señal de control: cambia mientras la señal este activa. El Flip-Flop es sensible al FLANCO del reloj: solo cambia en el borde de subida o bajada. El flip-flop es mas estable y se usa en circuitos sincronos."],
    ["que es latch", "Un Latch es un elemento de memoria sensible al nivel de una señal de habilitacion. Tipos: SR, D y JK. Mientras la habilitacion este activa, la salida puede cambiar."],
    ["que es flip flop", "Un Flip-Flop almacena 1 bit y cambia solo en el flanco del reloj. Tipos: SR, D, JK y T. Son la base de registros, contadores y memorias sincronas."],
    ["latch sr", "El Latch SR tiene entradas S Set y R Reset. S=1 pone la salida en 1, R=1 la pone en 0. Estado prohibido: S=1 y R=1 al mismo tiempo."],
    ["latch d", "El Latch D tiene una entrada D y una habilitacion E. Cuando E=1 la salida sigue a D. Cuando E=0 mantiene el ultimo valor. Elimina el estado prohibido del SR."],
    ["flip flop d", "El Flip-Flop D captura el valor de la entrada D en cada flanco de reloj. Es el mas usado para registros de almacenamiento."],
    ["flip flop jk", "El Flip-Flop JK mejora el SR. J activa, K desactiva. Cuando J=1 y K=1 la salida conmuta. No tiene estado prohibido."],
    ["flip flop t", "El Flip-Flop T tiene una sola entrada. Cuando T=1 el estado cambia en cada flanco. Cuando T=0 mantiene su valor. Se usa en contadores."],
    ["multiplexor", "Un multiplexor MUX selecciona una entre varias entradas y la dirige a la salida. Un MUX 8 a 1 tiene 8 entradas de datos, 3 lineas de seleccion y 1 salida."],
    ["que es mux", "Un multiplexor MUX selecciona una entre varias entradas y la dirige a la salida. Un MUX 8 a 1 tiene 8 entradas de datos, 3 lineas de seleccion y 1 salida."],
    ["mux 8 entradas", "El MUX 8 a 1 tiene 8 entradas I0 a I7, 3 lineas de seleccion S0 S1 S2 y 1 salida Y. Las 3 lineas permiten seleccionar cualquiera de las 8 entradas mediante combinaciones binarias del 000 al 111."],
    ["demultiplexor", "Un demultiplexor DEMUX toma una entrada y la dirige a una de varias salidas segun las lineas de seleccion. Es el proceso inverso al multiplexor."],
    ["demux 8 salidas", "El DEMUX 1 a 8 tiene 1 entrada D, 3 lineas de seleccion S0 S1 S2 y 8 salidas Y0 a Y7. Segun la combinacion de seleccion, la entrada se dirige a una de las 8 salidas y las demas quedan en 0."],
    ["diferencia mux demux", "El MUX toma muchas entradas y produce una sola salida. El DEMUX toma una sola entrada y la distribuye a muchas salidas. Son operaciones inversas usadas en telecomunicaciones y buses de datos."],
    ["sumador medio", "El sumador medio o Half Adder suma dos bits A y B. Produce la Suma usando XOR y el Acarreo usando AND. No puede procesar acarreo de entrada."],
    ["sumador completo", "El sumador completo o Full Adder suma tres bits: A, B y un acarreo de entrada Cin. Produce Suma con XOR de los tres y Acarreo de salida. Es la base para sumadores de multiples bits."],
    ["circuito secuencial", "Un circuito secuencial tiene salidas que dependen de las entradas actuales Y del estado anterior almacenado. Tiene memoria. Ejemplos: flip-flops, contadores y registros de desplazamiento."],
    ["circuito combinacional", "Un circuito combinacional produce salidas que dependen SOLO de las entradas actuales. No tiene memoria. Ejemplos: sumadores, multiplexores y decodificadores."],
    ["mapa de karnaugh", "El mapa de Karnaugh es una herramienta visual para simplificar funciones booleanas. Se organizan los valores en una cuadricula donde celdas adyacentes difieren en un solo bit. Se agrupan los unos en potencias de 2 para obtener la expresion minima."],
    ["karnaugh", "El mapa de Karnaugh simplifica funciones booleanas visualmente. Agrupa celdas con valor 1 en grupos de 1, 2, 4 u 8. Mientras mas grande el grupo, mas variables se eliminan de la expresion."],
    ["para que sirve karnaugh", "El mapa de Karnaugh sirve para minimizar el numero de compuertas en un circuito, reducir costos de hardware y obtener la expresion booleana mas simple en forma de suma de productos o producto de sumas."],
    ["semiconductores 2026", "En 2026 la industria de semiconductores es una de las mas estrategicas del mundo. Los nodos de fabricacion han alcanzado los 2 y 3 nanometros. La demanda esta impulsada por inteligencia artificial, vehiculos electricos, centros de datos y dispositivos de borde o edge computing."],
    ["semiconductores", "Los semiconductores son materiales con conductividad electrica entre un conductor y un aislante. El silicio es el mas usado. Son la base de todos los circuitos digitales: transistores, chips, microprocesadores y memorias."],
    ["industria semiconductores", "La industria de semiconductores en 2026 mueve billones de dolares anuales. Las tensiones geopoliticas entre Estados Unidos y China han acelerado la construccion de fabricas locales llamadas fabs en Europa, America y Asia."],
    ["que es un semiconductor", "Un semiconductor es un material cuya conductividad puede controlarse con temperatura, luz o campos electricos. El silicio y el germanio son los mas comunes. Los semiconductores permiten fabricar transistores, que son la base de toda la electronica digital."],
    ["empresas semiconductores", "Las empresas mas relevantes en semiconductores en 2026 son: TSMC que fabrica los chips mas avanzados del mundo, NVIDIA lider en GPUs para inteligencia artificial, Intel que fabrica procesadores y recupera terreno en fabricacion, AMD con procesadores de alto rendimiento, Samsung y SK Hynix en memorias, y ASML que fabrica las maquinas de litografia EUV indispensables para chips avanzados."],
    ["tsmc", "TSMC Taiwan Semiconductor Manufacturing Company es la fabrica de chips mas avanzada del mundo. En 2026 produce en nodos de 3 y 2 nanometros. Fabrica chips para Apple, NVIDIA, AMD y muchas otras empresas. Su impacto en sistemas digitales es total: sin TSMC no existirian los procesadores modernos."],
    ["nvidia", "NVIDIA es lider mundial en GPUs y en 2026 domina el mercado de chips para inteligencia artificial. Sus procesadores se usan en centros de datos, supercomputadoras y sistemas de conduccion autonoma. Su impacto en sistemas digitales es enorme al acelerar el computo paralelo masivo."],
    ["intel", "Intel es uno de los pioneros en microprocesadores. En 2026 ha recuperado terreno con su proceso Intel 18A y compite directamente con TSMC en fabricacion avanzada. Sus procesadores Core y Xeon son fundamentales en computadores personales y servidores."],
    ["samsung semiconductores", "Samsung es lider mundial en memorias DRAM y NAND Flash. En 2026 tambien fabrica chips avanzados para clientes externos compitiendo con TSMC. Su impacto en sistemas digitales incluye las memorias de todos los dispositivos electronicos del mundo."],
    ["impacto semiconductores sistemas digitales", "Los semiconductores son el fundamento fisico de los sistemas digitales. Sin ellos no existirian los transistores, compuertas logicas, microprocesadores, memorias ni ningun circuito digital. En 2026 la miniaturizacion extrema permite incluir miles de millones de transistores en un chip del tamano de una una."],
    ["innovacion educacion semiconductores", "La innovacion en educacion con semiconductores y sistemas digitales incluye laboratorios de simulacion virtual, kits de FPGA para practicas, cursos en linea de diseno digital y programas universitarios enfocados en diseño de chips. En 2026 paises como India, Alemania y Colombia han aumentado la inversion en educacion tecnica en electronica."],
    ["innovacion educacion", "La innovacion educativa con sistemas digitales se refleja en el uso de simuladores como Logisim y Multisim, plataformas de aprendizaje con FPGAs como las de Xilinx y Altera, y laboratorios remotos que permiten practicar diseno digital desde cualquier lugar."],
    ["novedad proyectos educacion", "En 2026 los proyectos de sistemas digitales en educacion incluyen: diseno de procesadores simples en FPGA, implementacion de redes neuronales en hardware, proyectos de IoT con microcontroladores, y chatbots educativos como DigiBot que explican conceptos de electronica digital de forma interactiva."],
    ["impacto proyectos digitales educacion", "El impacto de los proyectos de sistemas digitales en educacion es significativo. Desarrollan pensamiento logico, habilidades de diseno y resolucion de problemas. Los estudiantes que aprenden diseno digital tienen alta empleabilidad en sectores como telecomunicaciones, automatizacion e inteligencia artificial."],
    ["sistemas digitales futuro", "El futuro de los sistemas digitales esta marcado por la computacion cuantica, chips neuromorifcos que imitan el cerebro humano, procesadores con inteligencia artificial integrada, y semiconductores de materiales mas alla del silicio como el carburo de silicio y el nitruro de galio para mayor eficiencia energetica."],
    ["semiconductores futuro", "En el futuro los semiconductores evolucionaran hacia materiales alternativos al silicio como el grafeno y el nitruro de galio. La integracion tridimensional de chips 3D stacking permite mayor densidad. La computacion cuantica usara semiconductores especializados para procesar informacion de formas radicalmente distintas."],
    ["futuro sistemas digitales", "El futuro de los sistemas digitales incluye procesadores con IA embebida, edge computing para procesar datos en el dispositivo sin nube, chips de baja potencia para IoT, y la convergencia entre electronica digital y biotecnologia en dispositivos medicos inteligentes."],
    ["algebra de boole", "El Algebra de Boole trabaja con variables que solo valen 0 o 1. Sus operaciones son AND multiplicacion, OR suma y NOT complemento. Sus leyes permiten simplificar circuitos logicos reduciendo compuertas y costo."],
    ["de morgan", "Los teoremas de De Morgan: primero, el complemento de A AND B es igual a NOT A OR NOT B. Segundo, el complemento de A OR B es igual a NOT A AND NOT B. Son esenciales para transformar y simplificar circuitos."],
    ["sistema binario", "El sistema binario usa solo 0 y 1. Es la base de todos los sistemas digitales. Ejemplo: 1011 en binario es 11 en decimal porque es 1x8 + 0x4 + 1x2 + 1x1."],
    ["sistema hexadecimal", "El hexadecimal usa 16 simbolos del 0 al 9 y de A a F. Ejemplo: FF en hexadecimal es 255 en decimal. Se usa mucho en programacion por su compacidad."],
    ["sistema octal", "El octal usa digitos del 0 al 7. Ejemplo: 17 en octal es 15 en decimal porque es 1x8 + 7x1."],
]
def limpiar(texto):
    texto = texto.lower().strip()
    texto = re.sub(r'[¿?¡!.,]', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto

def get_response(pregunta):
    pregunta = limpiar(pregunta)
    mejor = None
    mejor_score = 0

    for par in respuestas:
        clave = par[0]
        if clave == pregunta:
            return par[1]
        palabras_clave = set(clave.split())
        palabras_pregunta = set(pregunta.split())
        score = len(palabras_clave & palabras_pregunta)
        if score > mejor_score:
            mejor_score = score
            mejor = par[1]

    if mejor_score >= 1:
        return mejor

    return ("No tengo informacion especifica sobre eso. Puedes preguntarme sobre: "
            "compuertas AND OR NOT NAND NOR XOR, latch, flip-flop, multiplexor, "
            "sumadores, semiconductores 2026, empresas como TSMC o NVIDIA, "
            "educacion digital, futuro de sistemas digitales, algebra de Boole y Karnaugh.")

def main():
    print("=" * 60)
    print("   DIGIBOT - Asistente de Sistemas Digitales creado por Karol Rojas")
    print("   Escribe 'salir' para terminar")
    print("=" * 60 + "\n")

    bienvenida = "Hola! Soy DigiBot un asistente de Sistemas Digitales creado por Karol Rojas. Preguntame sobre sistemas digitales, semiconductores o educacion digital."
    print(f"DigiBot: {bienvenida}\n")
    hablar(bienvenida)

    while True:
        pregunta = input("Tu: ").strip()
        if not pregunta:
            continue
        respuesta = get_response(pregunta)
        print(f"\nDigiBot: {respuesta}\n")
        hablar(respuesta)
        if limpiar(pregunta) in ["salir", "adios", "chao"]:
            break

if __name__ == "__main__":
    main()
