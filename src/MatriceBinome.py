import CSVReader

def createMatriceBinome(file):
    matricePref = CSVReader.createMatrice(file)
    #print(len(matricePref))
    tailleMatriceBinome = ((len(matricePref)-1)*(len(matricePref)-2))/2
    matriceBinome = [[0 for j in range(0,4)] for i in range(0,tailleMatriceBinome)]
    #matrice2 = [['', '1', '2', '3', '4'],['1', '-1', 'AB', 'TB', 'B'],['2', 'P', '-1', 'B', 'B'],['3', 'AB', 'B', '-1', 'I'],['4', 'B', 'B', 'B', '-1']]
    n = 2
    m = 1
    j = 0
    while j!=(tailleMatriceBinome) and n!=(len(matricePref)):
        matriceBinome[j][0] = CSVReader.getElemMatrice(matricePref,m,0)
        matriceBinome[j][1] = CSVReader.getElemMatrice(matricePref,n,0)
        matriceBinome[j][2] = CSVReader.getElemMatrice(matricePref,m,n)
        matriceBinome[j][3] = CSVReader.getElemMatrice(matricePref,n,m)
        j = j+1
        if (n == len(matricePref)-1 and m != len(matricePref)-1):
            m=m+1
            n=m+1
        else:
            n=n+1
    return matriceBinome

def createMatriceTrinome(file):
    matricePref = CSVReader.createMatrice(file)
    tailleMatriceTrinome = ((len(matricePref)-1)*(len(matricePref)-2)*(len(matricePref)-3))/6
    matriceTrinome = [[0 for j in range(0,9)] for i in range(0,tailleMatriceTrinome)]
    p=3
    n=2
    m=1
    j=0
    while j!=(tailleMatriceTrinome) and p!=(len(matricePref)):
        matriceTrinome[j][0] = CSVReader.getElemMatrice(matricePref,m,0)
        matriceTrinome[j][1] = CSVReader.getElemMatrice(matricePref,n,0)
        matriceTrinome[j][2] = CSVReader.getElemMatrice(matricePref,p,0)
        matriceTrinome[j][3] = CSVReader.getElemMatrice(matricePref,m,n)
        matriceTrinome[j][4] = CSVReader.getElemMatrice(matricePref,n,m)
        matriceTrinome[j][5] = CSVReader.getElemMatrice(matricePref,m,p)
        matriceTrinome[j][6] = CSVReader.getElemMatrice(matricePref,p,m)
        matriceTrinome[j][7] = CSVReader.getElemMatrice(matricePref,n,p)
        matriceTrinome[j][8] = CSVReader.getElemMatrice(matricePref,p,n)
        j=j+1
        if (p==len(matricePref)-1 and n==len(matricePref)-2 and m!=len(matricePref)-1):
            m=m+1
            n=m+1
            p=n+1
        elif (p==len(matricePref)-1 and n!=len(matricePref)-2 and m!=len(matricePref)-1):
            n=n+1
            p=n+1
        else:
            p=p+1
    return matriceTrinome

#matrice = createMatriceBinome('../preferences.csv')
#print(matrice)

def triMatriceBinome(matriceBinome,apprec):
    newMatriceBinome = []
    n = len(matriceBinome) - 1
    i = 0
    while(i<=n):
        apprec1 = matriceBinome[i][2]
        apprec2 = matriceBinome[i][3]
        if (apprec1!=apprec and apprec2!=apprec):
            newMatriceBinome.append(matriceBinome[i])
        i=i+1
    return newMatriceBinome

def triMatriceTrinome(matriceTrinome,apprec):
    newMatriceTrinome = []
    n = len(matriceTrinome) - 1
    i = 0
    while(i<=n):
        apprec1 = matriceTrinome[i][3]
        apprec2 = matriceTrinome[i][4]
        apprec3 = matriceTrinome[i][5]
        apprec4 = matriceTrinome[i][6]
        apprec5 = matriceTrinome[i][7]
        apprec6 = matriceTrinome[i][8]
        if (apprec1!=apprec and apprec2!=apprec and apprec3!=apprec and apprec4!=apprec and apprec5!=apprec and apprec6!=apprec):
            newMatriceTrinome.append(matriceTrinome[i])
        i=i+1
    return newMatriceTrinome

def supprBinome(matriceBinome, a, b):
    newMatriceBinome = []
    n = len(matriceBinome) - 1
    i = 0
    while(i<=n):
        e1 = matriceBinome[i][0]
        e2 = matriceBinome[i][1]
        if (e1!=a and e2!=b and e1!=b and e2!=a):
            newMatriceBinome.append(matriceBinome[i])
        i=i+1
    return newMatriceBinome

def supprTrinome2(matriceTrinome, a, b):
    newMatriceTrinome = []
    n = len(matriceTrinome) - 1
    i = 0
    while(i<=n):
        e1 = matriceTrinome[i][0]
        e2 = matriceTrinome[i][1]
        e3 = matriceTrinome[i][2]
        if (e1!=a and e2!=b and e1!=b and e2!=a and e3!=a and e3!=b):
            newMatriceTrinome.append(matriceTrinome[i])
        i=i+1
    return newMatriceTrinome

def supprTrinome3(matriceTrinome, a, b, c):
    newMatriceTrinome = []
    n = len(matriceTrinome) - 1
    i = 0
    while(i<=n):
        e1 = matriceTrinome[i][0]
        e2 = matriceTrinome[i][1]
        e3 = matriceTrinome[i][2]
        if (e1!=a and e2!=b and e1!=b and e2!=a and e3!=a and e3!=b and e1!=a and e2!=b and e3!=c):
            newMatriceTrinome.append(matriceTrinome[i])
        i=i+1
    return newMatriceTrinome


def occurrenceEleve(matriceBinome, n):
    tabEtu = [0 for i in range(0,n)]
    k=0
    while(k<len(matriceBinome)):
        a=int(matriceBinome[k][0])
        b=int(matriceBinome[k][1])
        tabEtu[a-1]=tabEtu[a-1]+1
        tabEtu[b-1]=tabEtu[b-1]+1
        k=k+1
    return tabEtu

def occurenceEleveTrinome(matriceTrinome, n):
    tabEtu = [0 for i in range(0,n)]
    k=0
    while(k<len(matriceTrinome)):
            a=int(matriceTrinome[k][0])
            b=int(matriceTrinome[k][1])
            c=int(matriceTrinome[k][2])
            tabEtu[a-1]=tabEtu[a-1]+1
            tabEtu[b-1]=tabEtu[b-1]+1
            tabEtu[c-1]=tabEtu[c-1]+1
            k=k+1
    return tabEtu

def verifOccurence(occ):
    i = len(occ)
    j = 0
    res = True
    while (j<i):
        if (occ[j] == 0):
            res = False
        j=j+1
    return res

def critique(occ):
    k = 0
    while ((k<len(occ)) and (occ[k]!=1)):
        k=k+1
    if (k != len(occ)):
        return k
    else:
        return -1

def estCritique(occ, a):
    return occ[a-1]==1

def binomeTri(occ, critique, binome):
    occ[critique-1]=occ[critique-1]-1
    occ[binome-1]=occ[binome-1]-1

def trinomeTri(occ, critique, binome, c):
    occ[critique-1]=occ[critique-1]-1
    occ[binome-1]=occ[binome-1]-1
    occ[c-1]=occ[c-1]-1

