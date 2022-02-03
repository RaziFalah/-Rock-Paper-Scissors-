#Made by Razi Falah
#Copyright (C) 2022 razifalah.com
#https://razifalah.com
#According to the applied license: LICENSE GNU General Public License v3.0
#You do not have the right to republish sell or edit this project, use it only for private use or educational purposes
import os
from time import sleep
import random

from matplotlib.pyplot import draw

print("==========================================")
print("Welcome to Rock, Paper, Scissors in python")
print("By Razi Falah:)                           ")
print("==========================================")
print("GAME IS LOADING...                        ")
sleep(2)
os.system('clear')

print("================")
print("|     Menu     |")
print("|  bot vs bot  |")
print("| human vs bot |")
print("|human vs human|")
print("================")


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

def HUMANvsBOT():
    stuff = ["Rock", "Paper", "Scissors"]
    name_of_1 = input("The name of the first player: ")
    name_of_2 = "BOT(A.I)"
    ans = input("Pick your woepon: ")
    sleep(1)
    print("Proccessing...")
    print(name_of_2 + ": " +  random.choice(stuff))

def HUMANvsHUMAN():
    stuff = ["Rock", "Paper", "Scissors"]
    name_of_1 = input("The name of the first player: ")
    name_of_2 = input("The name of the second player: ")
    ans_of_1 = input(f"{name_of_1}: Pick your wopean: ")
    ans_of_2 = input(f"{name_of_2}: Pick your wopean: ")
    print(name_of_1 + ": " + ans_of_1)
    sleep(1)
    print("Proccessing...")
    print(name_of_2 + ": " +  ans_of_2)

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




