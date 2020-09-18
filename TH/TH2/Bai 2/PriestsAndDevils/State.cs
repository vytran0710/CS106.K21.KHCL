using System;
using System.Collections.Generic;
using System.Text;

namespace PriestsAndDevils
{
    class State
    {
        public int nP;
        public int nD;
        public bool side;
        public State prevState;
        public int stateLevel = 0;
        public void printState()
        {
            if(this.side==false)
            {
                Console.WriteLine(this.nP + "/" + this.nD + " " + "RIGHT" + " " + (3 - this.nP).ToString() + "/" + (3 - this.nD).ToString());
            }
            else
            {
                Console.WriteLine(this.nP + "/" + this.nD + " " + "LEFT" + " " + (3 - this.nP).ToString() + "/" + (3 - this.nD).ToString());
            }
        }
        public State(int nP, int nD, bool side, State prevState, int stateLevel)
        {
            this.nP = nP;
            this.nD = nD;
            this.side = side;
            this.prevState = prevState;
            this.stateLevel = stateLevel;
        }
    }
}
