using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace _8_puzzle
{
    class Node
    {
        public Node prevNode;
        public int[, ] puzzle;
        public int x, y;
        public int cost, level;

        public void printNode()
        {
            for(int i = 0; i < this.puzzle.GetLength(0); i++)
            {
                for(int j = 0; j < this.puzzle.GetLength(1); j++)
                {
                    Console.Write(puzzle[i, j] + " ");
                }
                Console.WriteLine();
            }
            Console.WriteLine("----------------");
        }

        public Node(Node prevNode, int[, ] puzzle, int x, int y, int cost, int level)
        {
            this.prevNode = prevNode;
            this.puzzle = puzzle;
            this.x = x;
            this.y = y;
            this.cost = cost;
            this.level = level;
        }
    }
}
