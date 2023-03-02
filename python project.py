import operator
import os
import re
import subprocess
import time
class adblibrary:
    def __init__(self):
      print("My adb commads")

def log_validation():
     with open("F:/example/logfile1.txt", 'w+') as f:
      res = subprocess.run("adb shell service list",stdout=f,shell=True)
     print("command output",res)
     #f.seek(0)
     #content = f.read()
     #print("content", content)
     #f.close()


# string validationl
#if activity in content:
 #   print('Pass - string exist in a file - Pass')
#else:
#    print('Fail - string does not exist in a file')

log_validation()

