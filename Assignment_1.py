#!/usr/bin/env python
# coding: utf-8

# # Quetion1

X = int(input('Val1:'))
Y = int(input('Val2:'))
print(pow(X,Y))


# # Queston2
li= [int(i) for i in input('Enter the value:').split()]
print(li)
var=[]
for i in li:
	if(i%3 == 0):
		var.append(int(i))
print(var)

