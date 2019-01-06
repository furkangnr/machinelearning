# In this chapter I will cover deep learning : NEURAL NETWORKS !
# First Lets see how a perceptron algorithm works in code :

import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    """ This is our step function which return 1 for values equal or greater than 0, return 0 otherwise"""
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    """ This function will take inputs as X, models weights as W and bias as b 
    and returns 1 ( fires neuron ) if X*W + b is >= 0 , returns 0 ( no fire on neuron) otherwise."""
    return stepFunction((np.matmul(X,W)+b)[0])


def perceptronStep(X, y, W, b, learn_rate = 0.01):
    """ This is a simple perceptron trick which basically updates weights (W) and bias (b) according to the
    prediction and the ground truth (y) and returns updated W and b. It takes learn_rate as a keyword argument"""
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i] - y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b = b + learn_rate
        elif y[i] - y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
    

def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    """ This function runs the perceptron algorithm repeatedly ( num_epochs ) on the dataset and saves 
    sboundry lines which can later be plotted on the dataset."""
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] 
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines

# For dataset that are can not be seperated by linear lines, perceptron algorithm simply can not work as
# expected. We need to redefine  our perceptron algorithm to generalize well on curves etc.

"""
In order for gradient descent to be applicable, we need an error function which is continuous not discrete !
Error function also must be differentiable to apply gradient descent algorithm !
two conditions must be met : 1) continuous error 2) differentiable error !
In order to do that , we also need to move from discrete predictions to "" Continuous Predictions "" !!!
To do that, we use sigmoid function instead of step function. Sigmoid function will give us values 
between 0 and 1. It shows the probability of a point being blue or probability of point being red instead
of labelling it as 0 and 1. 
""" 

""" 
There is a problem with the sigmoid function when it comes to multi class classification problems.
If there are more than 2 classes, we need to calculate the probabilities of each of them by using softmax 
function. Before that we need to convert all probabilities to a positive value. It is done by using 
exponential function. 
"""
# here is the code for softmax function  :
def softmax(L):
    """a function that takes a list of numbers as input, and returns the list of values 
    given by the softmax function. """
    expL = np.exp(L)
    sumexpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0 / sumexpL)
    return result
##another way to create a softmax function is : this is simpler
def softmax(L):
    expL = np.exp(L)
    return np.divide(expL, expL.sum())

"""     Maximum Likelihood Theorem :
Basically, we accept the model which gives us the highest probability for a prediction ( most certain ).
However, when calculating probabilities we must avoid using products of each probability since it is harder
to get a high probability when thousands of probabilities between 0 and 1 multiplied. We need another way to 
calculate the probability.IT IS LOGARITHM since it has a beautiful feature which is :
                                LOG(AB) = LOG(A) + LOG(B)

A good model will give us lower cross entropy whereas bad model will yield a higher cross entropy.
We are adding negative of logarithm of probabilities to calculate cross entropies. 

"""

# HERE IS THE CODE FOR CROSS ENTROPY FORMULA :

def cross_entropy(Y, P):
    """Write a function that takes two lists containing numbers Y, P ( Y for ground truth, P for prediction ) 
    as input and returns the float corresponding to their cross-entropy according to cross-entropy formula."""
    sum = 0
    for i in range(len(Y)):
        sum = sum + (Y[i] * np.log(P[i])) + (1.0 - Y[i])* np.log(1.0 - P[i])
    sum = -1.0 * sum 
    return sum

# ANOTHER WAY TO CALCULATE CROSS ENTROPY !:
def cross_entropy(Y, P):
    Y = np.float(Y)
    P = np.float(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


"""Now lets implement gradient descent algorithm in Python 
first we need to implement sigmoid function.  """

def sigmoid(x):
    sigmoid = 1 / 1 + np.exp(-x)
    return sigmoid

# secondly lets implement the prediction function: 
def output_formula(features, weights, bias):
    y_hat = sigmoid(np.dot(features, weights) + bias)
    return y_hat

# lets implement the error ( log - loss function )
def error_formula(y, output):
    error = - y * np.log(output) - (1-y) * np.log(1- output)
    return error

# now it is time to implement gradient descent step:
def update_weights(x, y, weights, bias, learnrate):
    output = output_formula(x, weights, bias)
    d_Error = error_formula(y, output)
    weights = weights - learnrate * d_Error * x
    bias = bias - learnrate * d_Error
    return weights, bias
