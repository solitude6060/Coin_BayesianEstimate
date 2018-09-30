#P76071200 CSIE NCKU
#Chung-Yao Ma 2018/09/30

import math
import numpy as np
import random
from matplotlib import pyplot as plt
import scipy
from scipy import optimize

def combination(n, m):
    return int(math.factorial(n)/math.factorial(m)/math.factorial(n-m))

def binomial_ten(n, p):
    return combination(10, n)*(p**n)*((1-p)**(10-n))

def mle(n):
    max_theta = scipy.optimize.fmin(lambda p: -binomial_ten(n, p), 0,disp=False)
    max_pb =  round(max_theta[0],4)
    return max_pb

def mp(list_prior, n):
    max = 0
    max_theta = 0
    for p in range(11):
        theta = p/10
        if list_prior[p]*binomial_ten(n, theta) >= max:
            max = list_prior[p]*binomial_ten(n, theta)
            max_theta = theta
    return max_theta


#two head and eight tail
#prior
aList = [1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11, 1/11]
bList = [0.01, 0.01, 0.05, 0.08, 0.15, 0.4, 0.15, 0.08, 0.05, 0.01, 0.01]

a_marginal = 0
b_marginal = 0

a_posterior = []
b_posterior = []
likelihood  = []


for i in range(11):
    theta = i/10
    a_marginal += aList[i]*binomial_ten(2, theta)
    b_marginal += bList[i]*binomial_ten(2, theta)

for i in range(11):
    theta = i/10
    a_posterior.append(aList[i]*binomial_ten(2, theta)/a_marginal)
    b_posterior.append(bList[i]*binomial_ten(2, theta)/b_marginal)
    likelihood.append(binomial_ten(2, theta))


print("(1)-(a) p by MLE : ", mle(2))
print("(1)-(a) p by MAP : ", mp(aList, 2))

print("(1)-(b) p by MLE : ", mle(2))
print("(1)-(b) p by MAP : ", mp(bList, 2))

########################graph########################
a_posterior_data = np.array(a_posterior)
b_posterior_data = np.array(b_posterior)
likelihood_data =  np.array(likelihood)
a_prior = np.array(aList)
b_prior = np.array(bList)
 
x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])


#########################(a)###########################
plt.figure(1)

plt.subplot(131)
plt.xlim([-0.1, 1.1])
plt.ylim([0, 1])
plt.bar(x, a_prior, width = 0.05)
plt.title('(a) prior')
plt.xlabel('theta')
plt.ylabel('probability')
plt.xticks(np.arange(0, 1, step=0.1))

plt.subplot(132)
plt.xlim([-0.1, 1.1])
plt.ylim([0, 1])
plt.bar(x, likelihood_data, width = 0.05)
plt.title('(a) likelihood')
plt.xlabel('theta')
plt.ylabel('probability')
plt.xticks(np.arange(0, 1, step=0.1))

plt.subplot(133)
plt.xlim([-0.1, 1.1])
plt.ylim([0, 1])
plt.bar(x, a_posterior_data, width = 0.05)
plt.title('(a) posterior')
plt.xlabel('theta')
plt.ylabel('probability')
plt.xticks(np.arange(0, 1, step=0.1))

plt.show()

#########################(b)###########################
plt.figure(2)

plt.subplot(131)
plt.xlim([-0.1, 1.1])
plt.ylim([0, 1])
plt.bar(x, b_prior, width = 0.05)
plt.title('(b) prior')
plt.xlabel('theta')
plt.ylabel('probability')
plt.xticks(np.arange(0, 1, step=0.1))

plt.subplot(132)
plt.xlim([-0.1, 1.1])
plt.ylim([0, 1])
plt.bar(x, likelihood_data, width = 0.05)
plt.title('(b) likelihood')
plt.xlabel('theta')
plt.ylabel('probability')
plt.xticks(np.arange(0, 1, step=0.1))

plt.subplot(133)
plt.xlim([-0.1, 1.1])
plt.ylim([0, 1])
plt.bar(x, b_posterior_data, width = 0.05)
plt.title('(b) posterior')
plt.xlabel('theta')
plt.ylabel('probability')
plt.xticks(np.arange(0, 1, step=0.1))

plt.show()

