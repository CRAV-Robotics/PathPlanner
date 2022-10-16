import pygame
import sys
from RRTClass import RRTMap
from RRTClass import RRTGraph



def main():
    MapDimension = (600,600)
    start = (50,50)
    goal = (500,500)

    obsDim = 40
    obsNum = 20

    pygame.init()
    map = RRTMap(start,goal,MapDimension, obsDim, obsNum)
    graph = RRTGraph(start,goal,MapDimension, obsDim, obsNum)

    obstacles = graph.makeObs()

    map.drawMap(obstacles)

    pygame.display.update()
    pygame.event.clear()

    while True :
    #pygame.event.event_name(pygame.K_0)
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        




if __name__== '__main__':
    main()