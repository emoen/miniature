import numpy as np
import pandas as pd
import math
import sys
import os
#from line_profiler import LineProfiler
import heapq_27_with_index as heapq #import heapq
import WaitingTime
from operator import itemgetter
from multiprocessing import Pool
import operator

class CarTime:
    def __init__(self, car, time):
        self.car = car
        self.time = time
      
    def cmp_lt(x, y):        
        return (x.time < y.time) if hasattr(x, '__lt__') else (not y.time <= x.tim)
        
    def __eq__(self, other):
        return self.time == other.time
        
class Car:
    row=0       #start posision
    column=0    #start posision
    time=0      #start time

class Ride:
    rideNumber = None    #int
    startRow = None      #int
    startColumn = None   #int
    endRow = None        #int
    endColumn = None     #int
    earliestStart = None #int
    latestFinish = None  #int
    completed = False    #bool
    rideTime = None      #int
    used = False         #bool
    possibleCount = None #int
    goodness = None      #int
    nextRide = None      #int

#Globals
score, bonus = 0,0
cars, rides, waitingTimes, heap, heapIndex, completedByCar = None, None, None, None, None, None
carTimeHeap, carTimeHeapIndex, carTimes = None, None, None
def resetGlobalVars():
    global cars, rides, score, bonus, waitingTimes, heap, heapIndex, completedByCar
    score, bonus = 0,0
    cars, rides, waitingTimes, heap, heapIndex, completedByCar = None, None, None, None, None, None
    carTimeHeap, carTimeHeapIndex, carTimes = None, None, None
    
def parseList(filename):
    global rides, bonus
    
    with open(filename, 'r') as fp:
        firstLine = fp.readline()
        nRows, nCols, nCars, nRides, bonus, nTimes = [int(i) for i in firstLine.split()]
        
        i = 0
        rides = list(range(nRides))
        for line in fp:
            startRow, startCol, endRow, endCol, earliestStart, latestFinish = [int(l) for l in line.split()]
            
            ride = Ride()
            ride.rideNumber = i
            ride.startRow = startRow
            ride.startColumn = startCol
            ride.endRow = endRow
            ride.endColumn = endCol
            ride.earliestStart = earliestStart
            ride.latestFinish = latestFinish
            ride.completed = False
            ride.rideTime = abs(startRow - endRow) + abs(startCol - endCol)
            ride.used = False
            ride.possibleCount = 0
            ride.goodness = 0
            ride.nextRide = 0
                
            rides[i] = ride
            i += 1
        
    return nRows, nCols, nCars, nRides, bonus, nTimes   
   
def scoreAFile( afilename ):
    global rides, cars, score, bonus, completedByCar, waitingTimes,heap, heapIndex
    global carTimeHeap, carTimeHeapIndex, carTimes 
    resetGlobalVars()
    nRows, nCols, nCars, nRides, bonus, nTimes = parseList( afilename )
    
    rides2 = sorted(rides, key=operator.attrgetter('rideTime'))
    
    ride_last = [(i.startRow, i.startColumn, i.rideTime) for i in rides2[len(rides2)-10:len(rides2)]]
    print("last: rideTime:"+str(ride_last))
    
    cars = [Car() for i in range(nCars)] #np.zeros((nCars, 3)) #cars start at (0,0) and T=0
    completedByCar = list( [{'carRides': 0, 'rideId': []} for i in range(nCars)] )
    #schedule(nCars, nRides)
    
    heap = [] #length nRides * nCars 
    heapIndex = dict()
    carTimes = []
    carTimeHeap = []
    carTimeHeapIndex = dict()
    insertInHeap2(nCars, nRides)
    schedule2_2(nCars, nRides)

    for i in range(nCars):
        completedByCar[i]['carRides'] = len(completedByCar[i]['rideId'])
     
    return score, completedByCar

def insertInHeap3(nCars):
    global carTimeHeap, carTimeHeapIndex, cars
    global carTimeHeap, carTimeHeapIndex, carTimes 
    
    for i in range(nCars):
        carTime = CarTime()
        carTime.car = i
        carTime.time = 0
        heapq.heappush2(carTimeHeap, carTime, carTimeHeapIndex)
        carTimes[i] = carTime

def insertInHeap2(nCars, nRides):
    global waitingTimes, heap, heapIndex
    
    waitingTimes = [[None for x in range(nRides)] for y in range(nCars)] #new HeapElement<HashcodeMain.WaitingTime>[nCars, nRides];
    for i in range(nCars):
        for j in range(nRides):
            if canCarTakeRide(i, j):
                w = WaitingTime.WaitingTime()
                w.ride = j
                w.car = i
                w.wait = getWaitingTime(i, j)
                w.length = rides[j].rideTime
                w.lengthInv = 1./ w.length
                w.getsBonus = getsBonus(w.car, w.ride)
                w.updateScore()
                wKeys = (w.wait, (w.car, w.ride))
                heapq.heappush2(heap, wKeys, heapIndex)
                waitingTimes[i][j] = w
                rides[i].possibleCount += 1

def scoreRides(nRides):
    for i in range(nRides):
        computeRideScore(i)

def updateRideScores(rideTaken, nRides, nCars):
    for i in range(nRides):
        if rides[i].nextRide == rideTaken and not rides[i].completed:
            computeRideScore(i);
            for j in range(nCars):
                if waitingTimes[j, i] != None:
                    waitingTimes[j, i].updateScore();

def computeRideScore(car):
    #todo: impl
    return 0

'''
def shortestWait(car):
    global cars
    
    WaitingTime w = null;
    var node = list[car].First;
    double min = double.MaxValue;
    while (node != null)
    {
        if (node.Value.score < min)
        {
            w = node.Value;
            min = w.score;
        }
        node = node.Next;
    }
    return w;
    }
'''
        
#@profile
def schedule2_2(nCars, nRides):
    global heap, heapIndex, waitingTimes
    while len(heap) > 0:
        (wait, (car,ride)) = heapq.heappop2(heap, heapIndex) 
        w = waitingTimes[car][ride]
        waitingTimes[w.car][w.ride] = None
        if not rides[w.ride].completed and canCarTakeRide(w.car, w.ride): #and (rides[w.ride].endRow < 5000 and rides[w.ride].endCol < 3000 and rides[w.ride].endRow > 500): #   and getsBonus(w.car, w.ride):
            for i in range(nCars):
                if waitingTimes[i][w.ride] != None:
                    tmp = waitingTimes[i][w.ride]
                    wKeys = (tmp.wait, (tmp.car,tmp.ride))
                    heapq.heappop_arbitrary(heap, heapIndex, wKeys) #heap.Delete(waitingTimes[i, w.ride])
                    waitingTimes[i][w.ride] = None
                
            takeRide(w.car, w.ride)
            for i in range(nRides):
                if waitingTimes[w.car][i] != None:
                    newW = WaitingTime.WaitingTime()
                    newW.ride = i
                    newW.car = w.car
                    newW.wait = getWaitingTime(w.car, i)
                    newW.getsBonus = getsBonus(w.car, i);
                    if newW.wait < 0:
                        newW = waitingTimes[w.car][i]
                        wKeys = (newW.wait,(newW.car, newW.ride))
                        heapq.heappop_arbitrary(heap, heapIndex, wKeys) 
                        waitingTimes[w.car][i] = None
                        rides[i].possibleCount -= 1
                    else:
                        wToDelete = waitingTimes[w.car][i]
                        wTupeToDelete = (wToDelete.wait,(wToDelete.car, wToDelete.ride))
                        newWKeys = (newW.wait,( newW.car, newW.ride ))
                        heapq.changeValue(heap, wTupeToDelete, newWKeys, heapIndex) 
                        waitingTimes[w.car][i].wait = newW.wait
                        waitingTimes[w.car][i].getsBonus = newW.getsBonus
                        
def getWaitingTime(car, ride):
    global cars
    return getActualStartTime(car, ride) - cars[car].time
     
def schedule(nCars, nRides):
    global rides
    for aCar in range(nCars):
        for aRide in range(nRides):
            if not rides[aRide].completed and getsBonus(aCar, aRide) and canCarTakeRide(aCar, aRide):
                takeRide(aCar, aRide)
    
    for aCar in range(nCars):
        for aRide in range(nRides):
            if not rides[aRide].completed and canCarTakeRide(aCar, aRide):
                takeRide(aCar, aRide)

def updateCarWithRide(car, ride):
    actualStartTime = getActualStartTime(car, ride) #UpdateCarWithRide(ref cars[car], ride);
    endTime = actualStartTime + rides[ride].rideTime
    cars[car].row = rides[ride].endRow
    cars[car].column = rides[ride].endColumn
    cars[car].time = endTime
    return actualStartTime
    
def takeRide2(car, ride):
    global cars, rides, score, completedByCar, bonus
    global carTimeHeap, carTimeHeapIndex, carTimes 
    
    oldCarTime = CarTime(car, cars[car].time)
    rides[ride].completed = True
    actualStartTime = updateCarWithRide(car, ride) #UpdateCarWithRide(ref cars[car], ride);
    completedByCar[car]['rideId'] += [ rides[ride].rideNumber ]
    score += rides[ride].rideTime
    if actualStartTime == rides[ride].earliestStart:
        score += bonus
    heapq.changeValue(carTimeHeap, oldCarTime, CarTime(car, cars[car].time), carTimeHeapIndex )
      
def takeRide(car, ride):
    global cars, rides, score, completedByCar, bonus
    rides[ride].completed = True
    actualStartTime = getActualStartTime(car, ride)
    endTime = actualStartTime + rides[ride].rideTime
    cars[car].row = rides[ride].endRow
    cars[car].column = rides[ride].endColumn
    cars[car].time = endTime
    completedByCar[car]['rideId'] += [ rides[ride].rideNumber ]
    score += rides[ride].rideTime
    if actualStartTime == rides[ride].earliestStart:
        score += bonus
        
def getActualStartTime(car, ride):
    global cars, rides
    timeToStart = distanceToStart(car, rides[ride])
    return max(cars[car].time + timeToStart, rides[ride].earliestStart)
        
def getsBonus(car, ride):
    global cars
    timeToStart = distanceToStart(car, rides[ride])
    actualStartTime = max(cars[car].time + timeToStart, rides[ride].earliestStart)
    if actualStartTime == rides[ride].earliestStart:
        return True
    return False

def canCarTakeRide(car, ride):
    global cars, rides
    if cars[car].time + rideTimeForCar(car, ride) < rides[ride].latestFinish:
        return True
    return False

def rideTimeForCar(car, ride):
    global rides
    curRide = rides[ride]
    timeToStart = distanceToStart(car, curRide)
    return timeToStart + curRide.rideTime

def distanceToStart(car, curRide):
    global cars
    nowRow = cars[car].row
    nowCol = cars[car].column

    return abs(curRide.startColumn - nowCol) + abs(curRide.startRow - nowRow)

def doWrite(filename, scores):
    F = open(filename, "w")
    for dictElement in scores:
        ridesStr = ' '.join(map(str, dictElement['rideId']))
        F.writelines(str(dictElement['carRides'])+" "+ridesStr+"\n")
    
def main(argv):
    
    #profile = LineProfiler(scoreAFile("infile/small.in"))
    #profile.print_stats()
    example, completedByCar = scoreAFile("infile/example.in")
    print("example:"+str(example))
    doWrite("output/example.txt", completedByCar)

    small, completedByCar = scoreAFile("infile/small.in")
    print("small:"+str(small))
    doWrite("output/small.txt", completedByCar)

    medium, completedByCar =  scoreAFile("infile/medium.in")
    print("medium:"+str(medium))
    doWrite("output/medium.txt", completedByCar)
    
    #big, completedByCar = scoreAFile("infile/big.in")
    #print("big:"+str(big))
    #doWrite("output/big.txt", completedByCar)
            
    #high_bonus, completedByCar = scoreAFile("infile/high_bonus.in")
    #print("high_bonus:"+str(high_bonus))
    #doWrite("output/high_bonus.txt", completedByCar)
        
    #pool = Pool(3)
    #medium, cbc_medium, big, cbc_big, high_bonus, cbc_high_bonus = pool.map(scoreAFile, ["infile/medium.in", "infile/big.in", "infile/high_bonus.in"])
    
    scores = pd.read_csv("scores.txt", delimiter=' ', header=None, index_col=False)
    if scores.iloc[0,1] < example:
       scores.iloc[0,1] = example 
    if scores.iloc[1,1] < small:
        scores.iloc[1,1] = small
    if  scores.iloc[2,1] < medium:
        scores.iloc[2,1] = medium
    #if  scores.iloc[3,1] < big:
    #    scores.iloc[3,1] = big
    #if  scores.iloc[4,1] < high_bonus:
    #    scores.iloc[4,1] = high_bonus
    scores.iloc[5,1] = scores[1][0:5].sum()
    scores.to_csv("scores.txt", sep=' ', header=None, index=False)
    print(scores)
   
if __name__ == "__main__":
    main(sys.argv)
