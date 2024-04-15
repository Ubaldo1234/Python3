quantity = 3
itemno = 567
price = 49

myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print(f"I want {quantity} pieces of item number {itemno} for {price:.2f} dollars.")