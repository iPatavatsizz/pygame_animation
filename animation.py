# CharacterRenderer.py
# by iPatavatsizz/Hx0z
# v 0.1
# https://github.com/iPatavatsizz/pygame_animation

"""

...
* Struggles with animation sprite?
- Look my ready test sprite
- Make your all animations in a image file.
- 0th sprite(0, 0) in your animation image will automatically set for 'still' state. *important!
- others depends on your list order in self.character/list ['still', 'move_down']
- for example you did 5 state animation image
1st -> 'still'
2nd -> 'move_up'
3rd -> 'move_down'
4th -> 'move_left'
5th -> 'move_right'
then you must set your state list like this order. self.characters['states'] = ['still', 'move_up', 'move_down', 'move_left', 'move_right']

another example for full understand:
1st -> 'still'
2nd -> 'move_left'
3rd -> 'move_down'
4th -> 'move_right'
5th -> 'move_up'
then you must set your state list like this order. self.characters['states'] = ['still', 'move_left', 'move_down', 'move_right', 'move_up']

* If you don't use like this order, when you move right your character, he will move right but his animation play like he is moving left.
```

# I tried my best to you understand(2).
# You'r welcome.
# That's all.
"""

import os
from typing import NoReturn, Dict
import pygame

if not pygame.get_init():
    pygame.init()

module_path: str = os.getcwd()


# states must equal image height (like 5 animations with 5 animation cols on sprite.)
def clipSurface(surface: pygame.Surface, size: tuple = (32, 32), states: list = ['still']) -> Dict:
    if surface:
        w = int(surface.get_width() / size[0])
        h = int(surface.get_height() / size[1])
        surfaces = []
        animations = {}
        for y in range(h):
            for x in range(w):
                surfaces.append(surface.subsurface((x * size[0], y * size[1]), (size[0], size[1])))
            if y == 0:
                animations.update({states[y]: surfaces[0]})  # for still state.
                animations.update({states[y + 1]: surfaces})
            else:
                animations.update({states[y + 1]: surfaces})
            surfaces = []  # After defining them, clear surfaces to append new row's(x/w) surfaces
        return animations
    return {}


def statePath(path: str = None) -> Dict:
    if path:
        _path = module_path
        path = path.split('/')
        file = path[-1]  # Get sprite
        folders = path[:-1]  # Get folders
        for v in range(len(folders)):
            if os.path.isdir(_path):
                _path = os.path.join(_path, folders[v])
        if os.path.isfile(os.path.join(_path, file)):
            return {'state': True, 'file': file, 'fpath': os.path.join(_path, file), 'path': _path, 'folders': folders}
        return {'state': False, 'file': file, 'fpath': None, 'path': _path, 'folders': folders}
    return None


class Character(pygame.sprite.Sprite):
    def __init__(self, surface: pygame.Surface = None, path: str = None, animate: bool = True) -> NoReturn:
        pygame.sprite.Sprite.__init__(self)
        self.module_path = module_path  # Get current directory of the module
        self.surface = surface  # Get surface to draw
        self.character = {
            'states': ['still', 'move_down', 'move_left', 'move_up', 'move_right'],  # Set state for character processes
            'state': None,
            'pos': pygame.math.Vector2(0, 0),  # Create 2D Vector for character position
            'speed': 2,  # Set speed for character processes
            # 'rect': pygame.Rect(self._imageAlpha.get_rect())  # Create Rect for sprite collisions.
            'animate': animate,
            'animation_count': 0,
            'fps': 30
        }
        #  Create method dict for storing variables.
        self._loadSprite = {}  # create dict for storing loadSprite method's variables.
        self.loadSprite(path)
        self.states_surfaces = clipSurface(self.image_surface, (32, 32), self.character['states'])

    def loadSprite(self, path: str) -> NoReturn:
        o = statePath(path)
        if o['state']:
            self.file = o['file']
            self.fpath = o['fpath']
            path = o['path']
            folders = o['file']
            self.image_surface = pygame.image.load(self.fpath).convert_alpha()
            self.scale_surface = pygame.transform.scale2x(self.image_surface)
            self._loadSprite.update({self.file: {
                'path': path,
                'folders': folders,
                'image_surface': self.image_surface,
                'scale_surface': self.scale_surface
            }})
            self.character['rect'] = self.image_surface.get_rect()

    # Surface -> Surface to draw, fps -> Animation frames of character image
    def animate(self, surface: pygame.Surface = None, fps: int = 30) -> NoReturn:
        if self.character['animate']:
            self.fps = fps
            surface = (surface or self.surface)
            animations = self.states_surfaces
            for animation in animations:
                if self.character['state'] == animation:
                    a = animations[animation]
                    if type(a) == pygame.Surface:
                        surface.blit(a, self.character['pos'])
                    else:
                        ac = len(a)
                        c = self.character['animation_count']
                        if c >= ac * self.fps:
                            self.character['animation_count'] = 0
                        else:
                            surface.blit(a[int(c / self.fps)], self.character['pos'])

    def update(self):
        # Character Move
        key = pygame.key.get_pressed()

        # print(self.character['state'])

        if key[pygame.K_w]:
            self.character['state'] = "move_up"
            self.character['pos'][1] -= self.character["speed"]
            self.character['animation_count'] += 2.5 * self.character['speed']
            print(self.character['animation_count'], int(2.5 * self.character['speed']))
        elif key[pygame.K_s]:
            self.character['state'] = "move_down"
            self.character['pos'][1] += self.character["speed"]
            self.character['animation_count'] += 2.5 * self.character['speed']
        elif key[pygame.K_a]:
            self.character['state'] = "move_left"
            self.character['pos'][0] -= self.character["speed"]
            self.character['animation_count'] += 2.5 * self.character['speed']
        elif key[pygame.K_d]:
            self.character['state'] = "move_right"
            self.character['pos'][0] += self.character["speed"]
            self.character['animation_count'] += 2.5 * self.character['speed']
        else:
            self.character['state'] = "still"
            self.character['animation_count'] = 0
