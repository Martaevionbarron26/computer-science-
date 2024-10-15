# Creat a function called fre shipping
# that tells you if you quallify for free shipping
#you only get free shipping is at least 25$
#you are at least 18 years old or have parants consent
#your function should take four paramenters
#prime (bool) , cost (float) , age (int) , consent (bool)
#hihe hint
#you can use more than one logical operator in a condition
# use parethesis to grup if needed 


def Free_shipping(age, prime, money, consent):
    if age >=18 or consent == True and money <=25 or prime == True:
        print("Free shipping")


    else:
        print("No free shpping")