plik = open ("PanTadeusz.txt","r")
linia = plik.readlines()
plik.close()
print ("Ostatnie 8 linijek kodu to:")
print (linia[len(linia)-8])

#czyta tylko tą 8, a nie ostatnie 8