import pygame

class Level:
    def __init__(self):

        #Obtenir la surface à afficher
        self.display_surface = pygame.display.get_surface()

        # Sprite initialisation (visible et obstacles)
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):
        #Update et dessiner le jeu
        pass
