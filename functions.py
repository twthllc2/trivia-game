#Majotori, juego de trivia en el que tus decisiones impactan en la vida de los personajes
import sys
import time
import random
from vardata import *
#Aquí se encuentran las distintas funciones y cosas varias
def ver_puntuacion():
    print("Número de aciertos:")
    print(a)
    print("Número de fallos:")
    print(b)

def esperando_resultado():
    print("Sorteando entre aciertos y fallos...")
    time.sleep(time_duration_2)

def pantalla_titulo():
    boton2 = str(input("M A J O T O R I O"))
    time.sleep(time_duration_menu)
    print("1. Jugar")
    time.sleep(time_duration_menu)
    print("2. Ayuda")
    time.sleep(time_duration_menu)
    menu = str(input("Selecciona: "))
    if menu == ("1"):
        print("Has seleccionado: Jugar")
        time.sleep(time_duration)
    elif menu == ("2"):
        print("Has seleccionado: Ayuda")
        time.sleep(time_duration)
        print("Analiza las opciones y escribe el número correcto para acertar.")
        time.sleep(time_duration)
        print("¡Ten cuidado! Muchas personas van a depender de tus respuestas.")
        time.sleep(time_duration)
        boton1 = str(input("Pulsa enter para comenzar: "))
    else:
        print("No se ha entendido tu respuesta. Selección automática modo jugar.")
        time.sleep(time_duration)

def game_over():
    print("Fin del juego")
    time.sleep(time_duration_fin)

def historia1():
    print("Érase una vez un ingeniero llamado Ramero")
    time.sleep(time_duration)
    print("Su más grande sueño era el de conseguir alguna hazaña histórica a lo largo de su vida")
    time.sleep(time_duration)
    print("<<¿Alguien me podría ayudar para pasar a la historia?>> - Pensaba Ramero en su casa")
    time.sleep(time_duration)
    print("De repente, un sonido deja impresionado al ingeniero. Cuando se gira, puede ver a una pequeña brujita")
    time.sleep(time_duration)
    print("<<Soy la bruja Alva, y te propongo un juego>> - Le dice ella, habiendo escuchado la plegaria de Ramero")
    time.sleep(time_duration)
    print("La brujita le propone jugar a un juego de trivia, en el que dependiendo de sus aciertos algo bueno o malo le ocurrirá")
    time.sleep(time_duration)
    print("Ramero, lleno de confianza, decide aceptar la propuesta de Alva")

def historia2_mal():
    print("Al improviso, la pequeña bruja desaparece, y nada parece cambiar en la vida de Ramero")
    time.sleep(time_duration)
    print("De repente, un día empieza a escuchar un gran ruido desde fuera de su casa")
    time.sleep(time_duration)
    print("Cuando mira hacia arriba, ya es demasiado tarde")
    time.sleep(time_duration)
    print("Una de las naves del millonario Ilon Máskaras colisiona con su casa por un fallo de diseño")
    time.sleep(time_duration)
    print("Finalmente, Ramero no consiguió pasar a la historia por lo que le habría gustado")

def historia2_bien():
    print("Al improviso, la pequeña bruja desaparece, y nada parece cambiar en la vida de Ramero")
    time.sleep(time_duration)
    print("De repente, un día el teléfono del ingeniero empieza a sonar escándalosamente")
    time.sleep(time_duration)
    print("Cuando lo coge, resulta ser una llamada del multimillonario Ilon Máskaras")
    time.sleep(time_duration)
    print("Este le propone una colaboración para crear una de sus naves espaciales")
    time.sleep(time_duration)
    print("Gracias al talento del ingeniero, consigue ser el primer humano en pisar Marte tras dos meses")
    time.sleep(time_duration)

def historia3_1_():
    print("Sonero es un joven estudiante del instituto Montaña Amarilla")
    time.sleep(time_duration)
    print("<<Ojalá poder sacar 10 en todo sin tener que estudiar>> - Pensaba el pobre joven")
    time.sleep(time_duration)
    print("De repente, un sonido alerta a Sonero. Cuando se gira, tiene detrás a la pequeña brujita.")
    time.sleep(time_duration)
    print("Le propone participar en un juego de trivia para garantizarle unos buenos resultados escolares.")
    time.sleep(time_duration)
    print("Confiado con sus grandes conocimientos, Sonero accede al plan de Alva.")
    time.sleep(time_duration)

def historia3_2_():
    print("Tonaro es un anciano muy intelectual, quien ha llevado toda su vida viviendo al límite.")
    time.sleep(time_duration)
    print("<<Ojalá poder volver a ser joven y vivir aventuras de nuevo?>> - Pensaba el viejo")
    time.sleep(time_duration)
    print("De repente, un sonido alerta a Tonaro. Cuando se gira, la pequeña bruja Alva está detrás suyo..")
    time.sleep(time_duration)
    print("Le propone participar en un juego de trivia para devolverle a sus tiempos de oro..")
    time.sleep(time_duration)
    print("Confiado con sus gran experiencia, Tonaro accede a jugar.")
    time.sleep(time_duration)

def historia3_1_fb():
    print("Al finalizar, la brujita desaparece y nada parece cambiar en la vida de Sonero.")
    time.sleep(time_duration)
    print("De repente, un día de clases, un profesor le llama para ir al aula del director.")
    time.sleep(time_duration)
    print("Este le dice que su nivel intelectual es tan alto que directamente le dan el título.")
    time.sleep(time_duration)
    print("De esta forma, Sonero consigue terminar su etapa de estudios y no hacer nada por el resto de su vida.")
    time.sleep(time_duration)

def historia3_1_fm():
    print("Al finalizar, la brujita desaparece y nada parece cambiar en la vida de Sonero.")
    time.sleep(time_duration)
    print("De repente, un día de clases, un profesor le llama para ir al aula del director.")
    time.sleep(time_duration)
    print("Este le dice que su nivel intelectual es tan decadente que no puede seguir estudiando en su centro.")
    time.sleep(time_duration)
    print("Esto hace que Sonero no pueda hacer nada fructífero por el resto de su vida.")
    time.sleep(time_duration)

def historia3_2_fb():
    print("Al finalizar, la brujita desaparece y nada parece cambiar en la vida de Tonaro.")
    time.sleep(time_duration)
    print("De repente, un día, al despertar, nota como sus articulaciones vuelven a responderle.")
    time.sleep(time_duration)
    print("Cuando se mira en el espejo, puede ver que vuelve a poseer un cuerpo joven y fructuoso.")
    time.sleep(time_duration)
    print("De esta forma, Tonaro puede volver a hacer sus bizarras aventuras que hacía de joven")
    time.sleep(time_duration)

def historia3_2_fm():
    print("Al finalizar, la brujita desaparece y nada parece cambiar en la vida de Tonaro.")
    time.sleep(time_duration)
    print("De repente, un día el viejo nota que sus movimientos son todavía más lentos que antes.")
    time.sleep(time_duration)
    print("Cuando se mira en el espejo, puede ver que su cuerpo ha envejecido muchísimo en esa noche.")
    time.sleep(time_duration)
    print("De esta forma, Tonaro no puede ni plantearse volver a su activa vida, viviendo en una tortura")
    time.sleep(time_duration)

pantalla_titulo()
historia1()

#Aquí se encuentran la lista de preguntas
print(lista_colores)
respuesta_pregunta1 = str(input("¿De qué color es la letra G del logotipo de Google?: "))
if respuesta_pregunta1 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a+1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (color_azul))
    b = b + 1
    print(siguiente_preg)

print(lista_logotipos)
respuesta_juego2 = str(input("¿Cuál de estos logotipos es de color naranja?: "))
if respuesta_juego2 == ("3"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    time.sleep(time_duration)
    print(respuesta_inc)
    print("La respuesta correcta es " + (logo_xiaomi))
    b = b + 1
    print(siguiente_preg)

print(lista_estrellas)
respuesta_juego3 = str(input("¿Cuantas estrellas hay en el Sistema Solar?: "))
if respuesta_juego3 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (estrellas_una))
    b = b + 1
    print(siguiente_preg)

print(lista_pena)
respuesta_juego4 = str(input("¿Cuál de estas se encuentra en Estepona?: "))
if respuesta_juego4 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (pena_blanca))
    b = b + 1
    print(siguiente_preg)

print(lista_marcas_coche)
respuesta_juego5 = str(input("¿De qué marca es el coche de Takumi Fujiwara en la serie Initial D?: "))
if respuesta_juego5 == ("4"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (marca_toyota))
    b = b + 1
    print(siguiente_preg)

print(lista_traccion)
respuesta_juego6 = str(input("¿Qué significa FF en un automóvil?: "))
if respuesta_juego6 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " +(traccion_delantera))
    b = b + 1
    print(siguiente_preg)


print(lista_nombres_reality)
respuesta_juego7 = str(input("¿Cuál de estos personajes de Total Drama solía llevar una camiseta amarilla?: "))
if respuesta_juego7 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (nombre_reality_trent))
    b = b + 1
    print(siguiente_preg)

print(lista_youtube)
respuesta_juego8 = str(input("¿Cuál de estos creadores de contenido es el creador original de Majotori?: "))
if respuesta_juego8 == ("3"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (youtuber_alvamajo))
    b = b + 1
    print(siguiente_preg)

print(lista_cantantes_franceses)
respuesta_juego9 = str(input("¿Cuál de estos cantantes o productores musicales no es francés?: "))
if respuesta_juego9 == ("3"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (cantante_stromae))
    b = b + 1
    print(siguiente_preg)

print(lista_capitales)
respuesta_juego10 = str(input("¿Cuál es la capital de Hungría?: "))
if respuesta_juego10 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (ciudad_budapest))
    b = b+1
    print(siguiente_preg)

ver_puntuacion()
esperando_resultado()

#Este es el proceso que hace que salga el final bueno o el malo. Las respuestas, en realidad, no influyen
if a >= b:
    historia2_bien()
else:
    historia2_mal()

#Aquí se da la segunda selección de historias
print("¿Con cuál de los siguientes personajes quieres seguir?")
time.sleep(time_duration_menu)
print("1. Sonero")
time.sleep(time_duration_menu)
print("2. Tonaro")
time.sleep(time_duration_menu)
seleccion1 = str(input("Selecciona: "))
if seleccion1 == ("1"):
    print("Has seleccionado: Sonero")
    time.sleep(time_duration)
    historia3_1_()
elif seleccion1 == ("2"):
    print("Has seleccionado: Tonaro")
    time.sleep(time_duration)
    historia3_2_()
else:
    print("No se ha entendido tu respuesta..")
    game_over()


#Aquí empieza la segunda tanda de preguntas
print(lista_pk)
respuesta_juego11 = str(input("¿Cuál de estos pokémons es de tipo agua?: "))
if respuesta_juego11 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (pk_vaporeon))
    b = b + 1
    print(siguiente_preg)

print(lista_cic)
respuesta_juego12 = str(input("¿Cuál de estos ciclistas ha ganado las tres grandes vueltas?: "))
if respuesta_juego12 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (cic_nibali))
    b = b + 1

print(lista_len)
respuesta_juego13 = str(input("¿Cuál es el lenguaje empleado para crear este juego?: "))
if respuesta_juego13 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (len_python))
    b = b + 1

print(lista_mc)
respuesta_juego14 = str(input("¿Cuál de estos raperos es el autor de Lose Yourself?: "))
if respuesta_juego14 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (mc_eminem))
    b = b + 1

print(lista_ano)
respuesta_juego15 = str(input("¿En qué año se dio la revolución francesa?: "))
if respuesta_juego15 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (ano_1789))
    b = b + 1

print(lista_namae)
respuesta_juego16 = str(input("¿Cómo se apellida el protagonista de la serie Metástasis?: "))
if respuesta_juego16 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (namae_blanco))
    b = b + 1

print(lista_pil)
respuesta_juego17 = str(input("¿Qué piloto español tiene el récord en el circuito de Bahrain?: "))
if respuesta_juego17 == ("2"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (pil_delarosa))
    b = b + 1

ver_puntuacion()
esperando_resultado()

if seleccion1 == ("1"):
    if a >= b:
        historia3_1_fb()
    else:
        historia3_1_fm()
else:
    if a >= b:
        historia3_2_fb()
    else:
        historia3_2_fm()
