print("PFLANZENMASCHINE-SERVER")
print("Import modules")
from flask import *
print("ALERT <INIT> ALERT")
ids=list()
keys=list()
strs=list()
print("Starting up...")
app = Flask(__name__)
def createkey(id, key, str):
    ids.append(id)
    keys.append(key)
    strs.append(str)
    return id
def removekey(id):
    rmid=ids.index(id)
    ids.remove(rmid)
    keys.remove(rmid)
    strs.remove(rmid)
    return rmid
def getkey(id):
