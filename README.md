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

## Methods/Functions

### init(surface, image, animate, size, fps)

### Parameters/Variables

#### surface: pygame.surface Surface to draw sprite

#### image: str("assests/player.png")  Image path to load

#### animate:   bool(True/False)           True for animation

#### size   :   tuple(int, int)            Size of character, exmple: You draw your character 11x89 pixel use(11, 89) or 32x32 use (32, 32)

### Description

-> Returns Character class.

-> animate()
parameters:
    fps: integer, frame per second to draw animation
desc: draws character (sprite/image) to surface.
example usage:
    character.animate(fps=30)

-> update()
desc: updates character class
parameters:
* no parameters for this, just call it.