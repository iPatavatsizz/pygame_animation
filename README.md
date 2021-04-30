# pygame_animation

> **Pygame Animation Module / Hx0z**

game.py

```py
import pygame
import animation
from sys import exit

if not pygame.get_init():
    pygame.init()

# Initalize Surfaces
display = pygame.display.set_mode((800, 400))
main_surface = pygame.Surface(display.get_size())

# Initalize character
my_character = animation.init(main_surface, "assests/characters/mycharacter.png", True)

clock = pygame.time.Clock()


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    main_surface.fill((0, 0, 0))
    character1.animate(fps=30)
    character1.update()
    display.blit(main_surface, (0, 0))
    pygame.display.update()


pygame.quit()
exit()
```
