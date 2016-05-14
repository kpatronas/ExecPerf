# ExecPerf
A simple Python tool that you enter the name of a program, the number of times to run it and a file name to generate a graph with the execution time of each run

Example:
  ./execPerf.py "sensors" 100 out.svg
  First parameter: The name of the program that we want to run, in this example is sensors
  Second parameter: How many times to run this program
  Third parameter: the graph name
  
Graph description:
  x - axis: The execution time in milisecond
  y - axis: The number of runs
  Legend: The name of the program and its parameters, plus min,max,avg values in milisecond
  Graph point: if you hover each graph point you can see details, like value and the run number
