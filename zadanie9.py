file = open("PanTadeusz.txt", "rt")
data = file.read()
words = data.split()

print('Liczba wyrazów w pliku :', len(words))

#działa