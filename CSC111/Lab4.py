'''
Program:  lab4.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due:     9/19/2016
Written  9/19/2016

Program description: 
Program usage: <any special instructions>
'''
# Import statements go here
from math import *

# Constant declarations go here
gravity = 6.6726*10**-11 #N m^2/kg^2
mass_planet = 5.972*10**24
mass_satellite = 0.0
a = ((7917/2)*1.6093)*1000 #radious of earth in meters

'''
Function:  Main
Author:  Robert Crow
Function description: Calculating using time formula and outputs result

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):
    #variable declarations
    user_height = float(input("Enter orbit height above Earth, in miles: "))
    user_height = (user_height*1.6093)*1000
    orbit = sqrt(((4 * pi**2) / (gravity * mass_planet))*((a+user_height)**3))/60
    
    
    #function body
    print("The orbit period will be about %d.1"% orbit, " minutes")

#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE
if __name__ == '__main__':
    main()
