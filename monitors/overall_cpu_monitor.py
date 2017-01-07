#!/usr/bin/python

import psutil
import json

# Check for the number of CPUs (logic units included)
cpu_count = psutil.cpu_count()

# TODO : format output according to number of CPUs

times = psutil.cpu_times()
print json.dumps(times.__dict__)