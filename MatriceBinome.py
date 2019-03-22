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

def newMatriceBinome(matriceBinome):
    newMatrice = [[0 for i in range(0,3)]for i in range (0,len(matriceBinome))]
    j=0
    while(j<len(matriceBinome)):
        k=0
        while(k<len(matriceBinome)):
            newMatrice[k][0]=matriceBinome[k][0]
            newMatrice[k][1]=matriceBinome[k][1]
            newMatrice[k][2]=minAppreciationBinome(matriceBinome[k][2], matriceBinome[k][3])
            k=k+1
        j=j+1
    return newMatrice

def minAppreciationBinome(appr1, appr2):
    if(appr1==appr2=="AR" or appr1=="AR" or appr2=="AR"):
        return 0
    else:
        if(appr1==appr2=="I" or appr1=="I" or appr2=="I"):
            return 1
        else:
            if(appr1==appr2=="P" or appr1=="P" or appr2=="P"):
                return 2
            else:
                if(appr1==appr2=="AB" or appr1=="AB" or appr2=="AB"):
                    return 3
                else:
                    if(appr1==appr2=="B" or appr1=="B" or appr2=="B"):
                        return 4
                    else:
                        return 5

def binomeApp(matriceB,critique,binome):
    i=0
    end=True
    rep=''
    while(i<len(matriceB) and end):
        if(matriceB[i][0]==critique and matriceB[i][1]==binome):
            if(matriceB[i][2]==matriceB[i][3]):
                rep=matriceB[i][2]
            elif(matriceB[i][2]=='TB' or matriceB[i][3]=='TB'):
                rep='TB'
            elif(matriceB[i][2]=='B' or matriceB[i][3]=='B'):
                rep='B'
            elif(matriceB[i][2]=='AB' or matriceB[i][3]=='AB'):
                rep='AB'
            elif(matriceB[i][2]=='P' or matriceB[i][3]=='P'):
                rep='P'
            elif(matriceB[i][2]=='I' or matriceB[i][3]=='I'):
                rep='I'
            else:
                rep='AR'
            end=False
        i=i+1
    if (matriceB[i-1][2]==rep):
        return matriceB[i-1][3]
    else:
        return matriceB[i-1][2]

