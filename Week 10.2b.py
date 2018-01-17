from CashRegister2 import *

def main():
    x=CashRegister2()
    price=None
    while price !="0":
        price=input("Enter the item price or type '0' to finish the list: ")
        if price != "0":
            if price.isalpha() != False:
                print()
                print("Only number or '0'. Try again.")
                print()
            else:
                price=float(price)
                x.addItem(price)

    print()

    print("Total price: ",x.getTotal())
    print("Total items: ",x.getCount())
    print()
    totalCash=0.0
    while totalCash<x.getTotal():
        totalCash=float(input("Enter the money amount: "))
        if totalCash<x.getTotal():
            print("Missing", (x.getTotal()-totalCash))
        else:
            if totalCash==x.getTotal():
                print("Good day")
            else:
                print("Here's the change: ",x.giveChange(totalCash))
                print("Good day")

main()
    

    
