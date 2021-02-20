import json
import os

def check():
    if os.path.exists("data.json") == True:
        print("yes")
    else:
        f = open("data.json","a+")
        f.close()

check()

