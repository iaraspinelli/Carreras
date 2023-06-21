import pygame
import sys #Modulo incorporado para acceder a funcionalidades del sistema operativo que interactua con Python
import random
from constantes import *
from conexion_bd import *
from fondos import Carretera
from jugador import AutoPlayer
from obstaculos import AutosEnemigos, Aceite


def jugar_juego(pantalla, nombre_usuario):

    reloj = pygame.time.Clock()
    TIEMPO = 0
    DESCONTROLAR = 0

    carretera = Carretera("ejercicios.py/pygame/JUGANDO/carretera.jpeg", ANCHO_VENTANA, ALTO_VENTANA, 0, 5)
    font_score_vidas = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE)

    auto_player = AutoPlayer("ejercicios.py/pygame/JUGANDO/auto_jugador.png")
    autos_enemigos = []
    aceite = Aceite()

    juego_corriendo = True
    while juego_corriendo:
        carretera.actualizar(pantalla, ANCHO_VENTANA)
        aceite.actualizar(pantalla)
        if(len(autos_enemigos) >= 0 and len(autos_enemigos) < 5):
            for i in range(5):
                auto_enemigo = AutosEnemigos(autos_enemigos) 
                auto_enemigo.rect.x = auto_enemigo.rect.x+(i*100)
                autos_enemigos.append(auto_enemigo)
        for auto_enemigo in autos_enemigos:
            auto_enemigo.actualizar(pantalla, auto_enemigo.velocidad)
        auto_player.dibujar(pantalla)
        auto_player.sonido.play()
        auto_player.colisionar_autos(autos_enemigos)
        auto_player.colisionar_aceites(aceite, DESCONTROLAR, TIEMPO)
        if auto_player.vidas < 1:
            crear_database()
            guardar_puntaje(nombre_usuario, score)
            JUGAR = game_over(pantalla)
            return JUGAR

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    auto_player.actualizar("arriba")
                if evento.key == pygame.K_DOWN:
                    auto_player.actualizar("abajo")

        milis = reloj.tick(60) / 1000
        TIEMPO += milis

        score = int(TIEMPO*40)
        titulo_score = font_score_vidas.render("SCORE:", True, WHITE)
        score_usuario = font_score_vidas.render(str(score), True, WHITE)
        titulo_vidas = font_score_vidas.render("VIDAS: ", True, WHITE)
        vidas_usuario = font_score_vidas.render(str(auto_player.vidas), True, WHITE)
        pantalla.blit(titulo_score,(30, 40))
        pantalla.blit(titulo_vidas,(30, 70))
        pantalla.blit(vidas_usuario, (200, 70))
        pantalla.blit(score_usuario, (200, 40))

        pygame.display.flip()



def game_over(pantalla):
    
    sonido_game_over = pygame.mixer.Sound("ejercicios.py/pygame/JUGANDO/game_over.wav")
    sonido_game_over.play()
    font_ranking = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE)
    font_game_over = pygame.font.SysFont(TIPO_FUENTE, TAMAÑO_FUENTE_GAME_OVER)
    
    juego_corriendo = True
    while juego_corriendo:

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                juego_corriendo = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_click = list(evento.pos)
                if (lista_click[0] > ver_ranking_rect.left and lista_click[0] < ver_ranking_rect.right):
                    if (lista_click[1] > ver_ranking_rect.top and lista_click[1] < ver_ranking_rect.bottom):
                        JUGAR = 2
                        return JUGAR

        pantalla.fill(BLACK)
        game_over = font_game_over.render("GAME OVER", True, WHITE)
        game_over_rect = pygame.Rect(POS_LEFT_GAME_OVER, POS_TOP_GAME_OVER, 600, 200)
        ver_ranking = font_ranking.render("VER RANKING", True, WHITE)
        ver_ranking_rect = pygame.Rect(POS_LEFT_BOTONES, POS_TOP_BOTON_RANKING, 200, 50)
        pantalla.blit(game_over, game_over_rect)
        pantalla.blit(ver_ranking,ver_ranking_rect)

        pygame.display.flip()