tekst = []
abcd = open("PanTadeusz.txt", 'r')
for line in abcd.readlines():
    tekst.append([line])
    for i in line.split(","):
        tekst[-1].append(i)
koniec = [line.split(',') for line in abcd.readlines()]