#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4

##!/usr/bin/python
#import pygame

import argparse


def getMaskBit(leftValue, middleValue, rightValue):
 bitPosition = (int(leftValue) << 2) + (int(middleValue) << 1) + (int(rightValue) << 0)
 return (1 << bitPosition)

def getNewValue(rule, maskBit):
  return bool(rule & maskBit)


def applyRule(rule, row, index):
  leftValue   = row[index - 1] if (index > 0) else 0
  middleValue = row[index]
  rightValue  = row[index + 1] if (index < (len(row) - 1)) else 0

  return getNewValue(rule, getMaskBit(leftValue, middleValue, rightValue))


def getNextRow(rule, row):
  newRow = []
  for i in range(len(row)):
    newRow.append(applyRule(rule, row, i))
  return newRow

def displayChar(cell):
  return "#" if (cell) else " "

def printRow(row):
  print ("[", end="")
  for x in row:
    print (displayChar(x), end="")
  print ("]")


def generateTestSet():
  testSet = []
  for i in range(8):
    testSet.append([bool(i & 4), bool(i & 2), bool(i & 1)])
  return testSet

def testRule(rule):
  testResult = 0
  testSet = generateTestSet()
  for i in range(8):
    if (applyRule(rule, testSet[i], 1)):
      testResult += (1<< i)
  return testResult


for i in range(255):
  assert(i == testRule(i))


parser = argparse.ArgumentParser()
parser.add_argument("--rule")
parser.add_argument("--gens")


args = parser.parse_args()


rule = int(args.rule)
gens = int(args.gens)

row = []
for x in range(200):
  row.append(False)

row[100] = True


nextRow = row
for x in range(gens):
  printRow(nextRow)
  nextRow = getNextRow(rule, nextRow)



