#!/usr/bin/env python
''' Heindall Process Opened Files Monitor
    Collects information of number of opened files by proccesses and return as
    a json single string as below:
    [[pid, 'pname', no_files_opened],[pid, 'pname', no_files_opened],...]
'''
from os import listdir
import json

def get_nofiles_by_process():
    ''' Run through the linux system files searching for processes and its
        opened files list
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

            pname = file_buffer[0].split('(')[1].split(')')[0]

            file_handler.close()
        # Can't continue without a pname
        except IOError:
            file_handler.close()
            continue


        # Get info of the number of opened files of the process
        files_list = listdir('/proc/' + pid + '/fd')
        files_opened = len(files_list)


        process_list += [[int(pid), pname, int(files_opened)]]

    # Return processes list with number of opened files information
    return process_list

# Prints list in json formats
print json.dumps(get_nofiles_by_process())
