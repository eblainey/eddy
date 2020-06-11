#!usr/bin/python3

##imports


#!usr/bin/python3
import struct
import itertools
import sys
from typing import List
import matplotlib.pyplot as plt


##add a __init__.py to make it a module

def unpack_data():

    f = open('binary.b', 'rb')
    chunks = iter(lambda: f.read(20), b'')

    signal= []
    for chk in chunks:
        #each chk tuple is dim(3)
        point = (struct.unpack('<idd', chk))
        signal.append(point)
        #pass
    #print(signal)

    #organize data
    list1 = []
    list2 = []
    list3 = []
    for i in signal:
       list1.append(i[0])
       list2.append(i[1])
       list3.append(i[2])

       pass
    pass


###init() to initialize communications
##def init():