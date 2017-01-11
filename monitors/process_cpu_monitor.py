#!/usr/bin/python
''' Heindall Process cpu Monitor
    Collect cpu used by proccesses and return as a json single string as
    below:
    [[pid, 'pname', parent_pid, cpu_percentage],...]
'''

import os
import time
import json

def totalCpuTime():

    # Measure total cpu ticks

    f = open('/proc/stat')
    d = f.readline().split(' ')
    f.close()

    totalCpuTicks = 0

    for value in d:
        if value.isdigit():
            totalCpuTicks = int(value) + totalCpuTicks
    
    return totalCpuTicks

totalCpu = []

pids = [[pid] for pid in os.listdir('/proc') if pid.isdigit()]
pidsIter = pids[:]

for i in range(2):

    totalCpu.append(totalCpuTime())

    index = 0

    for pid in pidsIter:

        file = '/proc/' + pid[0] + '/stat'

        # remove processes which hava terminated from list

        if not os.path.exists(file):
            pids[index] = []
            index += 1
            continue

     	f = open(file)
    	s = f.read().split(' ')
        f.close()

        # If first iteration add proc name and parent pid to list 

        if i == 0:
            pids[index].append(s[1])
            pids[index].append(s[3])

    
    	''' all values are decremented by 1 due to python index
            13 -> utime : user mode ticks
            14 -> stime : kernel mode ticks
        '''

        cpuTime = int(s[13]) + int(s[14])
        pids[index].append(cpuTime)
        index += 1

    time.sleep(1)

pids = [i for i in pids if i != []]
output = []

for i in range(0,len(pids)):
    processCpuTime = 100 * (float(pids[i][4] - pids[i][3]) / float(totalCpu[1] - totalCpu[0]))
    output.append([pids[i][0], pids[i][1], pids[i][2], processCpuTime])

print json.dumps(output)
