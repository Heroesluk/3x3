
tab = ['-','-','-','-','-','-','-','-','-']
sab = [1,2,3,4,5,6,7,8,9]

def prin():
    print("\n".join(map(" ".join, zip(*[iter(tab)] * 3))))

def sprawdz():
    if ('x' == tab[0] and 'x' == tab[1] and 'x' == tab[2] or 'x' == tab[3] and 'x' == tab[4] and 'x' == tab[5]
    or 'x' == tab[6] and 'x' == tab[7] and 'x' == tab[8] or 'x' == tab[0] and 'x' == tab[3] and 'x' == tab[6]
    or 'x' == tab[1] and 'x' == tab[4] and 'x' == tab[7] or 'x' == tab[2] and 'x' == tab[5] and 'x' == tab[8]
    or 'x' == tab[0] and 'x' == tab[4] and 'x' == tab[8] or 'x' == tab[2] and 'x' == tab[4] and 'x' == tab[6]):
        print("Wygral krzyzyk")
        quit()

def spraw():
    if ('o' == tab[0] and 'o' == tab[1] and 'o' == tab[2] or 'o' == tab[3] and 'o' == tab[4] and 'o' == tab[5]
    or 'o' == tab[6] and 'o' == tab[7] and 'o' == tab[8] or 'o' == tab[0] and 'o' == tab[3] and 'o' == tab[6]
    or 'o' == tab[1] and 'o' == tab[4] and 'o' == tab[7] or 'o' == tab[2] and 'o' == tab[5] and 'o' == tab[8]
    or 'o' == tab[0] and 'o' == tab[4] and 'o' == tab[8] or 'o' == tab[2] and 'o' == tab[4] and 'o' == tab[6]):
        print("Wygral kolko")
        quit()

def inpucik():
    print("Tura krzyzyka")
    x = input()
    tab[x - 1] = 'x'
    prin()
    sprawdz()
    spraw()

    print("Tura kolka")
    x = input()
    tab[x - 1] = 'o'
    prin()
    sprawdz()
    spraw()



inpucik()
inpucik()
inpucik()
inpucik()
inpucik()
inpucik()
inpucik()
inpucik()
inpucik()






