from tkinter import *
import matplotlib.pyplot as plt
from Points import *

root = Tk()
root.title("Data Fitter")

xLabel = Label(root, text="x")
xLabel.grid(row=0, column=0)
yLabel = Label(root, text="y")
yLabel.grid(row=1, column=0)
xEntry = Entry(root)
xEntry.grid(row=0, column=1)
yEntry = Entry(root)
yEntry.grid(row=1, column=1)

set1 = Points()

def processPress():
    set1.addPoint(float(xEntry.get()), float(yEntry.get()))
    xEntry.delete(0, 'end')
    yEntry.delete(0, 'end')
    newP = Label(root, text= "x = " + str(set1.x_points[set1.index]) + ", y = " + str(set1.y_points[set1.index]))
    newP.grid()

def plotPoints():
    if(len(set1.x_points) > 1):
        mini = min(set1.x_points)
        maxi = max(set1.x_points)

        newPoints = np.linspace(mini, maxi, 1000)
        newYPoints = set1.newtonEval(newPoints)

        plt.clf()
        plt.scatter(set1.x_points, set1.y_points, color="orange")
        plt.plot(newPoints, newYPoints)
        plt.show()


EnterButn = Button(root, text="Add Point", command=processPress)
EnterButn.grid(row=2,column=1)

NewtonBtn = Button(root, text="Interpolate!", command=plotPoints)
NewtonBtn.grid(row=3,column=1)
root.mainloop()


