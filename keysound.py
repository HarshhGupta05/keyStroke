import os
import pygame
from pynput import keyboard

folder = os.path.dirname(os.path.abspath(__file__))
pygame.mixer.init()
sound = pygame.mixer.Sound(os.path.join(folder, "ElevenLabs.mp3"))

pressed = set()

def on_press(key):
    if key in pressed:
        return
    pressed.add(key)
    sound.play()

def on_release(key):
    pressed.discard(key)
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
