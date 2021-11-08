from Node import Node
from parser import parser
from varElim import varElim

parse = parser
varE = varElim

f = open("alarm.bif", "r")
g = open("child.bif", "r")
h = open("hailfinder.bif", "r")
i = open("insurance.bif", "r")
j = open("win95pts.bif", "r")

bifList = [f,g,h,i,j]

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

# query variables for each network
alarmQ = ['HYPOVOLEMIA', 'LVFAILURE', 'ERRLOWOUTPUT']
childQ = ['Disease']
hailQ = ['SatContMoist', 'LLIQ']
insuranceQ = ['MedCost', 'ILiCost', 'PropCost']
winQ = ['Problem1', 'Problem2', 'Problem3', 'Problem4', 'Problem5', 'Problem6']

# evidence sets for each query
alarmEvidLittle = {'HRBP' : 'High', 'CO' : 'Low', 'BP' : 'High' }
alarmEvidMed = {'HRBP' : 'High', 'CO' : 'Low', 'BP' : 'High', 'HRSAT' : 'Low', 'HREKG' : 'Low', 'History': 'True'}
childEvidLittle = {'LowerBodyO2' : '<5', 'RUQO2' : '>=12', 'CO2Report' : '>=7.5', 'XrayReport' : 'AsyPatchy'}
childEvidMed = {'LowerBodyO2' : '<5', 'RUQO2' : '>=12', 'CO2Report' : '>=7.5', 'XrayReport' : 'AsyPatchy', 'GruntingReport' : 'Yes', 'LVHReport' : 'Yes', 'Age' : '11-30 Days'}
hailEvidLittle = {'RSFcst' : 'XNIL', 'N32StarFcst' : 'XNIL', 'MountainFcst' : 'XNIL', 'AreaMoDryAir' : 'VeryWet'}
hailEvidMed = {'RSFcst' : 'XNIL', 'N32StarFcst' : 'XNIL', 'MountainFcst' : 'XNIL', 'AreaMoDryAir' : 'VeryWet', 'CombVerMo' : 'Down', 'AreaMeso_ALS' : 'Down', 'CurPropConv' : 'Strong'}
insuranceEvidLittle = {'Age' : 'Adolescent', 'GoodStudent' : 'False', 'SeniorTrain' : 'False', 'DrivQuality' : 'Poor'}
insuranceEvidMed = {'Age' : 'Adolescent', 'GoodStudent' : 'False', 'SeniorTrain' : 'False', 'DrivQuality' : 'Poor', 'MakeModel' : 'Luxury', 'CarValue' : 'FiftyThousand', 'DrivHistory' : 'Zero'}
winEvidOne = {'Problem1' : 'No_OutPut'}
winEvidTwo = {'Problem2' : 'Too_Long'}
winEvidThree = {'Problem3' : 'No'}
winEvidFour = {'Problem4' : 'No'}
winEvidFive = {'Problem5' : 'No'}
winEvidSix = {'Problem6' : 'Yest'}
winEvid = [winEvidOne, winEvidTwo, winEvidThree, winEvidFour, winEvidFive, winEvidSix]
insuarnceEvid = [insuranceEvidLittle, insuranceEvidMed]
hailEvid = [hailEvidLittle, hailEvidMed]
childEvid = [childEvidLittle, childEvidMed]
alarmEvid = [alarmEvidLittle, alarmEvidMed]



# alarm little
for i in alarmQ:
    for j in alarmEvid:
        varE.query(bayesDict,j, i)
