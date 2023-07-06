import pandas as pd
from FileLoader import FileLoader

class SpatioTemporalData:
	def __init__(self, df) -> None:
		self.df = df

	def where(self, yr):
		tmp = self.df.groupby(self.df.Year)
		tdf = tmp.get_group(yr)
		np_arr = pd.unique(tdf[['City']].values.ravel())
		res = np_arr.tolist()
		print(res)

	def when(self, city):
		tmp = self.df.groupby(self.df.City)
		tdf = tmp.get_group(city)
		np_arr = pd.unique(tdf[['Year']].values.ravel())
		res = np_arr.tolist()
		print(res)

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	# Output
	# Loading dataset of dimensions 271116 x 15

	sp = SpatioTemporalData(data)
	sp.where(1896)
	# Output
	# [’Athina’]

	sp.where(2016)
	# Output
	# [’Rio de Janeiro’]

	sp.when('Athina')
	# Output
	# [2004, 1906, 1896]

	sp.when('Paris')
	# Output
	# [1900, 1924]