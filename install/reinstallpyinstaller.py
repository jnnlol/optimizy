import os
import time


print("This file is for problems with pyinstaller, it won't fix all but it downloads latest version.")

os.system("pip uninstall pyinstaller")
time.sleep(1)
os.system("pip install pyinstaller")