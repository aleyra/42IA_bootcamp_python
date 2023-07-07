import pandas as pd
from FileLoader import FileLoader

def country_to_NOC(country):
	d = dict()
	df = pd.read_csv('../data/ISO-3166-Countries-with-Regional-Codes.csv')
	name = df['name'].tolist()
	noc = df['alpha-3'].tolist()
	for i in range(len(noc)):
		d.update({name[i]:noc[i]})
	return(d[country])

def how_many_medals_by_country(df, country):
	res = dict()
	tmp = df.groupby(df.NOC)
	tdf = tmp.get_group(country_to_NOC(country))
	tdf = tdf.drop(['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight'], axis = 1)
	tdf = tdf.drop_duplicates(keep = 'first')
	yrs = pd.unique(tdf[['Year']].values.ravel())
	tmp = tdf.groupby(tdf.Year)

	for i in yrs:
		tdic = dict({'G':0, 'S':0, 'B':0})
		y_i = tmp.get_group(i)
		m = y_i.groupby(y_i.Medal)
		#il faut aussi trier par event. Attention ! on peut avoir jusqu'à 3 médailles pour certains Event
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

	# print(country_to_NOC('France'))
	how_many_medals_by_country(data, 'France')
