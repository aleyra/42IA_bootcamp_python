import sys

atoMorse = {
		'0' : "-----",
		'1' : ".----",
		'2' : "..---",
		'3' : "...--",
		'4' : "....-",
		'5' : ".....",
		'6' : "-....",
		'7' : "--...",
		'8' : "---..",
		'9' : "----.",
		'A' : ".-",
		'B' : "-...",
		'C' : "-.-.",
		'D' : "-..",
		'E' : ".",
		'F' : "..-.",
		'G' : "--.",
		'H' : "....",
		'I' : "..",
		'J' : ".---",
		'K' : "-.-",
		'L' : ".-..",
		'M' : "--",
		'N' : "-.",
		'O' : "---",
		'P' : ".--.",
		'Q' : "--.-",
		'R' : ".-.",
		'S' : "...",
		'T' : "-",
		'U' : "..-",
		'V' : "...-",
		'W' : ".--",
		'X' : "-..-",
		'Y' : "-.--",
		'Z' : "--..",
		' ' : "/"
}

if __name__ == "__main__":
	if len(sys.argv) == 1:
		exit()

	txt_init = ""
	for i in range(1, len(sys.argv)):
		txt_init += sys.argv[i]
		if i != len(sys.argv) - 1:
			txt_init += ' '
	split = txt_init.split()
	for i in range(1, len(split)):
		if not split[i].isalnum():
			print("ERROR")
			exit()

	txt_init = txt_init.upper()
	txt = ""
	for i in range(0, len(txt_init)):
		txt += atoMorse[txt_init[i]]
		if i != len(txt_init) - 1:
			txt += ' '
	print(txt)