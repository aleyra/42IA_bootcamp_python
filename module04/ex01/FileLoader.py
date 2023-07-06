import pandas as pd

class FileLoader:
	def load(self, path):
		df = pd.read_csv(path)
		print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
		return df

	def display(self, df, n):
		print(df.head(n))
