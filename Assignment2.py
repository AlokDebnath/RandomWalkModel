import wolframalpha
import math
import random
import matplotlib.pyplot as plt
import numpy as np

def n_random_gen (n):
	arr = []
	i = 0
	while i < n:
		val = random.uniform(0, 1)
		if val > 0.5:
			if  i == 0:
				arr.append(1)
			else:
				arr.append(arr[i-1] + 1)
		else:
			if i == 0:
				arr.append(-1)
			else:
				arr.append(arr[i-1] - 1)
		i += 1
	return arr

def graph_rep(steps1, steps2):
	y1 = steps1
	y2 = steps2
	x1 = range(len(steps1))
	x2 = range(len(steps2))
	plt.plot(x1, y1)
	plt.plot(x2, y2)
	plt.show()

n = int(input()) # This is number of steps

sum = 0

for r in range(0, 100):
	steps1 = n_random_gen(n)
	steps2 = n_random_gen(n)

	cnt = 0

	for i in range (len(steps1)):
		if steps1[i] == steps2[i]:
			cnt +=1
	sum += float(cnt/(2*n))

avg = sum/100

print (avg)

app_id = 'WRH85J-ARL87GYTLW'
client = wolframalpha.Client(app_id)

res = client.query('((2*'+str(n)+')!)/(((2^'+str(n)+')*('+str(n)+'!))^2)')

for pods in res.pods:
	for sub in pods.subpods:
		if sub.plaintext != None:
			print(sub.plaintext)

# Formula: ((2*n)!)/(((2^n)*(n!))^2)
