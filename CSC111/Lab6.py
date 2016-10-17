'''
Program:  Lab6.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due: 10/10/2016
Written  10/5/2016

Program description: Random position of space invader trying to hit it

Program usage: Normal
'''

# Import statements go here
from math import *
from random import *

# Constant declarations go here

'''
Function:  Main
Author:  Robert Crow
Function description: 
'''
def main( ):

    #variable declarations

    #introduction
    print( "Space Defender" )
    ship_x, ship_y = get_invader()
    shot_angle, shot_range = get_shot()
    if not verify_shot(shot_angle, shot_range):
        return
    shot_x,shot_y = compute_shot(shot_angle, shot_range)
    display_result(shot_x, shot_y, ship_x, ship_y)
        
'''
Function:  Get_invader
Author:  Robert Crow
Function description:  gets a random position for ship_x and y and outputs it

Return: ship_x and ship_y
'''
def get_invader( ):
    #variable declarations
    ship_x = 0
    ship_y = 0

    #function body
    seed(0)
    
    #place space invader x = +/- 20, y =1-20
    ship_x = randint( -20, 20 )
    ship_y = randint( 1, 20 )
    print( "Invading ship is at (%d, %d)" % ( ship_x, ship_y ))    

    return  ship_x, ship_y #if needed

'''
Function:  Get_shot
Author:  Robert Crow
Function description:  prompts for angle and range

Return: shot_angle and shot_range
'''
def get_shot( ):
    #variable declarations
    shot_angle = 0
    shot_range = 0

    #function body
    #get defender shot angle and range
    shot_angle = float( input( "Shot angle (180 - 0 ): " ) )
    shot_range = float( input( "Shot range ( 1 to 30 ): " ) )
    

    return shot_angle, shot_range  #if needed

'''
Function:  verify_shot
Author:  Robert Crow
Function description:  vertifing if the shot

Parameters: shot_angle and shot_range

'''
def verify_shot( shot_angle, shot_range):
    #variable declarations
    
    #function body
    #check user input, exit on error, otherwise compute x,y
    if( shot_angle > 180 ):
        print( "You're shooting in the ground to the left!" )
        return False
    elif (shot_angle < 0 ):
        print( "You're shooting in the ground to the right." )
        return False
    elif shot_range > 30:
        print( "Your weapon doesn't reach that far." )
        return False
    else:
        return True
        
'''
Function:  Comput_shot
Author:  Robert Crow
Function description:  does the calculations for shot x and y

parmenter:shot_range, shot_angle

Return: shot_x and shot_y
'''
def compute_shot(shot_range, shot_angle):
    #variable declarations
    shot_x = 0
    shot_y = 0

    #function body
    shot_x = shot_range * cos( radians( shot_angle ) )
    shot_y = shot_range * sin( radians( shot_angle ) )
    

    return (shot_x, shot_y) #if needed

'''
Function:  Display_result
Author:  Robert Crow
Function description:  checks if its hit and outputs right message

parameter: shot_x and shot_y
'''
def display_result(shot_x, shot_y, ship_x, ship_y):
    #variable declarations
    kill_radius = 1;

    #function body
    
    #show x,y for debugging/testing
    print( "Shot at %.1lf  %.1lf " % (shot_x, shot_y ) )

    #check hit status
    if abs( shot_x - ship_x ) < kill_radius:
        if abs( shot_y - ship_y ) < kill_radius:
            print( "You hit it! The enemy is destroyed" )
        elif shot_y < ship_y:
            if shot_y > ship_y - 2 * kill_radius:
                print( "You damaged the enemy ship" )
            else:
                print( "You missed. Better luck next time." )
    else:
        print( "You missed. Better luck next time." )


#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE
if __name__ == '__main__':
    main()
