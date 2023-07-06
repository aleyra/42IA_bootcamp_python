import pandas as pd
# import numpy as np
from FileLoader import FileLoader

def how_many_medals(df, name):
	res = dict()
	# print(df.columns)
	tmp = df.groupby(df.Name)
	tdf = tmp.get_group(name)
	# print(tdf)
	year = pd.unique(tdf[['Year']].values.ravel())
	# print(type(year))
	tmp = tdf.groupby(tdf.Year)

	for i in year:
		tdic = dict({'G':0, 'S':0, 'B':0})
		y_i = tmp.get_group(i)
		m = y_i.groupby(y_i.Medal)
		type_medal = pd.unique(y_i[['Medal']].values.ravel())
		if 'Gold' in type_medal:
			tdic['G'] = m.get_group('Gold').shape[0]
		if 'Silver' in type_medal:
			tdic['S'] = m.get_group('Silver').shape[0]
		if 'Bronze' in type_medal:
			tdic['B'] = m.get_group('Bronze').shape[0]
		res.update({i:tdic})
	print(res)
    
if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	# Output
	# Loading dataset of dimensions 271116 x 15

	how_many_medals(data, 'Kjetil Andr Aamodt')
	# Output
	# {1992: {’G’: 1, ’S’: 0, ’B’: 1},
	# 1994: {’G’: 0, ’S’: 2, ’B’: 1},
	# 1998: {’G’: 0, ’S’: 0, ’B’: 0},
	# 2002: {’G’: 2, ’S’: 0, ’B’: 0},
	# 2006: {’G’: 1, ’S’: 0, ’B’: 0}}