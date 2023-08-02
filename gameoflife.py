import time
import pygame
import numpy as np

color_fondo = (21, 21, 21)
color_cuadricula = (38, 28, 44)
celulapormorir = (180, 165, 165)
celulaporvivir = (196, 182, 182)

def update(pantalla, celulas, size, progreso=False):
    update_celulas = np.zeros((celulas.shape[0], celulas.shape[1]))
    #El siguiente bucle permite tomar cada célula para ponerlas en la cuadrícula 
    #Tomando tanto la lógica del juego como la sintaxis de Python
    for fila, col in np.ndindex(celulas.shape):
        #Calcula cuantas celulas vivas hay alrededor de una célula cualquiera usando listas
        #La idea es sumar las celulas de arriba más las de abajo, restando la celula cuyo estado queremos definir.
        celulaviva = np.sum(celulas[fila-1:fila+2, col-1:col+2]) - celulas[fila, col]
        color = color_fondo if celulas[fila, col] == 0 else celulaporvivir

        #El siguiente ciclo es para establecer las reglas de Juego de la vida

        if celulas[fila, col] == 1:
            if celulaviva < 2 or celulaviva > 3:
                if progreso:
                    color = celulapormorir
            elif 2 <= celulaviva <=3:
                update_celulas[fila, col] = 1
                if progreso:
                    color = celulaporvivir
        else:
            if celulaviva == 3:
                 update_celulas[fila, col] = 1
                 if progreso: 
                     color = celulaporvivir

        pygame.draw.rect(pantalla, color, (col * size, fila * size, size - 1, size - 1))
    
    return update_celulas

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800,600))

    #Sin progreso solo tenemos el color de la cuadricula que se irá llenando con las especificaciones de la funciún update
    celulas = np.zeros((60, 80))
    pantalla.fill(color_cuadricula)
    update(pantalla, celulas, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False
    
    #Bucle del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(pantalla, celulas, 10)
                    pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                    posicion = pygame.mouse.get_pos()
                    celulas[posicion[1] // 10, posicion[0] // 10] = 1
                    update(pantalla, celulas, 10)
                    pygame.display.update()

        pantalla.fill(color_cuadricula)

        if running:
            celulas = update(pantalla, celulas, 10, progreso=True)
            pygame.display.update
        
        time.sleep(0.001)

if __name__ == '__main__':
    main()