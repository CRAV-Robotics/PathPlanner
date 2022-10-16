import random
import math
import pygame

class RRTMap():
    def __init__(self, start, goal, MapDimensions, obsDim, obsNum):
        self.start = start
        self.goal = goal
        self.MapDimension = MapDimensions
        self.MapHeight, self.MapWidht = self.MapDimension

        # Windows Setting :

        self.MapWindowsName = "RRT PATH PLANNER"
        pygame.display.set_caption(self.MapWindowsName)
        self.map = pygame.display.set_mode(self.MapDimension)
        self.map.fill((255,255,255))
        self.nodeRad = 0
        self.nodeThickness = 0
        self.edgeThickness = 1

        self.obstacles = []
        self.obsDim = obsDim
        self.obsNum = obsNum

        # COLOR :
        self.Grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.White = (255,255,255)



    def drawMap(self, obstacles):
        pygame.draw.circle(self.map,self.Green,self.start,self.nodeRad+10,0)
        pygame.draw.circle(self.map,self.Blue,self.goal,self.nodeRad+10,0)
        self.drawObs(obstacles)

    def drawPath(self):
        pass

    def drawObs(self,obstacles):
        obstacleList = obstacles.copy()

        while (len(obstacleList)>0):
            obstacle = obstacleList.pop(0)
            pygame.draw.rect(self.map,self.Grey,obstacle)
    


class RRTGraph():
    def __init__(self, start, goal, MapDimensions, obsDim, obsNum):
        (x,y) = start
        self.start = start
        self.goal = goal
        self.goalFlag = False
        self.MapHeight, self.MapWidht = MapDimensions
        self.x = []
        self.y = []
        self.parent = []

        # Initial Tree
        self.x.append(x)
        self.y.append(y)
        self.parent.append(0)
        
        # Obstacles
        self.obstacles = []
        self.obsDim = obsDim
        self.obsNum = obsNum
        
        # path
        self.goalState = None
        self.path=[]

    def makeRandomRect(self):
        upperX = int(random.uniform(0,self.MapWidht-self.obsDim))
        upperY = int(random.uniform(0,self.MapHeight-self.obsDim))

        return(upperX,upperY)

    def makeObs(self):
        obs =[]

        for i in range(0,self.obsNum):
            rectang = None
            startgoalcol = True

            while startgoalcol:
                coordRect = self.makeRandomRect()
                rectang = pygame.Rect(coordRect,(self.obsDim,self.obsDim))

                if rectang.collidepoint(self.start) or rectang.collidepoint(self.goal):
                    startgoalcol = True

                else : 
                    startgoalcol = False

            obs.append(rectang)
        self.obstacles = obs.copy()

        return obs

    def addNode(self):
        pass
    def removeNode(self):
        pass

    def addEdge(self):
        pass

    def numberOfNodes(self):
        pass




