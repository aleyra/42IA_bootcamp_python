class Evaluator:
	# def __init__(self, coefs, words) -> None:
	# 	c = coefs
	# 	w = words
	
	# def __str__(self) -> str:
	# 	to_print = f"{c}\n{w}"
	# 	return to_print
	
	def zip_evaluate(c, w):
		if len(c) != len(w):
			return -1
		tmp = list(zip(c, w))
		res = 0
		for i in range(len(tmp)):
			res += tmp[i][0] * len(tmp[i][1])
		return res
	
	def enumerate_evaluate(c, w):
		tmp = dict(enumerate(w))
		res = 0
		for i in range(len(c)):
			res += c[i] * len(tmp[i])
		return res

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    r = Evaluator.zip_evaluate(coefs, words)
    print(f' res = {r}')
    # r = Evaluator.enumerate_evaluate(coefs, words)
    # print(f' res = {r}')