#automatic field verifier

#Assumes that 0 is identity for underlying additive group
#Assumes that 1 is identity for distributive gorup

import findingRings as fr

def fieldVerify(gMatrix,rMatrix):
    #Identity

    i = 0
    while i < len(rMatrix):
        if rMatrix[i][1] != i:
            return False
        i+=1
    i = 0
    while i < len(rMatrix):
        if rMatrix[1][i] != i:
            return False
        i+=1

    #Invertible (Except for 0)

    i = 1
    while i < len(rMatrix):
        j = 0
        tau = 0
        while j < len(rMatrix[i]):
            if rMatrix[i][j] == 1:
                tau+=1
            j+=1
        if tau != 1:
            return False
        i+=1

     #distributive and associativie

    i = 0
    while i < len(rMatrix):
        j = 0
        while j < len(rMatrix):
            k = 0
            while k < len(rMatrix):
                if rMatrix[i][rMatrix[j][k]] != rMatrix[rMatrix[i][j]][k]: #Associative Check
                    return False
                if rMatrix[i][gMatrix[j][k]] != gMatrix[rMatrix[i][j]][rMatrix[i][k]]: #Distributive Check
                    return False
                k+=1
            j+=1
        i+=1
    return True

def itemizeF(Grp, er, locationlist):
    i = 0
    if len(locationlist) <= 1:
        
        while i < len(er): #for each value

            er[locationlist[0][0]][locationlist[0][1]] = i # set it to the possible value
            if fieldVerify(Grp, er):
                print fr.textize(er)

            i+=1
    else:
        while i < len(er): # for each value
            er[locationlist[0][0]][locationlist[0][1]] = i # set it to the possible value
            itemizeF(Grp, er, locationlist[1:]) #cut out the current entry and itemize that shit

            i+=1

def fieldG(Grp): #Given a group we brute force search every possible ring on that group
    w = len(Grp) #side length of ring table

    #create table of all zeroes and the ring is upheld.
    er = []
    tau = []
    i = 0
    while i < w:
        j = 0
        er.append([])
        while j < w:
            if i == 1:
                er[i].append(j)
            elif j ==1:
                er[i].append(i)
            else:
                tau.append([i,j])
                er[i].append(0)
            j+=1
        i+=1

    #Brute force search time
    
    itemizeF(Grp, er, tau)

TestGroup2 = [[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2]]
TestGroup3 = [[0,1,2],[1,2,0],[2,0,1]]
#fieldG(TestGroup2)

if __name__=='__main__':
    print fieldG(fr.TestGroup)




    
