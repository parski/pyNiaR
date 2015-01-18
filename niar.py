#!/usr/bin/env python
# -*- coding: utf-8 -*-

#************#
# n in a row #
#************#

# implemented in python 2.7 by parski

import sys, os

# class Token is the little thing you put in the grid slots
class Token(object):
	def __init__(self, team):
		self.team = team
		
	def getTeam(self):
		return self.team

# class Grid is the matrix
class Grid(object):
	def __init__(self, width, height, n):
		self.matrix = [[0 for x in range(height)] for x in range(width)]
		self.width, self.height, self.n = width, height, n
		
	def insertTokenIntoSlot(self, token, slot):
		for index, cell in enumerate(self.matrix[slot]):
			if cell != 0:
				self.matrix[slot][index - 1] = token
				return (token.getTeam(), slot, index - 1)
			elif index == self.height - 1:
				self.matrix[slot][index] = token
				return (token.getTeam(), slot, index)
		return False
		
	def isSlotFull(self, slot):
		if slot[0] == 0:
			return False
		return True
		
	def checkTokenForInARow(self, tokenData):
		e = w = s = ne = nw = se = sw = 0
		step = 1
		while step <= self.n and step < self.height - tokenData[2]:
			if self.matrix[tokenData[1]][tokenData[2] + step].getTeam() == tokenData[0]:
				step += 1
				s = step
				if s == self.n:
					return True
			else:
				break
		step = 1
		while step <= self.n and step + tokenData[1] < self.width:
			if self.matrix[tokenData[1] + step][tokenData[2]] != 0:
				if self.matrix[tokenData[1] + step][tokenData[2]].getTeam() == tokenData[0]:
					e = step
				else:
					break
				step += 1
			else:
				break
		step = 1
		while step <= self.n and step <= tokenData[1]:
			if self.matrix[tokenData[1] - step][tokenData[2]] != 0:
				if self.matrix[tokenData[1] - step][tokenData[2]].getTeam() == tokenData[0]:
					w = step
				else:
					break
				step += 1
			else:
				break
		if e + w + 1 >= self.n:
			return True
		step = 1
		while step <= self.n and step <= tokenData[1] and step <= tokenData[2]:
			if self.matrix[tokenData[1] - step][tokenData[2] - step] != 0:
				if self.matrix[tokenData[1] - step][tokenData[2] - step].getTeam() == tokenData[0]:
					nw = step
				else:
					break
				step += 1
			else:
				break
		step = 1
		while step <= self.n and step < self.height - tokenData[2] and step + tokenData[1] < self.width:
			if self.matrix[tokenData[1] + step][tokenData[2] + step] != 0:
				if self.matrix[tokenData[1] + step][tokenData[2] + step].getTeam() == tokenData[0]:
					se = step
				else:
					break
				step += 1
			else:
				break
		if nw + se + 1 >= self.n:
			return True
		step = 1
		while step <= self.n and step < self.height - tokenData[2] and step <= tokenData[1]:
			if self.matrix[tokenData[1] - step][tokenData[2] + step] != 0:
				if self.matrix[tokenData[1] - step][tokenData[2] + step].getTeam() == tokenData[0]:
					sw = step
				else:
					break
				step += 1
			else:
				break
		step = 1
		while step <= self.n and step + tokenData[1] < self.width and step <= tokenData[2]:
			if self.matrix[tokenData[1] + step][tokenData[2] - step] != 0:
				if self.matrix[tokenData[1] + step][tokenData[2] - step].getTeam() == tokenData[0]:
					ne = step
				else:
					break
				step += 1
			else:
				break
		step = 1
		if sw + ne + 1 >= self.n:
			return True
		return False
		
	def printGrid(self):
		y = 0
		while y < self.height:
			x = 0
			while x < self.width:
				if self.matrix[x][y] == 0:
					sys.stdout.write('[ ]')
				else:
					sys.stdout.write('[' + self.matrix[x][y].getTeam() + ']')
				x += 1
			sys.stdout.write("\n")
			y += 1
			
	def isGridFull(self):
		fullSlots = 0
		for slot in self.matrix:
			if self.isSlotFull(slot):
				fullSlots += 1
		if fullSlots == self.width:
			return True
		return False

# main

# bootstrapping
os.system('clear')
print("N in a row.\n\nPress Ctrl + C to quit.\n")

playerAmount = 0
while playerAmount == 0:
	playerAmount = raw_input('How many players want to party?: ')
	try:
		int(playerAmount)
	except ValueError:
		print("Please enter an integer from 1 to infinity.")
		playerAmount = 0
	playerAmount = int(playerAmount)
	
players = [64] * playerAmount
for index, player in enumerate(players):
	while len(str(players[index])) != 1:
		nameCandidate = str(raw_input("Enter player " + str(index + 1) + " token character: "))
		if len(nameCandidate) != 1:
			print("A character means a character, not an arbitrary number of characters.")
		elif nameCandidate in players:
			print("Another player already has that character. Don't be a player hater.")
		else:
			players[index] = nameCandidate

width = 0
while width == 0:
	width = raw_input('Grid width: ')
	try:
		int(width)
	except ValueError:
		print("Please enter an integer from 1 to infinity.")
		width = 0
	width = int(width)

height = 0
while height == 0:
	height = raw_input('Grid height: ')
	try:
		int(height)
	except ValueError:
		print("Please enter an integer from 1 to infinity.")
		height = 0
	height = int(height)

n = 0
while n == 0:
	n = raw_input('N: ')
	try:
		int(n)
	except ValueError:
		print("Please enter an integer from 1 to infinity.")
		n = 0
	n = int(n)

os.system('clear')
g = Grid(width, height, n)
print("Try to get " + str(n) + " in a row.\n")
g.printGrid()

# game loop
winner = None
playerTurn = 0
while winner is None:
	while not g.isGridFull():
		if playerTurn == len(players):
			playerTurn = 0
		print("\nIt's player " + str(players[playerTurn]) + "'s turn.\n")
		slotNumber = 0
		while slotNumber == 0:
			slotNumber = raw_input("Insert into slot (1 to " + str(g.width) + "): ")
			try:
				int(slotNumber)
			except ValueError:
				print("Please enter an integer from 1 " + str(g.width) + "): ")
				slotNumber = 0
			slotNumber = int(slotNumber)
		t = Token(players[playerTurn])
		if slotNumber > 0 and slotNumber <= g.width:
			if not g.isSlotFull(g.matrix[slotNumber - 1]):
				if g.checkTokenForInARow(g.insertTokenIntoSlot(t, slotNumber - 1)):
					winner = t.getTeam()
					os.system('clear')
					print("Game over!\n")
					g.printGrid()
					break
		if not g.isSlotFull(g.matrix[slotNumber - 1]):
			playerTurn += 1
		os.system('clear')
		print("Try to get " + str(n) + " in a row.\n")
		g.printGrid()
	if winner is None:
		print("\nGrid full. No winner!")
		break
	else:
		print("\nMista Scratchy-san! We have big winna: " + str(winner))