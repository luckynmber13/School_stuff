'''
Program:  HW5.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due:     10/3/2016
Written  9/28/2016

Program description: Sees if sphere will fit in cube
'''
# Import statements go here
from math import *

# Constant declarations go here


'''
Function:  Main
Author:  Robert Crow
Function description: takes inputs from user and calculates that radius and sees if it will fit in the cube from a given cube side length
'''
def main( ):
    #variable declarations
    #takes input and converts it to positive in case someone puts in a negative number
    volume = abs(float(input("Enter sphere volume: ")))
    length_cube = abs(float(input("Enter cube side length: ")))
    #Calculations
    radius = (3*(volume)/(4*pi))**(1/3)
    diameter = radius * 2
    volume_cube = length_cube**3
    
    #function body
    #finds the percent of it
    percent = (diameter/length_cube)*100
    #if statement to figure out where it goes
    if percent <= 101 and percent >= 99:
        print("Perfect Fit")
    elif percent < 99 and percent > 85:
        print("Loose Fit")
    elif percent <= 85:
        print("Bouncing around inside")
    elif volume <= volume_cube:
        print("Modified Fit")
    else:
        print("Doesn't Fit")
    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE
if __name__ == '__main__':
    main()
