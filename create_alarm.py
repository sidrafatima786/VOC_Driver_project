import pygame
import numpy as np

pygame.mixer.init()
pygame.mixer.Sound(np.array([4096 * np.sin(2.0 * np.pi * 440.0 * t / 44100) for t in range(44100)], dtype=np.int16)).save('alarm.wav')
