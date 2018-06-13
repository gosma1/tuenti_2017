#!/usr/bin/python

#import sys
import math

## Open the file with read only permit
f = open('submitInput.txt',"r")
## Read the first line 
line = f.readline().replace('\n',' ')
counter = 0

if (counter == 0 and line):
     counter = counter + 1
     N = int(line) + 1
else:
    print ("error\n")
    exit()
while (counter < N):
    line = f.readline().replace('\n',' ')
    numero = int (line)
    resultado=0
    resultado = math.ceil(math.log2(numero))
    print("Case #",counter,': ',resultado, sep="")
    counter = counter + 1
f.close()
