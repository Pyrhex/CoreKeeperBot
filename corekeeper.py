import os
import time
import traceback
import discord
import os
import requests
from dhooks import Webhook
from steam import Steam
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
STEAM_API_KEY = os.getenv('STEAM_API_KEY')

class FileModified():
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback
        self.modifiedOn = os.path.getmtime(file_path)
    def start(self):
        try:
            while (True):
                modified = os.path.getmtime(self.file_path)
                if modified != self.modifiedOn:
                    self.modifiedOn = modified
                    if self.callback():
                        break
        except Exception as e:
            print(traceback.format_exc())
def sendWebhook(url, message, color):
    data = {}
    data["embeds"] = [
        {
            "title" : message,
            "color" : color
        }
    ]
    try:
        result = requests.post(url, json = data)
        result.raise_for_status()
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success! Notification sent!')   
        
def getNameFromID(id):
    steam = Steam(STEAM_API_KEY)
    user = steam.users.get_user_details(id)
    return(user["player"]["personaname"])

def file_modified():
    hook = Webhook(WEBHOOK_URL)
    num_newlines = 0
    with open("../CoreKeeperServerLog.txt", 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)    
            while num_newlines < 1:
                f.seek(-2, os.SEEK_CUR)
                if f.read(1) == b'\n':
                    num_newlines += 1
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
        try:
            if "connection from" in last_line:
                sendWebhook(WEBHOOK_URL, getNameFromID(''.join([n for n in last_line if n.isdigit()])) + " has joined the game", "65280")
            if "Disconnected" in last_line:
                sendWebhook(WEBHOOK_URL, getNameFromID(''.join([n for n in last_line if n.isdigit()])) + " has left the game", "16711680")
        except Exception as e:
            print(e)
    return False

fileModifiedHandler = FileModified(r"../CoreKeeperServerLog.txt",file_modified)
fileModifiedHandler.start()
