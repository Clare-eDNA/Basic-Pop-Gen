# Creating a random population generator
# With a plot!

from math import ceil  #Import ceiling
print (ceil(2.5)) #Rounds up

from random import random #Import random number
ceil(random()*6-3) #Makes a random number from -3-3
print ceil(random()*6-3) #The randomizer code you want


lst=[] #First, create a list to put your numbers in

x=50 #Start off with 50

for i in range(0,1000):  #Start your 4loop, range for years is 1-1000
    x=x+round(random()*6)-3 #start with x, add a random number, return x
    lst.append(x) #Add your x to the list
    print (x) #print out the numbers (if you want, this can be deleted)
  
import matplotlib.pyplot as plt #Import syntax to print

plt.plot(lst) #print your list