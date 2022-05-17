import numpy as np

class Perceptron:
    def __init__(self, no_of_inputs, inputs, labels, bias=-2, epochs=10, learning_rate=0.1):
        self.inputs = inputs
        self.labeled_outputs = labels
        self.bias = bias
        self.epochs = epochs
        self.l_rate = learning_rate
        self.weights = np.random.rand(1, no_of_inputs) # random numbers from 0 to 1

    #predict the output based on the dot product of weights to input
    def predict(self, each_input):
        return np.dot(self.weights[:], each_input) + self.bias

    #step function
    def activation(self, inpt):
        prediction = self.predict(inpt)
        if prediction > 0:
            output = 1
        else:
            output = 0
        return output

    #train the perceptron
    def train(self):
        for cycle in range(self.epochs):
            for each_inp, each_out in zip(self.inputs, self.labeled_outputs):
                self.weights[:] += self.l_rate * (each_out - self.activation(each_inp)) * each_inp

inputs = np.array([[0,0], [1,0], [0,1], [1,1]])
AND_Outputs = [0,0,0,1]

def testing_all_inputs(no_of_inputs, inputs, output_labels, bias=-2):
    perceptron = Perceptron(no_of_inputs, inputs, output_labels, bias)
    perceptron.train()

    for each in inputs:
        print(perceptron.activation(each))

print("AND Gate Output")
testing_all_inputs(2, inputs, AND_Outputs)
