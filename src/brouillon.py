import MatriceBinome
import CSVReader
matriceBinome=[]
occ=0
n=0

if (MatriceBinome.verifOccurence(occ) == True):
    copieMatriceBinome = matriceBinome
    matriceBinome = MatriceBinome.triMatriceBinome(matriceBinome, "AR")
    occ = MatriceBinome.occurrenceEleve(matriceBinome,n-1)
    print(occ)
    print(matriceBinome)
    if (MatriceBinome.verifOccurence(occ) == False):
        matriceBinome = copieMatriceBinome
    else:
        copieMatriceBinome = matriceBinome
        matriceBinome = MatriceBinome.triMatriceBinome(matriceBinome, "I")
        occ = MatriceBinome.occurrenceEleve(matriceBinome, n-1)
        print(occ)
        print(matriceBinome)
        if (MatriceBinome.verifOccurence(occ) == False):
            matriceBinome = copieMatriceBinome


print(len(matriceBinome))
print(MatriceBinome.occurrenceEleve(matriceBinome, 4))
matrice3=MatriceBinome.triMatriceBinome(matriceBinome,'B')
print(MatriceBinome.occurrenceEleve(matrice3,4))
print(MatriceBinome.verifOccurence(MatriceBinome.occurrenceEleve(matrice3,4)))



matriceBinome = [[0 for j in range(0,4)] for i in range(0,6)]
matrice2 = [['', '1', '2', '3', '4'],['1', '-1', 'AB', 'TB', 'B'],['2', 'P', '-1', 'B', 'B'],['3', 'AB', 'B', '-1', 'I'],['4', 'B', 'B', 'B', '-1']]
n = 2
m = 1
j = 0
while j!=(6) and n!=(len(matrice2)):
    matriceBinome[j][0] = CSVReader.getElemMatrice(matrice2,m,0)
    matriceBinome[j][1] = CSVReader.getElemMatrice(matrice2,n,0)
    matriceBinome[j][2] = CSVReader.getElemMatrice(matrice2,m,n)
    matriceBinome[j][3] = CSVReader.getElemMatrice(matrice2,n,m)
    j = j+1
    if (n == len(matrice2)-1 and m != len(matrice2)-1):
        m=m+1
        n=m+1
    else:
        n=n+1
print(triMatriceBinome(matriceBinome,'AB'))
