import argparse
parser = argparse.ArgumentParser()
parser.add_argument("lastChar")
args = parser.parse_args()
print(args.lastChar)


def lastChar(word):
	namestr = ','.join(word)
	lenght = len(namestr)
	last = namestr[lenght - 1]
	return last

# def last_char():
# 	ask_last_char =  input("last char of word in french: ")
# 	if ask_last_char == 1:
# 		good_last_char = ask_last_char
# 	else:
# 		exit 
with open("dictionary.txt", "r") as f:
	frenchWord = []
	for line in f:
		stripped_line = line.strip()
		frenchWord.append(stripped_line)

wordWithO = []
wordLastChar = []

for i in range(len(frenchWord)):
	last = lastChar(frenchWord[i])
	if id(last) == id(ask_last_char):
		print(frenchWord[i], last)
		wordWithO.append(frenchWord[i])

for i in range(len(wordWithO)):
	print(wordWithO[i])
