import math


softmax = [0.7, 0.1, 0.2]

target = [1, 0, 0]

loss = - (math.log(softmax[0]*target[0]) + 
		math.log(softmax[1]*target[1]) + 
		math.log(softmax[2]*target[2]))

print(loss)

