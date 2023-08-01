import time
import pygame
import numpy as np

color_fondo = (21, 21, 21)
color_cuadricula = (38, 28, 44)
celulapormorir = (180, 165, 165)
celulaporvivir = (196, 182, 182)

def update(pantalla, celulas, tamaño, progreso=False):
    update_celulas = np.empty((celulas.shape[0],celulas.shape[1]))