import numpy as np
import random

def activation_function(weighted_sum):
    if weighted_sum > 0:
        return 1
    elif weighted_sum < 0:
        return 0

def perceptron(gate):
    bias = (1,) # the bias is always one
    learning_rate = 0.1
    epochs = 50 # how many times the machine learns
    weights = []

    # appending 3 random weights between 0 and 1, one for each input and one for the bias
    for i in range(3):
        weights.append(random.uniform(0, 1))

    for i in range(epochs):
        inputs, expected_output = random.choice(gate)
        inputs = inputs + bias # adding the bias here
        weighted_sum = np.dot(inputs, weights)
        guess = activation_function(weighted_sum) # finding the sign of the weighted sum
        error = expected_output - guess
        weights += learning_rate * error * np.asarray(inputs) # changing the weights to include the error times input, won't change if there's no error

    inputs, expected_output = random.choice(gate)
    print("inputs: " + str(inputs))
    inputs = inputs + bias
    weighted_sum = np.dot(inputs, weights)
    print("Weighted sum: " + str(weighted_sum))
    print("Expected output: " + str(expected_output))
    print("Perceptron guess: " + str(activation_function(weighted_sum)) + '\n')

and_gate = [
    # [(inputs), expected output]
    [(0, 0), 0],
    [(0, 1), 0],
    [(1, 0), 0],
    [(1, 1), 1]
]

for i in range(4):
    print("AND Gate")
    perceptron(and_gate)