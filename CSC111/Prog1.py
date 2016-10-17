'''
Program:  prog1.py
Author:  Robet Crow
Class:   CSC 111
Instructor:  V Manes
Due:     10/28/2016
Written  9/26/2016

Program description: Calculates taxes depending on income and marital status

'''


'''
Function:  Main
Author:  Robert Crow
Function description:  Pulls values from funcutions and outputs them
'''
def main( ):

    #variable declarations
    
    #pulls the values you require later
    
    marital_status = get_status()
    income = get_income()
    tax_due = compute_tax(marital_status,income)
    
    #function body
    
    #prints the statements
    
    if marital_status == "S":
        marital_status = "Single"
    elif marital_status == "M":
        marital_status = "Married"
    print("Filing status: ", marital_status)
    print("Taxable income: $%.2f" %income)
    print("Tax due: $%.2f" %tax_due)
    
'''
Function:  get status()
Author:  Robert Crow
Function description:  Gets what your marital_status and checks for errors


Return: marital_status
'''
def get_status( ):
    
    #variable declarations
    
    x = 0
    
    #function body
    
    #while statement to give you 3 trys
    while x != 3:
        marital_status = input("Enter filing status (S - single, M - married): ")
        #adds one to x
        x += 1
        #puts the value to upper case and strips the white space
        marital_status = marital_status.upper()
        marital_status = marital_status.strip()
        #if statement to exit the while
        if marital_status == "S":
            break
        elif marital_status == "M":
            break
        #prints errors
        print("You entered ",marital_status, "which is not valid.")
    if marital_status != "M" and marital_status != "S":
        print("Only single or married filing status is accepted. Too many tries Program ending.")
        exit()    

    return marital_status


'''
Function:  Get_income()
Author:  Robert Crow
Function description:  Error checks and gets income


Return: income
'''
def get_income( ):
    
    #variable declarations
    x = 0
    income = 0
    #function body
    #loop for the three trys
    while x != 3:
        #try statement to make sure its a number
        try:
            income = float(input("Enter your Taxable Income: "))
        except:
            print("Invalid input")
        #adds one to x
        x += 1
        #checking if income is greater then 0
        if income > 0:
            break
        print("You must enter a number greater than 0.")
    if income <= 0:
        print("Income must be greater than 0. Too many attempts, program ending.")
        exit()
    
    return income

'''
Function:  compute_tax()
Author:  Robert Crow
Function description:  Calulates the taxes you need

Return: tax_due
'''
def compute_tax(marital_status, income):
    
    #variable declarations
    tax_due = 0

    #function body
    #checks if you are single and does the calculations for taxes
    if marital_status == "S":
        if income > 0 and income <= 8925:
            tax_due = income*.10
        elif income > 8925 and income <= 36250:
            tax_due = (8925*.10)+((income-8925)*.15)
        elif income > 36250 and income <= 87850:
            tax_due = (8925*.10)+((36250-8925)*.15)+((income-36250)*.25)
        elif income > 87850:
            #outputs and exits program
            print("You should consult a tax professional.")
            exit()
    #checks if you are marriged and does the calculations for taxes
    elif marital_status == "M":
        if income > 0 and income <= 17850:
            tax_due = income*.10
        elif income > 17850 and income <= 72500:
            tax_due = (17850*.10)+((income-17850)*.15)
        elif income > 72500 and income <= 146400:
            tax_due = (17850*.10)+((72500-17850)*.15)+((income-72500)*.25)
        elif income > 146400:
            #outputs and exits program
            print("You should consult a tax professional.")
            exit()
    return tax_due

    
#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
    main()
