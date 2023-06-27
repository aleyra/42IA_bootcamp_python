from time import sleep

def ft_progress(lst):
	to_print = "ETA: {}s [{}%][{}] {}/{} | elapsed time {}s"
	eta = 0
	pourcent_progress = 0
	arrow = ""
	done = 0
	max = len(lst)
	e_time = 0
	print(to_print.format(eta, pourcent_progress, arrow, done, max, e_time))


# if __name__ == "__main__":
	# listy = range(1000)
	# ret = 0
	# for elem in ft_progress(listy):
	# 	ret += (elem + 3) % 5
	# 	sleep(0.01)
	# print()
	# print(ret)

	# listy = range(3333)
	# ret = 0
	# for elem in ft_progress(listy):
	# 	ret += elem
	# 	sleep(0.005)
	# print()
	# print(ret)