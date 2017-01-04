#!/usr/bin/python

import psutil

# Check for the number of CPUs (logic units included)
cpu_count = psutil.cpu_count()

times = psutil.cpu_times()

print times