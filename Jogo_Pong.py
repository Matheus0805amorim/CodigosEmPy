#jogo do ping pong

========================================================================
                            DOCUMENTAÇÃO
                              JOGO PONG
========================================================================

1. Introdução:
   O jogo Pong é um clone simples do clássico jogo de arcade Pong. Neste
   jogo, dois jogadores controlam barras retangulares que se movem para 
   cima e para baixo, tentando rebater uma bola em direção ao adversário 
   para marcar pontos. O jogo continua até que um jogador alcance uma 
   pontuação predefinida ou até que o jogador decida encerrar o jogo.

2. Funcionamento:
   O jogo Pong é implementado em Python usando a biblioteca Pygame. Abaixo
   estão os principais componentes e funcionalidades do jogo:

   - Configurações da janela: Define as dimensões da janela do jogo, a taxa
     de quadros por segundo (FPS) e as cores usadas no jogo.

   - Configurações das barras do jogador: Define as dimensões, velocidade e 
     posição inicial das barras do jogador.

   - Configurações da bola: Define as dimensões, velocidade e posição inicial
     da bola.

   - Função reset_ball(): Retorna a posição inicial da bola quando é necessário
     reiniciar o jogo.

   - Função main(): A função principal do jogo. Aqui, o jogo é inicializado e
     o loop principal do jogo é executado. Ele trata eventos, atualiza a posição
     dos objetos do jogo, detecta colisões e desenha os objetos na tela.

   - Movimentação do jogador: O jogador 1 pode mover sua barra para cima com a
     tecla "W" e para baixo com a tecla "S".

   - Movimentação da bola: A bola se move continuamente pela tela. Quando colide
     com as paredes ou barras, sua direção é invertida.

   - Colisões: O jogo verifica constantemente se a bola colide com as barras dos
     jogadores ou com as paredes. Se a bola atingir a barra do jogador, sua direção
     horizontal é invertida.

   - Desenho na tela: Os objetos do jogo (barras dos jogadores e bola) são desenhados
     na tela a cada quadro.

   - Encerramento do jogo: O jogo continua em um loop até que o jogador decida fechar
     a janela do jogo.

3. Execução:
   Para executar o jogo, basta executar o script Python. Uma janela será aberta 
   exibindo o jogo. Os jogadores podem controlar suas barras usando as teclas 
   especificadas no código. O jogo continuará até que o jogador decida fechar a 
   janela do jogo.

4. Conclusão:
   Este é um exemplo básico de um jogo Pong implementado em Python usando a biblioteca
   Pygame. Ele demonstra conceitos fundamentais de desenvolvimento de jogos, como
   movimentação de objetos, detecção de colisões e manipulação de eventos.

   O código pode ser estendido e modificado para adicionar mais funcionalidades, como
   efeitos sonoros, pontuação, níveis de dificuldade, entre outros.




import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela do jogo
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da barra do jogador
PLAYER_WIDTH, PLAYER_HEIGHT = 15, 100
PLAYER_SPEED = 5

# Configurações da bola
BALL_WIDTH, BALL_HEIGHT = 15, 15
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Criação da janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Função para reiniciar a posição da bola
def reset_ball():
    return WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2

# Função principal do jogo
def main():
    # Posição inicial do jogador e da bola
    player1_y = HEIGHT // 2 - PLAYER_HEIGHT // 2
    player2_y = HEIGHT // 2 - PLAYER_HEIGHT // 2
    ball_x, ball_y = reset_ball()
    ball_dx = BALL_SPEED_X * random.choice((1, -1))
    ball_dy = BALL_SPEED_Y * random.choice((1, -1))

    # Loop principal do jogo
    running = True
    while running:
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação do jogador 1 (esquerda)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= PLAYER_SPEED
        if keys[pygame.K_s] and player1_y < HEIGHT - PLAYER_HEIGHT:
            player1_y += PLAYER_SPEED

        # Movimentação do jogador 2 (direita)
        if ball_dx > 0:
            if player2_y + PLAYER_HEIGHT / 2 < ball_y + BALL_HEIGHT / 2:
                player2_y += PLAYER_SPEED
            elif player2_y + PLAYER_HEIGHT / 2 > ball_y + BALL_HEIGHT / 2:
                player2_y -= PLAYER_SPEED

        # Movimentação da bola
        ball_x += ball_dx
        ball_y += ball_dy

        # Verifica se a bola colide com a parede superior ou inferior
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_HEIGHT:
            ball_dy *= -1

        # Verifica colisão com jogador 1
        if ball_x <= PLAYER_WIDTH and player1_y < ball_y + BALL_HEIGHT < player1_y + PLAYER_HEIGHT:
            ball_dx *= -1

        # Verifica colisão com jogador 2
        if ball_x >= WIDTH - PLAYER_WIDTH - BALL_WIDTH and player2_y < ball_y + BALL_HEIGHT < player2_y + PLAYER_HEIGHT:
            ball_dx *= -1

        # Verifica se a bola passa pelos limites da tela
        if ball_x <= 0 or ball_x >= WIDTH - BALL_WIDTH:
            ball_x, ball_y = reset_ball()

        # Desenha os objetos na tela
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, player1_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        pygame.draw.rect(screen, WHITE, (WIDTH - PLAYER_WIDTH, player2_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT))
        pygame.display.flip()

        # Limita a taxa de quadros por segundo
        clock.tick(FPS)

    # Encerra o Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
A movimentação da barra do jogador 2 (direita) é controlada de forma autônoma, com base na posição da bola. 
A barra se move para cima se a bola estiver acima do centro da barra e se move para baixo se a bola estiver abaixo do centro da barra. Isso cria um adversário automatizado para o jogador.
