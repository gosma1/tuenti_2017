#!/usr/bin/python

#import sys
#import math

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
    n_tiradas = int (line)
    t_tiradas = f.readline().replace('\n','').split(' ')
    tiradas=list(map(int,t_tiradas))
    leg=0
    n_bowl=1
    puntuacion=0
    resultado=""
    for i in range(0,n_tiradas):
        if (leg==10): leg=10
        else:
            if (tiradas[i]==10 and n_bowl ==1):
                puntuacion=puntuacion+tiradas[i]+tiradas[i+1]+tiradas[i+2]
                resultado=resultado+" "+str(puntuacion)
                leg=leg+1
            else:
                if (n_bowl == 2): 
                    if((tiradas[i]+tiradas[i-1])==10):
                        puntuacion=puntuacion+tiradas[i]+tiradas[i-1]+tiradas[i+1]
                        resultado=resultado+" "+str(puntuacion)
                        leg=leg+1
                    else: 
                        puntuacion=puntuacion+tiradas[i]+tiradas[i-1]
                        resultado=resultado+" "+str(puntuacion)
                        leg=leg+1
                    n_bowl =1
                else:  
                    n_bowl =2 
    print("Case #",counter,':',resultado, sep="")
    counter = counter + 1
f.close()
