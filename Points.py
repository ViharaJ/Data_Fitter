import numpy as np
import math

class Points:

    def __init__(self):
        self.x_points = []
        self.y_points = []
        self.matrix = []
        self.index = -1;

    def addPoint(self, x, y):
        self.x_points.append(x)
        self.y_points.append(y)
        self.index = self.index + 1
        self.updateMatrix()


    def updateMatrix(self):
        newInfo = []
        for i in range(0,self.index+1):
            if i==0:
                newInfo.append(self.y_points[self.index])
            else:
                ans = (newInfo[i-1] - self.matrix[self.index-1][i-1])/(self.x_points[self.index] - self.x_points[self.index-i])
                newInfo.append(ans)

        self.matrix.append(newInfo)

    def newtonEval(self,x):
        ans = 0

        for i in range(0, self.index+1):
            value = 0
            for j in range(0, i+1):
                if j==0:
                    value = self.matrix[i][i]
                else:
                    value *= (x - self.x_points[j-1])

            ans += value

        return ans

