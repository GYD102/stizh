import math
from random import randint
from random import sample

def flatten(x):
    return [i if (i >= 0) else 0 for i in x]

def generateBase():
    S = [50 for i in range(10)]
    for i in range(len(S)):
        S[i] = S[i] - sum([randint(1, 8) for j in range(11)])
    S[2]= S[4] = 50
    S[7] = math.floor(50 - 3.0 * sum([randint(1, 8) for i in range(11)]) / 4.0)
    S = flatten(S)
    return S

def neighbors(S, i):
    T = [S[(i + 1) % 10], S[i - 1]]
    count = 0
    for i in T:
        if i == 0:
            count = count - 1.0
        elif i < 5:
            count = count - 0.5
    return count

def countdown(S, dam):
    count = 0
    while (sum(S) > 0):
        try:
            temp = [i for i in S]
            S = [S[i] + dam * neighbors(temp, i) for i in range(len(S))]
            S = flatten(S)
            count = count + 1
        except KeyboardInterrupt:
            print(S)
            return 0
    return count
        
print(1.0 * sum([countdown(generateBase(),6) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),5) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),4) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),3) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),2) for i in range(1000)]) / 1000.0)
