import pygame
import random

class AutoPlayer:

    def __init__ (self, imagen) -> None:
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (70, 50))
        self.rect = self.imagen.get_rect()
        self.rect.x = 200
        self.rect.y = 190
        self.vidas = 5
        self.movimiento = 70
        self.sonido = pygame.mixer.Sound("ejercicios.py/pygame/JUGANDO/motor_auto.mp3")


    def actualizar(self, direccion):
        if direccion == "arriba":
            self.rect.y -= self.movimiento
            if self.rect.y < 115:
                self.rect.y = 115
        if direccion == "abajo":
            self.rect.y += self.movimiento
            if self.rect.y > 330:
                self.rect.y = 330
        if self.rect.x < 200:
            self.rect.x = 200

    
    def colisionar_autos(self, lista_autos):
        sonido_choque = pygame.mixer.Sound("ejercicios.py/pygame/JUGANDO/choque.wav")
        for auto in lista_autos:
            if self.rect.colliderect(auto.rect) and self.vidas > 0:
                lista_autos.remove(auto)
                self.vidas = self.vidas - 1
                self.sonido.stop()
                sonido_choque.play()


    def colisionar_aceites(self, aceite, descontrolar, tiempo):
        sonido_patinar = pygame.mixer.Sound("ejercicios.py/pygame/JUGANDO/patinar.wav")
        if self.rect.colliderect(aceite.rect):
            descontrolar = tiempo
            if descontrolar > 0 and (tiempo -descontrolar < 1):
                self.rect.x += random.randint(-10, 10)
                self.rect.y += random.randint(-10, 10)
                self.sonido.stop()
                sonido_patinar.play()
            else:
                descontrolar = 0


    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

