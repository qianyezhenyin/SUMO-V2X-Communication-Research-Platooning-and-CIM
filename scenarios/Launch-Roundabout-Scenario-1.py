import os
import sys
import traci
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.simlib import setUpSimulation

setUpSimulation("../maps/A13NorthCircularRoundabout/A13NorthCircularRoundabout.sumocfg", 1)
step = 0
while step < 5000:
    traci.simulationStep()
    step += 1

traci.close()
