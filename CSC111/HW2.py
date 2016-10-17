'''
Program:  HW2.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due:     9/12/2016
Written  9/7/2016

Program description: How much rice the ruler will have t pay the humble man 

Program usage: <any special instructions>
'''

# Constant declarations go here
amnt_of_rice = 2**64 - 1
rice_in_a_ton = 32000000
feet_in_a_mile = 5280
car_capacity = 100 #In Tons
len_of_train_car = 65 #Feet


'''
Function:  Main
Author:  Robert Crow
Function description: Calculates and outputs the calculations

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):
    #variable declarations
    rice_in_tons = amnt_of_rice // rice_in_a_ton
    amnt_of_train_cars = rice_in_tons // car_capacity
    train_len_feet = len_of_train_car * amnt_of_train_cars
    train_len_miles = train_len_feet // feet_in_a_mile

    #function body
    print("The total number of rice grains is: %.4e" % amnt_of_rice)
    print("That equals %.4e" % rice_in_tons)
    print(("It will take %.4e" % amnt_of_train_cars) + " train cars.")
    print(("The train's length will be %.4e" % train_len_miles)+ " mile.")

    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
   main()
