# Chris Davis
# Final Project
# Car Sales Application
# 4/1/2019

def introduction():
    print ("\t\tWelcome to Car's the Right Way")
    print ("\t\t\\n Here we show all prices up front")
    print ("\t\tYou will know what you are paying for!")
    print ("\t\tGo ahead and see why our way is the best way!")

def color():
    colors = open("CarSalesApplicationColor.txt", "r")
    color = colors.readlines()
    print ("We dont charge for the color")
    print (color)
    choiceColor = input("What color would you like? ")
    return choiceColor
    colors.close()

def vechical(vechical,vechicalBill):
    vechical()
    vechicalBill()
    print ("You have your choice of three vechical types!"
    print ("
    1-Car - $8,000
    2-SUV - $10,000
    3-Truck - $12,000
    ")
    vechical = input (int("What type of vechical would you like? "))
    while vechical != "1" or vechical != "2" or vechical != "3":
        if vechical == "1":
            bill = 8,000
        elif vechical == "2":
            print ("Nice Choice!")
            vechicalBill = 10,000
        elif vechical == "3":
            print ("A Truck Nice") 
            vechicalBill = 12,000
        else:
            print("Please enter a valid choioce")
            vechicalBill = input (int("What type of vechical would you like? "))
    return vechical, vechicalBill   

def engine(engineChoice, engineBill):
    engineChoice()
    engineBill()
    while engine != "1" or enigne != "2" or engine != "3":
        print("How fast do you want to go??")
        print("
        1- Small - $5,000
        2- Meduim - $7,000
        3- Large - $9,000
        ")
        engineChoice = input(int("What size engine do you want? "))
        if engineChoice == "1":
            print ("Well at least you will get good gas milage!")
            engineBill = 5,000
        elif engineChoice == "2":
            print("Right in the middle good gas milage and power!")
            engineBill = 7,000
        elif engineChoice == "3":
            print ("You better hold on to you pants!")
            engineBill == 9,000
        return engineChoice, engineBill

def recipt(subTotal, tax, total)
recipt = open("recipt.txt", "w")
recipt.write(subTotal)
recipt.write(tax)
recipt.write(total)
return recipt


        

      


def main():
    




    while choice != 3:
        print(
            "What would you like to do?
            0- Build your custom vechicle
            1- Exit")
            choice = input(int("Choice: "))

        if choice == "1":
            def introduction():
            def vechical(vechical,vechicalBill):
            def engine(engineChoice, engineBill):

            subTotal = vechicalBill + engineBill
            tax = subTotal* .0571
            total = subTotal + tax

            def recipt(subTotal, tax, total)
            print (recipt)

        else:
            print ("Thank you for visting Car's the Right Way")
            print ("Have a nice day")

main()

input("\nPress the enter key to exit")