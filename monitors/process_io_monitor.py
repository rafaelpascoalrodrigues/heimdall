#!/usr/bin/python
''' Heindall Process IO Monitor
    Collect IO used by proccesses and return as a json single string as
    below:
    [[pid, 'pname', parent_id, read_bytes, write_bytes],...]
'''

import os
import time
import json

def getProcessIO():

	# return variable
	processDict = dict()

	for pid in os.listdir('/proc'):
		if not pid.isdigit():
			continue

		# Get process info
		file = '/proc/' + pid + '/stat'

		try:			
			handler = open(file, 'r')
			buff = handler.read().split(' ')
			handler.close()
		except IOError:
			handler.close()
			continue

		processName = buff[1].split('(')[1].split(')')[0]
		parentPid = int(buff[3])

		# Get IO stats
		file = '/proc/' + pid + '/io'

		try:			
			handler = open(file, 'r')
			buff = handler.read().split('\n')
			handler.close()
		except IOError:
			handler.close()
			continue

		# Get process read_bytes and write_bytes	
		readBytes = int(buff[4].split(' ')[1])
		writeBytes = int(buff[5].split(' ')[1])

		processDict[pid] = {'read' : readBytes, 'write' : writeBytes, 'p_name' : processName, 'parent_id': parentPid}

	return processDict

def measure():

	# measure IO 
	ioIni = getProcessIO()

	# wait 1 sec
	time.sleep(1)

	# measure again
	ioFinal = getProcessIO()

	processList = list()

	for pid in ioFinal:
		# check if process has terminated between measures
		if pid in ioIni:
			ioRead = ioFinal[pid]['read'] - ioIni[pid]['read']
			ioWrite = ioFinal[pid]['write'] - ioIni[pid]['write']

			processList += [[pid, ioFinal[pid]['p_name'], ioFinal[pid]['parent_id'], ioRead, ioWrite]]

	return processList

print json.dumps(measure())
