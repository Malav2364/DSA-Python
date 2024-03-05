# practical 3 
# generating random numbers with specified length

import random as rn
import string as str 
all_characters=str.ascii_letters+str.digits+str.punctuation
length=int(input("Enter the required length: "))

print("The password is: ",(''.join(rn.choices(all_characters,k=length))))