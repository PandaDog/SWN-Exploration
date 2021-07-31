__author__ = "Panda-Dog"
__version__ = 0.1
__copyright__ = "All Rights Reserved"
__email__ = "rgmckay@nevada.unr.edu"

# TODO
# 1. Change lists to a JSON file to ease editing
# 2  Create output macro to insert Roll20 of the events (Excluding encounters)
# 3  Enable unique party support, user supplies list of party names so output is more streamlined

##IMPORTS##
import sys
import os
import random
import math
import pprint
import json
import easygui


def loadJson(filepath):
    with open(filepath, 'r') as json_file:
        tmp = json_file.read()
        table = json.loads(tmp)
        return table
        # Example Macro &{template:default} {{name=Shift fires his gun!}} {{Laser Pistol:=[[d20+4]] vs AC}}  {{Damage:=[[1d6+1]]}}


def printJsonTable(table):
    print(json.dumps(table, indent=1))


def Generate_Roll20_Macro(message):
    print("&{template:default} {{" + message + "}}" + '\n')


def generateProblem():
    twist = random.choice(problems['problem']['twists'])
    restraint = random.choice(problems['problem']['restraints'])
    print(restraint + '. ' + twist)


def generatePatron():
    trust = random.choice(patrons['Trustworthiness'])
    challenge = random.choice(patrons['Challenge'])
    patronForce = random.choice(patrons['Force'])
    eager = random.choice(patrons['Eagerness'])
    reward = random.choice(patrons['Potential_Non-Cash_Rewards'])
    print(trust + ' ' + challenge + ' ' +
          patronForce + ' ' + eager + ' ' + reward)


def generatePlace():
    returnString = "Taco"
    return returnString


def generateUrbanEncounter():
    venue = random.choice(urbanEncounters['urbanEncounters']['generalVenue'])
    reasonInvolved = random.choice(
        urbanEncounters['urbanEncounters']['reasonInvolved'])
    eventNature = random.choice(
        urbanEncounters['urbanEncounters']['eventNature'])
    conflictReason = random.choice(
        urbanEncounters['urbanEncounters']['conflict'])
    atagonist = random.choice(urbanEncounters['urbanEncounters']['antagonist'])
    print(venue + ' ' + reasonInvolved + ' ' + eventNature +
          ' ' + conflictReason + ' ' + atagonist)


def generateWildEncounter():
    weather = random.choice(
        wildEncounters['wildernessEncounters']['weatherLighting'])
    nature = random.choice(
        wildEncounters['wildernessEncounters']['nature'])
    friend = random.choice(
        wildEncounters['wildernessEncounters']['friendlies'])
    ranges = random.choice(
        wildEncounters['wildernessEncounters']['range'])
    hostiles = random.choice(
        wildEncounters['wildernessEncounters']['hostiles'])
    print(weather + ' ' + nature + ' ' + friend +
          ' ' + ranges + ' ' + hostiles)


problems = loadJson("problem.json")
patrons = loadJson("patrons.json")
places = loadJson("places.json")
NPC = loadJson("npc.json")
wildEncounters = loadJson("wildernessEncounters.json")
urbanEncounters = loadJson("urbanEncounters.json")
conflictTypes = loadJson("conflictType.json")
simpleNPC = loadJson("onerollNPC.json")


def main():
    generateProblem()
    generatePatron()
    generateUrbanEncounter()
    generateWildEncounter()

    # If not importing. run main function
if __name__ == '__main__':
    main()
