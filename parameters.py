import math

#Mixer constants
MIXER_FACTOR = 1  #Increase or decrease the action of the mixer

MIXER_HEIGHT_PONDERATION = 0.3 #Controls the importance of height in the mixing process
MIXER_ROLL_PONDERATION   = 0.03 #Controls the importance of roll in the mixing process
MIXER_PITCH_PONDERATION  = 0.15 #Controls the importance of pitch in the mixing process

#INTRODUCE THE CONSTANTS FOR EACH PID CORRECTION

#HEIGHT
CTE_HEIGHT_PROPORTIONALITY= 0.2
CTE_HEIGHT_INTEGRATION= 0
CTE_HEIGHT_DERIVATION= 0.001

#PITCH
CTE_PITCH_PROPORTIONALITY= 0.2
CTE_PITCH_INTEGRATION= 0
CTE_PITCH_DERIVATION= 0.001

#ROLL
CTE_ROLL_PROPORTIONALITY=0.2
CTE_ROLL_INTEGRATION=0.01
CTE_ROLL_DERIVATION=0.001

######### PID Controller constants ##########

def MAX_FOIL_ANGLE ():
    MAX_FOIL_ANGLE = 20 #In degrees and respect the origin (whether it is 0 or 90)
    return MAX_FOIL_ANGLE 
   
    
def MIN_FOIL_ANGLE ():
    MIN_FOIL_ANGLE = -20 #In degrees and respect the origin (whether it is 0 or 90)
    return MIN_FOIL_ANGLE  #in real testing 0º equals 90º
    
def PID_HEIGHT_MIN_CORRECTION (simulator):
    PID_HEIGHT_MIN_CORRECTION = -300
    if simulator==True:
        return PID_HEIGHT_MIN_CORRECTION / 1000 #mm to m
    else:
        return PID_HEIGHT_MIN_CORRECTION  

def PID_HEIGHT_MAX_CORRECTION (simulator):
    PID_HEIGHT_MAX_CORRECTION =  300
    if simulator==True:
        return PID_HEIGHT_MAX_CORRECTION / 1000
    else:
        return PID_HEIGHT_MAX_CORRECTION  
    
def PID_PITCH_MIN_CORRECTION ():
    PID_PITCH_MIN_CORRECTION  = -15
    return float(PID_PITCH_MIN_CORRECTION*math.pi/180)
    

def PID_PITCH_MAX_CORRECTION ():
    PID_PITCH_MAX_CORRECTION  =  15 #degrees
    return float(PID_PITCH_MAX_CORRECTION*math.pi/180)
   
    
def PID_ROLL_MIN_CORRECTION ():
    PID_ROLL_MIN_CORRECTION   = -20
    return  float(PID_ROLL_MIN_CORRECTION * math.pi / 180)

def PID_ROLL_MAX_CORRECTION ():
    PID_ROLL_MAX_CORRECTION   =  20
    return float(PID_ROLL_MAX_CORRECTION * math.pi / 180)
    
    
def DESIRED_PITCH ():
    DESIRED_PITCH = 0.017
    return DESIRED_PITCH  #in real testing the neutral position for the foils is 90ª

def DESIRED_ROLL():
    DESIRED_ROLL = 0.017
    return DESIRED_ROLL  
    
def DESIRED_HEIGHT(simulator):
    DESIRED_HEIGHT = 500
    if simulator==True:
        return DESIRED_HEIGHT / 1000
    else:
        return DESIRED_HEIGHT 


