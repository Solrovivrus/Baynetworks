from os import stat
import copy
import itertools


class varElim:

    # --------------------------------------------------------------------------------------------
    # The normalize function takes the probability values and ensures that they add up to 1.0. 
    # Function will take the probability values in as a list and return a tuple of the normalized 
    # values. normalize() will divide each component of our list by the entire value of prob and 
    # return the scaled values. 
    @staticmethod
    def normalize(prob):
        return tuple(i * 1/(sum(prob)) for i in prob)


    # --------------------------------------------------------------------------------------------
    # The makeFactor function takes the currently selected variable, the factor variables for the 
    # selected variable, and the evidence provided. Returned will be a list of the variables as well
    # as a dictionary containing the state and probability of the variables. 
    @staticmethod
    def makeFactor(variable, factorV, evid, bn):
        varE = varElim

        permutations = {}
        variables = factorV[variable]
        variables.sort()

        allVariables = copy.deepcopy(bn[variable]['parents'])
        allVariables.append(variable)
        print(allVariables)

        entries = {}
        assignment = {}
        possibilities = {}

        print(bn[allVariables[0]]['CPD'])

        for i in evid.keys():
            for j in allVariables:
                if i == j:
                    for k in bn[j]['CPD'].keys():
                        for l in k[1]:
                            if evid[i].values() == l:
                                del bn[j]['CPD'][k]

                        

    # --------------------------------------------------------------------------------------------
    # The pwProd function takes in the common variable and list of factors and returns a list of 
    # new factors. 
    @staticmethod
    def pwProd(var, factors):
        pass

    # --------------------------------------------------------------------------------------------
    # The sumOut function takes in the selected variable and a list of the factors and returns a 
    # list of the summed out factors. 
    @staticmethod
    def sumOut(var, factors):
        pass

    # --------------------------------------------------------------------------------------------
    # The elimAsk function calculates the distribution over the query variable using variable 
    # elimination. It takes the query variable and evidence and returns the distribution over the 
    # query variable. 
    @staticmethod
    def elimAsk(query, evid, bn):
        varE = varElim
        # to keep track of those variables that have been eliminated
        eliminated = set()
        # initializing list for factors
        factors = []

        # while len(eliminated) < len(bn)
        
        # filtering variables which have been eliminated
        # bn is the given bayesnet, not sure yet on how to bring it in
        variables = list(filter(lambda k: k not in eliminated, list(bn)))

        # filtering variables which may have some children which ahven't been eliminated
        variables = list(filter(lambda x: all(c in eliminated for c in bn[x]['children']), variables))

        # getting the factors set up
        factorV = {}
        for var in variables:
            factorV[var] = [p for p in bn[var]['parents'] if p not in evid]
            if var not in evid:
                factorV[var].append(var)
        
        variable = sorted(factorV.keys(), key = (lambda x: (len(factorV[x]), x)))[0]
        print("Variable: " + str(variable)) 

        # let's make some factors!
        if len(factorV[variable]) > 0:
            factors.append(varE.makeFactor(variable, factorV, evid, bn))



    # --------------------------------------------------------------------------------------------
    # The query function takes in the bayes net to be used, evidence, and query variable
    @staticmethod
    def query(bn, evid, query):
        varE = varElim
        return varE.elimAsk(query, evid, bn)

        

