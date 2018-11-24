from telethon import TelegramClient, sync
from telethon.tl.patched import Message
from string_session import StringSession
import variables
import os

API_ID = "445674"
API_HASH =" 921ce6d709ed0b6f8b487747c18b50e6"
TELEGRAM_APPID=473887
TELEGRAM_APIHASH="aef057abbbd06dbae724a7e7a8dca9ef"



class User:
    client = 0;
    dataloaded = False
    dataready = False
    data = {}
    mishadata = None
    chatter = None
    def __init__(self, uname ):
        if uname in os.listdir("./sessions"):
            with open("./sessions/"+uname,"r") as i:
                session = i.read()
                self.client = TelegramClient(StringSession(session), TELEGRAM_APPID, TELEGRAM_APIHASH)
                self.client.start()
        else:
            session = StringSession()
            self.client = TelegramClient(session,TELEGRAM_APPID,TELEGRAM_APIHASH)
            self.client.start()
            with open("./sessions/"+uname,"w") as o:
                o.write(session.save())
    def dialogue_changed(self, user): 
        dataloaded = False
        self.chatter = user
        if user not in self.data.keys():
            self.data[user] = []
            for mes in self.client.iter_messages(self.client.get_entity(user),limit = 300):
                if not type(mes) is Message:
                    #print(type(mes))
                    continue
                text = mes.text
                out = mes.out
                date = mes.date
                friend = user
                id = mes.id
                self.data[user].append({  "text":text,
                    "in":not out,
                    "time":date,
                    "chat":user,
                    "id":id})

        else:
            temp = []
            for mes in self.client.iter_messages(self.client.get_entity(user),limit = 300,min_id=(self.data[user][0] and self.data[user][0]["id"] or 0) ):
                if not type(mes) is Message:
                    #print(type(mes))
                    continue
                text = mes.text
                out = mes.out
                date = mes.date
                friend = user
                id = mes.id
                temp.append({  "text":text,
                    "in":not out,
                    "time":date,
                    "chat":user,
                    "id":id})
            self.data[user] = temp + self.data[user]
                         

        dataloaded = True
        self.mishadata = variables.NIKITA(self.data)
        print(self.mishadata)

    def getData():
        return mishadata
    
        
xo = User("XoMute")
xo.dialogue_changed("deedone")
#input()
#xo.dialogue_changed("deedone")



