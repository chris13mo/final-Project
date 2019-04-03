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
    colors = open("CarSalesApplicationColor.txt", "r")
    color = colors.readlines()
    print ("We dont charge for the color")
    print (color)
    choiceColor = input("What color would you like? ")
    return choiceColor
    colors.close()

def vechical():
    vechical = ""
    vechicalBill = 0
    print ("You have your choice of three vechical types!")
    print(
        """
          1-Car - $8,000
          2-SUV - $10,000
          3-Truck - $12,000
          """
            )
    
    while vechical != 1 or vechical != 2 or vechical != 3:
        vechical = input ("What type of vechical would you like? ")
        if vechical == "1":
            bill = 8000
        elif vechical == "2":
            print ("Nice Choice!")
            vechicalBill = 10000
        elif vechical == "3":
            print ("A Truck Nice") 
            vechicalBill = 12000
        else:
            print("Please enter a valid choice")
            vechicalBill = input ("What type of vechical would you like? ")
        return  vechicalBill   

def engine():
    engineBill= ""
    while engine != 1 or enigne != 2 or engine != 3:
        print("How fast do you want to go??")
        print(
            """
        1- Small - $5,000
        2- Meduim - $7,000
        3- Large - $9,000
        """)
        engineChoice = input("What size engine do you want? ")
        if engineChoice == "1":
            print ("Well at least you will get good gas milage!")
            engineBill = int(5000)
        elif engineChoice == "2":
            print("Right in the middle good gas milage and power!")
            engineBill = int(7000)
        elif engineChoice == "3":
            print ("You better hold on to you pants!")
            engineBill = int(9000)
        else:
             engineChoice = input("Please enter a valid choice '1', '2', '3'")
        return  engineBill

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

    
   
    while choice != "1":
        print(
            """
            What would you like to do?
            0- Build your custom vechicle
            1- Exit
            """)
        choice = input("Choice: ")

        if choice == "0":
            
            vechicalBill = vechical()
            engineBill = engine()
            

            subTotal = vechicalBill + engineBill
            tax = subTotal* .0571
            total = subTotal + tax

            calRecipt(subTotal, tax, total)
            recipt=open("recipt.txt", "r" )
            print (recipt.read())
            recipt.close()

        elif choice == "1":
            break
            
        else:
            choice = input ("Please enter valid entry either '0' or '1': ")

    print ("Thank you for visting Car's the Right Way")
    print ("Have a nice day")

main()

input("\nPress the enter key to exit")



