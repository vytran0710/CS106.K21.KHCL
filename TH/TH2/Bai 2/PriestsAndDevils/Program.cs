using System;
using System.Collections.Generic;

namespace PriestsAndDevils
{
    class Program
    {
        static public int stopProgram=0;

        static public bool validState(State s)
        {
            if(s.nP>3)
            {
                return false;
            }
            if (s.nD > 3)
            {
                return false;
            }
            if (s.nP < 0)
            {
                return false;
            }
            if (s.nD < 0)
            {
                return false;
            }
            if (s.nP > 0 && s.nD > s.nP)
            {
                return false;
            }
            if(3-s.nP > 0 && 3-s.nD > 3-s.nP)
            {
                return false;
            }
            return true;
        }

        static public void BFS(State startingState)
        {
            Queue<State> qS = new Queue<State>();
            qS.Enqueue(startingState);
            while (qS.Count > 0)
            {
                State s = qS.Dequeue();
                if (s.nP == 0 && s.nD == 0 && s.side == false)
                {
                    Console.WriteLine("SOLUTION FOUND AT LEVEL: " + (s.stateLevel).ToString());
                    Stack<State> sS = new Stack<State>();
                    State reverseS = s;

                    while (reverseS.prevState!=null)
                    {
                        sS.Push(reverseS);
                        reverseS = reverseS.prevState;
                    }
                    sS.Push(new State(3, 3, true, null, 0));

                    while(sS.Count>0)
                    {
                        reverseS = sS.Pop();
                        reverseS.printState();
                    }
                    do
                    {

                        Console.WriteLine("1. KEEP ON SEARCHING\t2. STOP");
                        stopProgram = int.Parse(Console.ReadKey().KeyChar.ToString());

                        Console.WriteLine();
                        Console.WriteLine("------------------------------------");

                    }
                    while (stopProgram < 1 || stopProgram > 2);
                    if(stopProgram==2)
                    {
                        break;
                    }
                }

                State s1 = new State(s.nP - 1, s.nD, false, s, s.stateLevel + 1);
                if (validState(s1) && s.side == true)
                {
                    qS.Enqueue(s1);
                }

                State s2 = new State(s.nP - 2, s.nD, false, s, s.stateLevel + 1);
                if (validState(s2) && s.side == true)
                {
                    qS.Enqueue(s2);
                }

                State s3 = new State(s.nP - 1, s.nD - 1, false, s, s.stateLevel + 1);
                if (validState(s3) && s.side == true)
                {
                    qS.Enqueue(s3);
                }

                State s4 = new State(s.nP, s.nD - 1, false, s, s.stateLevel + 1);
                if (validState(s4) && s.side == true)
                {
                    qS.Enqueue(s4);
                }
                State s5 = new State(s.nP, s.nD - 2, false, s, s.stateLevel + 1);
                if (validState(s5) && s.side == true)
                {
                    qS.Enqueue(s5);
                }

                State s6 = new State(s.nP + 1, s.nD, true, s, s.stateLevel + 1);
                if (validState(s6) && s.side == false)
                {
                    qS.Enqueue(s6);
                }

                State s7 = new State(s.nP + 2, s.nD, true, s, s.stateLevel + 1);
                if (validState(s7) && s.side == false)
                {
                    qS.Enqueue(s7);
                }

                State s8 = new State(s.nP + 1, s.nD + 1, true, s, s.stateLevel + 1);
                if (validState(s8) && s.side == false)
                {
                    qS.Enqueue(s8);
                }
                State s9 = new State(s.nP, s.nD + 1, true, s, s.stateLevel + 1);
                if (validState(s9) && s.side == false)
                {
                    qS.Enqueue(s9);
                }

                State s10 = new State(s.nP, s.nD + 2, true, s, s.stateLevel + 1);
                if (validState(s10) && s.side == false)
                {
                    qS.Enqueue(s10);
                }
            }
        }

        static void Main(string[] args)
        {
            State s = new State(3, 3, true, null, 1);
            BFS(s);
        }
    }
}
