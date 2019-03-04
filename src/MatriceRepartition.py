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

file = '../preferences.csv'
