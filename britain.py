import code
import sys

fi = open('wordlist','r')
words = []
for line in fi:
	words.append(line.strip())

american = words[int(len(words)/2):]
brit = words[:int(len(words)/2)]

class british(code.InteractiveConsole):
	def runsource(self, source, filename='<input>',symbol='single'):
		s = source
		for i in range(len(american)):
			s = s.replace(brit[i], american[i])
		super().runsource(s)

english = british()
english.interact(banner='')
