import pygame
import random

def getSuperficies(path,filas,columnas):
    lista = []
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
            lista.append(superficie_fotograma)

    return lista


class AutosEnemigos:

    def __init__(self, lista_enemigos) -> None:
        self.lista_autos_enemigos = getSuperficies("ejercicios.py/pygame/JUGANDO/autos.png", 3, 1)
        self.auto_enemigo = random.choice(self.lista_autos_enemigos)
        self.auto_enemigo = pygame.transform.scale(self.auto_enemigo,(70,50))
        self.rect = self.auto_enemigo.get_rect()
        self.rect.x = 700
        self.rect.y = random.choice([120, 190, 260, 330])
        self.velocidad = 4
        self.lista_enemigos = lista_enemigos

    def actualizar(self, pantalla, velocidad):
        pantalla.blit(self.auto_enemigo, self.rect)
        self.rect.x -= velocidad
        if self.rect.right < 0:
            self.rect.x = 700
            self.rect.y = random.choice([120, 190, 260, 330])
            self.velocidad = 4


class Aceite:
    def __init__(self) -> None:
        self.aceite = pygame.image.load("ejercicios.py/pygame/JUGANDO/aceite.png")
        self.aceite = pygame.transform.scale(self.aceite,(30,30))
        self.rect = self.aceite.get_rect()
        self.rect.x = 730
        self.rect.y = random.choice([130, 200, 270, 340])

    def actualizar(self, pantalla):
        pantalla.blit(self.aceite, self.rect)
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.x = 730
            self.rect.y = random.choice([130, 200, 270, 340])


