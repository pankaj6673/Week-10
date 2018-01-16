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

   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

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
    print("Deleting the list...")
    print()
    x.clear()
    if x.getCount() == 0:
        print("List deleted.")

main()
    
