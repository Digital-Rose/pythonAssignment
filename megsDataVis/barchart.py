#Megs Bar Chart Graphics
from random import randint
from graphics import *
import numpy as np
window = GraphWin("Megs Data Visualisation", 700, 500)

#Arrays
floats=[]
circles = []
labels = ["<40","40-50","50-60","60-70","70+"]
countArray = [ 0,0,0,0,0 ]
colours = [color_rgb(255,0,0),color_rgb(255,255,0),color_rgb(0,255,0),color_rgb(0,100,255),color_rgb(100,0,255)]

# Draw Background
box = Rectangle(Point(0,0),Point(800,800))
box.setFill(color_rgb(0,0,0))
box.draw(window)
#Title
text = Text(Point(350,30),"Class Grades 2014 Visualisation")
text.setFill(color_rgb(255,255,255))
text.setFace('arial')
text.setSize(25)
text.draw(window)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
lines = datafile.readlines();
for line in lines:
	numbers = line.split(",")
	for number in numbers:
		floatNum = float(number)
		floats.append(floatNum)
		
#Count how many marks are in each range
for m in range(0,len(floats)-1):
	if (floats[m] > 70):
		countArray[4] = countArray[4] + 1
	elif (floats[m]> 60):
		countArray[3] = countArray[3] + 1
	elif (floats[m] > 50):
		countArray[2] = countArray[2] + 1
	elif (floats[m] > 40):
		countArray[1] = countArray[1] + 1
	elif (floats[m] < 40):
		countArray[0] = countArray[0] + 1
	
def drawBar(label,x,count,colour):
	text = Text(Point(x+25,425),label)
	text.setFill(color_rgb(255,255,255))
	text.setFace('arial')
	text.setSize(14)
	text.draw(window)
	
	#Draws the bar starting at the bottom point up to height. 
	#Note if more numbers added then count*100 needs to change
	for i in range(400,400-(count*100),-2):
		box = Rectangle(Point(x,400),Point(x+50,i))
		box.setFill(colour)
		box.draw(window)
	#Draws the text just below the height of the bar
	text = Text(Point(x+25,410-(count*100)),count)
	text.setFill(color_rgb(0,0,0))
	text.setFace('arial')
	text.setSize(10)
	text.draw(window)
	
drawBar(labels[0],100,countArray[0],colours[0])
drawBar(labels[1],200,countArray[1],colours[1])
drawBar(labels[2],300,countArray[2],colours[2])
drawBar(labels[3],400,countArray[3],colours[3])
drawBar(labels[4],500,countArray[4],colours[4])

#Draw box for text
box = Rectangle(Point(600,450),Point(690,490))
box.setOutline(color_rgb(255,255,255))
box.setWidth(4)
box.setFill(color_rgb(0,0,0))
box.draw(window)



mean = np.mean(floats)	
if (mean >= 40):
	text = Text(Point(645,470),"Class Passed!")
	text.setFace('arial')
	text.setFill(color_rgb(255,255,255))
	text.setSize(12)
	text.draw(window)
	
elif (mean < 40): 
	text = Text(Point(645,470),"Class Failed :(")
	text.setFill(color_rgb(255,255,255))
	text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()
		