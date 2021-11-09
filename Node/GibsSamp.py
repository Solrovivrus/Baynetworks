import random


def normalize(vector):
    """checks that all probs = 1. returns the distribution"""
    for val in vector.values():
        vector.values()[val] = (val - val.min()) / (val.max() - val.min())
    return vector


def makeSample(x, initialState, network):
    """This should return a sample for P(x|mb) where mb stands for the variables in our markov blanket
    our evid has our random evidence which will give the values.
    """
    dist = 0
    X = network
    print(x)
    print(initialState[x])
    parent = network[x]["parents"]
    if not parent:
        parentValues = 1
    else:
        parent = str(parent)[2:-2]
        parentValues = list(network[parent]["CPD"].values())

    child = network[x]["children"]
    if not child:
        childValues = 1
    else:
        child = str(child)[2:-2]
        childValues = list(network[child]["CPD"].values())
    print(child)
    for i in network.values():
        dist[i] = initialState[x] * parentValues + childValues
    return dist


class GibsSamp:
    """Here in this function we do our Gibbs Sampling by first taking our report and returning a random true/false
    """

    @staticmethod
    def GibbsSampling(network, evid, query):
        count = 1000
        initialState = evid
        vector = {}
        nonevid = []
        l = []
        ol = []
        for i in range(len(query)):
            choice = ["true", "false"]
            l.append(random.choice(choice))
            ol.append(.5)
        vector[tuple(l)] = tuple(ol)
        """Then we search the network for all parents which aren't our evidence and put it into a list
        """
        for var in network:
            if var not in evid:
                nonevid.append(var)

        """Then for each piece of our non evidence we will take random assortment of values and probabilities 
        for our markov sample.
        """
        for x in nonevid:
            initialState[x] = random.choice(list(network[x]["CPD"].values()))
        """Then we return 1000 samples of our non evidence with our network to make random samples which we can then
        return the normalized distribution for.
        """
        for y in range(count):
            for x in nonevid:
                initialState[x] = makeSample(x, initialState, network)
                vector[initialState[x]] += 1
        print(normalize(vector))
