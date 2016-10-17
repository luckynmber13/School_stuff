'''
Program:  HW3a.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due:     9/19/2016
Written  9/14/2016

Program description: Math equations with 2 user inputted values

Program usage: <any special instructions>
'''

'''
Function:  Main
Author:  Robert Crow
Function description: Calculates and outputs the calculations

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):
    #variable declarations
    user_value1 = float(input("First number: "))
    user_value2 = float(input("Second number: "))
    

    #function body
    print(user_value1," + ",user_value2," = ", (user_value1 + user_value2))
    print(user_value1," - ",user_value2," = ", (user_value1 - user_value2))
    print(user_value2," - ",user_value1," = ", (user_value2 - user_value1))
    print(user_value1," * ",user_value2," = ", (user_value1 * user_value2))
    print(user_value1," / ",user_value2," = ", (user_value1 / user_value2))
    print(user_value2," / ",user_value1," = ", (user_value2 / user_value1))
    print(user_value1,"^",user_value2," = ", (user_value1 ** user_value2))
    print("Integer division and modulus")
    print(user_value1," / ",user_value2," = ", int((user_value1 / user_value2)))
    print(user_value2," / ",user_value1," = ", int((user_value2 / user_value1)))
    print(user_value1," % ",user_value2," = ", int((user_value1 % user_value2)))
    print(user_value2," % ",user_value1," = ", int((user_value2 % user_value1)))
    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE
if __name__ == '__main__':
    main()
