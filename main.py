import pygame
import math
from section import Section

WIDTH, HEIGHT  = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Inverse kinematics')

white = (255,255,255)
black = (0,0,0)

L = 5       #lenght of one section
N = 60      #number of sections


def get_angle(xa, ya, xb, yb):
    #function to find angle between two points
    if ya - yb < 0:
        phi = math.atan(-(xb - xa) / (yb - ya)) - math.pi / 2
    elif ya - yb > 0:
        phi = math.atan(-(xb - xa) / (yb - ya)) + math.pi / 2
    elif ya - yb == 0:
        phi = 0

    return phi

def draw_window():
    WIN.fill(black)

    for section in sections:
        pygame.draw.line(WIN, white, (section.xa, section.ya), (section.xb, section.yb), width=section.width)

    pygame.display.update()

#MAIN PYGAME RUN LOOP
def run():
    run = True

    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        #ITERATE FORWARD AND FIT THE END POS TO MOUSE POS
        for i, section in enumerate(sections):
            if i == 0:
                section.phi = get_angle(x, y, section.xa, section.ya)
                section.update()

                section.xa += (x - section.xb) * 0.002
                section.ya += (y - section.yb) * 0.002

                prev_x = section.xa
                prev_y = section.ya

            else:
                section.phi = get_angle(prev_x, prev_y, section.xa, section.ya)
                section.update()

                section.xa += (prev_x - section.xb)
                section.ya += (prev_y - section.yb)
                prev_x = section.xa
                prev_y = section.ya

        #ITERATE BACKWARDS AND FIT START POS TO BOTTOM MID OF SCREEN
        for i, section in enumerate(reversed(sections)):
            if i == 0:
                section.xa = WIDTH/2
                section.ya = HEIGHT
                section.update()

                prev = section

            else:
                section.xa = prev.xb
                section.ya = prev.yb

                section.update()

                prev = section

        draw_window()


if __name__ == '__main__':
    # CREATE SECTIONS
    sections = []
    for i in range(N):
        new_section = Section(L + L * (N - i), HEIGHT / 2, L, 0.1, int(1 + i / 5))
        new_section.update()
        sections.append(new_section)

    run()
