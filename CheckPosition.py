import numpy as np
import math

pathDict = {
    'landStraightPath': np.array([[0,0,0],[1,1,1],[0,0,0]]),
    'landCurvePath' : np.array([[0,0,0],[0,1,1],[0,1,0]]),
    'waterStraightPath' : np.array([[0,0,0],[6,6,6],[0,0,0]]),
    'waterCurvePath' : np.array([[0,0,0],[0,6,6],[0,6,0]]),
    'bearStartPoint' : np.array([[0,1,0],[1,2,1],[0,1,0]]),
    'monkeyStartPoint' : np.array([[0,1,0],[1,4,1],[0,1,0]]),
    'duckStartPoint' : np.array([[0,6,0],[6,7,6],[0,6,0]]),
    'nemoStartPoint' : np.array([[0,6,0],[6,9,6],[0,6,0]]),
    'honeyEndPoint' : np.array([[0,1,0],[1,3,1],[0,1,0]]),
    'bananaEndPoint' : np.array([[0,1,0],[1,5,1],[0,1,0]]),
    'ducklingsEndPoint' : np.array([[0,6,0],[6,8,6],[0,6,0]]),
    'coralEndPoint' : np.array([[0,6,0],[6,10,6],[0,6,0]]),
    'obstacle' : np.array([[11,11,11],[11,11,11],[11,11,11]]),
    'emptyPath': np.array([[0,0,0],[0,0,0],[0,0,0]])
}


question_1 = {
    "start": [['bearStartPoint',0],['duckStartPoint',2]],
    "obstacle" : [1,9,11,22],
    "end":[['honeyEndPoint',23]]
}

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

QR_matrix = np.array( [ [0, 1, 0, 11, 11, 11, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                        [1, 2, 1, 11, 11, 11, 6, 7, 6, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 11, 11, 11, 0, 6, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 11, 11, 11],
                        [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 11, 11, 11],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 11, 11],
                        [0, 1, 0, 11, 11, 11, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 11, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 11, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 11, 11, 11, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 11, 11, 11, 1, 3, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 11, 11, 11, 0, 1, 0, 0, 0, 1]] )

def observe(matrix_value,pos,matrix):
    temp  = matrix[math.floor(pos/5)*3:math.floor(pos/5)*3+3,pos%5*3:pos%5*3+3]
    if False in (matrix_value == temp):
        return False
    else:
        return True


def checkTilePlacement(question,matrix):
    for i in range(len(question['start'])):
        matrix_value = pathDict[question['start'][i][0]]
        if observe(matrix_value,question['start'][i][1],matrix) == False:
            return False
        
    for i in range(len(question['obstacle'])):
        if observe(pathDict['obstacle'],question['obstacle'][i],matrix) == False:
            return False

    for i in range(len(question['end'])):
        matrix_value = pathDict[question['end'][i][0]]
        if observe(matrix_value,question['end'][i][1],matrix) == False:
            return False    

    return True     

print(checkTilePlacement(question_1,QR_matrix))