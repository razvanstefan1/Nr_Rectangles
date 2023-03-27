def count_rectangles(points):
    diagonale = 0  # variabila unde numaram cate diagonale valide am gasit
    puncteDict = dict()  # un dictionar in care punem punctele ca si chei si valorile pe true (folosit pt a accesa in O(1) punctele din lista)
    for i in range(len(points)):
        puncteDict[points[i]] = True #punctele care exista au valoarea true

    for i in range(len(points)): #consider i colt dreapta jos
        for j in range(i+1, len(points)): #consider j colt stanga sus, j pleaca de la i+1 ca sa nu avem acelasi punct si nici sa nu avem aceleasi 2 puncte doar ca inversate
            if (points[i][0]!=points[j][0] and points[i][1]!=points[j][1]   # verificam ca linia formata de cele 2 pct sa fie diagonala
                                                                                 # (daca e false conditia aceasta, inseamna ca linia e paralela cu OX sau OY)
               and puncteDict.get((points[i][0],points[j][1]))==True    #daca punctul din dreapta sus exista
               and puncteDict.get((points[j][0],points[i][1]))==True):  #si punctul din stanga jos exista
               #and points[i]!=points[j]  #COMENTEZ aceasta conditie pentru ca imi asum ca un punct nu apare de 2 ori in lista
                    diagonale+=1

    return diagonale//2  #din moment ce in variabila diagonale avem nr de diagonale valide, iar un dreptunghi are 2 diagonale, impartim la 2

# print(count_rectangles([(1,1),(1,3),(2,1),(3,1),(2,3),(3,3)]))
# print(count_rectangles([(1,1),(1,3),(2,1),(3,1)      ,(3,3)]))
# print(count_rectangles([(1, 1), (3, 1), (5, 1), (3, 3),(1,3),(3,-1),(1,-1),(5,-1),(5,3)]))
# print(count_rectangles([(1, 1),(0,0),(0,1),(1,0)]))

