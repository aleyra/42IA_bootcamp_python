import pandas as pd
from FileLoader import FileLoader

def youngest_fellah(df, y):
	res = dict()
	year = df.groupby(df.Year)
	dfy = year.get_group(y)
	sex = dfy.groupby(dfy.Sex)
	dff = sex.get_group('F')
	age = list(filter(lambda f:'Age' in f, dff.columns))
	min = dff[age].min()
	res.update({'f':min[0]})
	dfm = sex.get_group('M')
	age = list(filter(lambda f:'Age' in f, dfm.columns))
	min = dfm[age].min()
	res.update({'m':min[0]})
	print(res)

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	# Output
	# Loading dataset of dimensions 271116 x 15
	# print(data.info())
	youngest_fellah(data, 2004)
	# Output
	# {’f’: 13.0, ’m’: 14.0}