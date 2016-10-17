'''
Program:  HW4.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due:     9/26/2016
Written  9/21/2016

Program description: Figures out policy info depending age and gender and Marital status
Program usage: <any special instructions>
'''

'''
Function:  Main
Author:  Robert Crow
Function description: if statements to check what discount someone recieves

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):
    #variable declarations
    
    
    #function body
    print("Hardrocker Insurace Calculator")
    print("Enter the policy information below")
    gender = input("Your gender? (m or f): ")
    marital_status = input("Marital status? (s or m): ")
    age = int(input("Age?: "))
    policy = float(input("Policy base rate: $"))
    if gender == "f" and age > 20 and marital_status == "s":
        discount = (policy*.15)
        policy -= discount
    elif gender == "f" and marital_status == "m":
        discount = (policy*.25)
        policy -= discount
    elif gender == "m" and age > 25 and marital_status == "s":
        discount = (policy*.15)
        policy -= discount
    elif gender == "m" and marital_status == "m":
        discount = (policy*.20)
        policy -= discount
    else:
        discount = 0.0        
    print("You received a discount of $%.2f"% discount, ", making your total premium $%.2f" %policy)
    
          
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE
if __name__ == '__main__':
    main()
