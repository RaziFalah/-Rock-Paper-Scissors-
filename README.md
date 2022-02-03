#Rock-Paper-Scissors

<h1>About</h2>
A very basic program that can handle Rock-Paper-Scissors

<h1>Functionality</h1>

================<br /> 
|     Menu     |<br /> 
|  bot vs bot  |<br /> 
| human vs bot |<br /> 
|human vs human|<br /> 
================<br /> 

<h1>Tech</h1>

#In-program data:

```
["Rock", "Paper", "Scissors"]

```

#in-program imports

```
import os
from time import sleep
import random
from matplotlib.pyplot import draw
```

#Function 1
```
def BOTvsBOT():
    stuff = ["Rock", "Paper", "Scissors"]
    name_of_1 = input("The name of the first player: ")
    name_of_2 = input("The name of the second player: ")
    rand1 = random.choice(stuff)
    rand2 = random.choice(stuff)
    print(name_of_1 + ": " + rand1)
    sleep(1)
    print("Proccessing...")
    print(name_of_2 + ": " +  rand2)
```

#Function 2
```
def HUMANvsBOT():
    stuff = ["Rock", "Paper", "Scissors"]
    name_of_1 = input("The name of the first player: ")
    name_of_2 = "BOT(A.I)"
    ans = input("Pick your woepon: ")
    sleep(1)
    print("Proccessing...")
    print(name_of_2 + ": " +  random.choice(stuff))
```

#Function 3
```
    stuff = ["Rock", "Paper", "Scissors"]
    name_of_1 = input("The name of the first player: ")
    name_of_2 = input("The name of the second player: ")
    ans_of_1 = input(f"{name_of_1}: Pick your wopean: ")
    ans_of_2 = input(f"{name_of_2}: Pick your wopean: ")
    print(name_of_1 + ": " + ans_of_1)
    sleep(1)
    print("Proccessing...")
    print(name_of_2 + ": " +  ans_of_2)
```
    
#Menu manger
```

option = input("Select an option: ")
option = option.upper()
if(option == "BOT VS BOT"):
    BOTvsBOT()
elif(option == "HUMAN VS BOT"):
    HUMANvsBOT()
elif(option == "HUMAN VS HUMAN"):
    HUMANvsHUMAN()
else:
    print("Unkown choice, check you spells")
    
```
