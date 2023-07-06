import pandas as pd
# import numpy as np
from FileLoader import FileLoader

def how_many_medals(df, name):
	res = dict()
	# print(df.columns)
	tmp = df.groupby(df.Name)
	tdf = tmp.get_group(name)
	year = pd.unique(tdf[['Year']].values.ravel())
	# print(type(year))
	for i in range(len(year)):
		print(year[i])
		gold = 0
		silver = 0
		bronze = 0

    
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