# Coded by Dtil 29/12/2016

import psutil

# Check for the number of CPUs (logic units included)
cpu_count = psutil.cpu_count()

times = psutil.cpu_times()