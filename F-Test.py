# Chris Davis
# Final Project
# Car Sales Application
# 4/1/2019

def introduction():
    print ("\t\tWelcome to Car's the Right Way")
    print ("\n\t\tHere we show all prices up front")
    print ("\t      You will know what you are paying for!")
    print ("\t   Go ahead and see why our way is the best way!")

def color(): 
    choiceColor = 0
    colors = open("CarSalesApplicationColor.txt", "r")
    #color = colors.readlines()
    print ("\nWe dont charge for the color")
    for color in colors:
        print (color)
    while choiceColor < 1 or choiceColor > 5:
        try:
            choiceColor = int(input("Enter the number of the color would you like? "))
        except:
            continue
        if choiceColor == 1:
            usersColor = str("Red")
        if choiceColor == 2:
            usersColor = str("Blue")
        if choiceColor == 3:
            usersColor = str("Green")
        if choiceColor == 4:
            usersColor = str("Grey")
        if choiceColor == 5:
            usersColor = str("Black")
        else:
            print ("Please enter a valid Choice, '1', '2', '3', '4', '5': ")

    return usersColor
    colors.close()


def vechical():
    vechical = 0
    vechicalBill = 0
    print ("You have your choice of three vechical types!")
    print(
        """
          1-Car - $8,000
          2-SUV - $10,000
          3-Truck - $12,000
          """
            )
    
    while vechical < 1 or vechical > 3:
        try:
            vechical = int(input ("What type of vechical would you like? "))
        except:
            continue
        if vechical == 1:
            vechicalBill = int(8000)
            vechicalChoice = str("Car")
        elif vechical == 2:
            print ("Nice Choice!")
            vechicalBill = int(10000)
            vechicalChoice = str("SUV")
        elif vechical == 3:
            print ("A Truck Nice") 
            vechicalBill == int(12000)
            vechicalChoice = str("Truck")
        else:
            print("Please enter a valid choice")
            #vechical = int(input ("What type of vechical would you like? "))
    return  vechicalChoice, vechicalBill   

def engine():
    engineBill= ""
    engineSize = ""
    engineChoice = 0

    while engineChoice < 1 or  engineChoice > 3:
        print("How fast do you want to go??")
        print(
            """
        1- Small - $5,000
        2- Meduim - $7,000
        3- Large - $9,000
        """)
        try:
            engineChoice = int(input("What size engine do you want? "))
        except:
            continue
        if engineChoice == 1:
            print ("Well at least you will get good gas milage!")
            engineBill = int(5000)
            engineSize = str("Small Engine")
        elif engineChoice == 2:
            print("Right in the middle good gas milage and power!")
            engineBill = int(7000)
            engineSize = str("Meduim Engine")
        elif engineChoice == 3:
            print ("You better hold on to your pants!")
            engineBill = int(9000)
            engineSize = str("Large Engine")
        else:
             print("Please enter a valid choice '1', '2', '3'")
    return  engineSize, engineBill

def calRecipt(subTotal, tax, total):
    recipt = open("recipt.txt", "w")
    recipt.write(str(subTotal) + "\n")
    recipt.write(str(tax) + "\n")
    recipt.write(str(total) + "\n")
    recipt.close()
    return recipt


        

      


def main():
    choice = 0

    introduction()
    vechicalBill= 0
    engineBill= 0
    engineSize = ""
    vechicalChoice= ""
    usersColor= ""

    
   
    while choice != "1":
        print(
            """
            What would you like to do?
            0- Build your custom vechicle
            1- Exit
            """)
        choice = input("Choice: ")

        if choice == "0":
            
            vechicalChoice, vechicalBill = vechical()
            engineSize, engineBill = engine()
            usersColor = color()
            

            subTotal = vechicalBill + engineBill
            tax = subTotal* .0571
            tax= float("%0.2f"%tax)
            total = subTotal + tax

            calRecipt(subTotal, tax, total)
            recipt=open("recipt.txt", "r" )
            print ("\nYour Vechical")
            print ("You choose: ", vechicalChoice)
            print ("You choose: ", engineSize)
            print ("You choose: ", usersColor)
            print ("Vechical Sub Total:", recipt.readline())
            print ("Tax:", recipt.readline())
            print ("Total:", recipt.readline())
            recipt.close()

        elif choice == "1":
            break
            
        else:
            choice = input ("Please enter valid entry either '0' or '1': ")

    print ("Thank you for visting Car's the Right Way")
    print ("Have a nice day")

main()

input("\nPress the enter key to exit")



