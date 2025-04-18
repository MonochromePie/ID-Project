import numpy as np
import math


def matrix_dis(current_position, destination, matrix):
    a = np.where(matrix == destination)
    diff = current_position - np.array([a[0][0], a[1][0]])
    return math.sqrt(diff[0]**2 + diff[1]**2)

def makeCost(destination, matrix):
    cost = np.empty(np.shape(matrix))
    for i in range(np.shape(cost)[0]):
        for j in range(np.shape(cost)[1]):
            cost[i][j] = matrix_dis(np.array([i, j]),destination, matrix)
    return cost

def makeCheckedPathMatrix(list, matrix):
    path = np.empty(np.shape(matrix))
    for i in range(np.shape(path)[0]):
        for j in range(np.shape(path)[1]):
            if matrix[i][j] in list:
                path[i][j] = 0
            else:
                path[i][j] = 1
    return path

def searchNode(current_pos,matrix):
    searched = np.array([[current_pos[0],current_pos[1]+1],[current_pos[0]+1,current_pos[1]],[current_pos[0],current_pos[1]-1],[current_pos[0]-1,current_pos[1]]])
    deleteList = []
    
    for i in range(3,-1,-1):
        isInvalid = False
        for j in range(1,-1,-1):
            if searched[i][j] < 0 or searched[i][j] > np.shape(matrix)[0] or searched[i][j] > np.shape(matrix)[1]:
                isInvalid = True
        if isInvalid:
            deleteList.append(i)

    for i in range(len(deleteList)):
        searched = np.delete(searched, deleteList[i],axis=0)     
  
    valueInSearched = np.array([[0]])
    for i in range(len(searched)):
        value = matrix[searched[i][0]][searched[i][1]]
        valueInSearched = np.append(valueInSearched,np.array([[value]]),axis=0)
    valueInSearched = np.delete(valueInSearched,0,axis=0)
    valueInSearched = np.transpose(valueInSearched)

    return searched, valueInSearched

def Astar(start,end,path,matrix):
    G_cost = makeCost(start,matrix)
    H_cost = makeCost(end,matrix)
    F_cost = G_cost + H_cost
    Inf = 100 #any value high af so code just skip this
    
    checked_path = makeCheckedPathMatrix([start,end,path],matrix)

    for i in range(np.shape(matrix)[0]):
        for j in range(np.shape(matrix)[1]):
            if checked_path[i][j] == 1:
                F_cost[i][j] = Inf

    path_count = (matrix == path).sum()

    #start algorithm
    start_loc = np.transpose(np.where(matrix==start))[0]

    checked_path[np.where(matrix==start)] = 1
    F_cost_searched = np.full(shape=np.shape(matrix), fill_value=Inf)
    a,b = searchNode(start_loc,matrix)
    value_searched = np.array([])
    value_searched = np.concatenate((value_searched,b[0]))

    for i in range(len(a)):
        F_cost_searched[a[i][0]][a[i][1]] = F_cost[a[i][0]][a[i][1]]

    while path_count != 0:
        searchAt = np.transpose(np.where(F_cost_searched==np.min(F_cost_searched)))
        a,b = searchNode(searchAt[0],matrix)
        checked_path[searchAt[0][0],searchAt[0][1]] = 1
        
        for i in range(len(a)):
            if checked_path[a[i][0]][a[i][1]] != 1:
                F_cost_searched[a[i][0]][a[i][1]] = F_cost[a[i][0]][a[i][1]]
            else:
                F_cost_searched[a[i][0]][a[i][1]] = Inf
            if matrix[a[i][0]][a[i][1]] != path:
                    F_cost_searched[a[i][0]][a[i][1]] = Inf
        F_cost_searched[searchAt[0][0],searchAt[0][1]] = Inf 

        value_searched = np.concatenate((value_searched,b[0]))
        path_count -= 1
        print(F_cost_searched)
        if end in value_searched:
            return "Connected"
    
    return "Not Connected"

QR_matrix1 = np.array(  [[2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 4, 0, 5, 6, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] )
#Land path ID: 1
#bear ID: 2
#honey ID: 3
#monkey ID: 4
#banana ID: 5

#Water path ID: 6
#Duck ID: 7
#Duckling ID: 8
#Nemo ID: 9
#Coral ID: 10

#Obstacles ID: 11

print(Astar(2,3,1,QR_matrix1))


