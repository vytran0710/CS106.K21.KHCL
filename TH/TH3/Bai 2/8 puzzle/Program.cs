using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Security.Cryptography.X509Certificates;

namespace _8_puzzle
{
    class Program
    {
        static int[] row = { 1, 0, -1, 0 };
        static int[] col = { 0, -1, 0, 1 };

        static void swapPos(int[, ] puzzle, int x, int y, int curx, int cury)
        {
            int temp = puzzle[curx, cury];
            puzzle[curx, cury] = puzzle[x, y];
            puzzle[x, y] = temp;
        }

        static int estimateCost(int[, ] iniPuzzle, int[, ] finPuzzle)
        {
            int count = 0;
            for (int i = 0; i < iniPuzzle.GetLength(0); i++)
            {
                for (int j = 0; j < iniPuzzle.GetLength(1); j++)
                {
                    if(iniPuzzle[i, j] != finPuzzle[i, j])
                    {
                        ++count;
                    }
                }
            }
            return count;
        }

        static bool isValidPuzzle(Node n, int x, int y)
        {
            return (x >= 0 && x < n.puzzle.GetLength(1) && y >= 0 && y < n.puzzle.GetLength(0));
        }

        static void solvePuzzle(Node startingNode, int[, ] finalPuzzle)
        {
            Queue<Node> qN = new Queue<Node>();
            qN.Enqueue(startingNode);

            while(qN.Count>0)
            {
                Node s = qN.Dequeue();
                if (s.cost == 0)
                {
                    Node k = s;
                    Stack<Node> sN = new Stack<Node>();

                    while(k.prevNode!=null)
                    {
                        sN.Push(k);
                        k=k.prevNode;
                    }
                    startingNode.printNode();
                    while(sN.Count>0)
                    {
                        sN.Pop().printNode();
                    }
                    break;
                }
                for (int i = 0; i < 4; i++)
                {
                    if (isValidPuzzle(s, s.x + row[i], s.y + col[i]))
                    {
                        int[, ] puzzle = s.puzzle.Clone() as int[,]; ;

                        swapPos(puzzle, s.x + row[i], s.y + col[i], s.x, s.y);

                        Node next = new Node(s, puzzle, s.x + row[i], s.y + col[i], estimateCost(puzzle, finalPuzzle), s.level+1);

                        qN.Enqueue(next);
                    }
                }
            }
        }

        static void Main(string[] args)
        {
            string path;

            Console.WriteLine("Enter puzzle's path:");

            path = Console.ReadLine();

            String input = File.ReadAllText(@path);

            int i = 0, j = 0;
            int[,] initArray = new int[3, 3];
            foreach (var row in input.Split('\n'))
            {
                j = 0;
                foreach (var col in row.Trim().Split(' '))
                {
                    initArray[i, j] = int.Parse(col.Trim());
                    j++;
                }
                i++;
            }

            int[,] finalArray = new int[, ]
            {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 0}
            };


            Node startingNode = new Node(null, initArray, 1, 2, estimateCost(initArray, finalArray), 1);

            solvePuzzle(startingNode, finalArray);
        }
    }
}
