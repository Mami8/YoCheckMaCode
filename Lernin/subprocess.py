import subprocess
import time
import os

os.chdir("Python")
files = subprocess.getoutput("dir")

print(files)
