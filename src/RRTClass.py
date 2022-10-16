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

    def addNode(self,n,x,y):
        self.x.insert(n,x)
        self.y.insert(n,y)

    def removeNode(self,n):
        self.x.pop(n)
        self.y.pop(n)

    def addEdge(self,parent,child):
        self.parent.insert(child,parent)

    def addEdge(self,n):
        self.parent.pop(n)

    def numberOfNodes(self):
        return(len(self.x))
    
    def distance(self,n1,n2):
        (x1,y1) = (self.x[n1],self.y[n1]) 
        (x2,y2) = (self.x[n2],self.y[n2]) 
        px = (float(x1)-float(x2))**2
        py = (float(y1)-float(y2))**2
        return ((px+py)**0.5)

    def sampleEnv(self):
        x = int(random.uniform(0,self.MapWidht))
        y = int(random.uniform(0,self.MapHeight))
        return (x,y)

    def isFree(self):
        n = self.numberOfNodes()-1
        (x,y) = (self.x[n],self.y[n])
        obs = self.obstacles.copy()

        while len(obs)>0 :
            rectangle = obs.pop(0)
            if rectangle.collidepoint(x,y):
                self.removeNode(n)
                return False

        return True






