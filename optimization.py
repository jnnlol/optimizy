import time
import os
import colorama
from colorama import Fore
import shutil

colorama.init(autoreset=True)

while True:
    fto = input("(Y/N) Is this your first time opening OPTIMIZY/Installed new update?: ").lower()

    if fto == "n":
        print(Fore.GREEN+"Loading..."+Fore.RESET)
        time.sleep(1)
        os.system("cls")
        break
    elif fto == "y":
        print(Fore.RED + "--------------------------------------------------\nPlease make this file a .exe by running openmefirst.bat\nThis file is located in " + os.getcwd() + "/openmefirst.bat (os doesnt let me open it if you're using a .py file for some reason...)\n--------------------------------------------------" + Fore.RESET)
        input("Press ENTER To close...")
        quit()
    else:
        print("Please select an option!")
        input("Press ENTER To continue...")
        os.system("cls")

def deletetempfile():
    folder = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
    deleteFileCount = 0
    deleteFolderCount = 0

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo + 1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print('%s file deleted' % Fore.GREEN + itemName)
                deleteFileCount = deleteFileCount + 1
            elif os.path.isdir(file_path):
                if 'chocolatey' in file_path:
                    continue
                shutil.rmtree(file_path)
                print('%s folder deleted' % itemName)
                deleteFolderCount = deleteFolderCount + 1
        except Exception as e:
            print(Fore.RED + 'ignore this. couldnt delete %s' % Fore.RED + itemName + " But its ok dont worry")

    print(str(deleteFileCount) + ' files and ' + str(deleteFolderCount) + ' folders deleted.')
    input(Fore.GREEN + "Deleted ALL deletable temp files!")


name = "JNN OPTIMIZER | "


def internetoptimization():
    print(name + Fore.GREEN + name + "Starting INTERNET OPTIMIZATION.." + Fore.RESET)
    time.sleep(2)
    print(Fore.RED + name + "Please do not touch your keyboard." + Fore.RESET)
    time.sleep(1)

    print(name + Fore.GREEN + "Flushing OLD DNS" + Fore.RESET)
    time.sleep(1)
    os.system("ipconfig /flushdns")
    print(Fore.GREEN + name + "----------\nSTEP 1 DONE\n----------" + Fore.RESET)
    time.sleep(1)

    print(name + "Registering new DNS" + Fore.RESET)
    time.sleep(1)
    os.system("ipconfig /registerdns")
    print(Fore.GREEN + name + "----------\nSTEP 2 DONE\n----------" + Fore.RESET)
    time.sleep(1)

    print(name + "Releasing new DNS")
    time.sleep(1)
    os.system("ipconfig /release")
    print(Fore.GREEN + name + "----------\nSTEP 3 DONE\n----------" + Fore.RESET)
    time.sleep(1)

    print(name + "Renewing new DNS" + Fore.RESET)
    time.sleep(1)
    os.system("ipconfig /renew")
    print(Fore.GREEN + name + "----------\nSTEP 4 DONE\n----------" + Fore.RESET)
    time.sleep(1)

    print(name + "Saving NEW DNS" + Fore.RESET)
    time.sleep(1)
    os.system("netsh winsock reset")


def information():
    print(
        "Optimizy is a OPEN SOURCE FILE and it uses pyinstaller to make it to an exe, OPTIMIZY needs to be a .exe so you can run it as admin, therefore it can run commands with cmd. All pyinstaller does is just make it a .exe with the same code. You can review the code here and see there is no malicious activities. To review the code open this in notepad, notepad++, visual studio code, pycharm, or any IDE or Text reader!"
    )


title = Fore.BLUE + "OPTIMIZY " + Fore.RED + "BY JNN" + Fore.RESET

while True:
    print(title)
    options_input = input(Fore.YELLOW + "Options: \n1. Internet Optimization\n2. Clear temp files\n3. Im skeptical of OPTIMIZY and need more information!\nWhat will be your wise choice?: " + Fore.RESET)
    
    if options_input == "1":
        
        internetoptimization()
        os.system("cls")
        break
    elif options_input == "2":
        deletetempfile()
        print("Delete temp files finished!")
        os.system("cls")
        break
    elif options_input == "3":
        information()
        break
    else:
        print("Invalid option. Please select a valid option.")
        input("Press ENTER To continue...")
        os.system("cls")

input()