import pandas as pd
from FileLoader import FileLoader

def proportion_by_sport(df, yr, sport, gender):
	res = float()
	tmp = df.groupby(df.Year)#groupe par année
	tdf = tmp.get_group(yr)#recup que l'année yr
	# print(tdf)
	tmp = tdf.groupby(tdf.Sex)#groupe par genre
	tdf = tmp.get_group(gender)#recup que le genre gender
	tdf2 = pd.unique(tdf[['Name']].values.ravel())#vire les noms en double
	print(tdf2)
	res = tdf2.shape[0]
	tmp = tdf.groupby(tdf.Sport)#groupe par sport
	tdf = tmp.get_group(sport)#recup que le sport sport
	tdf2 = pd.unique(tdf[['Name']].values.ravel())#vire les noms en double
	res = tdf2.shape[0] / res

	print(res)

if __name__ == "__main__" :
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	# Output
	# Loading dataset of dimensions 271116 x 15
	proportion_by_sport(data, 2004, 'Tennis', 'F')
	# Output
	# 0.019302325581395347