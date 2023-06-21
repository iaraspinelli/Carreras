import pygame

class Botones:

    def __init__(self, imagen, ancho, alto, x, y) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto)) 
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

