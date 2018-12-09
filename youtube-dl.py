## Small command line program to save time when using the Youtube-dl module
## Nick Springham


import os
import time
import subprocess
import sys


command = r"youtube-dl --extract-audio --audio-format mp3 -o %(title)s.%(ext)s "
user_input = input("\nEnter full Youtube URL: ")

cmd_call = command + user_input

# command line argument to determine the folder and change the working directory to that folder
if sys.argv[1] == "pod":
  directory = r"C:\Users\Nick\Music\podcasts"
  os.chdir(directory)
elif sys.argv[1] == "aco":
  directory = r"C:\Users\Nick\Music\acoustic"
  os.chdir(directory)
else:
  directory = r"C:\Users\Nick\Music"
  directory = directory + "\\" + sys.argv[1]
  if os.path.isdir(directory):
    os.chdir(directory)
  else:
    os.mkdir(directory)
    os.chdir(directory)


time.sleep(1)

print("\n" + "Running: " + cmd_call + "\n")
print("This file will be found in: " + os.getcwd() + "\n")

# run the youtube dl
os.system(cmd_call)
subprocess.Popen('explorer '+ directory)
