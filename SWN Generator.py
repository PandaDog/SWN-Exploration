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
import random
import math
import pprint
import json
import easygui


def selectJsonFile():
    filePath = easygui.fileopenbox(
        title="Select Json File", filetypes="\*.json")
    return filePath


def loadJson(filePath):
    with open(filePath) as json_file:
        data = json.load(json_file)
        return data
    # Example Macro &{template:default} {{name=Shift fires his gun!}} {{Laser Pistol:=[[d20+4]] vs AC}}  {{Damage:=[[1d6+1]]}}


def Generate_Roll20_Macro(message):
    print("&{template:default} {{" + message + "}}" + '\n')


def main():
    print("Select your Json file.")
    jsonPath = selectJsonFile()
    data = loadJson(jsonPath)
    print(data)


    # If not importing. run main function
if __name__ == '__main__':
    main()
