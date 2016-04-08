# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    Num_Init_Timesteps = 150
    Num_Final_Timesteps = 150
    
    #for Num_Init_Timesteps, plot_position in [ (300,221), (150,223), (75,222), (0,224)]:
    for numViruses, plot_position in [ (20,311), (100,312), (500,313)]:

        pylab.subplot(plot_position)
        simulationWithDrug(numViruses, maxPop=1000, maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False}, \
                        mutProb=0.005, numTrials=numTrials, Num_Init_Timesteps=Num_Init_Timesteps, Num_Final_Timesteps=Num_Final_Timesteps)
        
    pylab.show()    
    
#simulationDelayedTreatment(200)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    Num_Init_Timesteps = 150
    Num_Final_Timesteps = 150
    
    for Num_Interim_Timesteps, plot_position in [ (300,221), (150,222), (75,223), (0,224)]:

        pylab.subplot(plot_position)
        simulationWithDrug(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05, \
                        resistances={'guttagonol': False, 'grimpex': False}, mutProb=0.005, numTrials=numTrials, \
                        Num_Init_Timesteps=Num_Init_Timesteps, Num_Interim_Timesteps=Num_Interim_Timesteps, \
                        Num_Final_Timesteps=Num_Final_Timesteps)
        
    pylab.show()    
    
simulationTwoDrugsDelayedTreatment(200)