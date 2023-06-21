import pygame

class FondosEstaticos:
    def __init__(self, imagen, ancho, alto) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto)) 
        self.rect = self.imagen.get_rect()

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)


class Carretera:
    def __init__ (self, imagen, ancho, alto, y, velocidad) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.rect_continuacion_x = ancho
        self.velocidad = velocidad

    def actualizar(self,pantalla,ancho):
        pantalla.blit(self.imagen,self.rect)
        pantalla.blit(self.imagen,(self.rect_continuacion_x, self.rect.y))
        self.rect.x -= self.velocidad
        self.rect_continuacion_x -= self.velocidad
        if self.rect.right <= 0:
            self.rect.x = ancho
        if self.rect_continuacion_x <= -ancho:
            self.rect_continuacion_x = ancho

