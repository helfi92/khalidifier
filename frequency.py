import nltk
import re
from collections import Counter
import collections
import os
import numpy

from pylab import *
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt



import matplotlib.pyplot as plt
import operator,string

f = open('dj.txt','r')
#f = open('TheTwoAmericas.txt','r')
#f = open('German.txt','r')


scale = {}
for line in f:
    line = line.split()
    for word in line:
        word = word.lower()
        nword = word.translate(string.maketrans("",""),string.punctuation)
        if nword in scale:
            scale[nword] += 1
        else:
            scale[nword] = 1

sorted_scale = sorted(scale.iteritems(),key=operator.itemgetter(1),reverse=True)

print 'Number of distinct words:',len(sorted_scale)

popular = 50
x = range(popular)
y=[]
print('Printing the frequency of Top 50 words')
print('word ,frequency')
for pair in range(popular):
    y = y + [sorted_scale[pair][1]]
    print(sorted_scale[pair],'Rank %s'%(pair+1),)


#step = 1000
#a = range(step)
#b = []
#print('Printing the Frequency of every 50 words in Steps of 1000')
#print('word,frequency')
#for pair in range(step):
 #   b = b + [sorted_scale[pair][1]]
  #  print(sorted_scale[pair],'Rank %s'%(pair+1))


plt.plot(x,y,'ro')
plt.xlabel('Word ranking')
plt.ylabel('Word frequency')
plt.yscale('log')  #to convert into logarithmic
plt.xscale('log')  #to convert into logarithmic
plt.grid(True)
#plt.plot(a,b,'ro')
#plt.xlabel('Word ranking')
#plt.ylabel('Word frequency')
#plt.yscale('log')  #to convert into logarithmic
#plt.xscale('log')  #to convert into logarithmic
#plt.grid(True)
plt.show()



