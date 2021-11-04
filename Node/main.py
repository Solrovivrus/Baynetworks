import parser
from Node import Node
from parser import parser

parse = parser

f = open("alarm.bif", "r")
BIF = f.readlines()
BIF = parse.fixWhiteSpace(BIF)
nodes = parse.parseBIF(BIF)
parse.printNodes(nodes)

for node in nodes:
    print(node)