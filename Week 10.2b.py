class CashRegister :
   
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
   
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   
   def getTotal(self) :
      return self._totalPrice

   def getCount(self) :
      return self._itemCount

   def giveChange(self,totalCash) :
        return (totalCash-self.getTotal())

def main():
    x=CashRegister()
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
    

    
