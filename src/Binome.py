import CSVReader
import MatriceBinome
import MatriceRepartition
import random

file = '../DONNEES/preferences10.csv'

def main(file):
    matricePref = CSVReader.createMatrice(file)
    matriceP = CSVReader.matricePref(file)
    matriceBinome = MatriceBinome.createMatriceBinome(file)
    matriceB = MatriceBinome.triMatriceBinome(matriceBinome, "AR")
    print(matriceB)
    matriceT = MatriceBinome.createMatriceTrinome(file)

    matriceTrinome = MatriceBinome.triMatriceTrinome(matriceT, "AR")

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
            p=n/2
            t=1
            b=(n/2)-1
        else:
            p=n/2
            t=0
            b=p
    nbreBinom=0
    nbreTrinom=0
    occ = MatriceBinome.occurrenceEleve(matriceBinome,n)

    while(conditionArret(matriceRepartition) == False):
        k=MatriceBinome.critique(occ)
        newMatriceT=newMatriceTrinome(matriceTrinome)
        newMatriceB=newMatriceBinome(matriceBinome)
        triCritique(matriceB, matriceTrinome, newMatriceB, newMatriceT, matriceRepartition, n, b, t, p, nbreBinom, nbreTrinom, occ)


def conditionArret(matriceRep):
    i=0
    res=True
    while (i<len(matriceRep)):
        j=0
        somme=0
        while (j<len(matriceRep)):
            somme = somme+matriceRep[i][j]
            j=j+1
        if (somme == 0):
            res=False
        i=i+1
    return res

def findBinomeC(critique, matriceBinome):
    k=0
    while(k<len(matriceBinome) and matriceBinome[k][0]!=critique and matriceBinome[k][1]):
        k=k+1
    if(k!=len(matriceBinome)):
        if(matriceBinome[k][0]==critique):
            return matriceBinome[k][1]
        else:
            return matriceBinome[k][0]
    else:
        return -1

def newMatriceBinome(matriceBinome):
    newMatrice = [[0 for i in range(0,3)]for i in range (0,len(matriceBinome))]
    j=0
    while(j<len(matriceBinome)):
        k=0
        while(k<len(matriceBinome)):
           m=0
           if(matriceBinome[k][2]=='TB'):
               m=m+5
           if(matriceBinome[k][3]=='TB'):
               m=m+5
           if(matriceBinome[k][2]=='B'):
               m=m+4
           if(matriceBinome[k][3]=='B'):
               m=m+4
           if(matriceBinome[k][2]=='AB'):
               m=m+3
           if(matriceBinome[k][3]=='AB'):
               m=m+3
           if(matriceBinome[k][2]=='P'):
               m=m+2
           if(matriceBinome[k][3]=='P'):
               m=m+2
           if(matriceBinome[k][2]=='I'):
               m=m+1
           if(matriceBinome[k][3]=='I'):
               m=m+1
           newMatrice[k][0]=matriceBinome[k][0]
           newMatrice[k][1]=matriceBinome[k][1]
           newMatrice[k][2]=m
           k=k+1
        j=j+1
    j=1
    k=j
    return newMatrice

def newMatriceTrinome(matriceT):
    newMatrice = [[0 for i in range(0,4)]for i in range (0,len(matriceT))]
    j=0
    while(j<len(matriceT)):
        k=0
        while(k<len(matriceT)):
            m=0
            if(matriceT[k][3]=='TB'):
                m=m+5
            if(matriceT[k][4]=='TB'):
                m=m+5
            if(matriceT[k][5]=='TB'):
                m=m+5
            if(matriceT[k][6]=='TB'):
                m=m+5
            if(matriceT[k][7]=='TB'):
                m=m+5
            if(matriceT[k][8]=='TB'):
                m=m+5
            if(matriceT[k][3]=='B'):
                m=m+4
            if(matriceT[k][4]=='B'):
                m=m+4
            if(matriceT[k][5]=='B'):
                m=m+4
            if(matriceT[k][6]=='B'):
                m=m+4
            if(matriceT[k][7]=='B'):
                m=m+4
            if(matriceT[k][8]=='B'):
                m=m+4
            if(matriceT[k][3]=='AB'):
                m=m+3
            if(matriceT[k][4]=='AB'):
                m=m+3
            if(matriceT[k][5]=='AB'):
                m=m+3
            if(matriceT[k][6]=='AB'):
                m=m+3
            if(matriceT[k][7]=='AB'):
                m=m+3
            if(matriceT[k][8]=='AB'):
                m=m+3
            if(matriceT[k][3]=='P'):
                m=m+2
            if(matriceT[k][4]=='P'):
                m=m+2
            if(matriceT[k][5]=='P'):
                m=m+2
            if(matriceT[k][6]=='P'):
                m=m+2
            if(matriceT[k][7]=='P'):
                m=m+2
            if(matriceT[k][8]=='P'):
                m=m+2
            if(matriceT[k][3]=='I'):
                m=m+1
            if(matriceT[k][4]=='I'):
                m=m+1
            if(matriceT[k][5]=='I'):
                m=m+1
            if(matriceT[k][6]=='I'):
                m=m+1
            if(matriceT[k][7]=='I'):
                m=m+1
            if(matriceT[k][8]=='I'):
                m=m+1
            newMatrice[k][0]=matriceT[k][0]
            newMatrice[k][1]=matriceT[k][1]
            newMatrice[k][2]=matriceT[k][2]
            newMatrice[k][3]=m
            k=k+1
        j=j+1
    return newMatrice

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
        if(newMatrice[j][2]==newMatrice[k][2]):
            allBestBinome.append(newMatrice[j])
        j=j+1
    random.shuffle(allBestBinome)
    k=random.randint(1,len(allBestBinome)-1)
    if(k!=0 or len(newMatrice)!=0):
        bestBinome=allBestBinome[k]
    else:
        bestBinome=-1
    return bestBinome

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
        if(newMatrice[j][2]==newMatrice[k][2]):
            allBestTrinome.append(newMatrice[j])
        j=j+1
    random.shuffle(allBestTrinome)
    k=random.randint(1,len(allBestTrinome)-1)
    if(k!=0 or len(newMatrice)!=0):
        bestTrinome=allBestTrinome[k]
    else:
        bestTrinome=-1
    return bestTrinome

def findBest(matriceB, matriceT):
    bestBinome=findBestBinome(matriceB)
    bestTrinome=findBestTrinome(matriceT)
    if(bestTrinome==-1):
        return findBestBinome(matriceB)
    else:
        trin=bestTrinome[3]/4
        bin=bestBinome[2]/2
        if (trin>bin):
            return findBestTrinome(matriceT)
        else:
            return findBestBinome(matriceB)


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

def trinomeApp(matriceB,critique,bin,trin):
    apprec1=binomeApp(matriceB,critique,bin)
    apprec2=binomeApp(matriceB,critique,trin)
    apprec3=binomeApp(matriceB,bin,trin)
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

def sumTaille2(a):
    return (a*(a-1))/2

def sumTaille3(a):
    return (a*(a-1)*(a-2))/6


def triCritique(matriceB, matriceT, newMatriceBinome, newMatriceTrinome, matriceR, n, b, t, p, nbreBinom, nbreTrinom, occ):
    compteur=b+t
    result=[0 for i in range(0,compteur)]
    nb=0
    while(compteur!=0):
        compteur=compteur-1
        critique=MatriceBinome.critique(occ)
        if(critique!=-1):
            bin=findBinomeC(critique,matriceB)
            indiceTrinome=rechercheTrinomeCritique(critique,bin,matriceB,occ)
            if(MatriceBinome.estCritique(occ, bin)):
                nbreBinom, matriceR = MatriceRepartition.addBinome(critique, bin, nbreTrinom, nbreBinom, p, matriceR)
                MatriceBinome.binomeTri(occ, critique, bin)
                b=b-1
                binome=[critique,bin,binomeApp(matriceB,critique,bin)]
                result[nb]=binome
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceT=MatriceBinome.supprTrinome2(matriceT,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceTrinome=MatriceBinome.supprTrinome2(newMatriceTrinome,critique,bin)
            elif(indiceTrinome!=-1):
                nbreTrinom, matriceR = MatriceRepartition.addTrinome(critique,bin,indiceTrinome,nbreBinom,nbreTrinom,p,matriceR)
                MatriceBinome.trinomeTri(occ,critique,bin,indiceTrinome)
                t=t-1
                trinome=[critique,bin,indiceTrinome,trinomeApp(matriceT,critique,bin,indiceTrinome)]
                result[nb]=trinome
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceB=MatriceBinome.supprBinome(matriceB,critique,indiceTrinome)
                matriceB=MatriceBinome.supprBinome(matriceB,indiceTrinome,bin)
                matriceT=MatriceBinome.supprTrinome3(matriceT,critique,bin,indiceTrinome)
                newMatriceTrinome=MatriceBinome.supprTrinome3(newMatriceTrinome,critique,bin,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,indiceTrinome,bin)
            elif(b!=0):
                nbreBinom, matriceR = MatriceRepartition.addBinome(critique,bin,nbreBinom,nbreTrinom,p,matriceR)
                MatriceBinome.binomeTri(occ,critique,bin)
                b=b-1
                binome=[critique,bin,binomeApp(matriceB,critique,bin)]
                result[nb]=binome
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceT=MatriceBinome.supprTrinome2(matriceT,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceTrinome=MatriceBinome.supprTrinome2(newMatriceTrinome,critique,bin)
            else:
                indiceTrinome=rechercheTrinome(critique,bin,matriceB)
                nbreTrinom, matriceR = MatriceRepartition.addTrinome(critique,bin,indiceTrinome,nbreBinom,nbreTrinom,p,matriceR)
                MatriceBinome.trinomeTri(occ,critique,bin,indiceTrinome)
                t=t-1
                trinome=[critique,bin,indiceTrinome,trinomeApp(matriceT,critique,bin,indiceTrinome)]
                result[nb]=trinome
                newMatriceTrinome=MatriceBinome.supprTrinome3(newMatriceTrinome,critique,bin,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,bin)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,critique,indiceTrinome)
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,indiceTrinome,bin)
                matriceT=MatriceBinome.supprTrinome3(matriceT,critique,bin,indiceTrinome)
                matriceB=MatriceBinome.supprBinome(matriceB,critique,bin)
                matriceB=MatriceBinome.supprBinome(matriceB,critique,indiceTrinome)
                matriceB=MatriceBinome.supprBinome(matriceB,indiceTrinome,bin)
        else:
            if(t==0):
                best=findBestBinome(newMatriceBinome)
                nbreBinom, matriceR = MatriceRepartition.addBinome(best[0],best[1],nbreBinom,nbreTrinom,p,matriceR)
                MatriceBinome.binomeTri(occ,best[0],best[1])
                b=b-1
                binome=[best[0],best[1],binomeApp(matriceB,best[0],best[1])]
                result[nb]=binome
                newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[1])
                newMatriceTrinome=MatriceBinome.supprTrinome2(newMatriceTrinome,best[0],best[1])
                matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[1])
                matriceT=MatriceBinome.supprTrinome2(matriceT,best[0],best[1])
            else:
                if(b==0):
                    best=findBestTrinome(newMatriceTrinome)
                    nbreTrinom, matriceR = MatriceRepartition.addTrinome(best[0],best[1],best[2],nbreBinom,nbreTrinom,p,matriceR)
                    MatriceBinome.trinomeTri(occ,best[0],best[1],best[2])
                    t=t-1
                    trinome=[best[0],best[1],best[2],trinomeApp(matriceT,best[0],best[1],best[2])]
                    result[nb]=trinome
                    newMatriceTrinome=MatriceBinome.supprTrinome3(newMatriceTrinome,best[0],best[1],best[2])
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[1])
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[2])
                    newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[1],best[1])
                    matriceT=MatriceBinome.supprTrinome3(matriceT,best[0],best[1],best[2])
                    matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[1])
                    matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[2])
                    matriceB=MatriceBinome.supprBinome(matriceB,best[1],best[1])
                else:
                    best=findBest(newMatriceBinome,newMatriceTrinome)
                    if(len(best)==3):
                        nbreBinom, matriceR = MatriceRepartition.addBinome(best[0],best[1],nbreBinom,nbreTrinom,p,matriceR)
                        MatriceBinome.binomeTri(occ,best[0],best[1])
                        b=b-1
                        binome=[best[0],best[1],binomeApp(matriceB,best[0],best[1])]
                        result[nb]=binome
                        newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[1])
                        newMatriceTrinome=MatriceBinome.supprTrinome2(newMatriceTrinome,best[0],best[1])
                        matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[1])
                        matriceT=MatriceBinome.supprTrinome2(matriceT,best[0],best[1])
                    else:
                        nbreTrinom, matriceR = MatriceRepartition.addTrinome(best[0],best[1],best[2],nbreBinom,nbreTrinom,p,matriceR)
                        MatriceBinome.trinomeTri(occ,best[0],best[1],best[2])
                        t=t-1
                        trinome=[best[0],best[1],best[2],trinomeApp(matriceT,best[0],best[1],best[2])]
                        result[nb]=trinome
                        newMatriceTrinome=MatriceBinome.supprTrinome3(newMatriceTrinome,best[0],best[1],best[2])
                        newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[1])
                        newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[0],best[2])
                        newMatriceBinome=MatriceBinome.supprBinome(newMatriceBinome,best[1],best[1])
                        matriceT=MatriceBinome.supprTrinome3(matriceT,best[0],best[1],best[2])
                        matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[1])
                        matriceB=MatriceBinome.supprBinome(matriceB,best[0],best[2])
                        matriceB=MatriceBinome.supprBinome(matriceB,best[1],best[1])
        nb=nb+1
        print(matriceB)
    i=0
    print("Repartition des groupes : ")
    while(i<len(result)):
        if(len(result[i])==3):
            print("Groupe " + str(i+1) + " : " + str(result[i][0]) + ", " + str(result[i][1]) + ", " + str(result[i][2]))
        else:
            print("Groupe " + str(i+1) + " : " + str(result[i][0]) + ", " + str(result[i][1]) + ", " + str(result[i][2]) + ", " + str(result[i][3]))
        i=i+1






main(file)


