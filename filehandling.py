# write one python script witch check folde exist or not 
# if it is exist then create one "Agenda.txt" file in it 

import os 
import sys

if os.path.exists("/home/mayur/study/Python_basic/pyton_in_15_days"):
    for i in range(1,16):
        os.chdir("/home/mayur/study/Python_basic/pyton_in_15_days")
        dirname = "Day"+ str(i)
        if os.path.exists(dirname):
            print("directory already present")
            os.chdir(dirname)
            with open("Agenda.txt","w") as file:
                file.write(dirname)
        else:
            os.mkdir(dirname)
            os.chdir(dirname)
            with open("Agenda.txt","w") as file:
                file.write(dirname)