#!/usr/bin/env python
import shlex
import time
import sys
import pygal
import datetime
from subprocess import Popen, PIPE

def min(list):
	i = 0
	min_location = 0
	min = list[0]
	for elm in list[1:]:
		if elm < min:
			min_location = i
			min = elm
		i=i+1
	return [min,min_location]

def max(list):
	i = 0
	max_location = 0
	max = list[0]
	for elm in list[1:]:
		i=i+1
		if elm > max:
			max_location = i
			max = elm
	return [max,max_location]

def avg(list):
	sum = 0
	for elm in list:
		sum += elm
	return (sum/(len(list)*1.0))

def executor(cmd):
    t1 = datetime.datetime.now()
    process = Popen(shlex.split(cmd),stdout=PIPE)
    process.communicate()
    t2 = datetime.datetime.now()
    exit_code = process.wait()
    td = t2 - t1
    return (exit_code,td)

def getArgs():
    if len(sys.argv) > 3:
        cmd = sys.argv[1]
        iterations = int(sys.argv[2])
        outfile = sys.argv[3]
        return (cmd,iterations,outfile)
    else:
        print "Example: execperf.py \"command -param1 -param2\" num_of_iterations output_file.svg"
        sys.exit()
    
if __name__ == '__main__':
    
    # Get command line arguments
    cmd,iterations,outfile = getArgs()
    
    # Init graph
    line_chart = pygal.Line(
        x_title	= 'Execution Num',
        y_title	= 'Execution Time(ms)',
        human_readable 	= True,
        legend_at_bottom= True
        )   
    line_chart.title = "Execution time of \"%s\" in ms for %d iterations "%(cmd,iterations) 
    tmp_list = []
    
    # Loop 
    for i in range(0,iterations):
        perfomance_data = executor(cmd)
        diff = perfomance_data[1]
        # Convert delta timestamp to ms
        tmp =  diff.days * 24 * 60 * 60 * 1000
        tmp += diff.seconds * 1000
        tmp += diff.microseconds / 1000
        tmp_list.append(tmp)
    
    # Generate graph from data
    line_chart.x_labels = map(str, range(1,iterations+1))
    line_chart.include_x_axis=True,
    line_chart.add(cmd+" - Min:"+str(min(tmp_list)[0])+"(ms) - Max:"+str(max(tmp_list)[0])+"(ms) - Avg:"+str(avg(tmp_list))+"(ms)",
    	tmp_list)
    line_chart.render_to_file(outfile)