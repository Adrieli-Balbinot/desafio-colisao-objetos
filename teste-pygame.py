import pygame
import sys
import random

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

PRETO = (0,0,0)
BRANCO = (255,255,255)

fonte = pygame.font.SysFont(None,50)

nome = "Adrieli"
sobrenome = "Balbinot"

texto1 = fonte.render(nome,True,BRANCO)
rect1 = texto1.get_rect(center=(200,300))

texto2 = fonte.render(sobrenome,True,BRANCO)
rect2 = texto2.get_rect(center=(600,300))

clock = pygame.time.Clock()


def gerar_cor():
    return (
        random.randint(1,255),
        random.randint(1,255),
        random.randint(1,255)
    )


def gerar_velocidade():
    vx = random.choice([-1,1])
    vy = random.choice([-1,1])
    return vx,vy


vel_x1,vel_y1 = gerar_velocidade()
vel_x2,vel_y2 = gerar_velocidade()


rodando=True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando=False


    tela.fill(PRETO)


    rect1.x += vel_x1
    rect1.y += vel_y1

    rect2.x += vel_x2
    rect2.y += vel_y2

    # Parede Adrieli

    if rect1.right >= largura:
        rect1.right = largura
        vel_x1 = -abs(vel_x1)

    if rect1.left <= 0:
        rect1.left = 0
        vel_x1 = abs(vel_x1)

    if rect1.bottom >= altura:
        rect1.bottom = altura
        vel_y1 = -abs(vel_y1)

    if rect1.top <= 0:
        rect1.top = 0
        vel_y1 = abs(vel_y1)



    # Parede Balbinot

    if rect2.right >= largura:
        rect2.right = largura
        vel_x2 = -abs(vel_x2)

    if rect2.left <= 0:
        rect2.left = 0
        vel_x2 = abs(vel_x2)

    if rect2.bottom >= altura:
        rect2.bottom = altura
        vel_y2 = -abs(vel_y2)

    if rect2.top <= 0:
        rect2.top = 0
        vel_y2 = abs(vel_y2)


    # Colisão entre eles
    if rect1.colliderect(rect2):

        vel_x1,vel_y1 = gerar_velocidade()
        vel_x2,vel_y2 = gerar_velocidade()

        texto1 = fonte.render(nome,True,gerar_cor())
        texto2 = fonte.render(sobrenome,True,gerar_cor())

        # Afasta um pouco os objetos
        rect1.x += vel_x1 * 10
        rect1.y += vel_y1 * 10

        rect2.x += vel_x2 * 10
        rect2.y += vel_y2 * 10

    tela.blit(texto1,rect1)
    tela.blit(texto2,rect2)


    clock.tick(500)

    pygame.display.flip()


pygame.quit()
sys.exit()