#!/usr/bin/env python
import random

def Air_Pressures():
    #Conversion from digital voltage readout to corresponding pressure
    
    """
    PFactor = 3
    Press_one = one*PFactor
    Press_two = two*PFactor
    Press_three = three*PFactor
    Press_four = four*PFactor
    
    return(Press_one, Press_two, Press_three, Press_four)
    """
    
    P_one = random.randint(0,5) + 10
    P_two = random.randint(0,5) + 20
    P_three = random.randint(0,5) + 30
    P_four = random.randint(0,5) + 40
    A_Pressures = [P_one, P_two, P_three, P_four]
    
    return(A_Pressures)

def Oil_Fuel(five, six, seven):
    #Conversion from digital voltage readout to corresponding oil pressure, oil temperature, and fuel level
    
    
    """
    OPFactor = 5        #Oil Pressure Factor
    OTemp_Factor = 6    #Oil Temp Factor
    FLevel_Factor = 7   #Fuel Level Factor
  
    return(O_Pressure, O_Temp, F_Level)
    """
    
    OPress = random.randint(0,5) + 50
    OTemp = random.randint(0,5) + 60
    FLevel = random.randint(0,5) + 70

    return(OPress, OTemp, FLevel)

def Speed_Tach():
    """
    S_Factor = 8
    T_Factor = 9
    return(Speed, Tach)
    """
    
    Speed = random.randint(0,5) + 80
    Tach = random.randint(0,5) + 90
    
    return(Speed, Tach)
    
