import numpy as np
import random

class NumPyCreator:
	def from_list(self, lst):
		return np.array(lst)

	def from_tuple(self, tpl):
		return np.array(tpl)
	
	def from_iterable(self, itr):
		return np.fromiter(itr, int)
	
	def from_shape(self, shape, value = 0):
		nb = 1
		for i in range(len(shape)):
			nb *= shape[i]
		t = []
		for i in range(nb):
			t.append(value)
		t = self.from_list(t)
		return t.reshape(shape)
	
	def random(self, shape):
		nb = 1
		for i in range(len(shape)):
			nb *= shape[i]
		t = []
		for i in range(nb):
			t.append(random.random())
		t = self.from_list(t)
		return t.reshape(shape)
	
	def identity(self, n):
		t = []
		for i in range(n):
			for j in range(n):
				if i == j:
					t.append(1)
				else:
					t.append(0)
		t = self.from_list(t)
		return t.reshape((n,n))

if __name__ == "__main__":
	npc = NumPyCreator()

	lst = [1, 2, 3, 4, 5]
	arr = npc.from_list(lst)

	tpl = (1, 2, 3, 4, 5)
	arr = npc.from_tuple(tpl)

	itr = (i for i in range(5))
	arr = npc.from_iterable(itr)
	
	v = 1
	shape = (2, 4)
	arr = npc.from_shape(shape, v)

	arr = npc.random(shape)
	
	dim = 3
	arr = npc.identity(3)
	print(arr)

	