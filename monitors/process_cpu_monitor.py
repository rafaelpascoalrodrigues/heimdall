#!/usr/bin/python
''' Heindall Process cpu Monitor
    Collect cpu used by proccesses and return as a json single string as
    below:
    [[pid, 'pname', parent_pid, cpu_percentage],...]
'''

import os
import time
import json

def getTotalCpuTime():
    # Measure total cpu ticks

    try:
        handler = open('/proc/stat')
        buff = handler.readline().split(' ')
        handler.close()

    except IOError:
        handler.close()
        return 0

    totalCpuTicks = 0
    for value in buff:
        if not value.isdigit():
            continue

        # Sum cpu ticks in all states
        totalCpuTicks += int(value)

    return float(totalCpuTicks)

def getProcessCpuTime():

    # return variable
    processDict = dict()

    for pid in os.listdir('/proc'):
        if not pid.isdigit():
            continue

        file = '/proc/' + pid + '/stat'

        try:
            handler = open(file, 'r')
            buff = handler.read().split(' ')
            handler.close()

        except IOError:
            handler.close()
            continue            

        # Get process cpu time in user and kernel mode 
        processCpuTime = float(buff[13]) + float(buff[14])
        processName = buff[1].split('(')[1].split(')')[0]
        parentPid = int(buff[3])

        processDict[pid] = {'cpu_time' : processCpuTime, 'p_name' : processName, 'parent_id' : parentPid}

    return processDict


def measure():

    # Measure cpu time
    totalIni = getTotalCpuTime()
    processIni = getProcessCpuTime()

    # Wait 1 sec
    time.sleep(1)

    # Measure again
    totalFinal = getTotalCpuTime()
    processFinal = getProcessCpuTime()

    # Calc total cpu ticks in 1 sec
    totalCpu = totalFinal - totalIni

    processList = list()

    for pid in processFinal:
        # Check if process has terminated between measures
        if pid in processIni:
            processCpuTime = 100 * (processFinal[pid]['cpu_time'] - processIni[pid]['cpu_time']) / totalCpu
            processList += [[pid, processFinal[pid]['p_name'], processFinal[pid]['parent_id'], processCpuTime]]

    return processList

print json.dumps(measure())
