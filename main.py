from display import Display
from utils import pygame


pygame.init()

# ---------------- Set Caption  ----------------- #
pygame.display.set_caption("Path Finding Algorithm")



# ----------------- Constants  ------------------ #
FPS = 60



# ----------------- Functions  ------------------ #
def main():

    display = Display()
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        display.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if display.get_started():
                continue

            clicked = pygame.mouse.get_pressed()
            if clicked:
                pos = pygame.mouse.get_pos()
                display.get_clicked_node(pos)
                if clicked[0]:  # LEFT MOUSE CLICK
                    display.left_mouse_click()

                elif clicked[2]:  # RIGHT MOUSE CLICK
                    display.right_mouse_click()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display.space_key_down()

                if event.key == pygame.K_BACKSPACE:
                    display.reset_display()

                if event.key == pygame.K_p:
                    display.path_key_down()

                if event.key == pygame.K_a:
                    display.all_key_down()

    pygame.quit()


if __name__ == "__main__":
    main()
