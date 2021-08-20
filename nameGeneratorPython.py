# nameGeneratorPython.py
# Modified Python translation of donjon's name generator: https://donjon.bin.sh/code/name/
# Uses a set of sample names in the form of a JSON file to generate new names using markov chains

# TODO:
# Add sample usage

import math, random, easygui, json

nameSet = {}
chainCache = {}

# Most dictionary calls use dictionary.get() to handle KeyError exceptions

def generateName(type): # returns a single name using sample nameSet = {type: ...}
    chain = markovChain(type)
    if (chain):
        return markovName(chain)
    return ''

def generateNameList(type, num): # returns a list of num names using sample nameSet = {type: ...}
    nameList = []
    i = 0
    while (i < num):
        nameList.append(generateName(type));
        i += 1
    return nameList

def markovChain(type):
    global chainCache
    chain = chainCache.get(type)
    if (chain):
        return chain
    else:
        nameList = nameSet.get(type)
        if (nameList and len(nameList)):
            chain = constructChain(nameList)
            if (chain):
                chainCache[type] = chain
                return chain
    return False

def constructChain(nameList):
    chain = {}
    i = 0
    while (i < len(nameList)):
        names = nameList[i].split()
        chain = incrChain(chain,'parts',len(names))
    
        j = 0
        while (j < len(names)):
            name = names[j]
            chain = incrChain(chain,'nameLen',len(name))
        
            c = name[0:1]
            chain = incrChain(chain,'initial',c)

            string = name[1: len(name)-1]
            lastC = c

            while(len(string) > 0):
                c = string[0:1]
                chain = incrChain(chain,lastC,c)

                string = string[1: len(string)-1]
                lastC = c
            j += 1
        i += 1
    return scaleChain(chain)

def incrChain(chain,key,token):
    if (chain.get(key)):
        if (chain[key].get(token)):
           chain[key][token] += 1
        else:
           chain[key][token] = 1
    else:
        chain[key] = {}
        chain[key][token] = 1
    return chain

def scaleChain(chain):
    tableLen = {}
    for key in list(chain.keys()):
            tableLen[key] = 0
            for token in list(chain[key].keys()):
                    count = chain[key][token]
                    weighted = math.floor((math.pow(count, 1.3)))

                    chain[key][token] = weighted
                    tableLen[key] += weighted

    chain['tableLen'] = tableLen
    return chain

def markovName(chain):
    parts = selectLink(chain,'parts')
    names = []

    i = 0
    while (i < parts):
        nameLen = selectLink(chain,'nameLen')
        c = selectLink(chain,'initial')
        name = c
        lastC = c
        i += 1

        while (len(name) < nameLen):
            c = selectLink(chain,lastC)
            if (not c):
                break
            name += c
            lastC = c

        names.append(name)

    return ' '.join(names)

def selectLink(chain,key):
    length = chain['tableLen'].get(key)
    if (not length):
        return False
    idx = math.floor(random.random() * length)
    tokens = list(chain[key].keys())
    acc = 0

    i = 0
    while (i < len(tokens)):
        token = tokens[i]
        acc += chain[key][token]
        if (acc > idx):
            return token
        i += 1
    return False

def getFilepath(): # this should be removed and added to a separate library

    print("Select your name sample.")
    filepath = easygui.fileopenbox()

    return filepath

def loadJSON(filepath): # this should be removed and added to a separate library

    tmp = open(filepath)
    dictVar = json.load(tmp)

    return dictVar

def parseDictionary(dictVar, active = False): # appends sample dictionary to nameSet{}; returns sample's top-level string for generateName(), generateNameList()

    # check if sample has object 'nameSet'

    try: 
        length = len(dictVar['nameSet'])
    except:
        return False

    # if there is more than one sample in set, prompt to select set if active == True; otherwise, merge sets

    if (length > 1):
        nameSetList = list(dictVar['nameSet'])
        if (active):
            print("There are multiple sets in this sample.")
            n = 1
            for i in dictVar['nameSet']:
                print(str(n) + ": " + str(i))
                n += 1
            n = int(input())
            sample = {nameSetList[n-1]: dictVar['nameSet'][nameSetList[n-1]]}
        else:
            sample = {'merged': []}
            for i in dictVar['nameSet']:
                for j in dictVar['nameSet'][i]:
                    sample['merged'].append(j)
    else:
        sample = dictVar['nameSet']

    global nameSet
    nameSet.update(sample)

    sampleName = str(list(sample)[0])

    return sampleName

def main():

    dictVar = loadJSON(getFilepath())
    sampleName = parseDictionary(dictVar, True)
    nameQuantity = int(input("How many names would you like generated?\n"))
    print(generateNameList(sampleName,nameQuantity))

if __name__ == '__main__':
    main()