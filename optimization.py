
import time
import os
import colorama
from colorama import Fore
import os
import shutil


#----------------------------------------------------------------------------------
# HEY GUYS! JNN HERE, Now you might think the exe is sketchy, well i would too!   |
# good job on being cautious about what you download online, but heres the thing. |
# for this  optimizer to run, you would need to make it a .exe because it needs   |
# admin on your computer to execute commands, for example to make your internet   |
# faster, then it has to use commands with os, but you can't run python files     |
# as admin! now the way i fixed this is i made it into a .exe with pyinstaller,   |
# which if you dont trust the .exe from releases in github, you can too!           -----
# but ofc the exe is easier to download. Stay safe guys and install your rqeuirements!!|
# thanks, -jnn                                                                         |
#---------------------------------------------------------------------------------------







def deletetempfile():
    folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'

    deleteFileCount = 0
    deleteFolderCount = 0

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo+1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print( '%s file deleted' %Fore.GREEN+itemName )
                deleteFileCount = deleteFileCount + 1

            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                print( '%s folder deleted' % itemName )
                deleteFolderCount = deleteFolderCount + 1

        except Exception as e:
            print(Fore.RED+'ignore this. couldnt delete %s' % Fore.RED+itemName+" But its ok dont worry")

    print(str(deleteFileCount)+' files and '+ str(deleteFolderCount)+' folders deleted.')
    input(Fore.GREEN+"Deleted ALL deletable temp files!")


# required to make this all into one file...

name = "JNN OPTIMIZER | "

def internetoptimization():
    print(name + Fore.GREEN + name + "Starting INTERNET OPTIMIZATION.."+Fore.RESET)
    time.sleep(2)
    print(Fore.RED + name + "Please do not touch your keyboard."+Fore.RESET)
    time.sleep(1)

    print(name + Fore.GREEN + "Flushing OLD DNS"+Fore.RESET)
    time.sleep(1)
    os.system("ipconfig /flushdns")
    print(Fore.GREEN + name + "----------\nSTEP 1 DONE\n----------"+Fore.RESET)
    time.sleep(1)
    
    print(name + "Registering new DNS"+Fore.RESET)
    time.sleep(1)
    os.system("ipconfig /registerdns")
    print(Fore.GREEN + name + "----------\nSTEP 2 DONE\n----------"+Fore.RESET)
    time.sleep(1)

    print(name + "Releasing new DNS")
    time.sleep(1)
    os.system("ipconfig /release")
    print(Fore.GREEN + name + "----------\nSTEP 3 DONE\n----------"+Fore.RESET)
    time.sleep(1)

    print(name + "Renewing new DNS"+Fore.RESET)
    time.sleep(1)
    os.system("ipconfig /renew")
    print(Fore.GREEN + name + "----------\nSTEP 4 DONE\n----------"+Fore.RESET)
    time.sleep(1)

    print(name + "Saving NEW DNS"+Fore.RESET)
    time.sleep(1)
    os.system("netsh winsock reset")





def makefileexe():
    print(Fore.GREEN+name+"Installing Pyinstaller..."+Fore.RESET)
    os.system("pip install pyinstaller")
    print(Fore.GREEN+name+"Done!"+Fore.RED+"Please do not touch your keyboard or mouse.+Fore.RESET"+Fore.RESET)
    time.sleep(2.5)
    os.system("python -m PyInstaller optimization.py --onefile")# if you changed the file name this wont work. make sure you replace optimization.py with the file name, if you downloaded this and didnt change anything then this should work.
    print(Fore.GREEN+name+"EXE Made! It is inside of the Dist folder in "+os.getcwd()+"\dist\optimization.exe"+Fore.RESET)





def reinstallpyinstaller():
    os.system("pip uninstall pyinstaller")
    print(Fore.GREEN+name+"Uninstalled pyinstaller!\nInstalling latest version..."+Fore.RESET)
    time.sleep(2)
    os.system("pip install pyinstaller")
    print(Fore.GREEN+name+"Done!"+Fore.RESET)




# important
colorama.init(autoreset=True)  # so colors show in terminal
title = Fore.BLUE + "OPTIMIZY "+ Fore.RED+"BY JNN"+Fore.RESET

print(title)

while True:
    options = input("Options: \n1. Internet Optimization\n2. Clear temp files\n3. (WON'T WORK IF YOU ALREADY HAVE THE .EXE FILE) Make this file into a .exe\n4. Reinstall PYINSTALLER\n5. Exit\nWhat will be your wise choice?: ")

    if options == "1":
        internetoptimization()
        print("Done! Going back to main menu!")
    elif options == "2":
        deletetempfile()
        print("Delete temp files finished!")
        print("Done! Going back to main menu!")
    elif options == "3":
        makefileexe()
        print("Done! Going back to main menu!")
    elif options == "4":
        reinstallpyinstaller()
        print("Done! Going back to main menu!")
    elif options == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

    input("Press ENTER to continue...")

input()