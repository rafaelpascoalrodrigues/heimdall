#!/usr/bin/python
''' Heimdall Process Memory Monitor
    Collect memory used by proccesses and return as a json single string as
    below:
    [[pid, ppid, 'pname', memory_Kb],
    [pid, ppid, 'pname', memory_Kb],...]
'''
from os import listdir
import json

def get_memory_by_process():
    ''' Run through the linux system files searching for processes and its
        memory information
    '''

    # Return variable
    process_list = list()

    # Run through all processes
    for pid in listdir('/proc'):
        # Continue only if the pid is numeric
        if not pid.isdigit():
            continue


        # Try to get process name
        try:
            file_check = '/proc/' + pid + '/stat'
            file_handler = open(file_check, 'r')
            file_buffer = [line.rstrip('\n') for line in file_handler]

            # Continue only if the pname exists
            if len(file_buffer) <= 0:
                file_handler.close()
                continue

            ppid = file_buffer[0].split(')')[1].split(' ')[2]
            pname = file_buffer[0].split('(')[1].split(')')[0]

            file_handler.close()
        # Can't continue without a pname
        except IOError:
            file_handler.close()
            continue


        # Get info of the process process
        try:
            file_check = '/proc/' + pid + '/status'
            file_handler = open(file_check, 'r')
            file_buffer = [line.rstrip('\n') for line in file_handler]

            # Memory used is the sum of data and stack
            size = 0
            for line in file_buffer:
                if 'VmData' in line or 'VmStk' in line:
                    size += int(line.split(' ')[-2])

            file_handler.close()
        except IOError:
            file_handler.close()

        process_list += [[int(pid), int(ppid), pname, int(size)]]

    # Return processes list with memory information
    return process_list

# Prints list in json formats
print json.dumps(get_memory_by_process())
