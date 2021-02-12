import os,time
from time import strftime
os.system('#!/usr/bin/zsh')
job=input("Enter the Command you want to execute: ")
print("On what time you want to execute the task!, time format=HH:MM:SS")
task_time=input("24 hour time:  ")
while strftime("%H:%M:%S") != task_time:
	if strftime("%H:%M:%S") == task_time:
		os.system(job)
		time.sleep(5)
		break
		
