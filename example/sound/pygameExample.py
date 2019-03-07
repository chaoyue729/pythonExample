'''
Here (OSX Mavericks) I got able to install this way:
    brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
    pip install https://bitbucket.org/pygame/pygame/get/default.tar.gz

https://stackoverflow.com/questions/22974339/pygame-installation-issue-in-mac-os
'''

#!/usr/bin/env python
import pygame

song = "/Users/whitexozu/Music/a.ogg"

pygame.init()
song = pygame.mixer.Sound(song)
clock = pygame.time.Clock()
song.play()
while True:
    clock.tick(0)
pygame.quit()