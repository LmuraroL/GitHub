secret_number = 777
print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Arrisca um palpite: "))
if number == secret_number:
    print("Acertou miseravi")
else:
    print("lascou-se")
while number != 777:
    number = int(input("Tenta novamente cabeção: "))
