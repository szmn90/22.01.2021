with open('PanTadeusz.txt') as old, open("NowyTadeusz.txt", 'w') as new:
    lines = old.readlines()
    new.writelines(lines[\n])

#nie umiem - nie działa