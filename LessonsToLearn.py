
# Tapsa
#
# How is your day Mr Amigo or Miss Amigo?
#
# I hope it is as nice as mine.
# To use multi comment just select the lines you like and press
# TODO: Ctrl+/
# Ctrl+/ with Linux and Windows with PyCharm ... but it is not working with me
print("....................................")
print("Variable -lesson")

customer = "Lea M"
order = ["car", "train", "airplain"]
hisName = "Cristian"
herName = "Miss Robinson"
yearsToCome = 1 - 0.5
time = 5 * 12
enoughTime = 50 / 2

"""
This is by the way
multi lines comment
Do you agree?
"""
print("....................................")
print("Uot put printing and commenting -lesson")
print("Trick to check substring ...if Lea exists in customer: ", "Lea" in customer)
print("Trick to check substring ...if Lea does not exist in customer: ", "Lea" not in customer)

comment1 = "Bonjour, Tapio. " \
           "Comment, ca va? " \
           "Je va bien. Mercy." \
           " Et tu?"

comment2 = """
Bonjour, Tapio. Comment, ca va? Je va bien. Mercy. Et tu?
"""

comment10 = """
Bonjour, Tapio.
Comment, ca va?
Je va bien. Mercy.
Et tu?
"""

commentName = """
Bonjour, {}.
Comment, ca va?
Je va bien. Mercy.
Et tu?
"""

commentName2 = f"""
Bonjour, {herName}.
Comment, ca va?
Je va bien. Mercy.
Et tu?
J'est {56 + yearsToCome} ans.
"""

if comment1 == comment2:
    print("Both comments are same.")
else:
    print("Well there is something different, because comment1 and comment2 are not same.")

message = "Ready for certification." if time >= enoughTime else "Not ready for testing my learnings."
# Use only with one if and else statement
print("....................................")
print("Playing around with list's in built methods -lesson")
numberList = [1, 2, 3, 4, -1, -10, -100]
print("/n" + "Number in the numberList's position 6: ", numberList[5])
print()
numberListMod = [numberList, ["Pekka", "Tiina"]]  # But do not mix different datatypes if it is not a must.
print("Number in the numberListMod's position (0,1): ", numberListMod[0][1], " and name at position (1,1) is ",
      numberListMod[1][1])

numberList.reverse()
print("Reversed numberList: ", numberList)
numberList.append(-1000000)
numberList.sort()
print("1. added and sorted numberList: ", numberList)
numberList.append(105)
numberList.sort()
print("2. added and sorted numberList: ", numberList)
numberList.remove(-1000000)
numberList.pop()
print("3. The second numberList above is modified by removing -1000 000 and last element of list: ", numberList)
del numberList[0:5]  # The sixth position is not removed.
print(
    "4. The third numberList above is modified by removing range 0 to 5, but (not element in position 5 of the list witch is the 6th element) of numberList: ",
    numberList)
print("....................................")
print("Comparing list and dictonary. Dictonary features  -lesson")
# Comparison of list and sets. Sets are not ordered and no dubblicated.
print()
numberListNew = [1, 1]
numberListSet = {1, 1}
lettersSet = {"A", "B", "B", "C", "C", "C"}
print("numberListNew: ", numberListNew)
print("numberListSet: ", numberListSet)
print("lettersSet: ", lettersSet)
# Union with sets
letterASet = {"A", "B", "C", "D"}
letterBSet = {"E", "F"}
union = letterASet | letterBSet
print(f"union {union}")
# intersection
letterAModSet = letterASet.add("G")
letterASet.add("H")
print(f"lettersASet = {letterASet}")
print(f"lettersAModSet = {letterAModSet}" + " ... No use to do like this...!")

letterBSet.add("G")
print(f"letterBSet = {letterBSet}")
# intersection = letterBMod & letterBMod
intersection = letterASet & letterBSet
print(f"intersection {intersection}")
print()
differenceAB = letterASet - letterBSet
differenceBA = letterBSet - letterASet
print(f"differenceAB: {differenceAB}")
print(f"differenceAB = {differenceBA}")
print()
print(comment1)
print(comment2)
print("Is it this feature you are looking for?")
print(comment10)
print(commentName.format(hisName))
print(commentName2)
print("....................................")
print("Dictionary -lesson")
# Dictonary is key and value paired structure.
person = {
    "name": "Tapsa",
    "age": "Still going strong ... Feel still young enough",
    "weight": "Not weighted in the maternity clinic."
}

print(f"keys of person: {person.keys()}")
print(f"value of person {person.values()}")
person["age"] = "Living the better half of my life."

print("The age of person: ", person.get("age"))
print(f"value of person {person.values()}")
print("....................................")
# for -loop
print("For loop with list and dictonary -lesson")
family = ["Nike", "Jean", "Tapi", "Mika"]
familySet = {"Nike2", "Jean2", "Tapi2", "Mika2"}
print("All family members in their own line, s'il vous plan.")
for member in family:
    print(member)
print()
print("""Same works also in the dictionary. See if you do not agree with me.
Do not forget that dictionary is not ordered in specific order. Did you forget that?
""")
for member in familySet:
    print(member)
print(" Mercy, boucoup or something similar.")
print("....................................")
# for loop with dictionary
print("Here is person dictionary to be printed out with 'for loop' for only You. lesson")
for key in person:
    print(f"key: {key} and value: {person[key]}")
print()
print("The another way to for loop dictionary for you and me.")
for key, value in person.items():
    print(f"key: {key} and value: {value}")
print()
print(person.items())
print("....................................")
print("Functions -lesson")

def timesEng() -> list:
    return ["spring", "summer", "autumn", "winter"]


def timesFra() -> list:
    return ["printemps", "ètè", "oauoumme", "hiver"]


def numberVarable():
    age = 100
    print(age)

print("....................................")
print("Comparing different kind of variables with inbuild type() function  -lesson")
customAverageAge = 57

isNewCustomer = True
cashOfYear = 10000.50

numberVarable()

print(customer)
print(type(customer))

print(order)
print(type(order))

print(customAverageAge)
print(type(customAverageAge))

print(isNewCustomer)
print(type(isNewCustomer))

print(yearsToCome)
print(type(yearsToCome))
print(cashOfYear)
print(type(cashOfYear))

print(timesEng())
print(timesFra())

print(message)
print("....................................")
numbersToAdd = [1, 23, 4535, 56, 3, 56, 100]
sum = 0
for number in numbersToAdd:
    sum += number
print(f"The sum of all numbers in the list numbersToAdd is {sum}")
print(f"sum: {sum}")
print("....................................")
# while -loop
print("The philosofy of while loop -lesson")
numberX = 0
while numberX < 10:
    numberX += 1
    print(numberX, " round")
else:
    print("While -loop ended.")
print()
numberX = 0
while numberX < 10:
    if numberX == 5:
        break
    numberX += 1
    print(numberX, " round")
print()
print("While -loop & continue")
numberZ = 0
while numberZ < 10:
    numberZ += 1
    if numberZ < 5:
        continue
    print(numberZ, " round")
print("....................................")
print("continue & brake -lesson")
numberXY = [1,2,3,4,5,6,7,8,9,10,11,12]
for number in numberXY:
    if number <= 3:
        print(f"3 first numbers are {number}")
    if number < 6:
        continue
    if number >= 6 & (number < 10):
        if number < 10:
            print(f"number between 6-9: {number}")
    if number == 11:
        print(f"Bye bye with number = {number}")
        break
print("....................................")
print("How to build up and use functions -lesson")
def greet(name, age=-1):
    print(f"Hello {name}, how are you?")
    if age >= 0:
        print(f"I know that your age is {age}")
    print("...A bianto...")
greet("Tapsa" )
greet("Mika",34)

name = "Tapsa"
personAge = 56
personGender = "m"
def is_adult(age):
    return age > 16

def genderConventer(gender:str, age):
    if gender.upper() == "M":
        if is_adult(age):
            return "Male"
        else:
            return "Boy"
    elif gender.upper() == "F":
        if is_adult(age):
            return "Female"
        else:
            return "Girl"
    else:
        return (f"'{gender}'-gendre is unknown and s(he) is {age} years.")

print(f"{name}: {genderConventer(personGender, personAge)}")
name = "Lea"
personAge = 60
personGender = "f"
print(f"{name}: {genderConventer(personGender, personAge)}")
name = "Piia"
personAge = 3
personGender = "f"
print(f"{name}: {genderConventer(personGender, personAge)}")
name = "Vertti"
personAge = 12
personGender = "Cat"
print(f"{name}: {genderConventer(personGender, personAge)}")

print("...................................")
# How to pick up just a few specific functions out of big library
# import math
print("Import the whole pakage or just a needed functions -lesson")
from math import isqrt
from math import floor, ceil, pow
print(isqrt(250))
print(isqrt(260))
print(floor(234.5))
print(floor(234.95))
print(ceil(234.95))
print(pow(2,8))
print("....................................")
# Now we check how to create functions and use them in another file
print("Let's import our own functions to in use another file. Right? -lesson")
import calulator

number1 = 203
number2 = 3
print(f"number1 is {number1}")
print(f"number2 is {number2}")
print(f"Adding number1 and number2: {calulator.add(number1, number2)}")
print(f"Subtracting number1 and number2: {calulator.subtrack(number1, number2)}")
print(f"Diving number1 and number2: {calulator.divide(number1, number2)}")
print(f"Multiplying number1 and number2: {calulator.multiply(number1, number2)}")
print(f"Powering number1 and number2: {calulator.power(number1, number2)}")
print("....................................")
# Let's create phone class for studing purpose
print("This is phone class example. -lesson")

class Phone:

    def __init__(self, modele, price):
        self.modele = modele
        self.price = price

    def call(self,number):
        print(f"{self.modele} -phone is calling ... {number}")

    def __str__(self):
        return f"modele = {self.modele}\nprice = {self.price}"

    # <__main__.Phone object at 0x0000026DEA616220> -> modele = Iphone +7 price = 1200

iphone = Phone("Iphone +7", 1200)
samsung = Phone("Samsung S20", 670)

iphone.call("358")

print(iphone.modele)
print(iphone.price)
iphone.call("5402454724")

print()

samsung.call("001")
print(samsung.modele)
print(samsung.price)
samsung.call("54024547440")

print()
print("iphone:")
print(iphone)
print("samsung:")
print(samsung)
print("....................................")
# Have you heard that practicing make champions?
import alphapet

#albhas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
changeWord = "peace"

# First try
#changeString = ""
#for albha in changeWord:
#    orderNumber = albhas.index(albha)
#    print(f"{alphapet.albhaChange(albha)}")

# Second try
#changeString = ""
#for albha in changeWord:
 #   print(albha)
  #  albhaChange: albhaTemp = albhaChange(albha)
   # print(f"{albhaTemp.alphaNumber2(albha)}")

# Some difficulties with me... You know, do you? Just check some help out of web like in url:
# https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python

# Third try
def changeFormat(word):
    changeString = ""
    for albha in word:
        orderNumber = ord(albha.lower())-ord("a")
        if orderNumber < 10:
            changeString = changeString + str(orderNumber)
        while orderNumber >= 10:
            orderNumber -= 10
            if orderNumber < 10:
                changeString = changeString + str(orderNumber)
    return(changeString)

changeWord1 = "peaceForMe"
changeWord2 = "peaceForYou"
changeWord3 = "o"

yourNumer = changeFormat(changeWord2)
print(f"Your number is {yourNumer}")
myNumer = changeFormat(changeWord1)
print(f"My number is   {myNumer}")
tempNumer = changeFormat(changeWord3)
print(f"Temp number is {tempNumer}")

#print(changeString)
print("....................................")
print("Date and time -lesson")
import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())

# I could also use neater solution like this one
from datetime import datetime
from datetime import date
print("\nHmmmmm.........")
print(datetime.now())
print("Today is",datetime.now().day)
print("This mount is",datetime.now().month)
print("How fast years go. This year is",datetime.now().year)
print(date.today())
print(datetime.now().time())
print("....................................")
print("This is about formating time and date  -lesson")
now = datetime.now()
print(f"now: {now}")
nowMod = now.strftime("%d %m %Y %H %M %S")
print(f"nowMod: {nowMod}")
nowMod2 = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"nowMod2: {nowMod2}")
nowMod3 = now.strftime("%d-%m-%Y %H:%M:%S")
print(f"nowMod3: {nowMod3}")
nowMod4 = now.strftime("%d-%B-%Y %H:%M:%S")
print(f"nowMod4: {nowMod4}")
nowMod5 = now.strftime("%d-%b-%Y %H:%M:%S")
print(f"nowMod5: {nowMod5}")

date1 = date.today().strftime("%d %m %Y")
print(f"date1: {date1}")
date2 = date.today().strftime("%d-%B-%Y")
print(f"date2: {date2}")

print("....................................")
print("playing around with files -lesson\n"
      "w for writting\n"
      "r for reading\n"
      "r+ for reading and writing\n"
      "a for appending\n")
file = open("./data.cvs", "w")
file = open("./data.cvs", "r+")
file.write("\nid,name,email\n")
file.write("1,Caroline,caroline@gmail.com\n")
file.write("2,Cabriel,cabriel@hotmail.com\n")
file.close()
file = open("./data.cvs", "a")
file.write("3,Jore,jore@gmail.com\n")
file.close()
print("....................................")
print("Reading from file -lesson")
file = open("./data.cvs", "r")
print("Let's read what is inside the file:",file.read())
file.close()
print("   ***   ***   ***   ")
file = open("./data.cvs", "r")
for line in file:
    print(line)
file.close()
print("   ***   ***   ***   ")
file = open("./data.cvs", "r")
print(file.readlines())
file.close()
print("   ***   ***   ***   ")
print("....................................")
print("Better structure with automated file closening to read and write files -lesson")
import os.path
filename = "data.cvs"  # same as ./data.cvs
if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"No such filename: {filename} exist.")
print("....................................")
print("Fetch data out of url address -lesson")
from urllib import request
r = request.urlopen("http://www.google.com")
# var = r.getcode() # TODO: I do not know why ... I can not get the methods
print(f"Status code of request r: {r.getcode()}")
print(f"Content of request r: {r.read()}")
# Some html -stuff... this time.
print("....................................")
print("Have a fun and read ten random jokes my friend -lesson")
#from urllib import request
url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(f"Status code of request r: {r.getcode()}")
print(f"Content of request r: {r.read()}")
print("   ***   ***   ***   \n Hmmmmmmmmmmmm1...")
#from urllib import request
url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(f"Status code of request r: {r.getcode()}")
print(f"Content of request r: {r.read()}")
print("   ***   ***   ***   \n Hmmmmmmmmmmmm2...")
#from urllib import request
import json
url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(f"Status code of request r: {r.getcode()}")
data = r.read()
jsonData = json.loads(data)
print(f"Content of request r: {jsonData}")

class Joke:

    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f"setup: {self.setup} punchline: {self.punchline}"

jokes = []

for js in jsonData:
    setup = js["setup"]
    punchline = js["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"\nThe length of jokes: {len(jokes)}\n")

for joke in jokes:
    print(joke)
print("....................................")
print("After installing requests with terminal and command 'pip3 install request' -lesson")
import requests
#import json
url = "https://official-joke-api.appspot.com/random_ten"

response = requests.get(url)
print(f"Status code of response: {response.status_code}")   # TODO:{response.status_code()}

jsonData = json.loads(response.text)                        # TODO:response.text()
print(f"Content of jsonData: {jsonData}")

jokes2 = []

for js in jsonData:
    setup = js["setup"]
    punchline = js["punchline"]
    joke = Joke(setup, punchline)
    jokes2.append(joke)

print(f"\nThe length of jokes: {len(jokes)}\n")

for joke in jokes2:
    print(joke)

print("....................................")
import pyttsx3
for joke in jokes2:
    print(joke)
# TODO:   pyttsx3.speak("It's rocks")
#    pyttsx3.speak("Setup")
#    pyttsx3.speak(joke.setup)
#    pyttsx3.speak("Answer")
#    pyttsx3.speak(joke.punchline)
print("Well, reading aloud text to speech did not work for me. I do have finnish keyboard but I am using english language. Very long traceback message was given to me and it started with followng lines in the comment.")
"""
Traceback (most recent call last):
  File "C:\Users\Omistaja\PycharmProjects\learPythonProject\venv\lib\site-packages\pyttsx3\__init__.py", line 20, in init
    eng = _activeEngines[driverName]
  File "C:\Users\Omistaja\Softa\Python\lib\weakref.py", line 131, in __getitem__
    o = self.data[key]()
KeyError: None
"""


print("Make text to speech -lesson")
print("....................................")
print("....................................")


