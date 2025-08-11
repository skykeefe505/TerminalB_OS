import time
import sys
import os

#defs

def cls(): print ("\n" * 100)

def bootscreen(): 
    print("###################################")
    print("")
    print("")
    print("           TERMINALB OS            ")
    print("")
    print("")
    print("###################################")

def loadingfilesboot():
    print("TERMINALB IS LOADING FILES")

def loadingbar():
    print("[               ]")
    time.sleep(0.5)
    print("[##             ]")
    time.sleep(0.7)
    print("[####           ]")
    time.sleep(0.7)
    print("[#######        ]")
    time.sleep(0.7)
    print("[###########    ]")
    time.sleep(0.7)
    print("[###############]")


def mainsetup():
    cls()
    print("Welcome!")
    print("Would you like to dial into a BBS or ChatRoom?")
    time.sleep(0.5)
    print("WIP")
    
#main
bootscreen()
time.sleep(5)
loadingfilesboot()
time.sleep(1)
loadingbar()
cls()
mainsetup()
