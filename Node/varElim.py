


class varElim:


    # --------------------------------------------------------------------------------------------
    # The normalize function takes the probability values and ensures that they add up to 1.0. 
    # Function will take the probability values in as a list and return a tuple of the normalized 
    # values. normalize() will divide each component of our list by the entire value of prob and 
    # return the scaled values. 

    def normalize(prob):
        return tuple(i * 1/(sum(prob)) for i in prob)

    # --------------------------------------------------------------------------------------------
    # The makeFactor function takes the currently selected variable, the factor variables for the 
    # selected variable, and the evidence provided. Returned will be a list of the variables as well
    # as a dictionary containing the state and probability of the variables. 
    def makeFactor(var, fvar, evid):
        pass

    # --------------------------------------------------------------------------------------------
    # The pwProd function takes in the common variable and list of factors and returns a list of 
    # new factors. 
    def pwProd(var, factors):
        pass

    # --------------------------------------------------------------------------------------------
    # The sumOut function takes in the selected variable and a list of the factors and returns a 
    # list of the summed out factors. 
    def sumOut(var, factors):
        pass

    # --------------------------------------------------------------------------------------------
    # The elimAsk function calculates the distribution over the query variable using variable 
    # elimination. It takes the query variable and evidence and returns the distribution over the 
    # query variable. 
    def elimAsk(query, evid):
        pass

