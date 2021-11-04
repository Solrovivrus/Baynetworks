class varElim:


    # --------------------------------------------------------------------------------------------
    # The normalize function takes the probability values and ensures that they add up to 1.0. 
    # Function will take the probability values in as a list and return a tuple of the normalized 
    # values. normalize() will divide each component of our list by the entire value of prob and 
    # return the scaled values. 

    def normalize(prob):
        return tuple(i * 1/(sum(prob)) for i in prob)
