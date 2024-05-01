import pygame
import random
"""
this is the 'optimized' version of my first program, honestly i have no idea how 
it was so optimized to begin with seing as i dint know the laungauge and i
smashed a pygame and a randomization tutioral together to make this.
"""
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("number genorator")

pygame.font.init()
Health_font = pygame.font.SysFont('comicsans', 40)
number_Font = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
DELAY = 900


def draw_window():
    draw_number()
    WIN.fill(WHITE)

def draw_number():
    randomlist = random.sample(range(1, 100), 10)
    draw_text = number_Font.render(str(randomlist), 1, BLACK)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(DELAY)

def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        draw_window()
        if pygame.event.get(pygame.QUIT):
            pygame.quit()


if __name__ == "__main__":
    main()