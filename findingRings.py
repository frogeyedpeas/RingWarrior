#Define a generalized ring
#set X
# u1 in X s.t. u1(a,b) in X- closed 
# for each a there is unique t such that u1(a,t) = e - unique total identity
# there exists e such that u1(a,e) = u1(e,a) -invertible
# u1(u1(a,b),c) = u1(a,u1(b,c)) - associative
# u2 in X s.t. u2(a,b) in X - closed
# u2(c, u1(a,b)) = u1(u2(c,a), u2(c,b)) - distributive
# u2(t,a) = u2(a,t) = a  #unique total identity
# u2(u2(a,b),c) = u2(a,u2(b,c))  associative

#Each Ring has an underlying Group but they themselves form another structure over it

def textize(matrix):
    i = 0
    tau = ""
    while i < len(matrix):
        s = ""
        j = 0
        while j < len(matrix[i]):
            s+=(str(matrix[i][j])+" ")
            j+=1
        i+=1
        tau += (s + "\n")
   
    return tau


def ringVerify(gMatrix, rMatrix): #single structure of group and ring:
    #if not (groupVerify(gMatrix)):
     #   return False

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
                

    
        

def groupVerify(matrix): #verifies if matrix in raw num form is valid
    #closure --> all elements are present
    #inverse --> every element has an inverse
    #identtiy --> there exists an element

    #Unique Inverse
    for rows in matrix:
        tau = 0
        
        for elements in rows:
            if elements == 0:
                tau +=1
        if tau != 1:
            return False

    #Property of Identity
    i = 0
    while i < len(matrix[0]):
        if matrix[0][i] != i:
            return False
        i+=1
    i = 0
    while i < len(matrix):
        if matrix[i][0] != i:
            return False
        i+=1

    #Associativity and Closure in One go:

    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix):
            k = 0
            while k < len(matrix):
              
                if matrix[matrix[i][j]][k] != matrix[i][matrix[j][k]]:
                    return False
               
                        
                k+=1
            j+=1
        i+=1
    return True

def itemize(Grp, er, locationlist):
    i = 0
    if len(locationlist) <= 1:
        
        while i < len(er): #for each value

            er[locationlist[0][0]][locationlist[0][1]] = i # set it to the possible value
            if ringVerify(Grp, er):
                print textize(er)

            i+=1
    else:
        while i < len(er): # for each value
            er[locationlist[0][0]][locationlist[0][1]] = i # set it to the possible value
            itemize(Grp, er, locationlist[1:]) #cut out the current entry and itemize that shit

            i+=1
            

def rngG(Grp): #Given a group we brute force search every possible ring on that group
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

    itemize(Grp, er, tau)
    

TestGroup = [[0,1,2,3,4,5],[1,0,4,5,2,3],[2,5,0,4,3,1],[3,4,5,0,1,2],[4,3,1,2,5,0],[5,2,3,1,0,4]]

TestGroup2 = [[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2]]

Enoch = [[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]]

TestGroup3 = [[0,1,2],[1,2,0],[2,0,1]]


print rngG(TestGroup)





        
