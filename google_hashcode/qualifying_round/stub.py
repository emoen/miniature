import numpy as np
import pandas as pd
import math
import sys
import os
from heapq import heappush, heappop
 
CAR_ROW = 0 #Globals
CAR_COL = 1
CAR_TIME = 2
cars, rides, score, completedByCar, bonus= None
def parseList(filename):
    global rides, bonus
    
    with open(filename, 'r') as fp:
        firstLine = fp.readline()
        #completed By global
        nRows, nCols, nCars, nRides, bonus, nTimes = [int(i) for i in firstLine.split()]
        
        i = 0
        rides = list(range(nRides))
        for line in fp:
            startRow, startCol, endRow, endCol, earlyestStart, latestFinish = [int(l) for l in line.split()]
            
            ride = dict()
            ride['rideNumber'] = i
            ride['startRow'] = startRow
            ride['startCol'] = startCol
            ride['endRow'] = endRow
            ride['endCol'] = endCol
            ride['earlyestStart'] = earlyestStart
            ride['latestFinish'] = latestFinish
            ride['completed'] = False
            ride['rideTime'] = abs(startRow - endRow) + abs(startCol - endCol)
            ride['used'] = False
            ride['possibleCount'] = 0
            
            rides[i] = ride
            i += 1
        
    return nRows, nCols, nCars, nRides, bonus, nTimes

def scoreAFile( afilename ):
    global rides, cars, score, bonus, completedByCar
    
    score = 0
    nRows, nCols, nCars, nRides, bonus, nTimes = parseList( afilename )
    
    #completed By global        
    cars = np.zeros((nCars, 3)) #cars start at (0,0) and T=0
    completedByCar = list( [{'carRides': 0, 'rideId': []} for i in range(nCars)] )
    
    #schedule(nCars, nRides)
    
    heap = [] #length nRides * nCars #Heap<WaitingTime> heap;
    insertInHeap();
    waitingTimes = [] #HeapElement<WaitingTime>[,] waitingTimes;
    scheduleHeap(nCars, nRides)
    for i in range(nCars):
        completedByCar[i]['carRides'] = len(completedByCar[i]['rideId'])
     
    return score

def insertInHeap(nCars, nRides):
    waitingTimes = new HeapElement<HashcodeMain.WaitingTime>[nCars, nRides];
    for i in range(nCars):
        for j in range(nRides)
            if CanCarTakeRide(i, j):
                w = dict()#new WaitingTime();
                w['ride'] = j
                w['car'] = i
                w['wait'] = WaitingTime(i, j)
                w['lengthInv'] = 1.0 / rides[j]['rideTime']
                w['getsBonus'] = getsBonus(w.car, i);
                waitingTimes[i, j] = heap.Insert(w);
                rides[i].possibleCount++;
     
def schedule(nCars, nRides):
    global rides
    '''for aCar in range(nCars):
        for aRide in range(nRides):
            print(rides[aRide])
            print(getsBonus(aCar, aRide))
            print(canCarTakeRide(aCar, aRide))
            if not rides[aRide]['completed'] and getsBonus(aCar, aRide) and canCarTakeRide(aCar, aRide):
                takeRide(aCar, aRide)
    '''
    for aCar in range(nCars):
        for aRide in range(nRides):
            if not rides[aRide]['completed'] and canCarTakeRide(aCar, aRide):
                takeRide(aCar, aRide)

def takeRide(car, ride):
    global cars, rides, score, completedByCar, bonus
    rides[ride]['completed'] = True
    actualStartTime = actualStartTimeFunc(car, ride)
    endTime = actualStartTime + rides[ride]['rideTime']
    cars[car, CAR_ROW] = rides[ride]['endRow']
    cars[car, CAR_COL] = rides[ride]['endCol']
    cars[car, CAR_TIME] = endTime
    completedByCar[car]['rideId'].append( rides[ride]['rideNumber'] )
    score += rides[ride]['rideTime']
    if actualStartTime == rides[ride]['earlyestStart']:
        score += bonus
        
def actualStartTimeFunc(car, ride):
    global cars, rides
    timeToStart = distanceToStart(car, rides[ride])
    return max(cars[car, CAR_TIME] + timeToStart, rides[ride]['earlyestStart'])
        
def getsBonus(car, ride):
    global cars
    timeToStart = distanceToStart(car, rides[ride])
    actualStartTime = max(cars[car, CAR_TIME] + timeToStart, rides[ride]['earlyestStart'])
    if actualStartTime == rides[ride]['earlyestStart']:
        return True
    return False

def canCarTakeRide(car, ride):
    global cars, rides
    if cars[car, CAR_TIME] + rideTimeForCar(car, ride) < rides[ride]['latestFinish']:
        return True
    return False

def rideTimeForCar(car, ride):
    global rides
    curRide = rides[ride]
    timeToStart = distanceToStart(car, curRide)
    return timeToStart + curRide['rideTime']

def distanceToStart(car, curRide):
    global cars
    nowRow = cars[car, CAR_ROW]
    nowCol = cars[car, CAR_COL]

    return abs(curRide['startCol'] - nowCol) + abs(curRide['startRow'] - nowRow)

def write_file():
    F = open("workfile.out","w")
    F.writelines(str(out_count)+"\n")
    F.write(str(out_matrix[0:out_count,:]))

    #print("completed by car:"+str(completedByCar))
    #print("Score:"+str(score))
    #out_matrix = np.array([[1,2,3],[2,3,4]])
    #np.savetxt("filename.txt", out_matrix.astype(int), fmt='%i', newline="\n")
    #print(out_matrix)

def main(argv):
    
    example = scoreAFile("infile/example.in")
    print("example:"+str(example))
    small = scoreAFile("infile/small.in")
    print("small:"+str(small))
    medium = scoreAFile("infile/medium.in")
    print("medium:"+str(medium))
    big = scoreAFile("infile/big.in")
    print("big:"+str(big))
    high_bonus = scoreAFile("infile/high_bonus.in")
    print("high_bonus:"+str(high_bonus))
    
    scores = pd.read_csv("scores.txt", delimiter=' ', header=None, index_col=False)
    if scores.iloc[0,1] < example:
       scores.iloc[0,1] = example 
    if scores.iloc[1,1] < small:
        scores.iloc[1,1] = small
    if  scores.iloc[2,1] < medium:
        scores.iloc[2,1] = medium
    if  scores.iloc[3,1] < big:
        scores.iloc[3,1] = big
    if  scores.iloc[4,1] < high_bonus:
        scores.iloc[4,1] = high_bonus
    scores.iloc[5,1] = scores[1].sum()
    scores.to_csv("scores.txt", sep=' ', header=None, index=False)
    print(scores)
    
if __name__ == "__main__":
    main(sys.argv)