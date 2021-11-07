import random


class GibsSamp:

    @staticmethod
    def normalize(vector):
        """checks that all probs = 1. returns the distribution"""
        for val in vector.values():
            vector.values()[val] = (val - val.min())/ (val.max() - val.min())
        return vector

    @staticmethod
    def makeSample(query, evid, network):
        """Here is the math needed for the markov blanket, idk how to code it"""
        pass

    @staticmethod
    def GibbsSampling(network, evid, query):
        count = 1000
        initialState = evid
        vector = {}
        # Z
        nonevid = []
        for i in range(len(query)):
            vector.update({"true, false": (.5, .5)})
        for var in network:
            if var not in evid:
                nonevid.append(var)
        for x in nonevid:
            initialState[x] = random.choice(list(network[x]["CPD"].items()))
        for y in range(count):
            for x in nonevid:
                initialState[x] = makeSample(x, initialState, network)
                vector[initialState[x]] += 1
        print(vector)
        print(normalize(vector))




