import subprocess
import sys
import PySimpleGUI as sg
import re
from time import sleep
import time 
import requests 



sg.theme('Dark Blue 3')


  
  

  

  
  
  
  




def tracert():
	layout = [
				[sg.Text('tracert GUI', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
				[sg.T('Enter HostName'), sg.Input(do_not_clear=False, key="hostname")],
				
				[sg.Text('Choose number of hops:')],
				[sg.Slider(range=(1, 100), orientation='h', size=(20, 10), default_value=12,key="slider")],
				#[sg.T('Save output to TEXT file. Choose Location>> '), sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
				[sg.Output(key='-OUTPUT-',size=(110,10), background_color='#C38EC7', text_color='white')],
				
				[sg.Button('Run', bind_return_key=True), sg.Button('Exit')] ]

	window = sg.Window('GUI Project', layout)
	
	
	while True:             # Event Loop
		event, values = window.read()
			#outputcmd.visibility=True
					
		# print(event, values)
		if event in(sg.WIN_CLOSED,'Exit'):
			window.close()
			event, values= main()
			
				
		elif event == 'Run':
			window['-OUTPUT-'].update('')
			
			runCommand(cmd="tracert -h %d %s" % (values["slider"], values["hostname"]), window=window)
			#outputcmd.visibility=True
		
	window.close()
	
	
	

def pingip():
	layout = [
				[sg.Text('PING GUI', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
				[sg.T('Enter HostName'), sg.Input(do_not_clear=False, key="pinginghost")],
				
				
				
				#[sg.T('Save output to TEXT file. Choose Location>> '), sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
				[sg.Output(key='-OUTPUT-',size=(110,10), background_color='#C38EC7', text_color='white')],
				
				[sg.Button('Run', bind_return_key=True), sg.Button('Back')] ]

	window = sg.Window('GUI Project', layout)
	
	
	while True:             # Event Loop
		event, values = window.read()
			#outputcmd.visibility=True
		
		if event==('Back'):
			window.close()
			event, values = main()
			
		

				
		elif event == 'Run':
			window['-OUTPUT-'].update('')
			
			runCommand(cmd="ping %s" % (values["pinginghost"]), window=window)
			#outputcmd.visibility=True
		
	window.close(); del window	

	

	

def ipconfigu():
	layout = [
				[sg.Text('IPCONFIG GUI', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
				[sg.T('Click Run or press ENTER to get your --ip configurations--'), sg.Input(do_not_clear=False, key="pinginghost")],
				
				[sg.Button('Run', bind_return_key=True)],
				
				#[sg.T('Save output to TEXT file. Choose Location>> '), sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
				[sg.Output(key='-OUTPUT-',size=(110,10), background_color='#C38EC7', text_color='white')],
				
				[sg.Button('Exit')]]

	window = sg.Window('GUI Project', layout)
	
	
	while True:             # Event Loop
		event, values = window.read()
			#outputcmd.visibility=True
		

		
		# print(event, values)
		if event== ('Exit'):
			window.close()
			event,values=main()
			
			
				
		elif event == 'Run':
			window['-OUTPUT-'].update('')
			
			runCommand(cmd="ipconfig", window=window)
			#outputcmd.visibility=True
		
	window.close()


	
def main():
	layout = [
				[sg.Text('NETWORK UTILITY', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
				[sg.Text('Use the Following Commands:')],
				[sg.Button('-ping GUI-'),sg.Button('-ipconfig GUI-'),sg.Button('-tracert GUI-')],
				[sg.Text("-----------------------------------------------------------------------------------------")],
				[sg.Text("-----------------------------------------------------------------------------------------")],
				
				[sg.Text('REALTIME SHELL: ',font=("Helvetica",20))],
				[sg.T('Enter Commands Here> '), sg.Input(key='-IN-', do_not_clear=False)],
				[sg.Output(key='-OUTPUT-',size=(110,10), background_color='#C38EC7', text_color='white')],
				
				[sg.Button('Run', bind_return_key=True), sg.Button('Exit')] ]

	window = sg.Window('GUI Project', layout)

	while True:             # Event Loop
		event, values = window.read()
		
		if event == '-tracert GUI-':
			window.hide()
			event, values = tracert()
				
			#outputcmd.visibility=True
		if event=='-ping GUI-':
			window.hide()
			event, values = pingip()
		if event=='-ipconfig GUI-':
			window.hide()
			event, values= ipconfigu()
		
		
		# print(event, values)
		if event in (sg.WIN_CLOSED, 'Exit'):
			break
		elif event == 'Run':
			window['-OUTPUT-'].update('')
			#outputcmd.visibility=True
			runCommand(cmd=values['-IN-'], window=window)
			
			
				
					
	window.close(); del window


def runCommand(cmd, timeout=None, window=None):
	nop = None
	""" run shell command
	@param cmd: command to execute
	@param timeout: timeout for command execution
	@param window: the PySimpleGUI window that the output is going to (needed to do refresh on)
	@return: (return code from command, command output)
	"""
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = ''
	for line in p.stdout:
		line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
		output += line
		print(line)
		
		window.Refresh() if window else nop        # yes, a 1-line if, so shoot me

	retval = p.wait(timeout)
	return (retval, output)
	


main()