#password generator
import random
def fun():
    len = int(input("Enter the length of your password:"))
    a = ('0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) _ + = . , > < ? /').split()
    print("".join(random.sample(a,len)))
fun()
again = input("Do you want to generate another password?(yes/no):")
while again!="no":
    fun()
    again = input("Do you want to generate another password?(yes/no):")
else:
    print("Thankyou")
