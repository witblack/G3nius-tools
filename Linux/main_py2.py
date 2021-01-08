#!/usr/bin/python2
# coding: utf-8
try:
	from termcolor import colored
	import os
	import sys
	import shutil
	import subprocess
	from time import sleep
except:
	print('[!] Some deepends not installed.')
	print('Run "pip install sys os termcolor time"')
	exit(1)
try:
	execfile(os.path.dirname(os.path.abspath(__file__)) + '/lib/functionsPyTwo.py')
except:
	print(colored('[!] Failed to load some some local libs.','red'))
	print(colored("If you're sure to don't change local files report it.",'red'))
	print(colored('Email : admin@bugzone.ir','red'))
	exit(1)
print(colored('[ *** ] ','green') + colored('Starting G3n!us ..','white'))
Location = os.path.dirname(os.path.abspath(__file__))
Menu_Numebrs = 0
Plugins = []
if os.path.isdir(Location + '/tmp'):
	shutil.rmtree(Location + '/tmp')
elif os.path.isfile(Location + '/tmp'):
	os.remove(Location + '/tmp')
os.mkdir(Location + '/tmp')
def Clear():
	global Version
	if OS == 'Windows':
		print(os.popen('cls').read())
	elif OS == 'Linux':
		print('\033c')
	else:
		print('\033c\x1bc')
	if OS == '':
		tmp_OS = 'Unknown'
	else:
		tmp_OS = OS
	print(colored(' _______________________________________________________________________','red'))
	print(colored('|','red') + colored(' ▒███▒ ▒████           █                ','magenta') + colored('  |','red') + colored(' Programmer info:          ','white') + colored('|','red'))
	print(colored('|','red') + colored('░█▒ ░█ █▒  ▓█          █                ','magenta') + colored('  |','red') + colored('---------------------------|','red'))
	print(colored('|','red') + colored('█▒          █ █▒██▒    █    █   █  ▒███▒','magenta') + colored('  |','red') + colored(' Programmed by WitBlack    ','green') + colored('|','red'))
	print(colored('|','red') + colored('█          ▒█ █▓ ▒█    █    █   █  █▒ ░█','magenta') + colored('  |','red') + colored(' Github ~>                 ','white') + colored('|','red'))
	print(colored('|','red') + colored('█   ██   ███░ █   █    █    █   █  █▒░  ','magenta') + colored('  |','red') + colored('Https://github.com/WitBlack','blue') + colored('|','red'))
	print(colored('|','red') + colored('█    █     ▓█ █   █    █    █   █  ░███▒','magenta') + colored('  |','red') + colored(' Website ~>                ','white') + colored('|','red'))
	print(colored('|','red') + colored('█▒   █      █ █   █         █   █     ▒█','magenta') + colored('  |','red') + colored('Https://BugZone.ir         ','blue') + colored('|','red'))
	print(colored('|','red') + colored('▒█░ ░█ █░  ▓█ █   █    █    █▒ ▓█  █░ ▒█','magenta') + colored('  |','red') + colored(' E-Mail ~>                 ','white') + colored('|','red'))
	print(colored('|','red') + colored(' ▒███▒ ▒████  █   █    █    ▒██▒█  ▒███▒','magenta') + colored('  |','red') + colored('admin@bugzone.ir           ','blue') + colored('|','red'))
	print(colored('|','red') + colored('                                 _________|___________________________|','red'))
	print(colored('|','red') + colored('________________________________|','red') + colored('                       ███           ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' Information :                  ','white') + colored('|','red') + colored(' ███████                 █           ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('--------------------------------','red') + colored('|','red') + colored('    █                    █           ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' Python Version: ','blue') + colored('2              ','white') + colored('|','red') + colored('    █     ███    ███     █    ▒███▒  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(" VERSION ",'blue') + colored(Version + '                  ','white') + colored('|','red') + colored('    █    █▓ ▓█  █▓ ▓█    █    █▒ ░█  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored(' OS: ','blue') + colored(tmp_OS + '			 ','white') + colored('|','red') + colored('    █    █   █  █   █    █    █▒░    ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █    █   █  █   █    █    ░███▒  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █    █   █  █   █    █       ▒█  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █    █▓ ▓█  █▓ ▓█    █░   █░ ▒█  ','magenta') + colored('|','red'))
	print(colored('|','red') + colored('                                ','white') + colored('|','red') + colored('    █     ███    ███     ▒██  ▒███▒  ','magenta') + colored('|','red'))
	print(colored('|________________________________|_____________________________________|','red'))
	print(colored('| Warning:','red') + colored(" Don't break or kill script while process runing.            ",'yellow') + colored('|','red'))
	print(colored('|______________________________________________________________________|\n','red'))
	del tmp_OS
def Generate_Menu(Plugin_List):
	ret = ''
	for Plugin in Plugin_List:
		ret += colored(str(Plugin[0]),'green') + ' ' + colored(Plugin[2],'white')
	return ret
try:
	List = os.listdir(Location+'/plugins')
except:
	print(colored("[!] Can't find plugins folder.",'red'))
	exit(1)
Name,Title,File,ID = None,None,None,0
for Name in List:
	ID += 1
	if not os.path.exists(Location + '/plugins/' + Name + '/main2.py'):
		if os.path.exists(Location + '/plugins/' + Name + '/main3.py'):
			print(colored('[!] Failed to load "' + Name + '" plugin.','yellow'))
			print(colored("Becase it's writen for Python3 and you're using Python2.",'yellow'))
		else:
			print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
			print(colored('Becase "main2.py" or "main3.py" file in script folder not exists.','red'))
		ID -= 1
		try:
			sleep(1.5)
		except:
			exit(0)
		continue
	if not os.path.exists(Location + '/plugins/' + Name + '/Title.txt'):
		print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
		print(colored('Becase "Title.txt" file in script folder not exists.','red'))
		ID -= 1
		try:
			sleep(1.5)
		except:
			exit(0)
		continue
	try:
		File = open(Location + '/plugins/' + Name + '/Title.txt','r')
		Title = File.read()
		File.close()
	except:
		print(colored('[!] Failed to load "' + Name + '" plugin.','red'))
		print(colored('Becase "Title.txt" file in script folder not have read permission.','red'))
		ID -= 1
		try:
			sleep(3)
		except:
			exit(0)
		continue
	File = open(Location + '/plugins/' + Name + '/main2.py','r')
	if File.read()[0:2] == '#!':
		OpenSource = True
	else:
		OpenSource = False
	File.close()
	Plugins.append([ID,Name,Title,OpenSource])
Menu_Numebrs = ID
del Name,Title,ID,File,OpenSource
if len(Plugins) == 0:
	print(colored('[!] ','red') + colored('No plugins were found health and available, So Exit.','yellow'))
	exit(1)
print(colored('[ *** ] G3n!us started successfully.','green'))
while True:
	Clear()
	print(Generate_Menu(Plugins) + colored(str(Menu_Numebrs + 1),'green') + colored(' Exit','white'))
	try:
		Choose = int(raw_input(colored('\n\nEnter your number: ','blue')))
	except:
		try:
			print(colored('Invalid Choose','yellow'))
			sleep(1)
			continue
		except:
			print(colored('Good by..', 'magenta'))
			exit(0)
	if Choose == Menu_Numebrs + 1:
		print(colored('Good by..', 'magenta'))
		exit(0)
	Find = False
	for Plugin in Plugins:
		if Plugin[0] == Choose:
			Find = True
			if Plugin[3]:
				Clear()
				try:
					try:
						execfile(Location + '/plugins/' + Plugin[1] + '/main2.py')
					except EndScript:
						pass
				except Exception as EX:
					print(colored('Some where plugin get error! Failed job(s).','red'))
					print(colored('Error:','red'))
					print(colored(EX,'red'))
				except:
					print(colored('Some where plugin get error! Failed job(s).','red'))
			else:
				Clear()
				try:
					subprocess.call(Location + '/plugins/' + Plugin[1] + '/main2.py')
				except Exception as EX:
					if str(EX)[0:28] == '[Errno 8] Exec format error:':
						print(colored("ERROR: This plugin not optimized for your CPU.",'red'))
						print(colored("Check lastest update, May by i'ts Ok.",'red'))
					else:
						print(colored('Some where plugin get error! Failed job(s).','red'))
						print(colored('Error:','red'))
						print(colored(EX,'red'))
				except:
					print(colored('Some where plugin get error! Failed job(s).','red'))
	if Find:
		try:
			Choose = raw_input(colored('[?] ', 'yellow') + colored(' Work finished. Do you want exit from script ? [y/n] ', 'white'))
		except:
			print(colored('Good by..', 'magenta'))
			exit(0)
		if str.lower(Choose) == 'y' or str.lower(Choose) == 'yes' or str.lower(Choose) == 'exit':
			print(colored('Good by..', 'blue'))
			exit(0)
	else:
            		print(colored('Plugin not found!','red'))