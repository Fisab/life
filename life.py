import time
import random
from tkinter import *
window = Tk()

s = 100

#switch
mode = 1 #0 - console 1 - graph

begin = time.time()

rules = [
	[ 0, 0, 0, 1, 0, 0, 0, 0, 0 ], # dead
	[ 0, 0, 1, 1, 0, 0, 0, 0, 0 ], # live
]

forms = {
	'glaider': [[2,2],[3,3],[1,4],[2,4],[3,4]]
}

alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
look = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

sizeField = round(s / 8)
amountAliveCells = s

canvas = Canvas(window, width=s, height=s)
canvas.pack()

i = 8
while i < s:
	canvas.create_line(0,i,s,i,width=1,fill="darkgreen")
	i += 8
i = 8
while i < s:
	canvas.create_line(i,0,i,s,width=1,fill="darkgreen")
	i += 8

field1 = []
field2 = []
cells = []
paintedCells = []

def newField(field):
	for i in range(sizeField):
		field.append([])
		for j in range(sizeField):
			field[i].append(".")

def printMap(field):
	print("    ", end='')
	for i in range(sizeField):
		print(i, end=' ')
#		print(alph[i], end=' ')#you can use letter instead of number
	print()
	for i in range(sizeField):
		if i < 10:
			print(i, end='  |')
		else:
			print(i, end=' |')
		for j in range(sizeField):
			print(field[i][j], end=' ')
		print()


def genAliveCells():
	for i in range(amountAliveCells):
		field1[random.randrange(0,sizeField)][random.randrange(0,sizeField)] = 'o'

def process(field, fieldN):
	neighborCells = 0
	for i in range(len(field)):
		for j in range(len(field[i])):
			for side in look:
				if field[(i + side[0] + sizeField) % sizeField][(j + side[1] + sizeField) % sizeField] == 'o':
					neighborCells += 1
			if field[i][j] == '.':
				if rules[0][neighborCells] == 1:
					fieldN[i][j] = 'o'
				else:
					fieldN[i][j] = '.'
			elif field[i][j] == 'o':
				if rules[1][neighborCells] == 1:
					fieldN[i][j] = 'o'
				else:
					fieldN[i][j] = '.'
			neighborCells = 0

def updateField():
	for i in range(len(field2)):
		for j in range(len(field2[i])):
			if field2[i][j] == 'o':
				field1[i][j] = 'o'
				if mode == 1:
					cells.append([j,i])

def paintCells():
	for i in cells:
		paintedCells.append(canvas.create_rectangle(i[0]*8,i[1]*8,i[0]*8+8,i[1]*8+8, fill="green", outline="green"))

def delCells():
	for i in paintedCells:
		canvas.delete(i)

newField(field1)
newField(field2)
genAliveCells()
if mode == 0:
	printMap(field1)
lastPrint = 0

while 1:
	if round(time.time() - begin, 1) - lastPrint > 1:
		process(field1, field2)
		field1 = []
		newField(field1)
		cells = []
		updateField()
		if mode == 0:
			printMap(field1)
		field2 = []
		newField(field2)
		lastPrint = round(time.time() - begin, 1)
		if mode == 1:	
			paintCells()
			window.update()
			delCells()
			paintedCells = []
