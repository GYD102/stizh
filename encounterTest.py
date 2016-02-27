import math
from random import randint
from random import sample

# Function sets all negative health point values to zero
def flatten(x):
    return [i if (i >= 0) else 0 for i in x]

def generateBase():
# Create 10 columns with 50 hit points each
    S = [50 for i in range(10)]
# Each column takes 11d8 damage
    for i in range(len(S)):
        S[i] = S[i] - sum([randint(1, 8) for j in range(11)])
# Reset health for columns 3 and 5 (trap malfunction)
    S[2]= S[4] = 50
# Reset health for column 8 and damage it for (3 * (11d8) / 4) damage
# (trap malfucntion)
    S[7] = math.floor(50 - 3.0 * sum([randint(1, 8) for i in range(11)]) / 4.0)
# Rid the hit point values of any negatives
    S = flatten(S)
    return S

# Create damage coefficients by counting the number of neighboring columns that
# are demolished (column 1 is neighbored by 10 and 2, 2 by 1 and 3, etc.)
def neighbors(S, i):
    T = [S[(i + 1) % 10], S[i - 1]]
    count = 0
    for i in T:
        if i == 0:
            count = count - 1.0
        elif i < 5:
            count = count - 0.5
    return count

# Count how many turns it would take a randomly damaged set of columns to
# collapse if each column takes dam damage from each demolished neighbor
def countdown(S, dam):
    count = 0
    while (sum(S) > 0):
        try:
            temp = [i for i in S]
            S = [S[i] + dam * neighbors(temp, i) for i in range(len(S))]
            S = flatten(S)
            count = count + 1
# Handle the possibility of none of the columns having collapsed in which case
# the columns would never collapse and the recursion would never end.
        except KeyboardInterrupt:
            print(S)
            return 0
    return count
        
# Print the averages of 1000 trials for damage constants of 3, 2.5, 2, 1.5,
# and 1 accordingly. Note that twice the damage constant is inputed.
print(1.0 * sum([countdown(generateBase(),6) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),5) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),4) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),3) for i in range(1000)]) / 1000.0)
print(1.0 * sum([countdown(generateBase(),2) for i in range(1000)]) / 1000.0)
