import random

def atoi(str):
	res = 0
	for i in range(len(str)):
		res = res * 10 + (ord(str[i]) - ord('0'))
	return res

if __name__ == "__main__":
	print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")

	nb = random.randint(1, 99)
	attempts = 0
	congrats = """Congratulations, you've got it!
You won in {} attempts!"""
	error = "That's not a number."
	too_high = "Too high!"
	too_low = "Too low!"
	question = "What's your guess between 1 and 99?\n>> "
	guess_nb = 0
	guess_txt = ""
	while guess_nb != nb:
		guess_txt = input(question)
		if not guess_txt.isdigit():
			print(error)
			continue
		guess_nb = atoi(guess_txt)
		if guess_nb > nb:
			print(too_high)
		elif guess_nb < nb:
			print(too_low)
		attempts += 1
	print(congrats.format(attempts))