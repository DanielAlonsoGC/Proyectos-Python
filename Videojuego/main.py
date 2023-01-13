import pygame
import random
import math
""" Inicializando pygame """
pygame.init()
""" creando pantalla """
pantalla=pygame.display.set_mode((800,600))
""" Tituto e icono del juego """
pygame.display.set_caption("Matando ovnis")
icono =pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

""" Jugador """
img_jugador=pygame.image.load("nave.png")
jugador_x=368
jugador_y=500
jugador_x_cambio = 0
""" Rival"""
img_rival=[]
rival_x=[]
rival_y=[]
rival_x_cambio = []
rival_y_cambio =[]
cantidad_rivales = 8

for e in range(cantidad_rivales):
    img_rival.append(pygame.image.load("rival.png"))
    rival_x.append(random.randint(0,736))
    rival_y.append(random.randint(50,200))
    rival_x_cambio.append(0.5)
    rival_y_cambio.append(50)

""" "bala" """
img_bala=pygame.image.load("bala.png")
bala_x=0
bala_y=500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False
""" puntaje """
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y= 10

""" funcion mostrar puntaje"""
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto,(x,y))

""" funcion jugador """
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))
""" funcion enemigo """
def rival(x,y,n):
    pantalla.blit(img_rival[n],(x,y))

"""  funcion disparar bala"""
def disparar_bala(x,y):
    global bala_visible
    bala_visible=True
    pantalla.blit(img_bala,(x+16,y+10))
""" Cuando hay colision entre bala y rival """
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_1 - y_2,2))
    if distancia <27:
        return True
    else:
        return False


ejecucion=True
while ejecucion:
    """ color de pantalla """
    pantalla.blit(fondo,(0,0))
    """ Iterando evento """
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            ejecucion = False
        """ Evento cuando se presiona una tecla """
        if evento.type ==pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio= -0.8
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio= 0.8
            if evento.key ==pygame.K_SPACE:
                if not bala_visible:
                    bala_x=jugador_x
                    disparar_bala(jugador_x,bala_y)
              
        """ Evento cuando se realiza el soltado de flecha """
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio=0
    """ Modificar la ubicacion del jugador """
    jugador_x += jugador_x_cambio
    """ manteniendo los bordes del jugador"""
    if jugador_x<=0:
        jugador_x=0
    elif jugador_x>=736:
        jugador_x=736
    """ Modificar la ubicacion del rival """
    for e in range(cantidad_rivales):
        rival_x[e] += rival_x_cambio[e]
        """ Manteniendo los bordes rival """
        if rival_x[e]<=0:
            rival_x_cambio[e]=1
            rival_y[e] += rival_y_cambio[e]
        elif rival_x[e]>=736:
            rival_x_cambio[e]=-1
            rival_y[e] +=rival_y_cambio[e]
        """ colision """ 
        colision = hay_colision(rival_x[e],rival_y[e],bala_x,bala_y)
        if colision:
            bala_y=500
            bala_visible=False
            puntaje+=1
            rival_x[e]=random.randint(0,736)
            rival_y[e]=random.randint(50,200)
            """ Envio de parametros a Jugador """
        rival(rival_x[e],rival_y[e],e)
    """ Movimiento de bala """
    if bala_y<= -64:
        bala_y=500
        bala_visible=False
    if bala_visible==True:
        disparar_bala(jugador_x,bala_y)
        bala_y -= bala_y_cambio
    
    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x,texto_y)
    
    """ Envio de parametros a Jugador """
    jugador(jugador_x,jugador_y)

    """ actualizar """
    pygame.display.update()

