from scapy.all import *
import pyshark
from collections import defaultdict
import sys
import math
import numpy as np

#filename='data-cap1-01.cap'
filename='data-cap1-01.cap'
#a1 = rdpcap('new.cap1')
#a2 = rdpcap('new.cap2')

#file1 = pyshark.FileCapture('data-cap-01.cap')
#file2 = pyshark.FileCapture('LLS_DDOS_1.0-dmz.dump')
#capture = pyshark.FileCapture('data-cap1-01.cap',['Flags'])


colors = {'red': [255,0,0,0]} 



cap = pyshark.FileCapture('cap-ctl.cap')

#print packet['WLAN']
print cap[0]['WLAN']._field_names
print cap[1]['WLAN']._field_names
print cap[2]['WLAN']._field_names
print cap[0]['WLAN'].get_raw_value('fc_type')
print cap[1]['WLAN'].get_field_value('fc_type')
print cap[2]['WLAN'].get_field_value('fc_type')
print cap[0]['WLAN'].layer_name
print cap[0]['WLAN'].get_field_value('bssid')
print cap[0]['WLAN'].get_field_value('addr')

for key, value in cap[0].iteritems():
	temp = [key, value]
	dictlist.append(temp)


type0 = 0
type1 = 0
type2 = 0





