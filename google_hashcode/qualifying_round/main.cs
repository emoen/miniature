using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DataStructures;
 
namespace HashcodeMain
{
    public class WaitingTime : IComparable
    {
        public double score()
        {
 
            double ret = wait;
             ret += 0.0001 / lengthInv;
             if (getsBonus)
                 ret *= 0.00000001;
            return ret;
        }
 
        public int CompareTo(object obj)
        {
            return score().CompareTo(((WaitingTime)obj).score());
        }
    }
 
    public class MainClass
    {
        static List<int[]> output;
        internal static int nRows, nCols, nCars, nRides, bonus, nTimes;
        const int ROW = 0, COL = 1, TIME = 2;
        static int score;
        static double weight;
        static Heap<WaitingTime> heap;
        static HeapElement<WaitingTime>[,] waitingTimes;
        /*struct Car
        {
            int row;
            int column;
            int time;
        }*/
        static int[,] cars;
        static List<int>[] completedByCar;
        internal struct Ride
        {
            public int rideNumber;
            public int startRow;
            public int startColumn;
            public int endRow;
            public int endColumn;
            public int earliestStart;
            public int latestFinish;
            public bool completed;
            public int rideTime;
            public bool used;
            public int possibleCount;
        };
        internal static Ride[] rides;
 
        public static List<int>[] Run(List<int[]> input, double weight)
        {
            MainClass.weight = weight;
            score = 0;
            ParseList(input);
            //SortRides();
            //Schedule();
            heap = new Heap<WaitingTime>(nRides * nCars);
            InsertInHeap();
            Schedule2();
            for (int i = 0; i < nCars; i++)
            {
                completedByCar[i][0] = completedByCar[i].Count - 1;
            }
            //output = new List<int[]>();
            return completedByCar;
        }
 
        private static void InsertInHeap()
        {
            waitingTimes = new HeapElement<HashcodeMain.WaitingTime>[nCars, nRides];
            for (int i = 0; i < nCars; i++)
            {
                for (int j = 0; j < nRides; j++)
                {
                    if (CanCarTakeRide(i, j))
                    {
                        var w = new WaitingTime();
                        w.ride = j;
                        w.car = i;
                        w.wait = WaitingTime(i, j);
                        w.lengthInv = 1.0 / rides[j].rideTime;
                        w.getsBonus = GetsBonus(w.car, i);
                        waitingTimes[i, j] = heap.Insert(w);
                        rides[i].possibleCount++;
                    }
                }
 
            }
        }
 
        private static void Schedule2()
        {
            while (heap.Count() > 0)
            {
                WaitingTime w = heap.Extract();
                waitingTimes[w.car, w.ride] = null;
                rides[w.ride].used = false;
                if (!rides[w.ride].completed)
                {
                    if (CanCarTakeRide(w.car, w.ride))
                    {
                        for (int i = 0; i < nCars; i++)
                        {
                            if (waitingTimes[i, w.ride] != null)
                            {
                                heap.Delete(waitingTimes[i, w.ride]);
                                waitingTimes[i, w.ride] = null;
                            }
                        }
                        TakeRide(w.car, w.ride);
                        for (int i = 0; i < nRides; i++)
                        {
                            if (waitingTimes[w.car, i] != null)
                            {
                                WaitingTime newW = new WaitingTime();
                                newW.ride = i;
                                newW.car = w.car;
                                newW.wait = WaitingTime(w.car, i);
                                newW.getsBonus = GetsBonus(w.car, i);
                                if (newW.wait < 0)
                                {
                                    // newW.wait = int.MaxValue;
                                    heap.Delete(waitingTimes[w.car, i]);
                                    waitingTimes[w.car, i] = null;
                                    rides[i].possibleCount--;
                                }
                                else
                                    heap.ChangeValue(waitingTimes[w.car, i], newW);
                            }
                        }
                    }
                }
 
            }
        }
 
        static private int WaitingTime(int car, int ride)
        {
            return ActualStartTime(car, ride) - cars[car, TIME];
        }
 
        private static void SortRides()
        {
            int[] endTimes = new int[nRides];
            for (int i = 0; i < nRides; i++)
            {
                endTimes[i] = rides[i].rideTime;
            }
            Array.Sort(endTimes, rides);
        }
 
        private static void Schedule()
        {
            for (int i = 0; i < nCars; i++)
            {
                for (int j = 0; j < nRides; j++)
                {
                    if (!rides[j].completed && GetsBonus(i, j) && CanCarTakeRide(i, j))
                        TakeRide(i, j);
                }
            }
            for (int i = 0; i < nCars; i++)
            {
                for (int j = 0; j < nRides; j++)
                {
                    if (!rides[j].completed && CanCarTakeRide(i, j))
                        TakeRide(i, j);
                }
            }
        }
 
        private static void ParseList(List<int[]> input)
        {
            ParseGlobals(input[0]);
            rides = new Ride[nRides];
            for (int i = 0; i < nRides; i++)
            {
                int j = i + 1;
                rides[i] = new Ride();
                rides[i].startRow = input[j][0];
                rides[i].startColumn = input[j][1];
                rides[i].endRow = input[j][2];
                rides[i].endColumn = input[j][3];
                rides[i].earliestStart = input[j][4];
                rides[i].latestFinish = input[j][5];
                rides[i].completed = false;
                rides[i].rideTime = RideTime(rides[i].startRow, rides[i].startColumn, rides[i].endRow, rides[i].endColumn);
                rides[i].rideNumber = i;
                rides[i].used = false;
                rides[i].possibleCount = 0;
            }
        }
 
        private static int RideTime(int startRow, int startColumn, int endRow, int endColumn)
        {
            return Math.Abs(startRow - endRow) + Math.Abs(startColumn - endColumn);
        }
 
        private static void ParseGlobals(int[] v)
        {
            nRows = v[0];
            nCols = v[1];
            nCars = v[2];
            nRides = v[3];
            bonus = v[4];
            nTimes = v[5];
            cars = new int[nCars, 3];
            completedByCar = new List<int>[nCars];
            for (int i = 0; i < nCars; i++)
            {
                completedByCar[i] = new List<int>();
                completedByCar[i].Add(i);
            }
        }
 
        public static int Evaluate()
        {
            return score;
        }
 
        private static void TakeRide(int car, int ride)
        {
            rides[ride].completed = true;
            int actualStartTime = ActualStartTime(car, ride);
            int endTime = actualStartTime + rides[ride].rideTime;
            cars[car, ROW] = rides[ride].endRow;
            cars[car, COL] = rides[ride].endColumn;
            cars[car, TIME] = endTime;
            completedByCar[car].Add(rides[ride].rideNumber);
            score += rides[ride].rideTime;
            if (actualStartTime == rides[ride].earliestStart)
                score += bonus;
        }
 
        private static int ActualStartTime(int car, int ride)
        {
            int timeToStart = DistanceToStart(car, rides[ride]);
            int actualStartTime = Math.Max(cars[car, TIME] + timeToStart, rides[ride].earliestStart);
            return actualStartTime;
        }
 
        private static bool GetsBonus(int car, int ride)
        {
            int timeToStart = DistanceToStart(car, rides[ride]);
            int actualStartTime = Math.Max(cars[car, TIME] + timeToStart, rides[ride].earliestStart);
            if (actualStartTime == rides[ride].earliestStart)
                return true;
            return false;
        }
 
        private static bool CanCarTakeRide(int car, int ride)
        {
            if (cars[car, TIME] + RideTimeForCar(car, ride) < rides[ride].latestFinish)
                return true;
            return false;
        }
 
        private static int RideTimeForCar(int car, int ride)
        {
            Ride curRide = rides[ride];
            int timeToStart = DistanceToStart(car, curRide);
            return timeToStart + curRide.rideTime;
        }
 
        private static int DistanceToStart(int car, Ride curRide)
        {
            int nowRow = cars[car, 0];
            int nowCol = cars[car, 1];
 
            return Math.Abs(curRide.startColumn - nowCol) + Math.Abs(curRide.startRow - nowRow);
        }
    }
}