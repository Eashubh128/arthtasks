
import os
import subprocess
import webbrowser
def choice_result(x):
   if (x == 1):
   	print(" Opening web browser >>>>>>>>> \n")
    name = input(" Enter what you want to search????? \n")
    webbrowser.open('https://{}'.format(name),new =2) 
   if (x == 2):
   	print(" Opening notepad >>>>>>>>> \n")
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
   if (x == 3):
   	print(" Opening calculator >>>>>>>>>>>> \n")
   	subprocess.Popen('C:\\Windows\\System32\\calc.exe')
   if (x == 4):
   	print(" Seems like you want to do remote login to a system \n ")
   	ip = input(" I would need the ip address of that system \n ")
    subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
    username = input("I would need the username of the system also")
    password = input("I would need the password of the system \n")
    os.system('cmd /k "ssh {}@{}"'.format(username,ip))


    
def menu():
	print("Choose a choice to continue : \t\n\
		Select 1 to \n\  Select 2 to  \n\ Select 3 to ")
import os
import serverautomation.py
import dockerconfig.py
import subprocess
import webbrowser
def choice_result(x):
   if (x == 1):
   	print(" Opening web browser >>>>>>>>> \n")
    name = input(" Enter what you want to search????? \n")
    webbrowser.open('https://{}'.format(name),new =2) 
   if (x == 2):
   	print(" Opening notepad >>>>>>>>> \n")
    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
   if (x == 3):
   	print(" Opening calculator >>>>>>>>>>>> \n")
   	subprocess.Popen('C:\\Windows\\System32\\calc.exe')
   if (x == 4):
   	print(" Seems like you want to do remote login to a system \n ")
   	ip = input(" I would need the ip address of that system \n ")
    subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
    username = input("I would need the username of the system also")
    password = input("I would need the password of the system \n")
    os.system('cmd /k "ssh {}@{}"'.format(username,ip))
   if (x == 5):
     dockerconfig()
   if (x == 6):
     serverautomation()
   return 0;
    
def menu():
	print("Choose a choice to continue : \t\n\
		Select 1 to websearch\n\  Select 2 to open notepad \n\ Select 3 to open the calculator \n\ Select 4 to remote login to a system \n\ Select 5 to configure Docker \n\ Select 6 to Configure Webserver")

    choice = int(input("Enter the choice from the menu shown:\t"));
    choice_result(choice)
    
    choice = int(input("Enter the choice from the menu shown:\t"));

    choice_result(choice)


    
