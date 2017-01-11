#!/usr/bin/python
''' Heindall Process IO Monitor
    Collect IO used by proccesses and return as a json single string as
    below:
    [[pid, 'pname', parent_pid, IO],...]
'''

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

		# Get process info

		file = '/proc/' + pid[0] + '/stat'

		if not os.path.exists(file):
			pids[index] = []
			index += 1
			continue

		f = open(file)
		s = f.read().split(' ')
		f.close()

		# If first iteration add proc name and parent pid to lis

		if i == 0:
			pids[index].append(s[1])
			pids[index].append(s[3])

		file = '/proc/' + pid[0] + '/io'

		f = open(file)
		s = f.read().split('\n')
		f.close()		

		# Get process read_bytes and write_bytes

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

	# Calc read_bytes and write_bytes in 1 sec

    io_read = pids[i][5] - pids[i][3]
    io_write = pids[i][6] - pids[i][4]

    output.append([pids[i][0], pids[i][1], pids[i][2] io_read, io_write])

print json.dumps(output)
