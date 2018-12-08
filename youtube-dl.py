## Small command line program to save time when using the Youtube-dl module
## Nick Springham

# update youtube-dl

import os
import time
import subprocess
import pyperclip



command = r"youtube-dl --extract-audio --audio-format mp3 -o %(title)s.%(ext)s "
user_input = input("\nEnter full Youtube URL: ")

cmd_call = command + user_input

# change directory
directory = r"C:\enter\destination\directory"
os.chdir(directory)

time.sleep(1)
print("\n" + "Running: " + cmd_call + "\n")
print("This file will be found in: " + os.getcwd() + "\n")
# run the youtube dl

#os.system(cmd_call)
subprocess.Popen('explorer '+ directory)
