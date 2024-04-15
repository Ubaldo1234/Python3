import re

texto = "Encuentra la palabra free para un descuento"
x=re.search("free",texto)
print(x)


#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
