class Vector:
	def __init__(self, values):
		#checks
		assert isinstance(values, list), "values: list of list of floats (for row vector) or list of lists of single float (for column vector)"
		if (len(values) != 1):#case column
			for i in range(len(values)):
				assert isinstance(values[i], list), "the list must contain lists of 1 float or 1 list of several floats"
				assert len(values[i]) == 1, "the list must contain lists of 1 float"
				assert (isinstance(values[i][0], float) or isinstance(values[i][0], int)), "the list must contain lists of 1 float"
		else:#case line
			assert isinstance(values[0], list), "the list must contain 1 list of floats"
			for i in range(len(values[0])):
				assert (isinstance(values[0][i], float) or isinstance(values[0][i], int)), "the list must contain 1 list of floats"
		
		#init
		self.values = values
		self.shape = [0, 0]
		if (len(values) != 1):#case column
			self.shape[0] = len(values)
			self.shape[1] = 1
		else:#case line
			self.shape[0] = 1
			self.shape[1] = len(values[0])
		self.shape = tuple(self.shape)

	#overload
	def __str__(self) -> str:
		to_print = "["
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				to_print += f"[{self.values[i][0]}]"
				if i != len(self.values) - 1:
					to_print += ", "
			to_print += "]"
		else:#case line
			to_print += "["
			for i in range(len(self.values[0])):
				to_print += f"{self.values[0][i]}"
				if i != len(self.values[0]) - 1:
					to_print += ", "
			to_print += "]]"
		return to_print
	
	def __repr__(self) -> str:
		to_print = "["
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				to_print += f"[{self.values[i][0]}]"
				if i != len(self.values) - 1:
					to_print += ", "
			to_print += "]"
		else:#case line
			to_print += "["
			for i in range(len(self.values[0])):
				to_print += f"{self.values[0][i]}"
				if i != len(self.values[0]) - 1:
					to_print += ", "
			to_print += "]]"
		return to_print
		# return str(self)

	def __add__(self, v):
		#check
		assert self.shape == v.shape, "this is between 2 vectors of same shape"
		#prog
		values = []
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				values.append([self.values[i][0] + v.values[i][0]])
		else:#case line
			for i in range(len(self.values[0])):
				values.append(self.values[0][i] + v.values[0][i])
			values = [values]
		return Vector(values)
	
	def __sub__(self, v):
		#check
		assert self.shape == v.shape, "this is between 2 vectors of same shape"
		#prog
		values = []
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				values.append([self.values[i][0] - v.values[i][0]])
		else:#case line
			for i in range(len(self.values[0])):
				values.append(self.values[0][i] - v.values[0][i])
			values = [values]
		return Vector(values)
	
	def __mul__(self, l):
		assert (isinstance(l, float) or isinstance(l, int)), "this is between a vector and a scalar"
		values = []
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				values.append([self.values[i][0] * l])
		else:#case line
			for i in range(len(self.values[0])):
				values.append(self.values[0][i] * l)
			values = [values]
		return Vector(values)
	
	def __rmul__(self, l):
		assert (isinstance(l, float) or isinstance(l, int)), "this is between a vector and a scalar"
		values = []
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				values.append([self.values[i][0] * l])
		else:#case line
			for i in range(len(self.values[0])):
				values.append(self.values[0][i] * l)
			values = [values]
		return Vector(values)
	
	def __truediv__(self, l):
		assert (isinstance(l, float) or isinstance(l, int)), "this is between a vector and a scalar"
		values = []
		if (l == 0):
			try:
				self.values[0][0] / 0
			except ZeroDivisionError:
				raise ZeroDivisionError("division by zero")
		if self.shape[0] != 1:#case column
			for i in range(len(self.values)):
				values.append([self.values[i][0] / l])
		else:#case line
			for i in range(len(self.values[0])):
				values.append(self.values[0][i] / l)
			values = [values]
		return Vector(values)
	
	def __rtruediv__(self, l):
		assert (isinstance(l, float) or isinstance(l, int)), "this is between a vector and a scalar"
		try :
			l / [self.values[0][0]]
		except NotImplementedError:
			raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
	
	#methods
	def dot(self, v):
		#checks
		assert isinstance(v, Vector), "this is between 2 vectors of same shape"
		assert self.shape == v.shape, "this is between 2 vectors of same shape"
		#prog
		res = 0.
		if v.shape[1] == 1:#case column
			for i in range(len(v.values)):
				res += self.values[i][0] * v.values[i][0]
		else:#case line
			for i in range(len(self.values[0])):
				res += self.values[0][i] * v.values[0][i]
		return res
	
	def T(self):
		values = []
		if self.shape[1] == 1:#case column -> line
			for i in range(len(self.values)):
				values.append(self.values[i][0])
			values = [values]
		else:#case line -> column
			for i in range(len(self.values[0])):
				values.append([self.values[0][i]])
		return Vector(values)