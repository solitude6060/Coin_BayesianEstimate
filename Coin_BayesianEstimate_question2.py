#P76071200 CSIE NCKU
#Chung-Yao Ma 2018/09/30

import math
import random
from matplotlib import pyplot as plt
import numpy as np

def combination(n, m):
    return int(math.factorial(n)/math.factorial(m)/math.factorial(n-m))

#n : amount of head 
def binomial_ten(n, p):
    return combination(10, n)*(p**n)*((1-p)**(10-n))

def tossTenCoin():
    coinList = []

    for i in range(10):
        #1 : head, 0 : tail
        coin =  random.choice([0,1])
        coinList.append(coin)
    return coinList

def countHead(coinList):
    count = 0
    for i in coinList:
        if i == 1:
            count += 1
    return count


def drawBar(num, posterior):
    plt.figure(num)
    x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

    plt.xlim([-0.1, 1.1])
    plt.ylim([0, 1])
    plt.bar(x, posterior, width = 0.05)
    plt.title('(a) posterior')
    plt.xlabel('theta')
    plt.ylabel('probability')
    plt.xticks(np.arange(0, 1, step=0.1))
    plt.show()   

Prior = [1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11]
for i in range(50):
    coinlist = tossTenCoin()
    count = countHead(coinlist)
    marginal = 0
    for j in range(11):
        theta = j/10
        marginal += Prior[j]*binomial_ten(count, theta)
    
    posterior = []
    for k in range(11):
        theta = k/10
        posterior.append(Prior[k]*binomial_ten(count, theta)/marginal)

    if i % 10 == 0:
        drawBar(i, posterior)

    Prior = posterior

drawBar(50, posterior)