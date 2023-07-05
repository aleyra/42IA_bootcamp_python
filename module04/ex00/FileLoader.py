import pandas as pd

class FileLoader:
	def load(self, path):
		df = pd.read_csv(path)
		# print(df)
		print(f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
		# print(df.head(12))
		return df

	def display(self, df, n):
		print(df.head(n))#pourquoi ça marche pas
		# print(f"[{n} rows x {df.shape[1]} columns]")

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load("data.csv")
	# Output
	# Loading dataset of dimensions 32561 x 15
	loader.display(data, 12)
	# Output
	#cf subject