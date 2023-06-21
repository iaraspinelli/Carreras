import pygame
from constantes import *
from conexion_bd import mostrar_puntaje
from fondos import *
from botones import Botones
from jugar_juego import jugar_juego

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Carreras")

#---Inicio JUGAR = 0
fondo_inicio = FondosEstaticos("ejercicios.py/pygame/JUGAR0/fondo_inicio.jpg", ANCHO_VENTANA, ALTO_VENTANA)
boton_jugar = Botones("ejercicios.py/pygame/JUGAR0/jugar.png", ANCHO_BOTONES, ALTO_BOTONES, POS_LEFT_BOTONES, POS_TOP_BOTON_JUGAR)
boton_ranking = Botones("ejercicios.py/pygame/JUGAR0/ranking.png", ANCHO_BOTONES, ALTO_BOTONES, POS_LEFT_BOTONES, POS_TOP_BOTON_RANKING)

#---Ranking JUGAR = 2
fondo_ranking = FondosEstaticos("ejercicios.py/pygame/JUGAR2/fondo_ranking.jpg", ANCHO_VENTANA, ALTO_VENTANA)
boton_volver = Botones("ejercicios.py/pygame/JUGAR2/volver.png", 50, 50, 20,20)
font_ranking = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE)

#---Usuario JUGAR = 1
fondo_usuario = FondosEstaticos("ejercicios.py/pygame/JUGAR1/fondo_usuario.jpg", ANCHO_VENTANA, ALTO_VENTANA)
font_usuario = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE)
nombre_usuario = ""
nombre_usuario_rect = pygame.Rect(220, 10, 150, 30)


juego_corriendo = True
while juego_corriendo:

    lista_eventos = pygame.event.get()

    if JUGAR == 0:
        fondo_inicio.dibujar(pantalla)
        boton_jugar.dibujar(pantalla)
        boton_ranking.dibujar(pantalla)
        pygame.display.flip()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if (lista_click[0] > boton_jugar.rect.left and lista_click[0] < boton_jugar.rect.right):
                    if (lista_click[1] > boton_jugar.rect.top and lista_click[1] < boton_jugar.rect.bottom):
                        JUGAR= 1

                if (lista_click[0] > boton_ranking.rect.left and lista_click[0] < boton_ranking.rect.right):
                    if (lista_click[1] > boton_ranking.rect.top and lista_click[1] < boton_ranking.rect.bottom):
                        JUGAR= 2


    elif JUGAR == 2:
        ranking = mostrar_puntaje()
        fondo_ranking.dibujar(pantalla)
        boton_volver.dibujar(pantalla)
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if (lista_click[0] > boton_volver.rect.left and lista_click[0] < boton_volver.rect.right):
                    if (lista_click[1] > boton_volver.rect.top and lista_click[1] < boton_volver.rect.bottom):
                        JUGAR= 0

        titulo_nombre = font_ranking.render("NOMBRE", True, WHITE)
        titulo_score = font_ranking.render("SCORE", True, WHITE)
        pantalla.blit(titulo_nombre,(LEFT_RANKING, TOP_RANKING-50))
        pantalla.blit(titulo_score,(LEFT_RANKING*2.2, TOP_RANKING-50))

        for i in range(len(ranking)):
            nombre = str(ranking[i]['nombre'])
            texto_nombre = font_ranking.render(nombre, True, WHITE)
            pantalla.blit(texto_nombre,(LEFT_RANKING, TOP_RANKING+(i*25)))

            texto_tiempo = font_ranking.render(str(ranking[i]["score"]), True, WHITE)
            pantalla.blit(texto_tiempo,(LEFT_RANKING*2.3, TOP_RANKING+(i*25)))


    elif JUGAR == 1:
        fondo_usuario.dibujar(pantalla)
        nombre = font_usuario.render("Nombre player:", True, WHITE)
        nombre_usuario_surface = font_usuario.render(nombre_usuario, True, WHITE)
        pygame.draw.rect(pantalla, BLACK, nombre_usuario_rect, -1)
        pantalla.blit(nombre, (20, 20))
        pantalla.blit(nombre_usuario_surface,(nombre_usuario_rect.x+5, nombre_usuario_rect.y+10))

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    JUGAR = jugar_juego(pantalla, nombre_usuario)
                    if JUGAR == 2:
                        break
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[0:-1]
                else:
                    nombre_usuario += evento.unicode


    pygame.display.flip()

pygame.quit()