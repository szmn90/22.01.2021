def ostatnielinie(f,n):
    with open(f) as file:
        print('Ostatnie ',n, 'linijek pliku to: ',f)
        for line in (file.readlines()[-n:]):
            print(line,end='')

name = input('Nazwa pliku tekstowego: ')
n=int(input('Ile ostatnich linijek? '))
print(ostatnielinie(name,n))

#działa