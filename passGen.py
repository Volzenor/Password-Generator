#Import libraries
import random

#Define chars and set variables based on user input
chars = "qwertyuopasdfghjklizxcvbnm.!'^+%&/()=?_-+/*<>@¨~:.;1234567890"
keyword = str(input("Please enter a keyword: "))
length = int(input("Please enter the length of the password: "))

#Randomize keywords characters lower-upper conditions
keyword = list(keyword.lower()) 
for index,letter in enumerate(keyword):
    chance = random.randint(0,1)
    if chance == 1:
        keyword[index] = letter.upper()
keyword = "".join(keyword)

#If the keywords longer than the user inputed length cuts off some of it and sets it as password
if len(keyword) > length:
    password = keyword[:length]

#If the keywords the same length as the user inputed length sets it as password
elif len(keyword) == length:
    password = keyword

else:
    #Creates a string with the needed length
    length -= len(keyword)
    password = ""
    for i in range(length):
        password += random.choice(chars)

    #Chooses a random index to insert the keyword into than inserts
    keywordIdx = random.randint(0,len(password))
    password = list(password)
    password.insert(keywordIdx,keyword)
    password = "".join(password)

#Read it to learn what it does
print("Your generated password is: "+password)
