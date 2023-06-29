class Vector:
	def __init__(self, values, shape):
		#checks
		assert isinstance(values, list), "values: list of list of floats (for row vector) or list of lists of single float (for column vector)"
		assert len(values) == 1, "values, len : 1"
		if (len(values[0]) != 1):#[1.], [2.], [3.]
			for i in range(len(values[0])):
				assert isinstance(values[0][i], list), "the list must contain lists of 1 float"
				assert len(values[0][i]) == 1, "the list must contain lists of 1 float"
				assert isinstance(values[0][i][0], float), "the list must contain lists of 1 float"
		else:#[1., 2., 3.]
			assert isinstance(values[0], list), "the list must contain 1 list of floats"
			for i in range(len(values[0])):
				assert isinstance(values[0][i], float), "the list must contain 1 list of floats"
		assert isinstance(shape, tuple), "shape must be a uple of 2 int"
		assert len(shape) == 2, "shape must be a uple of 2 int"
		assert isinstance(shape[0], int), "shape must be a uple of 2 int"
		assert isinstance(shape[1], int), "shape must be a uple of 2 int"
		if (len(values[0]) != 1):
			assert shape[0] == len(values[0]), "shape must be (n, 1) where n is the size of the vector"
			assert shape[1] == 1, "shape must be (n, 1)"
		else:
			assert shape[0] == 1, "shape must be (1, n)"
			assert shape[1] == len(values[0]), "shape must be (1, n) where n is the size of the vector"
		
		#init
		self.values = values
		self.shape = shape

	#methods
	def dot(self, v):
		#checks
		assert isinstance(v, Vector), "this is between 2 vectors od same shape"
		assert self.shape == v.shape, "this is between 2 vectors od same shape"
		#prog
		res = 0.
		for i in range(len(v.values[0])):
			if v.shape[1] == 1:
				res += self.values[0][i][0] * v.values[0][i][0]
			else:
				res += self.values[0][i] * v.values[0].[i]
		return res
	
	def T(self):
		res = []
		if self.shape[1] == 1:
			res[0] = []
			#...
		else:
			for i in range(len(self.values[0])):
				#...