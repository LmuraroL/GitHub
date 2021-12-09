year = int(input("Enter a year: "))

#
# Write your code here.
#
if year % 4 != 0:
    print("É um ano comum")

elif year % 100 != 0:
    print("É um ano bissexto")

elif year % 400 != 0:
    print("É um ano comum")

else:
    print("É um ano bissexto")
