mport os

import platform

def shutdown():

system_name = platform.system()

if system_name == "Windows":

os.system("shutdown /s /t 1")