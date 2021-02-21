import json
import os

def check():
    if os.path.exists("data.json") == True:
        pass
    else:
        f = open("data.json","a+")
        f.write("[]")
        f.close()

check()

