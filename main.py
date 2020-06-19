import pygame
from obj import *
import random

#Pygame iniciando
pygame.init()

largura = 1024
altura = 768
speed_enemy = random.randint(15, 21)

# screen
screen = Display(lar=largura, alt=altura, text='Teste seus Reflexos 2', local_image='sprites/bg.png')
tela = screen.windows

#enemy1
enemy1 = Element(l_x=0, a_y=altura//2, speed=speed_enemy, local_image='sprites/inimigo.png')

#enemy2
enemy2 = Element(l_x=largura - 37, a_y=altura // 2, speed=speed_enemy, local_image='sprites/inimigo.png')

#enemy3
enemy3 = Element(l_x=largura // 2 + 37, a_y=0, speed=speed_enemy, local_image='sprites/inimigo.png')

#enemy4
enemy4 = Element(l_x=largura // 2 + 37, a_y=altura - 40, speed=speed_enemy, local_image='sprites/inimigo.png')

#player
player = Element(l_x=largura /2 -25, a_y=altura / 2, speed=35, local_image='sprites/player.png', hp=200)

#posições iniciais
pos_ini_x = largura / 2 - 25
pos_ini_y = altura / 2

#funções
#desenha na tela
def draw():

    pygame.font.init()
    font_default = pygame.font.get_default_font()
    font_size = pygame.font.SysFont(font_default, 50, 0, 0)
    hp_txt = 'HP: {}'.format(player.hp)
    hp_render = font_size.render(hp_txt, True, [66,201,32])

    tela.blit(screen.bg, (0,0))
    tela.blit(hp_render, (425, 0))
    tela.blit(enemy1.sprite.image, enemy1.sprite.rect)
    tela.blit(enemy2.sprite.image, enemy2.sprite.rect)
    tela.blit(enemy3.sprite.image, enemy3.sprite.rect)
    tela.blit(enemy4.sprite.image, enemy4.sprite.rect)
    tela.blit(player.sprite.image, player.sprite.rect)

#velocidade
def moviment():

    #movimento enemy1
    enemy1.sprite.rect[0] += enemy1.sprite.speed
    enemy1.sprite.rect[1] += enemy1.speed_y
    #movimento enemy2
    enemy2.sprite.rect[0] -= enemy2.sprite.speed
    enemy2.sprite.rect[1] -= enemy2.speed_y
    #movimento enemy3
    enemy3.sprite.rect[0] -= enemy3.sprite.speed
    enemy3.sprite.rect[1] -= enemy3.speed_y
    #movimento enemy4
    enemy4.sprite.rect[0] += enemy4.sprite.speed
    enemy4.sprite.rect[1] += enemy4.speed_y


    # definindo o limite da tela (eixo X) : Enemy 1
    if enemy1.sprite.rect[0] > largura - 37 or enemy1.sprite.rect[0] < 0:
        enemy1.sprite.speed *= -1

    # definindo o limite da tela (eixo Y) : Enemy 1
    if enemy1.sprite.rect[1] > altura - 38 or enemy1.sprite.rect[1] < 0:
        enemy1.speed_y *= -1

    # definindo o limite da tela (eixo X) : Enemy 2
    if enemy2.sprite.rect[0] > largura - 37 or enemy2.sprite.rect[0] < 0:
        enemy2.sprite.speed *= -1

    # definindo o limite da tela (eixo Y) : Enemy 2
    if enemy2.sprite.rect[1] > altura - 38 or enemy2.sprite.rect[1] < 0:
        enemy2.speed_y *= -1

    # definindo o limite da tela (eixo X) : Enemy 3
    if enemy3.sprite.rect[0] > largura - 37 or enemy3.sprite.rect[0] < 0:
        enemy3.sprite.speed *= -1

    # definindo o limite da tela (eixo Y) : Enemy 3
    if enemy3.sprite.rect[1] > altura - 38 or enemy3.sprite.rect[1] < 0:
        enemy3.speed_y *= -1

    # definindo o limite da tela (eixo X) : Enemy 4
    if enemy4.sprite.rect[0] > largura - 37 or enemy4.sprite.rect[0] < 0:
        enemy4.sprite.speed *= -1

    # definindo o limite da tela (eixo Y) : Enemy 4
    if enemy4.sprite.rect[1] > altura - 38 or enemy4.sprite.rect[1] < 0:
        enemy4.speed_y *= -1

#cosisões
def colision():

    colision_enemy1 = pygame.sprite.spritecollide(player.sprite, enemy1.group, False)
    colision_enemy2 = pygame.sprite.spritecollide(player.sprite, enemy2.group, False)
    colision_enemy3 = pygame.sprite.spritecollide(player.sprite, enemy3.group, False)
    colision_enemy4 = pygame.sprite.spritecollide(player.sprite, enemy4.group, False)

    colision_enemys1e2 = pygame.sprite.spritecollide(enemy1.sprite, enemy2.group, False)
    colision_enemys1e3 = pygame.sprite.spritecollide(enemy1.sprite, enemy3.group, False)
    colision_enemys1e4 = pygame.sprite.spritecollide(enemy1.sprite, enemy4.group, False)
    colision_enemys2e3 = pygame.sprite.spritecollide(enemy2.sprite, enemy3.group, False)
    colision_enemys2e4 = pygame.sprite.spritecollide(enemy2.sprite, enemy4.group, False)
    colision_enemys3e4 = pygame.sprite.spritecollide(enemy3.sprite, enemy4.group, False)

    if colision_enemy1:
        player.hp -= 10
        enemy1.sprite.speed *= -1
        enemy1.speed_y  *= -1

    if colision_enemy2:
        player.hp -= 10
        enemy2.sprite.speed *= -1
        enemy2.speed_y *= -1

    if colision_enemy3:
        player.hp -= 10
        enemy3.sprite.speed *= -1
        enemy3.speed_y

    if colision_enemy4:
        player.hp -= 10
        enemy4.sprite.speed *= -1
        enemy4.speed_y

    if colision_enemys1e2:
        enemy1.sprite.speed *= -1
        enemy1.speed_y *= -1
        enemy2.sprite.speed *= -1
        enemy2.speed_y

    if colision_enemys1e3:
        enemy1.sprite.speed *= -1
        enemy1.speed_y *= -1
        enemy3.sprite.speed *= -1
        enemy3.speed_y *= -1

    if colision_enemys1e4:
        enemy1.sprite.speed *= -1
        enemy1.speed_y *= -1
        enemy2.sprite.speed *= -1
        enemy2.speed_y *= -1

    if colision_enemys2e4:
        enemy2.sprite.speed *= -1
        enemy2.speed_y *= -1
        enemy4.sprite.speed *= -1
        enemy4.speed_y *= -1

    if colision_enemys3e4:
        enemy3.sprite.speed *= -1
        enemy3.speed_y *= -1
        enemy4.sprite.speed *= -1
        enemy4.speed_y *= -1

fps = pygame.time.Clock()
loop = True
while loop:

    fps.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:

            #controles: esquerda e direita
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.sprite.rect[0] -= player.sprite.speed
                if player.sprite.rect[0] <= largura * 0.25:
                    player.sprite.rect[0] = pos_ini_x

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.sprite.rect[0] += player.sprite.speed
                if player.sprite.rect[0] > largura * 0.75:
                    player.sprite.rect[0] = pos_ini_x

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.sprite.rect[1] -= player.sprite.speed
                if player.sprite.rect[1] < altura * 0.25:
                    player.sprite.rect[1] = pos_ini_y

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.sprite.rect[1] += player.sprite.speed
                if player.sprite.rect[1] > altura * 0.75:
                    player.sprite.rect[1] = pos_ini_y

    if player.hp <= 0:
        loop = False

    draw()
    moviment()
    colision()
    pygame.display.update()
