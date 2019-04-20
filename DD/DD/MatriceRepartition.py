import CSVReader
import MatriceBinome

def createMatriceRepartition(file):
    matriceBinome = MatriceBinome.createMatriceBinome(file)
    list = CSVReader.getFileContent(file)
    n = len(list)-1
    matriceRepartition = [[0 for i in range(0,n)] for j in range(0,n)]
    return matriceRepartition


def addBinome(a, b, nbreBinome, nbreTrinome, nbreProjet, matriceRepartition):
    if(nbreBinome+nbreTrinome<nbreProjet):
        matriceRepartition[b-1][a-1]=1
        matriceRepartition[a-1][b-1]=1
        nbreBinome=nbreBinome+1
    return nbreBinome, matriceRepartition

def addTrinome(a, b, c, nbreBinome, nbreTrinome, nbreProjet, matriceRepartition):
    if(nbreBinome+nbreTrinome<nbreProjet):
        matriceRepartition[b-1][a-1]=1
        matriceRepartition[c-1][a-1]=1
        matriceRepartition[a-1][b-1]=1
        matriceRepartition[c-1][b-1]=1
        matriceRepartition[a-1][c-1]=1
        matriceRepartition[b-1][c-1]=1
        nbreTrinome=nbreTrinome+1
    return nbreTrinome, matriceRepartition

def matriceR(result, file, nbreB, nbreT, nbreP):
    i=0
    matriceRepartion=createMatriceRepartition(file)
    while(i<len(result)):
        if(len(result[i])==2):
            nbreB, matriceRepartion = addBinome(result[i][0],result[i][1],nbreB, nbreT, nbreP,matriceRepartion)
        else:
            nbreT, matriceRepartion = addTrinome(result[i][0],result[i][1],result[i][2],nbreB, nbreT, nbreP,matriceRepartion)
        i=i+1
    return matriceRepartion

file = '../preferences.csv'
