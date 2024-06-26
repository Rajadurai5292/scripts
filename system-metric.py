#!/usr/bin/python3
#Calculate the system metrics such as load, memory and Storage
#x="syntellers"
#print(x)
#Import modules
import os
import sys
# Allow only the root user to execute the script
if os.geteuid()==0:
  print('Exceuted Successfully.')
else:
  print('Access Denied.')
#get the system load
#Defining the function
def get_system_load():
  print('Calculate the system load')
  print('Enter time range for system load (1,5,15):')
  time_range = int(input())
  if time_range==1:
    output =os.getloadavg()[0]
  elif time_range==5:
    output =os.getloadavg()[1]
  elif time_range==15:
    output =os.getloadavg()[2]
  else:
  print('Invalid input.')
  print('The system load average for %i minute is %s' %(time_range,output))
#Get the system memory
def get_system_memory():
  print('Calculate the system memory')

#Get the system storage
def get_system_storage():
  print('Calculate the system storage')

#Calling function
# get_system_load()
# calling function based on cli arguments
if sys.argv[1]=='load':
  get_system_load()
elif sys.argv[1]=='memory':
  get_system_memory()
elif sys.argv[1]== 'storage':
  get_system_storage()
else:
  print('Help: ./system-metric.py {load|memory|storage}')