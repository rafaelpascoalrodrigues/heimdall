import os
import time

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


## Ini ##

totalCpu = []

pids = [[pid] for pid in os.listdir('/proc') if pid.isdigit()]
pidsIter = pids[:]

for i in range(2):

    totalCpu.append(totalCpuTime())

    index = 0

    for pid in pidsIter:
 	f = open('/proc/' + pid[0] + '/stat')
    	s = f.read().split(' ')
        f.close()


        # If first iteration add proc name to list

        if i == 0:
            pids[index].append(s[1])

    
    	"""
    	all values are decremented by 1 due to python index
    
        13 -> utime : user mode ticks
    	14 -> stime : kernel mode ticks
    
    	"""
        cpuTime = int(s[13]) + int(s[14])
        pids[index].append(cpuTime)
        index += 1

    time.sleep(1)

for i in range(0,len(pids)):
    processCpuTime = 100 * (float(pids[i][3] - pids[i][2]) / float(totalCpu[1] - totalCpu[0]))

    print  pids[i][0] + ' : ' + pids[i][1] + ' : ' +str(processCpuTime)
