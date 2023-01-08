import os
import time
import traceback
import discord
from dhooks import Webhook

players = {
    "76561198041082081": "Austin",
    "76561198089087294": "Cody",
    "76561198168154937": "Brian"
}
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

def file_modified():
    hook = Webhook('INSERT WEBHOOK HERE')
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
                embed = discord.Embed(title=players[''.join([n for n in last_line if n.isdigit()])] + " has joined the game")
                hook.send(embed=embed)
            if "Disconnected" in last_line:
                embed = discord.Embed(title=players[''.join([n for n in last_line if n.isdigit()])] + " has left the game")
                hook.send(embed=embed)
        except:
            if "connection from" in last_line:
                embed = discord.Embed(title=''.join([n for n in last_line if n.isdigit()]) + " has joined the game")
                hook.send(embed=embed)
            if "Disconnected" in last_line:
                embed = discord.Embed(title=''.join([n for n in last_line if n.isdigit()]) + " has left the game")
                hook.send(embed=embed)
    return False

    
fileModifiedHandler = FileModified(r"../CoreKeeperServerLog.txt",file_modified)
fileModifiedHandler.start()
