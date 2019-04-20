import CSVReader
import MatriceBinome
import MatriceTrinome
import MatriceRepartition
import csv
import sys


launch_mode = "DEFAULT"
number_results_max = -1
ext = ""

for arg in sys.argv[1:]:
    sub_arg = arg[2:]
    if sub_arg[:3] == "arg":
        launch_mode = sub_arg[4:]
    elif sub_arg[:3] == "num":
        number_results_max = sub_arg[7:]
    elif sub_arg[:3] == "ext":
        ext = sub_arg[4:]

number_results_max = int(number_results_max)
file = "../DONNEES/preferences" + ext + ".csv"

def main():

    matricePref = CSVReader.createMatrice(file)
    matriceP = CSVReader.matricePref(file)
    matriceB = MatriceBinome.createMatriceBinome(file)
    matriceT = MatriceTrinome.createMatriceTrinome(file)

    matriceRepartition = MatriceRepartition.createMatriceRepartition(file)
    n = len(matricePref) - 1
    b = 0 #Nbre de binomes
    t = 0 #Nbre de trinomes
    p = 0 #Nbre de projets n>36
    if(n>36):
        p=18
        t=n-36
        b=p-t
    else:
        if(n%2==1):
            p=n//2
            t=1
            b=(n//2)-1
        else:
            p=n//2
            t=0
            b=p
    occB = MatriceBinome.occurrenceEleve(matriceB,n)
    occT = MatriceTrinome.occurenceEleveTrinome(matriceT,n)
    nbreRepartiton=1

    compteur=0
    while(compteur<nbreRepartiton):
        newMatriceTrinome=MatriceTrinome.newMatriceTrinome(matriceT)
        newMatriceBinome=MatriceBinome.newMatriceBinome(matriceB)
        compteur=b+t
        nb=0
        result=[0 for i in range(0,int(compteur))]
        r=-1
        result=triCritique(matriceB, matriceT, newMatriceBinome, newMatriceTrinome, n, b, t, p, occB, result, r, int(nb))
        matriceR=MatriceRepartition.matriceR(result,file,b,t,p)
        i=0
        print("Repartition des groupes : ")
        while(i<len(result)):
            if(len(result[i])==3):
                print("Groupe " + str(i+1) + " : " + str(result[i][0]) + ", " + str(result[i][1]) + ", " + str(result[i][2]))
            else:
                print("Groupe " + str(i+1) + " : " + str(result[i][0]) + ", " + str(result[i][1]) + ", " + str(result[i][2]) + ", " + str(result[i][3]))
            i=i+1
        writeDoc(result)


def writeDoc(result):
    line = ""
    i=0
    while(i<len(result)):
        j=0
        while(j<len(result[i])-1):
            line = line + str(CSVReader.getIdStudent(file,result[i][j])) + " "
            j=j+1
        #line = line + result[i][j] + " "
        line = line + "; "
        i=i+1
    line = line.split(";")
    print(line)

    with open('../RESULTATS/DD.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines.append(line)

    with open('../RESULTATS/DD.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)










def findBinomeC(critique, matriceBinome):
    k=0
    while(k<len(matriceBinome) and matriceBinome[k][0]!=critique and matriceBinome[k][1]!=critique):
        k=k+1
    if(matriceBinome[k-1][0]==critique):
        return matriceBinome[k-1][1],matriceBinome[k-1][0]
    else:
        return matriceBinome[k-1][0],matriceBinome[k-1][1]



def findBestBinome(newMatrice):
    j=0
    k=0
    allBestBinome=[]
    while(j<len(newMatrice)):
        if(newMatrice[k][2]<newMatrice[j][2]):
            k=j
        j=j+1
    allBestBinome.append(newMatrice[k])
    j=0
    while(j<len(newMatrice)):
        if(newMatrice[j][2]==newMatrice[k][2] and k!=j):
            allBestBinome.append(newMatrice[j])
        j=j+1
    return allBestBinome

def findBestTrinome(newMatrice):
    j=0
    k=0
    allBestTrinome=[]
    while(j<len(newMatrice)):
        if(newMatrice[k][3]<newMatrice[j][3]):
            k=j
        j=j+1
    allBestTrinome.append(newMatrice[k])
    j=0
    while(j<len(newMatrice)):
        if(newMatrice[j][2]==newMatrice[k][2] and k!=j):
            allBestTrinome.append(newMatrice[j])
        j=j+1
    return allBestTrinome

def findBest(matriceB, matriceT):
    allBestBinome=findBestBinome(matriceB)
    oneBestBinone=allBestBinome[0]
    allBestTrinome=findBestTrinome(matriceT)
    oneBestTrinome=allBestTrinome[0]
    if(len(allBestBinome)==1):
        return allBestBinome
    else:
        trin=oneBestTrinome[3]
        bin=oneBestTrinome[2]
        if (trin>bin):
            return allBestTrinome
        else:
            return allBestBinome


def rechercheTrinomeCritique(critique, bin, matriceB, occ):
    estCritique=False
    i=0
    while(i<len(matriceB) and not(estCritique)):
        if(matriceB[i][0]==bin and matriceB[i][1]!=critique):
            estCritique=MatriceBinome.estCritique(occ,matriceB[i][1])
        if(matriceB[i][1]==bin and matriceB[i][0]!=critique):
            estCritique=MatriceBinome.estCritique(occ,matriceB[i][0])
        i=i+1
    if(estCritique):
        return i-1
    else:
        return -1

def rechercheTrinome(critique, bin, matriceB):
    i=0
    while(i<len(matriceB)):
        if((matriceB[i][0]==critique and matriceB[i][1]!=bin) or (matriceB[i][0]==bin and matriceB[i][1]!=critique)):
            return matriceB[i][1]
        elif((matriceB[i][1]==critique and matriceB[i][0]!=bin) or (matriceB[i][1]==bin and matriceB[i][0]!=critique)):
            return matriceB[i][0]
        i=i+1



def triCritique(matriceB, matriceT, newMatriceBinome, newMatriceTrinome, n, b, t, p, occ, result, r, nb):
    compteur=b+t
    while(compteur!=0):
        compteur=compteur-1
        critique=MatriceBinome.critique(occ)
        if(critique!=-1):
            critique,bin=findBinomeC(critique,matriceB)
            indiceTrinome=rechercheTrinomeCritique(critique,bin,matriceB,occ)
            if(MatriceBinome.estCritique(occ, MatriceBinome.critique(occ))):
                MatriceBinome.binomeTri(occ, critique, bin)
                b=b-1
                binome=[critique,bin,MatriceBinome.binomeApp(matriceB,critique,bin)]
                result[nb]=binome
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceT=MatriceTrinome.supprTrinome2(matriceT,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceTrinome=MatriceTrinome.supprTrinome2(newMatriceTrinome,critique,bin)
            elif(indiceTrinome!=-1):
                MatriceTrinome.trinomeTri(occ,critique,bin,indiceTrinome)
                t=t-1
                trinome=[critique,bin,indiceTrinome,MatriceTrinome.trinomeApp(matriceB,critique,bin,indiceTrinome)]
                result[nb]=trinome
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceB=MatriceBinome.supprBinome(matriceB,critique,indiceTrinome)
                matriceB=MatriceBinome.supprBinome(matriceB,indiceTrinome,bin)
                matriceT=MatriceTrinome.supprTrinome3(matriceT,critique,bin,indiceTrinome)
                newMatriceTrinome=MatriceTrinome.supprTrinome3(newMatriceTrinome,critique,bin,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,indiceTrinome,bin)
            elif(b!=0):
                MatriceBinome.binomeTri(occ,critique,bin)
                b=b-1
                binome=[critique,bin,MatriceBinome.binomeApp(matriceB,critique,bin)]
                result[nb]=binome
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceT=MatriceTrinome.supprTrinome2(matriceT,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceTrinome=MatriceTrinome.supprTrinome2(newMatriceTrinome,critique,bin)
            else:
                indiceTrinome=rechercheTrinome(critique,bin,matriceB)
                MatriceTrinome.trinomeTri(occ,critique,bin,indiceTrinome)
                t=t-1
                trinome=[critique,bin,indiceTrinome,MatriceTrinome.trinomeApp(matriceB,critique,bin,indiceTrinome)]
                result[nb]=trinome
                newMatriceTrinome=MatriceTrinome.supprTrinome3(newMatriceTrinome,critique,bin,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,indiceTrinome,bin)
                matriceT=MatriceTrinome.supprTrinome3(matriceT,critique,bin,indiceTrinome)
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceB=MatriceBinome.supprBinome(matriceB,critique,indiceTrinome)
                matriceB=MatriceBinome.supprBinome(matriceB,indiceTrinome,bin)
        else:
            best=calculBest(t,b,newMatriceBinome,newMatriceTrinome)
            if(len(best)==1):
                if(len(best[0])==3):
                    MatriceBinome.binomeTri(occ,best[0][0],best[0][1])
                    b=b-1
                    binome=[best[0][0],best[0][1],MatriceBinome.binomeApp(matriceB,best[0][0],best[0][1])]
                    result[nb]=binome
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0][0],best[0][1])
                    newMatriceTrinome=MatriceTrinome.supprTrinome2(newMatriceTrinome,best[0][0],best[0][1])
                    matriceB=MatriceBinome.supprBinome(matriceB,best[0][0],best[0][1])
                    matriceT=MatriceTrinome.supprTrinome2(matriceT,best[0][0],best[0][1])
                else:
                    t=t-1
                    trinome=[best[0][0],best[0][1],best[0][2],MatriceTrinome.trinomeApp(matriceB,best[0][0],best[0][1],best[0][2])]
                    result[nb]=trinome
                    matriceB=MatriceBinome.supprBinome(matriceB,best[0][0],best[0][1])
                    matriceB=MatriceBinome.supprBinome(matriceB,best[0][0],best[0][2])
                    matriceB=MatriceBinome.supprBinome(matriceB,best[0][1],best[0][2])
                    matriceT=MatriceTrinome.supprTrinome3(matriceT,best[0][0],best[0][1],best[0][2])
                    newMatriceTrinome=MatriceTrinome.supprTrinome3(newMatriceTrinome,best[0][0],best[0][1],best[0][2])
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0][0],best[0][1])
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0][0],best[0][2])
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0][1],best[0][2])
            else:
                for i in best:
                    if(t==0):
                        MatriceBinome.binomeTri(occ,i[0],i[1])
                        b=b-1
                        binome=[i[0],i[1],MatriceBinome.binomeApp(matriceB,i[0],i[1])]
                        result[nb]=binome
                        newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[0],i[1])
                        newMatriceTrinome=MatriceTrinome.supprTrinome2(newMatriceTrinome,i[0],i[1])
                        matriceB=MatriceBinome.supprBinome(matriceB,i[0],i[1])
                        matriceT=MatriceTrinome.supprTrinome2(matriceT,i[0],i[1])
                    else:
                        if(b==0):
                            MatriceTrinome.trinomeTri(occ,i[0],i[1],i[2])
                            t=t-1
                            trinome=[i[0],i[1],i[2],MatriceTrinome.trinomeApp(matriceT,i[0],i[1],i[2])]
                            result[nb]=trinome
                            newMatriceTrinome=MatriceTrinome.supprTrinome3(newMatriceTrinome,i[0],i[1],i[2])
                            newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[0],i[1])
                            newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[0],i[2])
                            newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[1],i[1])
                            matriceT=MatriceTrinome.supprTrinome3(matriceT,i[0],i[1],i[2])
                            matriceB=MatriceBinome.supprBinome(matriceB,i[0],i[1])
                            matriceB=MatriceBinome.supprBinome(matriceB,i[0],i[2])
                            matriceB=MatriceBinome.supprBinome(matriceB,i[1],i[1])
                        else:
                            if(len(i)==3):
                                MatriceBinome.binomeTri(occ,i[0],i[1])
                                b=b-1
                                binome=[i[0],i[1],MatriceBinome.binomeApp(matriceB,i[0],i[1])]
                                result[nb]=binome
                                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[0],i[1])
                                newMatriceTrinome=MatriceTrinome.supprTrinome2(newMatriceTrinome,i[0],i[1])
                                matriceB=MatriceBinome.supprBinome(matriceB,i[0],i[1])
                                matriceT=MatriceTrinome.supprTrinome2(matriceT,i[0],i[1])
                            else:
                                MatriceTrinome.trinomeTri(occ,i[0],i[1],i[2])
                                t=t-1
                                trinome=[i[0],i[1],i[2],MatriceTrinome.trinomeApp(matriceT,i[0],i[1],i[2])]
                                result[nb]=trinome
                                newMatriceTrinome=MatriceTrinome.supprTrinome3(newMatriceTrinome,i[0],i[1],i[2])
                                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[0],i[1])
                                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[0],i[2])
                                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,i[1],i[1])
                                matriceT=MatriceTrinome.supprTrinome3(matriceT,i[0],i[1],i[2])
                                matriceB=MatriceBinome.supprBinome(matriceB,i[0],i[1])
                                matriceB=MatriceBinome.supprBinome(matriceB,i[0],i[2])
                                matriceB=MatriceBinome.supprBinome(matriceB,i[1],i[1])
                    r=triCritique(matriceB, matriceT, newMatriceBinome, newMatriceTrinome, n, b, t, p, occ, result, r, nb+1)
                    return(r)
        nb=nb+1
    return bestRepartition(result,r)

def calculBest(t,b,newMatriceBinome,newMatriceTrinome):
    if(t==0):
        best=findBestBinome(newMatriceBinome)
    else:
        if(b==0):
            best=findBestTrinome(newMatriceTrinome)
        else:
            best=findBest(newMatriceBinome,newMatriceTrinome)
    return best

def bestRepartition(result, r):
    if(r==-1):
        return result
    else:
        m=0
        n=0
        i=0
        while i<len(result):
            if(len(result[i])==3):
                if(result[i][2]=='TB'):
                    m=m+5
                elif(result[i][2]=='B'):
                    m=m+4
                elif(result[i][2]=='AB'):
                    m=m+3
                elif(result[i][2]=='P'):
                    m=m+2
                elif(result[i][2]=='I'):
                    m=m+1
            else:
                if(result[i][3]=='TB'):
                    m=m+5
                elif(result[i][3]=='B'):
                    m=m+4
                elif(result[i][3]=='AB'):
                    m=m+3
                elif(result[i][3]=='P'):
                    m=m+2
                elif(result[i][3]=='I'):
                    m=m+1
            i=i+1
        i=0
        while i<len(r):
            if(len(r[i])==3):
                if(r[i][2]=='TB'):
                    n=n+5
                elif(r[i][2]=='B'):
                    n=n+4
                elif(r[i][2]=='AB'):
                    n=n+3
                elif(r[i][2]=='P'):
                    n=n+2
                elif(r[i][2]=='I'):
                    n=n+1
            else:
                if(r[i][3]=='TB'):
                    n=n+5
                elif(r[i][3]=='B'):
                    n=n+4
                elif(r[i][3]=='AB'):
                    n=n+3
                elif(r[i][3]=='P'):
                    n=n+2
                elif(r[i][3]=='I'):
                    n=n+1
            i=i+1
        if(m>n):
            return result
        else:
            return r




main()


def triBinome(matriceB, matriceT, newMatriceBinome, newMatriceTrinome, occ, b, best):
    MatriceBinome.binomeTri(occ,best[0],best[1])
    b=b-1
    binome=[best[0],best[1],MatriceBinome.binomeApp(matriceB,best[0],best[1])]
    result=binome
    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[1])
    newMatriceTrinome=MatriceTrinome.supprTrinome2(newMatriceTrinome,best[0],best[1])
    matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[1])
    matriceT=MatriceTrinome.supprTrinome2(matriceT,best[0],best[1])
    return matriceB, matriceT, newMatriceBinome, newMatriceTrinome

def triTrinome(matriceB, matriceT, newMatriceBinome, newMatriceTrinome, occ, t, best):
    MatriceTrinome.trinomeTri(occ,best[0],best[1],best[2])
    t=t-1
    trinome=[best[0],best[1],best[2],MatriceTrinome.trinomeApp(matriceT,best[0],best[1],best[2])]
    result=trinome
    newMatriceTrinome=MatriceTrinome.supprTrinome3(newMatriceTrinome,best[0],best[1],best[2])
    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[1])
    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[2])
    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[1],best[1])
    matriceT=MatriceTrinome.supprTrinome3(matriceT,best[0],best[1],best[2])
    matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[1])
    matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[2])
    matriceB=MatriceBinome.supprBinome(matriceB,best[1],best[1])
    return matriceB, matriceT, newMatriceBinome, newMatriceTrinome
