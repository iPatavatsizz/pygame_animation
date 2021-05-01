# pygame_animation

> **Pygame Animation Module / Hx0z**

Updates for this module will come as soon as possible.

game.py - change v0.2.0

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
my_character = animation.Character(main_surface, "assests/characters/mycharacter.png", True)

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

## **Classes**

---

### *Character.Character(surface, image, animate, size, fps)*

Description

#### Base character class of animation module

Parameters/Variables

---
> **surface** *pygame.surface*

- **default:** None

---
> **image** *(str)*

- **default:** None

- **example:** "assests/player.png"

---
> **animate** *bool*

- **default:** True

- **example:** True/False

---
> **size** *tuple(int, int)*

- **default:** (32, 32)

- **example:** (11, 89)

---

##### **Size:** *Pixel size of sprite (32x32, 11,89, 64x64) -> (32,32 11,80, 64,64)*

## **Methods/Functions**

Use these funcs/methods in your game loop

---

### *Character.animate(fps)*

Description

#### Draws character to surface

### **Parameters /Variables**

---
> **fps** *integer*

- **default:** 30

- **example:** 30, 60

### *Character.update()*

Description

#### Updates character class parameters

Parameters /Variables

---

#### No parameters for this, just call it on your game loop
