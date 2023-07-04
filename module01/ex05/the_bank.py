class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount

def isCorrupt(account):
	if (len(account.__dict__) % 2 == 0):
		return True
	hasZip = False
	hasAddr = False
	for x in account.__dict__.keys():
		if x[0] == 'b':
			return True
		if x[0:2] == "zip":
			hasZip = True
		if x[0:3] == "addr":
			hasAddr = True
	if hasAddr == False or hasZip == False:
		return True
	if (not hasattr(account, 'name')
		or not hasattr(account, 'id')
		or not hasattr(account, 'value')):
		return True
	if (not isinstance(account.id, int)):
		return True
	if (not isinstance(account.value, int)
		and not isinstance(account, float)):
		return True

	if (account.value < 0):
		return True

	return False


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []
	
	def add(self, new_account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
			@return True if success, False if an error occured
		"""
		# test if new_account is an Account() instance and if
		# it can be appended to the attribute accounts
	
		if (not isinstance(new_account, Account)):
			return False
		##test if new_account can be appended to the attribute account
		#check if the account is corrupted
				# if (len(new_account.__dict__) % 2 == 0):
				# 	return False
				# hasZip = False
				# hasAddr = False
				# for x in new_account.__dict__.keys():
				# 	if x[0] == 'b':
				# 		return False
				# 	if x[0:2] == "zip":
				# 		hasZip = True
				# 	if x[0:3] == "addr":
				# 		hasAddr = True
				# if hasAddr == False or hasZip == False:
				# 	return False
				# if (not hasattr(new_account, 'name')
				# 	or not hasattr(new_account, 'id')
				# 	or not hasattr(new_account, 'value')):
				# 	return False
				# if (not isinstance(new_account.id, int)):
				# 	return False
				# if (not isinstance(new_account.value, int)
				# 	and not isinstance(new_account, float)):
				# 	return False

				# if (new_account.value < 0):
				# 	return False
		if isCorrupt(new_account) == True:
			return False

		self.accounts.append(new_account)
		return True
	
	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
			@origin: str(name) of the first account
			@dest: str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return True if success, False if an error occured
		"""
		if (not isinstance(origin, str)
      		or not isinstance(dest, str)
			or (not isinstance(amount, float) and not isinstance(amount, int))):
			return False
		if amount < 0:
			return False
		originIdx = -1
		destIdx = -1
		for i in range(len(self.accounts)):
			if self.accounts[i].name == origin:
				originIdx = i
			if self.accounts[i].name == dest:
				destIdx = i
		if (originIdx == -1 or destIdx == -1):
			return False
		if (isCorrupt(self.accounts[originIdx]) == True
      		or isCorrupt(self.accounts[destIdx]) == True):
			return False
		if (self.accounts[originIdx].value < amount):
			return False
		if originIdx != destIdx:
			self.accounts[originIdx].value -= amount
			self.accounts[destIdx].value += amount
		return True
	
	def fix_account(self, name):
		""" fix account associated to name if corrupted
			@name: str(name) of the account
			@return True if success, False if an error occured
		"""
		if (not isinstance(name, str)):
			return False
		idx = -1
		for i in range(len(self.accounts)):
			if (self.accounts[i].name == name):
				idx = i
		if idx == -1:
			return False
		if isCorrupt(self.accounts[idx]) == False:
			return True
		#corriger l'account

if __name__ == "__main__":
	thisdict = {
		"brand": "Ford",
		"model": "Mustang",
		"year": 1964
	}

	for x in thisdict.keys():
		print(x[0])
