import numpy as np
import nnfs
import matplotlib.pyplot as plt

nnfs.init()



def spiral_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)  # radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y



# X = [[1, 2, 3, 2.5],
# 	[2.0, 5.0, -1.0, 2.0],
# 	[-1.5, 2.7, 3.3, -0.8]]


class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases

class activation_relu:
	def forward(self, inputs):
		self.output = np.maximum(0, inputs)

class activation_softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))
        prob = exp_values / np.sum(exp_values, axis = 1, keepdims=True)
        self.output = prob

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_cce(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y, 1e-7, 1-1e-7)

        if len(y_true.shape) == 1:
            correct_conf = y_pred_clipped[range(samples), y_true]
        elif len(y.shape) == 2:
            correct_conf = np.sum(y_pred_clipped * y_true, axis = 1)

        negativelog = -np.log(correct_conf)
        return negativelog


X, y = spiral_data(100, 3)

dense1 = Layer_Dense(2, 3)
activation1 = activation_relu()

dense2 = Layer_Dense(3, 3)
activation2 = activation_softmax()

dense1.forward(X)

activation1.forward(dense1.output)

dense2.forward(activation1.output)

activation2.forward(dense2.output)



loss_function = Loss_cce()
loss = loss_function.calculate(activation2.output, y)


print(loss)