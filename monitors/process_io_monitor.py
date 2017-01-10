#!/usr/bin/python

import os
import re
import time
import json

# Regex
read = re.compile('read_bytes')
write = re.compile('write_bytes')

pids = [[pid] for pid in os.listdir('/proc') if pid.isdigit()]
pidsIter = pids[:]

for i in range(2): # Measure , wait 1 sec, measure agai

	index = 0

	for pid in pidsIter:

		file = '/proc/' + pid[0] + '/stat'

		if not os.path.exists(file):
			pids[index] = []
			index += 1
			continue

		f = open(file)
		s = f.read().split(' ')
		f.close()

		if i == 0:
			pids[index].append(s[1])

		file = '/proc/' + pid[0] + '/io'

		f = open(file)
		s = f.read().split('\n')
		f.close()		

		for line in s:
			if read.match(line):
				aux = line.split(' ')
				pids[index].append(int(aux[1]))
			if write.match(line):
				aux = line.split(' ')
				pids[index].append(int(aux[1]))

		index += 1

	time.sleep(1)

pids = [i for i in pids if i != []]
output = []

for i in range(0,len(pids)):
    io_read = pids[i][4] - pids[i][2]
    io_write = pids[i][5] - pids[i][3]

    # print pids[i][0] + ' : ' + pids[i][1] + ' : ' +str(processCpuTime)
    output.append([pids[i][0], pids[i][1], io_read, io_write])

print json.dumps(output)


