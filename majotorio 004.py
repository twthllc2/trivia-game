#Majotori, juego de trivia en el que tus decisiones impactan en la vida de los personajes
import sys
import time
import random
time_duration = 3
time_duration_2 = 8
time_duration_menu = 0.3
time_duration_fin = 60

#Aquí se encuentran todas las opciones para las preguntas
color_verde = str("1. Verde")
color_azul = str("2. Azul")
color_amarillo = str("3. Amarillo")
color_marron = str("4. Marron")
enhorabuena = str("Enhorabuena, respuesta correcta")
siguiente_preg = str("Siguiente pregunta")
respuesta_inc = str("respuesta incorrecta")
lista_colores = [color_verde, color_azul, color_amarillo, color_marron]
logo_xiaomi = str("3. Xiaomi")
logo_samsung = str("2. Samsung")
logo_lg = str("1. LG")
logo_sony = str("4. Sony")
lista_logotipos = [logo_lg,logo_samsung,logo_xiaomi,logo_sony]
estrellas_248 = str("1. 248")
estrellas_una = str("2. Solamente hay una")
estrellas_demasiadas = str("3. Demasiadas para ser contadas")
estrellas_none = str("4. No hay")
lista_estrellas = [estrellas_248, estrellas_una, estrellas_demasiadas, estrellas_none]
pena_blanca = str("1. Peñas blancas")
pena_akina = str("2. Monte Akina")
pena_bermeja = str("3. Peña  bermeja")
pena_rosada = str("4. Peña rosada")
lista_pena = [pena_blanca, pena_akina, pena_bermeja, pena_rosada]
marca_toyota = str("4. Toyota")
marca_bmw = str("2. BMW")
marca_hyundai = str("3. Hyundai")
marca_pontiac = str("1. Pontiac")
lista_marcas_coche = [marca_pontiac, marca_bmw, marca_hyundai, marca_toyota]
traccion_delantera = ("1. Motor delante, tracción delante")
traccion_todoterreno = ("2. Todoterreno")
traccion_descapotable = ("3. Descapotable")
traccion_nada = ("4. No tiene significado")
lista_traccion = [traccion_delantera, traccion_todoterreno, traccion_descapotable, traccion_nada]
nombre_reality_trent = str("1. Trent")
nombre_reality_gwen = str("2. Gwen")
nombre_reality_owen = str("3. Owen")
nombre_reality_scott = str("4. Scott")
lista_nombres_reality = [nombre_reality_trent, nombre_reality_gwen, nombre_reality_owen, nombre_reality_scott]
youtuber_alvamajo = str("3. Alva Majo")
youtuber_guinxu = str("2. Guinxu")
youtuber_rubius = str("1. El Rubius")
youtuber_ibai = str("4. Ibai")
lista_youtube = [youtuber_rubius, youtuber_guinxu, youtuber_alvamajo, youtuber_ibai]
cantante_daftpunk = str("1. Daft Punk")
cantante_davidguetta = str("2. David Guetta")
cantante_stromae = str("3. Stromae")
cantante_edithpiaf = str("4. Edith Piaf")
lista_cantantes_franceses = [cantante_daftpunk, cantante_davidguetta, cantante_stromae, cantante_edithpiaf]
ciudad_madrid = str("1. Madrid")
ciudad_budapest = str("2. Budapest")
ciudad_roma = str("3. Roma")
ciudad_algeciras = str("4. Algeciras")
lista_capitales = [ciudad_madrid, ciudad_budapest, ciudad_roma, ciudad_algeciras]
pk_vaporeon = str("1. Vaporeon")
pk_littleo = str("2. Littleo")
pk_xerneas = str("3. Xerneas")
pk_voltorb = str("4. Voltorb")
lista_pk = [pk_vaporeon, pk_littleo, pk_xerneas, pk_voltorb]
cic_quintana = str("1. Quintana")
cic_nibali = str("2. Nibali")
cic_bardet = str("3. Bardet")
cic_pinot = str("4. Pinot")
lista_cic = [cic_quintana, cic_nibali, cic_bardet, cic_pinot]
len_python = str("1. Python")
len_c = str("2. C++")
len_java = str("3. Java")
len_no = str("4. En nada")
lista_len = [len_python, len_c, len_java, len_no]
mc_pitbull = str("1. Pitbull")
mc_eminem = str("2. Eminem")
mc_kevinho = str("3. Mc Kevinho")
mc_thegame = str("4. The Game")
lista_mc = [mc_pitbull, mc_eminem, mc_kevinho, mc_thegame]
ano_1789 = str("1. 1789")
ano_1192 = str("2. 1192")
ano_1482 = str("3. 1482")
ano_20 = str("4. 20")
lista_ano = [ano_1789, ano_1192, ano_1482, ano_20]
namae_white = str("1. White")
namae_blanco = str("2. Blanco")
namae_cesar = str("3. Cesar")
namae_black = str("4. Black")
lista_namae = [namae_white, namae_blanco, namae_cesar, namae_black]
pil_alonso = str("1. Alonso")
pil_delarosa = str("2. De La Rosa")
pil_rodriguez = str("3. Rodríguez")
pil_gene = str("4. Gené")
lista_pil = [pil_alonso, pil_delarosa, pil_rodriguez, pil_gene]
pol_rubalcaba = str("1. Rubalcaba")
pol_rajoy = str("3. Rajoy")
pol_iglesias = str("2. Iglesias")
pol_rivera = str("4. Rivera")
lista_pol = [pol_rubalcaba, pol_iglesias, pol_rajoy, pol_rivera]
frase_nollegaaviejo = str("1. No llega a viejo")
frase_caminalento = str("2. Camina lento")
frase_lepillaelconejo = str("3. Le pilla el conejo")
frase_lequitanelpellejo = str("4. Le quitan el pellejo")
lista_frase = [frase_nollegaaviejo, frase_caminalento, frase_lepillaelconejo, frase_lequitanelpellejo]
prov_50 = str("3. 50")
prov_22 = str("1. 22")
prov_62 = str("2. 62")
prov_40 = str("4. 40")
lista_prov = [prov_22, prov_62, prov_50, prov_40]

#opciones de preguntas todavía no utilizadas.
marc_scottex = str("1. Scottex")
marc_hp = str("2. HP")
marc_lenovo = str("3. Lenovo")
marc_cabreiroa = str("4. Cabreiroá")
lista_marc = [marc_scottex, marc_hp, marc_lenovo, marc_cabreiroa]
pais_venezuela = str("1. Venezuela")
pais_colomia = str("2. Colombia")
pais_cuba = str("3. Cuba")
pais_ecuador = str("4. Ecuador")
lista_pais = [pais_venezuela, pais_colomia, pais_cuba, pais_ecuador]
jug_fabregas = str("1. Cesc Fábregas")
jug_torres = str("2. Fernando Alonso")
jug_xavi = str("3. Xavi")
jug_navas = str("4. Jesús Navas")
lista_jug = [jug_fabregas, jug_torres, jug_xavi, jug_navas]
strm_ibai = str("1. Ibai")
strm_djm = str("2. Dj Mariio")
strm_crist = str("3. Cristianghost")
strm_billy = str("4. Billy Cherokee")
lista_strm = [strm_ibai, strm_djm, strm_crist, strm_billy]
cars_mcqueen = ("1. Rayo McQueen")
cars_dondeldi = ("2. Mike Dondeldi")
cars_theking = ("3. El Rey")
cars_storm = ("4. Jackson Storm")
lista_cars = [cars_mcqueen, cars_dondeldi, cars_theking, cars_storm]

#En esta zona se experimenta para conseguir el sistema de aciertos
a = 0
b = 0
resp_cor = 0
resp_incor = 0
respuesta_correcta = a+1

def reset_ab():
    a = 0
    (a)
    b = 0
    (b)

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
    boton2 = str(input("M A J O T O R I O  v 0.0.3"))
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

def pantalla_creditos():
    print("Majotorio")
    time.sleep(time_duration)
    print("Desarrollado por Simone Moscato y Ayoub el Assri (creo que así se escribe)")
    time.sleep(time_duration)
    print("Inspirado en el videojuego Majotori de Alva Majo")
    time.sleep(time_duration)
    print("Creado con PyCharmsqebff")
    time.sleep(time_duration)

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
    time.sleep(time_duration)

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

def historia4_1():
    print("Matane es una joven delicada que lleva una vida retirada en el campo")
    time.sleep(time_duration)
    print("<<Ojalá poder tener una vida más normal>>, piensa ella.")
    time.sleep(time_duration)
    print("Instantáneamente, la brujita Alva aparece en frente de la chica.")
    time.sleep(time_duration)
    print("Viendo que no tiene nada que perder, acepta la propuesta de la bruja.")
    time.sleep(time_duration)

def historia4_1_fb():
    print("Cuando termina de responder, la brujita desaparece y nada parece cambiar en la vida de Makane.")
    time.sleep(time_duration)
    print("Sorprendentemente, un día un señor trajeado toca la puerta de la casa de la chica.")
    time.sleep(time_duration)
    print("Este insiste en llevarla a un instituto para poder cultirizar a la joven.")
    time.sleep(time_duration)
    print("De esta forma puede conseguir tener su tan anhelada vida como adolescente regular.")
    time.sleep(time_duration)

def historia4_1_fm():
    print("Cuando termina de responder, la brujita desaparece y nada parece cambiar en la vida de Makane.")
    time.sleep(time_duration)
    print("Sorprendentemente, un día un señor trajeado toca la puerta de la casa de la chica.")
    time.sleep(time_duration)
    print("Este insiste en llevarla a trabajar en un campo cercana para introducirla en el mundo laboral.")
    time.sleep(time_duration)
    print("De esta forma, la joven chica no consigue cumplir su sueño de vivir una adolescencia normal, viviendo toda su vida en el campo.")
    time.sleep(time_duration)

def historia4_2():
    print("Nekona es una joven niña amante de los animales, y especialmente, de los gatos.")
    time.sleep(time_duration)
    print("<<Ojalá mis padres me dejasen tener un gato en casa>>, piensa ella.")
    time.sleep(time_duration)
    print("Instantáneamente, la brujita Alva aparece en frente de la chica.")
    time.sleep(time_duration)
    print("Emocionada por poder tener un amigo peludo junto a ella, accede a participar en el juego de trivia.")
    time.sleep(time_duration)

def historia4_2_fb():
    print("Cuando termina de responder, la brujita desaparece y nada parece cambiar en la vida de Nekona.")
    time.sleep(time_duration)
    print("Un día, cuando abre la puerta de su casa, puede encontrarse una pequeña caja de cartón.")
    time.sleep(time_duration)
    print("Cuando la abre, un pequeño gato blanco y negro le saluda con un agudo maullido.")
    time.sleep(time_duration)
    print("La niña se queda totalmente enamorada del animal, convenciendo así a los padres a criar al gato.")
    time.sleep(time_duration)

def historia4_2_fm():
    print("Cuando termina de responder, la brujita desaparece y nada parece cambiar en la vida de Nekona.")
    time.sleep(time_duration)
    print("Un día, mientras se encuentra en su habitación, su padre entra tímidamente con un papel en la mano.")
    time.sleep(time_duration)
    print("En este se muestra cómo su hija ha desarrollado una fortísima alergia contra los gatos.")
    time.sleep(time_duration)
    print("Por culpa de su condición, Nekona nunca podrá disfrutar de una compañía gatuna en el resto de su vida.")
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

#Este es el proceso que hace que salga el final bueno o el malo. Ahora si que influyen el número de aciertos.
resultado_a = random.choice(range(a))
random_b = random.choice(range(b))

if resultado_a >= random_b:
    print("Habría ocurrido el final bueno")
else:
    print("Habría ocurrido el final malo")

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
a = 0
b = 0

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
    print(siguiente_preg)

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
    print(siguiente_preg)

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
    print(siguiente_preg)

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
    print(siguiente_preg)

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
    print(siguiente_preg)

print(lista_pil)
respuesta_juego17 = str(input("¿Qué piloto español de F1 tiene el récord de vuelta en el GP de Baréin?: "))
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
    print(siguiente_preg)

print(lista_pol)
respuesta_juego18 = str(input("¿Cuál de estos apellidos pertenece a un ex-presidente español?: "))
if respuesta_juego18 == ("3"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (pol_rajoy))
    b = b + 1
    print(siguiente_preg)

print(lista_frase)
respuesta_juego19 = str(input("¿Cómo acaba el dicho <Quién no sigue el consejo...>?: "))
if respuesta_juego19 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (frase_nollegaaviejo))
    b = b + 1
    print(siguiente_preg)

print(lista_prov)
respuesta_juego20 = str(input("¿Cuántas provincias tiene España?: "))
if respuesta_juego20 == ("3"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (prov_50))
    b = b + 1
    print(siguiente_preg)

ver_puntuacion()
esperando_resultado()

#Este es el proceso que hace que salga el final bueno o el malo. Las respuestas, en realidad, no influyen
resultado_d = random.choice(range(a))
resultado_c = random.choice(range(b))

if resultado_d >= resultado_c:
    print("Habría ocurrido el final bueno")
else:
    print("Habría ocurrido el final malo")

#Aquí se da la segunda selección de historias
print("¿Con cuál de los siguientes personajes quieres seguir?")
time.sleep(time_duration_menu)
print("1. Mokano")
time.sleep(time_duration_menu)
print("2. Nekona")
time.sleep(time_duration_menu)
seleccion2 = str(input("Selecciona: "))
if seleccion2 == ("1"):
    print("Has seleccionado: Sonero")
    time.sleep(time_duration)
    historia4_1()
elif seleccion1 == ("2"):
    print("Has seleccionado: Tonaro")
    time.sleep(time_duration)
    historia4_2()
else:
    print("No se ha entendido tu respuesta..")
    game_over()

#Aquí empieza la tercera tanda de preguntas
print(lista_marc)
respuesta_juego21 = str(input("¿Cuál de las siguientes marcas tiene un perro en su logotipo?: "))
if respuesta_juego21 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (marc_scottex))
    b = b + 1
    print(siguiente_preg)

print(lista_pais)
respuesta_juego22 = str(input("¿En cuál de estos países nació el rapero Pitbull?: "))
if respuesta_juego22 == ("3"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (pais_cuba))
    b = b + 1
    print(siguiente_preg)

print(lista_jug)
respuesta_juego23 = str(input("¿Quién dio la asistencia a Andrés Iniesta en la final del mundial en 2010?: "))
if respuesta_juego23 == ("1"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (jug_fabregas))
    b = b + 1
    print(siguiente_preg)

print(lista_cars)
respuesta_juego24 = str(input("¿Quién fue el principal antagonista en la película Cars 3?: "))
if respuesta_juego24 == ("4"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (cars_storm))
    b = b + 1
    print(siguiente_preg)

print(lista_strm)
respuesta_juego25 = str(input("¿Cuál de estos streamers es piloto de automovilismo?: "))
if respuesta_juego25 == ("4"):
    print(enhorabuena)
    time.sleep(time_duration)
    print(siguiente_preg)
    a = a + 1
else:
    print(respuesta_inc)
    time.sleep(time_duration)
    print("La respuesta correcta es " + (strm_billy))
    b = b + 1
    print(siguiente_preg)

if seleccion2 == ("1"):
    if a >= b:
        historia4_1_fb()
    else:
        historia4_1_fm()
else:
    if a >= b:
        historia4_2_fb()
    else:
        historia4_2_fm()


#Aquí empieza la segunda tanda de preguntas
a = 0
b = 0

pantalla_creditos()
game_over()