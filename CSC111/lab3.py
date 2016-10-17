'''
Program:  lab3.py
Author:  Robert Crow
Class:   CSC 111
Instructor:  V Manes
Due:     9/12/2016
Written  9/12/2016

Program description: Amount of pizza and soda you need

Program usage: <any special instructions>
'''

# Import statements go here


# Constant declarations go here
slices_in_pizza = 8
oz_in_bottle = 64
strd_pizza_serv = 3 #slices
strd_soda_serv = 12 #ounces




#be sure to comment the code enough, but not too much
#there should be a comment for every group of lines that do a
#related task. The comment should be very brief


#YOU MUST HAVE A FUNCTION main( )
'''
Function:  Main
Author:  Robert Crow
Function description:  Calculates amount of pizza and soda you need depending how many people you have. then how many slices per person depending on amount of pizzas and sodas you get.

Parameters: <list inputs>

Return: <describe return value,if any>
'''
def main( ):

    #variable declarations


    #function body

    #Part A
    print("How many pizzas and bottles using standard servings")
    num_people = int(input("How many people at the meeting? "))
    amnt_pizzas = ((num_people * strd_pizza_serv) // slices_in_pizza) + 1
    amnt_bottles = ((num_people * strd_soda_serv) // oz_in_bottle) + 1
    print("For ", num_people, " you will need ", amnt_pizzas, " pizzas and ", amnt_bottles, " bottles of soda.\n")
    
    #Part B
    print("How many slices and ounces per person, set # pizzas & bottles")
    people = int(input("How many peple at the meeting? "))
    amnt_pizzas_slices = (int(input("How many pizzas? ")) * slices_in_pizza)
    amnt_bottles_oz = (int(input("How many bottles? ")) * oz_in_bottle)
    amnt_slices_per_person = amnt_pizzas_slices // people
    amnt_oz_per_person = amnt_bottles_oz // people
    
    print("Each person will get ", amnt_slices_per_person, " slices and ", amnt_oz_per_person, " ounces of soda.")
    amnt_pizzas_slices_left = amnt_pizzas_slices % people
    amnt_bottles_oz_left = amnt_bottles_oz % people
    print("There will be ", amnt_pizzas_slices_left, " slices of pizza left over and ", amnt_bottles_oz_left, "ounces of soda left over.")
    

#DO NOT DELETE THESE LINES, THEY MUST BE LAST LINES IN FILE           
if __name__ == '__main__':
    main()
