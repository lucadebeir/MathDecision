import csv

def getElem(file, i, j):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if reader.line_num - 1 == i:
                return line[j]

def getElemMatrice(matrice, i, j):
    return matrice[i][j]

#print(getElem('../preferences.csv',2,0))

def getFileContent(file):
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        list = []
        for row in spamreader:
            list.append(row)
    return list

def createMatrice(file):
    list=getFileContent(file)
    matrice = [[0 for j in range(0,len(list))] for i in range(0,len(list))]
    matriceStudent = [[0 for j in range(0,2)] for i in range(0,len(matrice))]
    i=0
    while(i<len(list)):
        matriceStudent[i][0]=i
        matriceStudent[i][1]=matrice[i][0]
        i=i+1
    i = 0
    while i!=len(list):
        j = 0
        while j!=len(list):
            matrice[i][j] = getElem(file,i,j)
            j=j+1
        i=i+1
    i=0
    j=0
    while j!=len(matriceStudent):
        matrice[i][j]=getElemMatrice(matriceStudent,j,i)
        matrice[j][i]=getElemMatrice(matriceStudent,j,i)
        j=j+1
    return matrice

def createListeEtudiant(file):
    matrice=createMatrice(file)
    newMatrice = [[0 for j in range(0,2)] for i in range(0,len(matrice))]
    i=0
    while(i<len(matrice)):
        newMatrice[i][0]=i
        newMatrice[i][1]=matrice[i][0]
        i=i+1
    return newMatrice

def getIdStudent(file, i):
    listeEtudiant = createListeEtudiant(file)
    return listeEtudiant[i][1]


#matrice = createMatrice('../preferences.csv')
#print(matrice)

def matricePref(file):
    list=getFileContent(file)
    matrice = [[0 for j in range(0,len(list)-1)] for i in range(0,len(list)-1)]
    i=0
    while i!=len(list)-1:
        j = 0
        while j!=len(list)-1:
            matrice[i][j] = getElem(file,i+1,j+1)
            j=j+1
        i=i+1
    return matrice
