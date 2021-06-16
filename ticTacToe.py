#GLOBALS
ticTac=[[" "," "," "],[" "," "," "],[" "," "," "]]
mySym="X"
opSym="O"



def iswin(ticTac,sym):
    #horizontally
    for row,i in zip(ticTac,[0,1,2]):
        if row[0]==row[1] and row[1]==row[2] and row[2]==sym:
            return True
    
    
    #vertically
    newticTac=[[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
    #transpose the ticTacToe board
    for i in range(3):
        for j in range(3):
            newticTac[j][i]=ticTac[i][j]

    for column,i in zip(newticTac,[0,1,2]):
        if column[0]==column[1] and column[1]==column[2] and column[2]==sym:
            return True

    
    #diagonally
    diag1=[ticTac[0][0],ticTac[1][1],ticTac[2][2]]
    diag2=[ticTac[0][2],ticTac[1][1],ticTac[2][0]]
    for diag,i in zip([diag1,diag2],[0,1]):
            if  diag[0]==diag[1] and diag[1]==diag[2] and diag[2]==sym:
                return True
    return False

def heuristic_evaluation(ticTac,mySym,opSym):
    heuristicValues=[[0,0,0],
                     [0,0,0],
                     [0,0,0]]
    #horizontally
    for row,i in zip(ticTac,[0,1,2]):
        if row[0]==" " and row[1]==" " and row[2]==" ":
            heuristicValues[i][0]+=1
            heuristicValues[i][1]+=1
            heuristicValues[i][2]+=1
        elif (row[0]!=" " and row[1]==" " and row[2]==" " )or (row[0]==" " and row[1]!=" " and row[2]==" " ) or row[0]==" " and row[1]==" " and row[2]!=" " :
            heuristicValues[i][0]+=10
            heuristicValues[i][1]+=10
            heuristicValues[i][2]+=10
        elif (row[0]==mySym and row[1]==opSym and row[2]==" ") or (row[0]==mySym and row[1]==" "  and row[2]==opSym) or        (row[0]==" "  and row[1]==opSym  and row[2]==" ") or         (row[0]==" "  and row[1]==" "  and row[2]==opSym) or         (row[0]==opSym  and row[1]==mySym  and row[2]==" ") or         (row[0]==opSym  and row[1]==" "  and row[2]==mySym):
            heuristicValues[i][0]+=0
            heuristicValues[i][1]+=0
            heuristicValues[i][2]+=0
        elif (row[0]==opSym and row[1]==opSym and row[2]==" ") or        (row[0]==opSym and row[1]==" " and row[2]==opSym) or        (row[0]==" " and row[1]==opSym and row[2]==opSym):
            heuristicValues[i][0]+=100
            heuristicValues[i][1]+=100
            heuristicValues[i][2]+=100
        elif (row[0]==mySym and row[1]==mySym and row[2]==" ") or        (row[0]==mySym and row[1]==" " and row[2]==mySym) or        (row[0]==" " and row[1]==mySym and row[2]==mySym):
            heuristicValues[i][0]+=1000
            heuristicValues[i][1]+=1000
            heuristicValues[i][2]+=1000

    #vertically
    newticTac=[[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
    #transpose the ticTacToe board
    for i in range(3):
        for j in range(3):
            newticTac[j][i]=ticTac[i][j]

    for column,i in zip(newticTac,[0,1,2]):
        if  column[0]==" " and column[1]==" " and column[2]==" ":
            heuristicValues[0][i]+=1
            heuristicValues[1][i]+=1
            heuristicValues[2][i]+=1
        if (column[0]!=" " and column[1]==" " and column[2]==" " )or (column[0]==" " and column[1]!=" " and column[2]==" " ) or column[0]==" " and column[1]==" " and column[2]!=" " :
            heuristicValues[0][i]+=10
            heuristicValues[1][i]+=10
            heuristicValues[2][i]+=10
        if (column[0]==mySym and column[1]==opSym and column[2]==" ") or        (column[0]==mySym and column[1]==" "  and column[2]==opSym) or        (column[0]==" "  and column[1]==opSym  and column[2]==" ") or         (column[0]==" "  and column[1]==" "  and column[2]==opSym) or         (column[0]==opSym  and column[1]==mySym  and column[2]==" ") or         (column[0]==opSym  and column[1]==" "  and column[2]==mySym):
            heuristicValues[0][i]+=0
            heuristicValues[1][i]+=0
            heuristicValues[2][i]+=0
        if (column[0]==opSym and column[1]==opSym and column[2]==" ") or        (column[0]==opSym and column[1]==" " and column[2]==opSym) or        (column[0]==" " and column[1]==opSym and column[2]==opSym):
            heuristicValues[0][i]+=100
            heuristicValues[1][i]+=100
            heuristicValues[2][i]+=100
        if (column[0]==mySym and column[1]==mySym and column[2]==" ") or        (column[0]==mySym and column[1]==" " and column[2]==mySym) or        (column[0]==" " and column[1]==mySym and column[2]==mySym):
            heuristicValues[0][i]+=1000
            heuristicValues[1][i]+=1000
            heuristicValues[2][i]+=1000

    
    #diagonally
        diag1=[ticTac[0][0],ticTac[1][1],ticTac[2][2]]
        diag2=[ticTac[0][2],ticTac[1][1],ticTac[2][0]]
        for diag,i in zip([diag1,diag2],[0,1]):
            if  diag[0]==" " and diag[1]==" " and diag[2]==" ":
                if i==0:
                    heuristicValues[0][0]+=1
                    heuristicValues[1][1]+=1
                    heuristicValues[2][2]+=1
                else:
                    heuristicValues[0][2]+=1
                    heuristicValues[1][1]+=1
                    heuristicValues[2][0]+=1
                    
            elif (diag[0]!=" " and diag[1]==" " and diag[2]==" " )or (diag[0]==" " and diag[1]!=" " and diag[2]==" " ) or diag[0]==" " and diag[1]==" " and diag[2]!=" " :
                if i==0:
                    heuristicValues[0][0]+=10
                    heuristicValues[1][1]+=10
                    heuristicValues[2][2]+=10
                else:
                    heuristicValues[0][2]+=10
                    heuristicValues[1][1]+=10
                    heuristicValues[2][0]+=10

            elif (diag[0]==mySym and diag[1]==opSym and diag[2]==" ") or            (diag[0]==mySym and diag[1]==" "  and diag[2]==opSym) or            (diag[0]==" "  and diag[1]==opSym  and diag[2]==" ") or             (diag[0]==" "  and diag[1]==" "  and diag[2]==opSym) or             (diag[0]==opSym  and diag[1]==mySym  and diag[2]==" ") or             (diag[0]==opSym  and diag[1]==" "  and diag[2]==mySym):
                if i==0:
                    heuristicValues[0][0]+=0
                    heuristicValues[1][1]+=0
                    heuristicValues[2][2]+=0
                else:
                    heuristicValues[0][2]+=0
                    heuristicValues[1][1]+=0
                    heuristicValues[2][0]+=0

            elif (diag[0]==opSym and diag[1]==opSym and diag[2]==" ") or            (diag[0]==opSym and diag[1]==" " and diag[2]==opSym) or            (diag[0]==" " and diag[1]==opSym and diag[2]==opSym):
                if i==0:
                    heuristicValues[0][0]+=100
                    heuristicValues[1][1]+=100
                    heuristicValues[2][2]+=100
                else:
                    heuristicValues[0][2]+=100
                    heuristicValues[1][1]+=100
                    heuristicValues[2][0]+=100

            elif (diag[0]==mySym and diag[1]==mySym and diag[2]==" ") or            (diag[0]==mySym and diag[1]==" " and diag[2]==mySym) or            (diag[0]==" " and diag[1]==mySym and diag[2]==mySym):
                if i==0:
                    heuristicValues[0][0]+=1000
                    heuristicValues[1][1]+=1000
                    heuristicValues[2][2]+=1000
                else:
                    heuristicValues[0][2]+=1000
                    heuristicValues[1][1]+=1000
                    heuristicValues[2][0]+=1000

        return heuristicValues;    

def printGrid(ticTac):
    for row in ticTac:
        print( row[0]," | ",row[1], " | ", row[2])

def full(ticTac):
    for row in ticTac:
        for val in row:
            if val==" ":
                return False
    print("it's a draw")
    return True

def fillGrid(ticTac,Sym,x=0,y=0,loc=0,):
    if(loc!=0):
        y,x=[(int(loc)-1)%3,(int(loc)-1)//3]
        if(ticTac[x][y]!=" "):
            return False
        ticTac[x][y]=Sym
    else:
        ticTac[int(x)][int(y)]=Sym
    return True

def findMaxEvaluation(evaluation):
    maxEval=0
    x=0
    y=0
    for i in range(3):
        for j in range(3):
            if maxEval<evaluation[i][j] and ticTac[i][j]==" ":
                maxEval=evaluation[i][j]
                x=i
                y=j
    return [x,y]

def takeInput(ticTac):
    while(True):
            loc=int(input("enter location: ?  "))
            if fillGrid(ticTac,opSym,0,0,loc):
                break
            else:
                print("the position is already filled \n enter a location")
    return loc

print('''                   this is the board    
                        1|2|3
                        4|5|6
                        7|8|9
     
     
     enter any place of your choice ''')

while(not full(ticTac) ):  
    loc=takeInput(ticTac)
    printGrid(ticTac)
    if iswin(ticTac,mySym):
        print("you won")
        break
    print("\n\n\n-----------------------------------------------------------\n-----------------------------------------------------------\n\n\n")
    evaluation=heuristic_evaluation(ticTac,mySym,opSym)
    x,y=findMaxEvaluation(evaluation)
    if full(ticTac):
        break
    fillGrid(ticTac,mySym,x,y)
    printGrid(ticTac)
    if iswin(ticTac,mySym):
        print("computer wins")
        break