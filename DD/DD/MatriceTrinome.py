import CSVReader
import MatriceBinome

def createMatriceTrinome(file):
    matricePref = CSVReader.createMatrice(file)
    tailleMatriceTrinome = ((len(matricePref)-1)*(len(matricePref)-2)*(len(matricePref)-3))/6
    matriceTrinome = [[0 for j in range(0,9)] for i in range(0,int(tailleMatriceTrinome))]
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

def trinomeTri(occ, critique, binome, c):
    i=0
    while(i<len(occ)):
        if(occ[i]!=0):
            occ[i]=occ[i]-6
            i=i+1
    occ[critique-1]=0
    occ[binome-1]=0
    occ[c-1]=0

def newMatriceTrinome(matriceTrinome):
    newMatrice = [[0 for i in range(0,4)]for i in range (0,len(matriceTrinome))]
    j=0
    while(j<len(matriceTrinome)):
        k=0
        while(k<len(matriceTrinome)):
            newMatrice[k][0]=matriceTrinome[k][0]
            newMatrice[k][1]=matriceTrinome[k][1]
            newMatrice[k][2]=matriceTrinome[k][2]
            newMatrice[k][3]=minAppreciationTrinome(matriceTrinome[k][3], matriceTrinome[k][4], matriceTrinome[k][5], matriceTrinome[k][6], matriceTrinome[k][7], matriceTrinome[k][8])
            k=k+1
        j=j+1
    return newMatrice

def minAppreciationTrinome(appr1, appr2, appr3, appr4, appr5, appr6):
    if(appr1==appr2==appr3==appr4==appr5==appr6=="AR" or appr1=="AR" or appr2=="AR" or appr3=="AR" or appr4=="AR" or appr5=="AR" or appr6=="AR"):
        return 0
    else:
        if(appr1==appr2==appr3==appr4==appr5==appr6=="I" or appr1=="I" or appr2=="I" or appr3=="I" or appr4=="I" or appr5=="I" or appr6=="I"):
            return 1
        else:
            if(appr1==appr2==appr3==appr4==appr5==appr6=="P" or appr1=="P" or appr2=="P" or appr3=="P" or appr4=="P" or appr5=="P" or appr6=="P"):
                return 2
            else:
                if(appr1==appr2==appr3==appr4==appr5==appr6=="AB" or appr1=="AB" or appr2=="AB" or appr3=="AB" or appr4=="AB" or appr5=="AB" or appr6=="AB"):
                    return 3
                else:
                    if(appr1==appr2==appr3==appr4==appr5==appr6=="B" or appr1=="B" or appr2=="B" or appr3=="B" or appr4=="B" or appr5=="B" or appr6=="B"):
                        return 4
                    else:
                        return 5


def trinomeApp(matriceB,critique,bin,trin):
    apprec1=MatriceBinome.binomeApp(matriceB,critique,bin)
    apprec2=MatriceBinome.binomeApp(matriceB,critique,trin)
    apprec3=MatriceBinome.binomeApp(matriceB,bin,trin)
    res=''
    if(apprec1==apprec2==apprec3):
        res=apprec1
    elif(apprec1=='TB' or apprec2=='TB' or apprec3=='TB'):
        res='TB'
    elif(apprec1=='B' or apprec2=='B' or apprec3=='B'):
        res='B'
    elif(apprec1=='AB' or apprec2=='AB' or apprec3=='AB'):
        res='AB'
    elif(apprec1=='P' or apprec2=='P' or apprec3=='P'):
        res='P'
    elif(apprec1=='I' or apprec2=='I' or apprec3=='I'):
        res='I'
    else:
        res='AR'
    return res
