__author__ = "Panda-Dog"
__version__ = 0.1
__copyright__ = "All Rights Reserved"
__email__ = "rgmckay@nevada.unr.edu"

# TODO
# 1. Change lists to a JSON file to ease editing
# 2  Create output macro to insert Roll20 of the events (Excluding encounters)
# 3  Enable unique party support, user supplies list of party names so output is more streamlined


#############################################################################################################

##IMPORTS##
import sys
import os
import random
import math
import pprint
import json
import easygui

#############################################################################################################


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
    return grabSimpleData('problem', problems)


def generatePatron():
    return grabSimpleData('patron', patrons)


def generatePlace(isWild=False):
    reward = random.choice(places["places"]["rewards"])

    if isWild == False:
        civilizedOngoings = random.choice(
            places["places"]["civilizedOngoings"])
        wildernessOngoings = ''
    else:
        wildernessOngoings = random.choice(
            places["places"]["wildernessOngoings"])
        civilizedOngoings = ''

    hazardCategory = random.randint(0, len(places["places"]["hazard"]))

    hazardExample = random.choice(
        places["places"]["hazard"][hazardList[hazardCategory]]["specificExample"])

    hazardPotDanger = random.choice(
        places["places"]["hazard"][hazardList[hazardCategory]]["possibleDanger"])

    print(civilizedOngoings + wildernessOngoings + ' ' +
          hazardCategory + ' ' + hazardExample + ' ' + hazardPotDanger + reward)


def generateUrbanEncounter():
    return grabSimpleData("urbanEncounters", urbanEncounters)


def generateWildEncounter():
    return grabSimpleData("wildernessEncounters", wildEncounters)


def generateConflict():
    conflictCategory = random.choice(conflictList)

    conflictSituation = random.choice(
        conflictTypes['conflictType'][conflictCategory]['overallSituation'])

    conflictFocus = random.choice(
        conflictTypes['conflictType'][conflictCategory]['specificFocus'])

    print(conflictCategory + ': ' + conflictSituation + ' ' + conflictFocus)


def generateNPC():
    return grabSimpleData('npc', NPC)


def generateSimpleNPC():
    return grabSimpleData("onerollNPC", simpleNPC)


def grabSimpleData(firstElement, table, noParent=False):
    returnVal = []

    if noParent == False:
        for x in table[firstElement]:
            returnVal.append(random.choice(table[firstElement][str(x)]))
        return returnVal
    else:
        for x in table:
            returnVal.append(random.choice(table[x]))


    #############################################################################################################
conflictList = ['money', 'revenge', 'power', 'naturalDanger',
                'religion', 'ideology', 'ethnicity', 'resources']

hazardList = ['social', 'legal', 'environmental',
              'trap', 'animal', 'sentient', 'decay', 'PC-induced']

problems = loadJson("problem.json")
patrons = loadJson("patrons.json")
places = loadJson("places.json")
NPC = loadJson("npc.json")
wildEncounters = loadJson("wildernessEncounters.json")
urbanEncounters = loadJson("urbanEncounters.json")
conflictTypes = loadJson("conflictType.json")
simpleNPC = loadJson("onerollNPC.json")
adventureSeeds = loadJson("adventureSeeds.json")

#############################################################################################################


def main():
    print(generateNPC())
    print(generateNPC())

    # If not importing. run main function
if __name__ == '__main__':
    main()
