'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.jorge import Player

from elements.bug import Enemy


def StartScene():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    ''' Creamos y editamos la ventana de pygame (escena) '''
    ''' 1.-definir el tamaño de la ventana'''
    SCREEN_WIDTH = 1000  # revisar ancho de la imagen de fondo
    SCREEN_HEIGHT = 700  # revisar alto de la imagen de fondo

    ''' 2.- crear el objeto pantalla'''
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("./assets/pixelBackground.jpg").convert()
    ''' Preparamos el gameloop '''
    ''' 1.- creamos el reloj del juego'''

    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    ''' hora de hacer el gameloop '''
    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == QUIT:
                running = False
        
        screen.blit(background_image, (0, 0))
        #dibujamos todos los sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        #obtenemos todas las teclas presionadas actualmente
        pressed_keys = pygame.key.get_pressed()
        
        # actualizamos el sprite del jugador basado en las teclas presionadas
        player.update(pressed_keys)

        #actualizamos los enemigos
        enemies.update()

        #vemos si algun enemigo a chocado con el jugador
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
        
        pygame.display.flip()
        clock.tick(40)
    