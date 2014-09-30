from scapy.all import *
import sys
import math
import numpy as np
import threading
import multiprocessing
from multiprocessing import Process, Queue


mang = 0
data = 0
ctrl = 0

def process(packets):
	mang = 0
	data = 0
	ctrl = 0

	for packet in packets:
		# type / proto / FCfield / ID / SC / subtype
		if packet.haslayer(Dot11):
			
			
		
			if packet.type == 0:
				#print " Management packet of subtype : " + str(packet.subtype)
				mang = mang + 1

			elif packet.type == 2:
				data = data + 1
				#print packet.icv
				
				#print " Data packet of subtype : " + str(packet.subtype)
			else:
				ctrl = ctrl + 1
				#print " Control packet of subtype : " + str(packet.subtype)
			

def incre(init,q):

	i = 0
	j = init
	for i in range(100000000):
		j = j + 1
	q.put(j)

filename='data-cap1-01.cap'
filename1='new.cap1'
filename2='new.cap2'
filename3='new.cap3'
filename4='new.cap4'
filename5='new.cap5'
filename6='new.cap6'


packets = rdpcap(filename)
packets1 = rdpcap(filename1)
packets2 = rdpcap(filename2)
packets3 = rdpcap(filename3)
packets4 = rdpcap(filename4)
packets5 = rdpcap(filename5)
packets6 = rdpcap(filename6)

#process(packets)


srcList = [pkt.type for pkt in packets1]



print " management : " + str(mang)
print " data : " + str(data)
print " control : " + str(ctrl)

