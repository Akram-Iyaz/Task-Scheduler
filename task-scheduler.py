import os,time
from time import strftime
os.system('#!/usr/bin/zsh;zsh')
os.system('#!~/.zshrc')
os.system('source /usr/SHELL/.appeal.zsh')
job=input("Enter the Command you want to execute: ")
print("On what time you want to execute the task!\nTime format=HH:MM:SS\nNOTE ':' will be added automatically\n")
task_time=input("24 hour time:  ")
task_time=task_time[0:2]+":"+task_time[2:4]+":"+task_time[4:]
while True:
	if strftime("%H:%M:%S") == task_time:
		os.system(job)
		time.sleep(2)
		break
		
