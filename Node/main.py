from Node import Node
from parser import parser
import pprint

parse = parser

f = open("alarm.bif", "r")
BIF = f.readlines()
BIF = parse.fixWhiteSpace(BIF)
nodes = parse.parseBIF(BIF)


# creating a dictionary to house this info since I hate nodes
bayesDict = {}
# adding names of variables, nested dictionary with nested housing parents, children, states, and prob
for a in nodes:
    parentList = []
    for b in a.parents:
        parentList.append(b.getName())
    bayesDict[a.getName()] = {'parents' : parentList}

# adding children
for a in nodes:
    childList = []
    for c in a.children:
        childList.append(c.getName())
    bayesDict[a.getName()]['children'] = childList

# adding states/prob
for a in nodes:
    bayesDict[a.getName()]['CPD'] = a.getDist()

for k,v in bayesDict.items():
    print(k,v)
    print()


