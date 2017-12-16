# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile, timeit
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator
from selenium import webdriver

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="")
ki9.loginResult()

ki10 = LINETCR.LINE()
ki10.login(token="")
ki10.loginResult()
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage= """ 
╔═══════════════════
╠              ✍MENU V.1✍️
╠❂͜͡➣「Key」Gimage: [Judul]
╠❂͜͡➣「Key」Wikipedia: [Judul]
╠❂͜͡➣「Key」Youtube: [Judul]
╠❂͜͡➣「Key」Instagram: [Name]
╠❂͜͡➣「Key」Vn: [Text]
╠❂͜͡➣「Key」Musik: [Song Name]
╠❂͜͡➣「Key」Lirik: [Song Name]
╠❂͜͡➣「Key」Google: [Text]
╠❂͜͡➣「Key」Ig check: [Name
╠❂͜͡➣「Key」Ig bio: [Name]
╠❂͜͡➣「Key」Ig pict: [Name]
╠❂͜͡➣「Key」Ig pictl: [Link]
╠❂͜͡➣「Key」Ig vidl: [Link]
╠❂͜͡➣「Key」Ig link: [Name
╚═══════════════════
"""
helpMessage2= """ 
╔═══════════════════
╠              ✍MENU V.2✍️
╠❂͜͡➣「Key」Searchid: [Id]
╠❂͜͡➣「Key」Searchmid: [Mid]
╠❂͜͡➣「Key」AddId:[Id]
╠❂͜͡➣「Key」AddMid: [Mid]
╠❂͜͡➣「Key」Checkmid: [Mid]
╠❂͜͡➣「Key」Midcover: [Mid]
╠❂͜͡➣「Key」Midpict: [Mid]
╠❂͜͡➣「Key」Midbio: [Mid]
╠❂͜͡➣「Key」Midname:[Mid]
╠❂͜͡➣「Key」Bot:restart
╠❂͜͡➣「Key」Bot:runtime
╚═══════════════════

"""
helpMessage3= """ 
╔═══════════════════
╠              ✍MENU V.3✍️
╠❂͜͡➣「Key」Getinfo [@tag]
╠❂͜͡➣「Key」Getbio [@tag]
╠❂͜͡➣「Key」Getmid [@tag]
╠❂͜͡➣「Key」Getcontact [@tag
╠❂͜͡➣「Key」Getpict [@tag]
╠❂͜͡➣「Key」Getcover [@tag]
╠❂͜͡➣「Key」Getpicturl [@tag]
╠❂͜͡➣「Key」Getcoverurl [@tag]
╚═══════════════════
"""
helpMessage4= """ 
╔═══════════════════
╠              ✍MENU V.4✍️
╠❂͜͡➣「Key」Myname: [Name]
╠❂͜͡➣「Key」Mybio: [Name]
╠❂͜͡➣「Key」Myname
╠❂͜͡➣「Key」Mybio
╠❂͜͡➣「Key」Mypict
╠❂͜͡➣「Key」Mycover
╠❂͜͡➣「Key」Mypicturl
╠❂͜͡➣「Key」Mycoverurl
╠❂͜͡➣「Key」Friendlist
╠❂͜͡➣「Key」Glist/Glist2
╚═══════════════════
"""
helpMessage5= """ 
╔═══════════════════
╠              ✍MENU V.5✍️
╠❂͜͡➣「Key」Gn: [Name]
╠❂͜͡➣「Key」Ourl/Curl
╠❂͜͡➣「Key」Gpict
╠❂͜͡➣「Key」Gpicturl
╠❂͜͡➣「Key」Gpict [Name]
╠❂͜͡➣「Key」Tagall
╠❂͜͡➣「Key」Setview
╠❂͜͡➣「Key」Viewseen
╠❂͜͡➣「Key」Spam?
╠❂͜͡➣「Key」Set spam:[Text]
╠❂͜͡➣「Key」Spam:10-50 [@tag]
╚═══════════════════
"""
helpMessage6= """ 
╔═══════════════════
╠              ✍MENU V.6✍️
╠❂͜͡➣「Key」Copy [@tag]
╠❂͜͡➣「Key」Copy name [@tag]
╠❂͜͡➣「Key」Copy bio [@tag]
╠❂͜͡➣「Key」Copy image [@tag]
╠❂͜͡➣「Key」Copy cover [@tag]
╠❂͜͡➣「Key」Backup
╚═══════════════════
"""
setMessage= """ 
╔═══════════════════
╠    ✍MENU SETTING BOT✍️
╠❂͜͡➣「Key」Aread: on/off
╠❂͜͡➣「Key」Arespon: on/off
╠❂͜͡➣「Key」Autokick: on/off
╠❂͜͡➣「Key」Backup: on/off
╚═══════════════════
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid
Fmid = ki6.getProfile().mid
Gmid = ki7.getProfile().mid
Hmid = ki8.getProfile().mid
Imid = ki9.getProfile().mid
Jmid = ki10.getProfile().mid
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
admin = ["uc72e39d8c26cb3aacad5201e6f2c348c",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
owner = "uc72e39d8c26cb3aacad5201e6f2c348c"

wait = {
    "rn1":"Reva",
    "rn2":"Laras",
    "rn3":"Natasha",
    "rn4":"Wilona",
    "rn5":"Kadev",
    "rn6":"Cantik",
    "rn7":"Caim",
    "rn8":"Tasya",
    "rn9":"Acha",
    "rn10":"Ozawa",
    "sq":"Sayang",
    "AutoKick":False,    
    "detectMention":False,      
    "alwaysRead":False,   
    "kickMention":False,
    "talkban":True,
    "Pap":"http://www.rockcreekdothan.com/Common/images/jquery/galleria/image-not-found.png",
    "Key":False,
    "SetKey":"",
    "creator":"",
    "spam":"Your Account Has Been Spammed"
    'invite':{},
    'spam':{},
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'invite':False,
    'autoAdd':False,
    'message':"""тнαикѕ fσя α∂∂ιиg мє αѕ α fяιєи∂
≫ ɪғ ɪ ɴᴏᴛ ᴀɴsᴡᴇʀ ᴊᴜsᴛ sᴘᴀᴍ ≪
≫ sʟᴏᴡ ʀᴇsᴘᴏɴ ᴀᴛ 7ᴀᴍ ᴛɪʟʟ 6ᴘᴍ ≪

Ready:

≫ bot protect ≪
≫ SelfBot ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃☆
iD Line:
   🛡 http://line.me/ti/p/~satria_hk 🛡
""",
    "lang":"JP",
    "comment":"""Auto Like By SaTria
≫ ɪғ ɪ ɴᴏᴛ ᴀɴsᴡᴇʀ ᴊᴜsᴛ sᴘᴀᴍ ≪
≫ sʟᴏᴡ ʀᴇsᴘᴏɴ ᴀᴛ 7ᴀᴍ ᴛɪʟʟ 6ᴘᴍ ≪

Ready:

≫ Bot protect ≪
≫ SelfBot protect ≪
≫ Siri V10 ≪
≫ Vip Smule ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃☆
iD Line:
   🛡 http://line.me/ti/p/~satria_hk 🛡
""",
    'welmsg':"welcome to group",
    'commentOn':True,
    'commentBlack':{},
    'wblack':False,
    'dblack':False,
    'clock':False,
    'cName':"",
    'status':False,
    'blacklist':{},
    'whitelist':{},
    'wblacklist':False,
    'dblacklist':False,
    'qr':False,
    'pname':False,
    'poni':False,
    'Backup':False,
    'protectionOn':False,
    'winvite':False,
    'kickon':{},
    'pnharfbot':{},
    'pname':{},
    'pro_name':{},
    'kickon':False,
    'autorein':True,
    'welcomemsg':False,
    'Setkey':False,
    'steal':False,
    'stealcontact':False,

    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'copy':False,
    'target':{},
    'midstarget':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
mebackup = ki.getProfile()
mebackup.displayName = contact.displayName
mebackup.statusMessage = contact.statusMessage
mebackup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
mobackup = ki2.getProfile()
mobackup.displayName = contact.displayName
mobackup.statusMessage = contact.statusMessage
mobackup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
mabackup = ki3.getProfile()
mabackup.displayName = contact.displayName
mabackup.statusMessage = contact.statusMessage
mabackup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
mibackup = ki4.getProfile()
mibackup.displayName = contact.displayName
mibackup.statusMessage = contact.statusMessage
mibackup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
mubackup = ki5.getProfile()
mubackup.displayName = contact.displayName
mubackup.statusMessage = contact.statusMessage
mubackup.pictureStatus = contact.pictureStatus

contact = ki6.getProfile()
mlbackup = ki6.getProfile()
mlbackup.displayName = contact.displayName
mlbackup.statusMessage = contact.statusMessage
mlbackup.pictureStatus = contact.pictureStatus

contact = ki7.getProfile()
mnbackup = ki7.getProfile()
mnbackup.displayName = contact.displayName
mnbackup.statusMessage = contact.statusMessage
mnbackup.pictureStatus = contact.pictureStatus

contact = ki8.getProfile()
mmbackup = ki8.getProfile()
mmbackup.displayName = contact.displayName
mmbackup.statusMessage = contact.statusMessage
mmbackup.pictureStatus = contact.pictureStatus

contact = ki9.getProfile()
mpbackup = ki9.getProfile()
mpbackup.displayName = contact.displayName
mpbackup.statusMessage = contact.statusMessage
mpbackup.pictureStatus = contact.pictureStatus

contact = ki10.getProfile()
mqbackup = ki10.getProfile()
mqbackup.displayName = contact.displayName
mqbackup.statusMessage = contact.statusMessage
mqbackup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#----Gimage---#
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
#---Gimage----#    

#-----Runtime------#
mulai = time.time()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
#-----Runtime------#        

#-----Youtube----#
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
#-----Youtube-----#         
#----Restart----#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv) 
#----Restart----#    

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
				    except:
					try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki3.updateGroup(G)
                                except:
                                    try:
                                        ki4.updateGroup(G)
                                    except:
                                        try:
                                            ki5.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        ki.sendText(op.param1,"please do not change group name-_-")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in mid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Amid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Amid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Bmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Bmid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Cmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Dmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Emid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Fmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Gmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Gmid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Hmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Hmid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Imid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                if op.param3 in Imid:
                    if op.param2 in Jmid:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
#================================================
                if op.param3 in Jmid:
                    if op.param2 in Amid:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Gmid:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Hmid:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Imid:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Jmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
#================================================
        if op.type == 15:
            if wait["autorein"] == True:
               if op.param2 in admin:
                  klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                  kicker = random.choice(klist)
                  kicker.inviteIntoGroup(op.param1,[op.param2])

#===========================================
        if op.type == 32:
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if Bmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki2.rejectGroupInvitation(op.param1)
                        else:
                            ki2.acceptGroupInvitation(op.param1)
                    else:
                        ki2.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki2.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki2.cancelGroupInvitation(op.param1, matched_list)
            if Cmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki3.rejectGroupInvitation(op.param1)
                        else:
                            ki3.acceptGroupInvitation(op.param1)
                    else:
                        ki3.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki3.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')   
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki3.cancelGroupInvitation(op.param1, matched_list)
            if Dmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki4.rejectGroupInvitation(op.param1)
                        else:
                            ki4.acceptGroupInvitation(op.param1)
                    else:
                        ki4.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki4.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki4.cancelGroupInvitation(op.param1, matched_list)
            if Emid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki5.rejectGroupInvitation(op.param1)
                        else:
                            ki5.acceptGroupInvitation(op.param1)
                    else:
                        ki5.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki5.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki5.cancelGroupInvitation(op.param1, matched_list)
            if Fmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki6.rejectGroupInvitation(op.param1)
                        else:
                            ki6.acceptGroupInvitation(op.param1)
                    else:
                        ki6.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki6.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')   
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki6.cancelGroupInvitation(op.param1, matched_list)
            if Gmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki7.rejectGroupInvitation(op.param1)
                        else:
                            ki7.acceptGroupInvitation(op.param1)
                    else:
                        ki7.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki7.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki7.cancelGroupInvitation(op.param1, matched_list)
            if Hmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki8.rejectGroupInvitation(op.param1)
                        else:
                            ki8.acceptGroupInvitation(op.param1)
                    else:
                        ki8.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki8.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki8.cancelGroupInvitation(op.param1, matched_list)
            if Imid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki9.rejectGroupInvitation(op.param1)
                        else:
                            ki9.acceptGroupInvitation(op.param1)
                    else:
                        ki9.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki9.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')   
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki9.cancelGroupInvitation(op.param1, matched_list)
            if Jmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki10.rejectGroupInvitation(op.param1)
                        else:
                            ki10.acceptGroupInvitation(op.param1)
                    else:
                        ki10.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki10.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')   
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki10.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 15:
            if wait["welcomemsg"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nDih Baper Diaa.. Suee 😁😁\n(´･ω･`)")
                print "MEMBER OUT GROUP"
        if op.type == 17:
	   if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 contact = cl.getContact(op.param2)
                 image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                 cl.sendImageWithURL(op.param1,image)
                 cl.sendText(op.param1,"Hay    "+cl.getContact(op.param2).displayName +"\n"+  wait["welmsg"]+"\nGroup》》"+ str(ginfo.name))
                 cl.sendText(op.param1,"Hay    "+cl.getContact(op.param2).displayName +"Kenalin OWner Group   " + ginfo.creator.displayName)
                 c = Message(to=op.param1, from_=None, text=None, contentType=13)
                 c.contentMetadata={'mid':op.param2}
                 cl.sendMessage(c)
        if op.type == 17:
            if op.param2 not in admin:
                if op.param2 not in Bots:
                    if wait["steal"] == True:
                       contact = cl.getContact(op.param2)
                       image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                       random.choice(KAC).sendImageWithURL(op.param1,image)
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                       print "[command]Foto"
                    else:
                        pass
        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                if not op.param2 in Bots and admin: 
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    cl.sendText(op.param1,"blacklist users are not allowed to sign in  -_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param3}
                    cl.sendMessage(c)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    cl.sendText(op.param1,"please do not open link group-_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    cl.sendMessage(c)

                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots and admin:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    cl.sendText(op.param1,"please do not Kick Members-_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    cl.sendMessage(c)

                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True:  
                    klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        cl.sendText(op.param1,"you are prohibited from inviting-_-")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        cl.sendMessage(c)
        if op.type == 15:
             if op.param2 in admin:
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
           else: 
               pass

        if op.type == 19:
           if op.param3 in admin:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,admin)
           else: 
               pass

        if op.type == 19:
           if op.param3 in mid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,mid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Amid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Amid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Bmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Bmid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Cmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Cmid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Dmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Dmid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Emid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Emid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Fmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Fmid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Gmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Gmid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Hmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Hmid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Imid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Imid)
           else: 
               pass

        if op.type == 19:
           if op.param3 in Jmid:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,Jmid)
           else: 
               pass
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       ki10.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       ki10.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots and admin:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                       ki.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        ki2.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        ki3.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ticket = ki2.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        ki4.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ticket = ki3.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        ki5.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki4.updateGroup(X)
                    Ticket = ki4.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        ki6.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki5.updateGroup(X)
                    Ticket = ki5.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#===============================================
                if Fmid in op.param3:
                    if op.param2 in Bots and admin:
                        pass                    
                    try:
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                        ki7.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki6.updateGroup(X)
                    Ticket = ki6.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                        ki8.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki8.updateGroup(X)
                    Ti = ki8.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki7.updateGroup(X)
                    Ticket = ki7.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                        ki9.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki9.updateGroup(X)
                    Ti = ki9.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki8.updateGroup(X)
                    Ticket = ki8.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                        ki10.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    G = ki10.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki10.updateGroup(G)
                    Ti = ki10.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki9.updateGroup(X)
                    Ticket = ki9.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki11.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki12.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki13.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki14.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki15.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki10.updateGroup(X)
                    Ti = ki10.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                    
#================================================
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if wait["talkban"] == True:
             if msg.from_ in wait["talkblacklist"]:
                try:
                    random.choice(KAC).sendText(msg.to,ki.getContact(msg.fr
om_).displayName + " Jangan Ngomong Sue")
                    random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                except:
                    try:
                        random.choice(KAC).sendText(msg.to,ki.getContact(msg
.from_).displayName + " Jangan Ngomong Njiir")
                        random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        ki.sendText(msg.to,ki.getContact(msg.from_).displayName + " Jangan Ngomong Njiir")
                        ki.kickoutFromGroup(msg.to,[msg.from_])
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                random.choice(KAC).sendText(msg.to, data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Siboss lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Apa Sayang"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Your out",cName + " Your Out?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja kick you", cName + " Kenapa Tag saya? your out","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT"]
                     ret_ = "[Auto Kick] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  random.choice(KAC).sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break
        if op.type == 26:
            if wait["alwaysRead"] == True:
                msg = op.message
                if msg.toType == 2:
                    msg.to = msg.to
                    msg.from_ = msg.from_
                    cl.sendChatChecked(msg.to,msg.id)


        if op.type == 26:
            if wait["alwaysRead"] == True:
                msg = op.message
                if msg.toType == 0:
                    msg.to = msg.from_
                    msg.from_ = msg.to
                    cl.sendChatChecked(msg.from_,msg.id)
            
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["stealcontact"] == True:
                    if msg.from_ in admin:
                        _name = msg.contentMetadata["displayName"]
                        copy = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                print "[Target] Stealed"
                                break                             
                            else:
                                targets.append(copy)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.sendText(msg.to,"Target added" + _name)
                                    cl.findAndAddContactsByMid(target)
                                    contact = cl.getContact(target)
                                    y = contact.statusMessage
                                    cu = cl.channel.getCover(target)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cl.sendText(msg.to,"displayPicture " + contact.displayName)
                                    cl.sendImageWithURL(msg.to,image)
                                    cl.sendText(msg.to,"coverPicture " + contact.displayName)
                                    cl.sendImageWithURL(msg.to,path)
                                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                                    cl.sendText(msg.to,"|" + contact.displayName + "|\n\n" + y)
                                    wait["stealcontact"] = False
                                    break
                                except:
                                    pass                        
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 random.choice(KAC).sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 random.choice(KAC).sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 random.choice(KAC).sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     random.choice(KAC).findAndAddContactsByMid(target)
                                     random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         random.choice(KAC).findAndAddContactsByMid(invite)
                                         random.choice(KAC).inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         random.choice(KAC).sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
            	if wait["kickon"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                             break                             
                             else:
                                 targets.append(kick)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     random.choice(KAC).findAndAddContactsByMid(target)
                                     random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Done Kick : \n➡" + _name)
                                     wait["kickon"] = False
                                     break
                                 except:
                                     try:
                                         random.choice(KAC).findAndAddContactsByMid(invite)
                                         random.choice(KAC).kickoutFromGroup(op.param1,[invite])
                                         wait["kickon"] = False
                                     except:
                                         random.choice(KAC).sendText(msg.to,"Negative, Error detected")
                                         wait["kickon"] = False
                                         break
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Clone on"]:
                if msg.from_ in admin:
                    wait["clone"] = True
                    cl.sendText(msg.to,"Send contact To clone") 
            elif wait["SetKey"]+"Kick on" in msg.text:
                if msg.from_ in admin:
                    wait["kickon"] = True
                    cl.sendText(msg.to,"Send contact To kick")
            elif wait["SetKey"]+"Steal" in msg.text:
                if msg.from_ in admin:
                    wait["stealcontact"] = True
                    cl.sendText(msg.to,"Send contact")
            elif wait["SetKey"]+"Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")     
            elif wait["SetKey"]+"Invite on" in msg.text:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact To invite")
            elif (wait["SetKey"]+"Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace(wait["SetKey"]+"Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif (wait["SetKey"]+"Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace(wait["SetKey"]+"Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif wait["rn1"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn1"]+" invite:","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif wait["rn2"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn2"]+" invite:","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif wait["rn3"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn3"]+" invite:","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif wait["rn4"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn4"]+" invite:","")
                ki4.findAndAddContactsByMid(midd)
                ki4.inviteIntoGroup(msg.to,[midd])
            elif wait["rn5"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn5"]+" invite:","")
                ki5.findAndAddContactsByMid(midd)
                ki5.inviteIntoGroup(msg.to,[midd])
            elif wait["rn6"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn6"]+" invite:","")
                ki6.findAndAddContactsByMid(midd)
                ki6.inviteIntoGroup(msg.to,[midd])
            elif wait["rn7"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn7"]+" invite:","")
                ki7.findAndAddContactsByMid(midd)
                ki7.inviteIntoGroup(msg.to,[midd])
            elif wait["rn8"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn8"]+" invite:","")
                ki8.findAndAddContactsByMid(midd)
                ki8.inviteIntoGroup(msg.to,[midd])
            elif wait["rn9"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn9"]+" invite:","")
                ki9.findAndAddContactsByMid(midd)
                ki9.inviteIntoGroup(msg.to,[midd])
            elif wait["rn10"]+" invite:" in msg.text:
                midd = msg.text.replace(wait["rn10"]+" invite:","")
                ki10.findAndAddContactsByMid(midd)
                ki10.inviteIntoGroup(msg.to,[midd])
            #elif msg.text.lower() == 'mebot':
            elif wait["SetKey"]+"Mebot" in msg.text:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                cl.sendMessage(msg)
            elif wait["rn1"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif wait["rn2"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
            elif wait["rn3"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki3.sendMessage(msg)
            elif wait["rn4"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki4.sendMessage(msg)
            elif wait["rn5"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ki5.sendMessage(msg)
            elif wait["rn6"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                ki6.sendMessage(msg)
            elif wait["rn7"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ki7.sendMessage(msg)
            elif wait["rn8"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ki8.sendMessage(msg)
            elif wait["rn9"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ki9.sendMessage(msg)
            elif wait["rn10"]+" Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                ki10.sendMessage(msg)
                
#================================================
            #elif msg.text in ["Gift","gift"]:
            elif "Gift" in msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,"  「Gift Fiture」\n\n●Gift1\n●Gift2\n●Gift3\n●Gift4\n●Gift5\n●Gift6\n●Gift you\n●Bot1~6 gift")
            elif wait["SetKey"]+"Gift" in msg.text:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift1':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift2':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift3':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift4':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift5':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift6':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift you","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki2.sendMessage(msg)
            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki4.sendMessage(msg)

            elif msg.text in ["Bot5 Gift","Bot5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                ki5.sendMessage(msg)
            elif msg.text in ["Bot6 Gift","Bot6 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki6.sendMessage(msg)
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members: 
                    if _nametarget == g.displayName:
                        msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME', 'MSGTPL': '10'}
                        msg.text = None
                        cl.dendMessage(msg.to)

#-----------------------------------------------                                                
            elif wait["SetKey"]+"Chat stiker" in msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,"●Love\n●Love you\n●Wek\n●Hore\n●Ok/Okay\n●Tanks\n●Oye\n●Halo\n●Wow\n●Cius\n●Apa\n●Kesel\n●Hah\n●Miss you/Micuu\n●Huft\n●Njiir\n●Apa loe\n●Bobok\n●Sebel\n●Lol/No/Sue")
            elif msg.text.lower() == 'love you':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846754",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'wek':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'okay':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846758",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'tanks':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'oye':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846760",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'halo':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846761",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'love':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846762",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'wow':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846763",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'cius':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846764",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'apa':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846765",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'kesel':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846766",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'hah':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846767",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'micuu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846768",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'huft':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846769",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'miss you':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846770",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'njiir':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846771",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'apa loe':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846772",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'bobok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846773",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'sebel':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846774",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'no':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'sue':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846775",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'apa?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == '250c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1380280'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text.lower() == '200c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1319678'}
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            
            elif msg.text in ["B Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif wait["SetKey"]+"Cancel" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            #elif msg.text in ["Link on"]:
            elif wait["SetKey"]+"Link on" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif wait["SetKey"]+"Link off" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close ô€¨👈")
                    else:
                        cl.sendText(msg.to,"URL close ô€¨👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif msg.text in ["Seeinvite"]:
              if msg.from_ in admin:
                try:
                    gr = cl.getGroupIdsInvited()
                    inv = ""
                    for grp in gr:
                    	inv += "• " (cl.getGroup(grp).name)
                    cl.sendText(msg.to, "Pending Group :\n\n"+ inv +"\n\nTotal Pending Group :" +"["+str(len(gr))+"]")
                except:
                    cl.sendText(msg.to,"Nothing Group Invitation")
            elif wait["SetKey"]+"Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"『Group Name』\n" + str(ginfo.name) + "\n\n『Group ID』\n" + msg.to + "\n\n『Group Creator』\n" + gCreator + "\n\n『Members』:" + str(len(ginfo.members)) + "\n『Pending』:" + sinvitee + "")
                cl.sendMessage(msg)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
            
            elif msg.text.lower() == 'ginfo2':        
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Memid" == msg.text:
                cl.sendText(msg.to,mid)
            elif wait["rn1"]+" mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif wait["rn2"]+" mid" == msg.text:
                ki2.sendText(msg.to,Bmid)
            elif wait["rn3"]+" mid" == msg.text:
                ki3.sendText(msg.to,Cmid)
            elif wait["rn4"]+" mid" == msg.text:
                ki4.sendText(msg.to,Dmid)
            elif wait["rn5"]+" mid" == msg.text:
                ki5.sendText(msg.to,Emid)
            elif wait["rn6"]+" mid" == msg.text:
                ki6.sendText(msg.to,Fmid)
            elif wait["sq"]+" mid" == msg.text:
                ki.sendText(msg.to,Amid)
                ki2.sendText(msg.to,Bmid)
                ki3.sendText(msg.to,Cmid)
                ki4.sendText(msg.to,Dmid)
                ki5.sendText(msg.to,Emid)
                ki6.sendText(msg.to,Fmid)
                ki7.sendText(msg.to,Gmid)
                ki8.sendText(msg.to,Hmid)
                ki9.sendText(msg.to,Imid)
                ki10.sendText(msg.to,Jmid)
            elif wait["SetKey"]+"TL:" in msg.text:
                tl_text = msg.text.replace(wait["SetKey"]+"TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#================================================
            elif wait["sq"]+" name:" in msg.text:
                string = msg.text.replace(wait["sq"]+" name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈 Sukses\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif wait["sq"]+" Allbio:" in msg.text:
                string = msg.text.replace(wait["sq"]+" Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)

                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "Sukses👈")
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈\n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------------------------------
            elif wait["rn1"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn1"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈\n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------------------------------
            elif wait["rn2"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn2"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn3"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn3"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn4"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn4"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn5"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn5"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn6"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn6"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#================================================
            elif wait["rn7"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn7"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn8"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn8"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn9"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn9"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#------------------------------------------------
            elif wait["rn10"]+" up pname:" in msg.text:
                string = msg.text.replace(wait["rn10"]+" up pname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "Sukses👈")
#===============================================                                            
            elif wait["SetKey"]+"Kerang ajaib" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,"「Fitur Kerang Ajaib」\n\n●Kapan「text」\n●Apakah「text」\n●Berapa「text」")

            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            elif msg.text in ["Creator gw"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                jawab = ("This is my Creator","My creator is handsome","My creator is cool")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            elif wait["SetKey"]+"Translate" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,"「Fitur Translate」\n\n●Translate-arab「text」\n●Translate-korea「text」\n●Translate-chin「text」\n●Translate-japan「text」\n●"Translate-thai「text」\n●Translate-idn「text」\n●Translate-eng「text」\n●Id@en「text」\n●En@id「text」\n●Id@jp「text」\n●Jp@id「text」\n●Id@th「text」\n●Th@id「text」\n●Id@ar「text」\n●Ar@id「text」\n●Id@ko「text」\n●Ko@id「text」")
            elif "Translate-arab " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-arab ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'ar')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
            elif "Translate-korea " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-korea ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'ko')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
            elif "Translate-chin " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-chin ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'zh-cn')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
	    elif "Translate-japan " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-japan ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'ja')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
   	    elif "Translate-thai " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-thai ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'th')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
            elif "Translate-idn " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-idn ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'id')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')

            elif "Translate-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-eng ","")
                try:
                    translator = Translator()
                    trs = translator.translate(txt,'en')
                    A = trs.text
                    A = A.encode('utf-8')
                    cl.sendText(msg.to,A)
                except:
                      cl.sendText(msg.to,'Error.')
#=================================#
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")

            elif msg.text in ["Protect:on","Protect on"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:off","Qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:on","Qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:off","Protect off"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ\n\n"+ datetime.today().strftime('%H:%M:%S'))					
            elif "Blockinvite on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ\n\n"+ datetime.today().strftime('%H:%M:%S'))
				except:
					pass
            elif "steal on" in msg.text.lower():
                if msg.from_ in admin:
                    if wait["steal"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Steal join on(　^ω^)")
                        else:
                            cl.sendText(msg.to,"Done")
                    else:
                        wait["steal"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Steal join on(　^ω^)")
                        else:
                            cl.sendText(msg.to,"Done")
            elif "steal off" in msg.text.lower():
                if msg.from_ in admin:
                    if wait["steal"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Steal join off (´▽｀)")
                        else:
                            cl.sendText(msg.to,"Done")
                    else:
                        wait["steal"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Steal join off")
                        else:
                            cl.sendText(msg.to,"Done")
        	            
	    elif msg.text in ["Autorein off","auto reinvite:off"]:
              if msg.from_ in admin:
                if wait["autorein"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autorein"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Autorein on","auto reinvite:on"]:
              if msg.from_ in admin:
                if wait["autorein"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Already on\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to ,"Already on\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autorein"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to, "Already on\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Auto leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Auto leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text in ["Key on","key on"]:
                if wait["Key"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Key Set To on\n\n􀜁􀇔􏿿"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Key sudah on👈\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Key"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on👈")
                    else:
                        cl.sendText(msg.to,"Already on👈")
            elif msg.text in ["Key off","key off"]:
                if wait["Key"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set Key To off👈􀜁􀇔􏿿\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["Key"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off👈")
                    else:
                        cl.sendText(msg.to,"Already Off👈")
            elif msg.text in ["Like:on"]:
              if msg.from_ in admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"auto like on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"auto like on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"auto like on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"auto like on")
            elif msg.text in ["Like:off"]:
              if msg.from_ in admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"auto like off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"auto like off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"auto like off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"auto like off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Welcome message on","Wc on"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
            elif msg.text in ["Welcome message off","Wc off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Chatbot on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Chatbot off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","Read:on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto Sider ON")
                
            elif msg.text in ["Read off","Read:off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto Sider OFF")
                
            elif msg.text in ["Autorespon on","Tag on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Auto Respon ON")
                
            elif msg.text in ["Autorespon off","Tag off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto Respon OFF")
            
            elif msg.text in ["Autokick on","Notag on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"Auto Kick ON")
                
            elif msg.text in ["Autokick off","Notag off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"Auto Kick OFF") 
            elif msg.text in [wait["SetKey"]+"Set",wait["SetKey"]+"set"]:
                md = "🔐Setting For Bot🔐\n\n"
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀜁􀇔􏿿 Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "􀜁􀇔􏿿 Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add:off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Auto komentar:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto komentar:off 􀜁􀄰􏿿\n"
                if wait["welcomemsg"] == True: md+="􀜁􀇔􏿿 Welcome Message:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Welcome message:off 􀜁􀄰􏿿\n"
                if wait["detectMention"] == True: md+="􀜁􀇔􏿿 tag:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 tag:off 􀜁􀄰􏿿\n\n"
                if wait["pname"] == True: md+="􀜁􀇔􏿿NameLock:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿NameLock:off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀜁􀇔􏿿Backup:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿Backup:off 􀜁􀄰􏿿\n"
                if wait["poni"] == True: md+="􀜁􀇔􏿿Blockinvite:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿Blockinvite:off 􀜁􀄰􏿿\n"
                if wait["protectionOn"] == True: md+="􀜁􀇔􏿿Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿Protect:off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀜁􀇔􏿿Qr:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿Qr:off 􀜁􀄰􏿿\n\n"+ datetime.today().strftime('🔖Date: %Y-%m-%d \n⌛Days: %A \n⏰Time: %H:%M:%S')
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                cl.sendMessage(msg)
#--------------------------------------------------------

	    elif wait["SetKey"]+"Autokick:on" in msg.text:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif wait["SetKey"]+"Autokick:off" in msg.text:
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
	    elif wait["SetKey"]+"Backup:on" in msg.text:
	        wait["Backup"] = True
	    	cl.sendText(msg.to,"Backup Invite Member Active")

	    elif wait["SetKey"]+"Backup:off" in msg.text:
	    	wait["Backup"] = False
	    	cl.sendText(msg.to,"Backup Invite Member inActive")   
#--------------------------------------------------------	    	
	    elif wait["SetKey"]+"Aread:on" in msg.text:
	        wait["alwaysRead"] = True
	    	cl.sendText(msg.to,"Auto Read Active")

	    elif wait["SetKey"]+"Aread:off" in msg.text:
	    	wait["alwaysRead"] = False
	    	cl.sendText(msg.to,"Auto Read inActive")	    	
#-------------------------------------------------------- 
#-------------------------------------------------------- 
	    elif wait["SetKey"]+"Arespon:on" in msg.text:
	        wait["detectMention"] = True
	    	cl.sendText(msg.to,"Auto Respon Active")

	    elif wait["SetKey"]+"Arespon:off" in msg.text:
	        wait["detectMention"] = False
	    	cl.sendText(msg.to,"Auto Respon inActive")
#-------------------------------------------------------- 
	    elif msg.text in [wait["SetKey"]+"Restart"]:
		cl.sendText(msg.to, "Bot Program has been restarted")
		restart_program()
		print "@Restart"
#--------------------------------------------------------
            elif msg.text.lower() == 'bot:runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)	
            elif wait["SetKey"]+"Runtime" in msg.text:
                eltime = time.time() - mulai
                van = "「Selfbot 」\n" "Type:Runtime\nTime: "+ waktu(eltime)
                cl.sendText(msg.to,"「 Runtime Bot 」\n" "Status: Processing")
                cl.sendText(msg.to,van)	
                cl.sendText(msg.to,"「 Runtime Bot 」\n" "Status: Success")
#---------------------------------------------
            #elif msg.text.lower() == 'me':
            elif wait["SetKey"]+wait["me"] in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': creator}
                cl.sendText(msg.to,"􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿")
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'sf1 gid':
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,h)
            elif msg.text.lower() == 'sf2 gid':
                gid = ki2.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki2.getGroup(i).name,i)
                ki2.sendText(msg.to,h)
            elif msg.text.lower() == 'sf3 gid':
                gid = ki3.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki3.getGroup(i).name,i)
                ki3.sendText(msg.to,h)
            elif msg.text.lower() == 'sf4 gid':
                gid = ki4.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki4.getGroup(i).name,i)
                ki4.sendText(msg.to,h)
            elif msg.text.lower() == 'sf5 gid':
                gid = ki5.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki5.getGroup(i).name,i)
                ki5.sendText(msg.to,h)
            elif msg.text.lower() == 'sf6 gid':
                gid = ki6.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki6.getGroup(i).name,i)
                ki6.sendText(msg.to,h)

            elif msg.text.lower() == wait["SetKey"]+'groups':
                gs = cl.getGroupIdsJoined()
                num=1
                L = "『Groups List』\n"
                for i in gs:
                    L += "\n%i. %s\n%s\n" % (num, cl.getGroup(i).name + " | " + str(len (cl.getGroup(i).members)), i)
                    num=(num+1)
                L += "\nTotal Groups: [ %i ]" % len(gs)
                cl.sendText(msg.to, L + "\n                   °✍⟿SATRIA_SELF⟿\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == wait["sq"]+' out':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    ki10.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Satria Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif wait["SetKey"]+"Group creator" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")

#------------------------------------------------
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Khusus Creator")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
            elif msg.text in ["Group cancelall","Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Auto add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
#========================================
            elif wait["SetKey"]+"Update welcome:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace(wait["SetKey"]+"Update welcome:","")
                cl.sendText(msg.to,"update welcome to "+wait["welmsg"]+ " succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"welcome  message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
            elif "Key set:" in msg.text:
              if msg.from_ in admin:
                wait["SetKey"] = msg.text.replace("Key set:","")
                cl.sendText(msg.to,"update welcome to "+wait["SetKey"]+ " succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Mykey"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"「Key」\n\n" + wait["SetKey"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["SetKey"])
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Up squad:" in msg.text:
                wait["sq"] = msg.text.replace("Up squad:","")
                cl.sendText(msg.to,"Set To "+wait["sq"]+" Sukses")
            elif wait["rn1"]+" up rname:" in msg.text:
                wait["rn1"] = msg.text.replace(wait["rn1"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn1"]+" Sukses")
            elif wait["rn2"]+" up rname:" in msg.text:
                wait["rn2"] = msg.text.replace(wait["rn2"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn2"]+" Sukses")
            elif wait["rn3"]+" up rname:" in msg.text:
                wait["rn3"] = msg.text.replace(wait["rn3"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn3"]+" Sukses")
            elif wait["rn4"]+" up rname:" in msg.text:
                wait["rn4"] = msg.text.replace(wait["rn4"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn4"]+" Sukses")
            elif wait["rn5"]+" up rname:" in msg.text:
                wait["rn5"] = msg.text.replace(wait["rn5"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn5"]+" Sukses")
            elif wait["rn6"]+" up rname:" in msg.text:
                wait["rn6"] = msg.text.replace(wait["rn6"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn6"]+" Sukses")
            elif wait["rn7"]+" up rname:" in msg.text:
                wait["rn7"] = msg.text.replace(wait["rn7"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn7"]+" Sukses")
            elif wait["rn8"]+" up rname:" in msg.text:
                wait["rn8"] = msg.text.replace(wait["rn8"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn8"]+" Sukses")
            elif wait["rn9"]+" up rname:" in msg.text:
                wait["rn9"] = msg.text.replace(wait["rn9"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn9"]+" Sukses")
            elif wait["rn10"]+" up rname:" in msg.text:
                wait["rn10"] = msg.text.replace(wait["rn10"]+" up rname:","")
                cl.sendText(msg.to,"Set To "+wait["rn10"]+" Sukses")
            elif wait["me"]+" set:" in msg.text:
                wait["me"] = msg.text.replace(wait["me"]+" set:","")
                cl.sendText(msg.to,"Set To "+wait["me"]+" Sukses")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")
            
            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")   
#----------------------------------------
            elif "Invite to " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invite to ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.getGroupIdsJoined(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Sf1invite: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Sf1invite: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Sf2invite: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Sf2invite: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki2.findAndAddContactsByMid(msg.from_)
                            ki2.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki2.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Sf3invite: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Sf3invite: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki3.findAndAddContactsByMid(msg.from_)
                            ki3.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki3.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Sf4invite: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Sf4invite: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki4.findAndAddContactsByMid(msg.from_)
                            ki4.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki4.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Sf5invite: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Sf5invite: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki5.findAndAddContactsByMid(msg.from_)
                            ki5.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki5.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Sf6invite: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Sf6invite: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki6.findAndAddContactsByMid(msg.from_)
                            ki6.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki6.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif "Admin on @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"succes add to adminlist")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
            elif msg.text.lower() == 'admin list':
              if msg.from_ in owner:
                if owner == []:
                       cl.sendText(msg.to,"The adminlist is empty")
                else:
                        cl.sendText(msg.to,"loading...")
                        num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in admin:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════Staff List ═══════\n"
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Conmin"]:
                if wait["admin"] == {}:
                    cl.sendText(msg.to,"Not admin  ")
                else:
                    cl.sendText(msg.to,"Daftar admin")
                    h = ""
                    for i in wait["admin"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif "Expel on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Expel on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Succes remove admin from adminlist")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
#-----------------------------------------------l
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#========================================
            elif msg.text in ["Myname"]:
                h = cl.getContact(mid)
                cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
#==============================#
            elif msg.text in ["Getpict"]:
                    h = cl.getContact(msg.to)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Getvid"]:
                    h = cl.getContact(msg.to)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Getcover"]:
                    h = cl.getContact(msg.to)
                    cu = cl.channel.getCover(msg.to)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)

            elif wait["SetKey"]+"Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace(wait["SetKey"]+"Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif wait["SetKey"]+"Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace(wait["SetKey"]+"Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif wait["SetKey"]+"Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace(wait["SetKey"]+"Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif wait["SetKey"]+"Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace(wait["SetKey"]+"Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif wait["SetKey"]+"Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace(wait["SetKey"]+"Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"

            elif wait["rn1"]+" Steal cover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace(wait["rn1"]+" Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ki.getContact(target)
                            cu = ki.channel.getCover(target)
                            path = str(cu)
                            ki.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif wait["rn1"]+" Steal pic " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace(wait["rn1"]+" Steal pic ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = ki.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = ki.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    ki.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
#========================================
            elif msg.text in ["Restore"]:
                try:
                    ki.updateDisplayPicture(mebackup.pictureStatus)
                    ki.updateProfile(mebackup)
                    ki2.updateDisplayPicture(mobackup.pictureStatus)
                    ki2.updateProfile(mobackup)
                    ki3.updateDisplayPicture(mabackup.pictureStatus)
                    ki3.updateProfile(mabackup)
                    ki4.updateDisplayPicture(mibackup.pictureStatus)
                    ki4.updateProfile(mibackup)
                    ki5.updateDisplayPicture(mubackup.pictureStatus)
                    ki5.updateProfile(mubackup)
                    ki6.updateDisplayPicture(mlbackup.pictureStatus)
                    ki6.updateProfile(mlbackup)
                    ki7.updateDisplayPicture(mnbackup.pictureStatus)
                    ki7.updateProfile(mnbackup)
                    ki8.updateDisplayPicture(mmbackup.pictureStatus)
                    ki8.updateProfile(mmbackup)
                    ki9.updateDisplayPicture(mpbackup.pictureStatus)
                    ki9.updateProfile(mpbackup)
                    ki10.updateDisplayPicture(mqbackup.pictureStatus)
                    ki6.updateProfile(mqbackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#----------------------------------------------
            elif wait["sq"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki2.cloneContactProfile(target)
                                    ki3.cloneContactProfile(target)
                                    ki4.cloneContactProfile(target)
                                    ki5.cloneContactProfile(target)
                                    ki6.cloneContactProfile(target)
                                    ki7.cloneContactProfile(target)
                                    ki8.cloneContactProfile(target)
                                    ki9.cloneContactProfile(target)
                                    ki10.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#===============================================
            elif wait["SetKey"]+"Myclone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Myclone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif msg.text in ["Myrestore"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#===============================================
            elif wait["rn1"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn1"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn1"]+" restore" in msg.text:
                try:
                    ki.updateDisplayPicture(mebackup.pictureStatus)
                    ki.updateProfile(mebackup)
                    ki.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki.sendText(msg.to, str (e))
#===============================================
            elif wait["rn2"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn2"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki2.cloneContactProfile(target)
                                    ki2.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn2"]+" restore" in msg.text:
                try:
                    ki2.updateDisplayPicture(mobackup.pictureStatus)
                    ki2.updateProfile(mobackup)
                    ki2.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki2.sendText(msg.to, str (e))
#===============================================
            elif wait["rn3"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn3"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki3.cloneContactProfile(target)
                                    ki3.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn3"]+" restore" in msg.text:
                try:
                    ki3.updateDisplayPicture(mabackup.pictureStatus)
                    ki3.updateProfile(mabackup)
                    ki3.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki3.sendText(msg.to, str (e))
#===============================================
            elif wait["rn4"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn4"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki4.cloneContactProfile(target)
                                    ki4.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn4"]+" restore" in msg.text:
                try:
                    ki4.updateDisplayPicture(mibackup.pictureStatus)
                    ki4.updateProfile(mibackup)
                    ki4.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki4.sendText(msg.to, str (e))
#===============================================
            elif wait["rn5"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn5"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki5.cloneContactProfile(target)
                                    ki5.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn5"]+" restore" in msg.text:
                try:
                    ki5.updateDisplayPicture(mubackup.pictureStatus)
                    ki5.updateProfile(mubackup)
                    ki5.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki5.sendText(msg.to, str (e))
#===============================================
            elif wait["rn6"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn6"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki6.cloneContactProfile(target)
                                    ki6.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn6"]+" restore" in msg.text:
                try:
                    ki6.updateDisplayPicture(mlbackup.pictureStatus)
                    ki6.updateProfile(mlbackup)
                    ki6.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki6.sendText(msg.to, str (e))
#================================================
            elif wait["rn7"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn7"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki7.cloneContactProfile(target)
                                    ki7.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn7"]+" restore" in msg.text:
                try:
                    ki7.updateDisplayPicture(mnbackup.pictureStatus)
                    ki7.updateProfile(mnbackup)
                    ki7.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki7.sendText(msg.to, str (e))
#===============================================
            elif wait["rn8"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn8"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki8.cloneContactProfile(target)
                                    ki8.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn8"]+" restore" in msg.text:
                try:
                    ki8.updateDisplayPicture(mmbackup.pictureStatus)
                    ki8.updateProfile(mmbackup)
                    ki8.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki8.sendText(msg.to, str (e))
#===============================================
            elif wait["rn9"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn9"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki9.cloneContactProfile(target)
                                    ki9.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn9"]+" restore" in msg.text:
                try:
                    ki9.updateDisplayPicture(mpbackup.pictureStatus)
                    ki9.updateProfile(mpbackup)
                    ki9.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki9.sendText(msg.to, str (e))
#===============================================
            elif wait["rn10"]+" clone @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["rn10"]+" clone @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki10.cloneContactProfile(target)
                                    ki10.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif wait["rn10"]+" restore" in msg.text:
                try:
                    ki10.updateDisplayPicture(mqbackup.pictureStatus)
                    ki10.updateProfile(mqbackup)
                    ki10.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki10.sendText(msg.to, str (e))
#================================================
            elif msg.text == "Lurking":
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Result":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Lurking dulu dudul Baru bilang Result Point.")
#===============================================
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki10.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki10.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif (wait["rn1"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif (wait["rn2"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif (wait["rn3"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif (wait["rn4"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif (wait["rn5"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif (wait["rn6"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki6.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"Error")
            elif (wait["rn7"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki7.kickoutFromGroup(msg.to,[target])
                       except:
                           ki7.sendText(msg.to,"Error")
            elif (wait["rn8"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki8.kickoutFromGroup(msg.to,[target])
                       except:
                           ki8.sendText(msg.to,"Error")
            elif (wait["rn9"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki9.kickoutFromGroup(msg.to,[target])
                       except:
                           ki9.sendText(msg.to,"Error")
            elif (wait["rn10"]+" kiss " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki10.kickoutFromGroup(msg.to,[target])
                       except:
                           ki10.sendText(msg.to,"Error")
            elif ("Vkick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")
#------------------------------------------------

#------------------------------------------------    
            elif wait["SetKey"]+"Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace(wait["SetKey"]+"Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif wait["SetKey"]+"Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace(wait["SetKey"]+"Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                cl.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif wait["SetKey"]+"Ban:" in msg.text:                  
                       nk0 = msg.text.replace(wait["SetKey"]+"Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif wait["SetKey"]+"Unban:" in msg.text:                  
                       nk0 = msg.text.replace(wait["SetKey"]+"Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    cl.sendText(msg.to,_name + " Not In Blacklist")
                                    
            elif msg.text in ["Clear"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"􀠁􀆩􏿿 Nothing in the blacklist")
                else:
                    random.choice(KAC).sendText(msg.to,"􀠁􀆩􏿿 following is a blacklist")
                    num=1
                    msgs="User Black List\n"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n%i. %s" % (num, mi_d.displayName)
                        num=(num+1)
                    msgs+="\n\nTotal %i blacklist user(s)" % len(["blacklist"])
                    cl.sendText(msg.to, msgs)
                    #mc = ""
                    #for mi_d in wait["blacklist"]:
                        #mc += ">" +cl.getContact(mi_d).displayName + "\n"
                    #ki.sendText(msg.to,mc)

            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="════════List Blacklist═══════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n%i• %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n════════List Blacklist═══════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "════════List Blacklist═══════"
                    for mm in matched_list:
                        cocoa+="\n%i• %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═══════List Blacklist═══════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)

            elif msg.text == 'Kill ban':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif wait["sq"]+" Cleanse" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace(wait["sq"]+" Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    ki.sendText(msg.to,"Just some casual cleansing ")
                    ki2.sendText(msg.to,"Group cleansed.")
                    ki3.sendText(msg.to,"Bye All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        ki2.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                ki2.sendText(msg,to,"Group cleanse")
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
#========================================

#-----------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "Offline" in msg.text:
                midd = msg.text.replace("Offline","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
            elif cms(msg.text,["Sc off"]):
                    cl.sendText(msg.to,"Script Off")
                    exit(1)
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#----------------------------------------------

#==============================================
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + " Hadir 􀨁􀄻􏿿" + "􀜁􀅔􏿿"
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + " Hadir 􏿿" + "􀜁􀅔􏿿"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + " Hadir 􀨁􀄻􏿿" + "􀜁􀅔􏿿"
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + " Hadir 􀨁􀄻􏿿" + "􀜁􀅔􏿿"
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + " Hadir 􀨁􀄻􏿿"+ "􀜁􀅔􏿿"
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + " Hadir 􀨁􀄻􏿿" + "􀜁􀅔􏿿"
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName + " Hadir 􀨁􀄻" + "􀜁􀅔􏿿"
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = profile.displayName + " Hadir " + "􀜁􀅔􏿿"
                ki8.sendText(msg.to, text)
                profile = ki9.getProfile()
                text = profile.displayName + " Hadir 􏿿" + "􀜁􀅔􏿿"
                ki9.sendText(msg.to, text)
                profile = ki10.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                ki10.sendText(msg.to, text)
            elif msg.text.lower() == 'responsename':
               
                ki.sendText(msg.to, wait["rn1"])
                ki2.sendText(msg.to, wait["rn2"])
                ki3.sendText(msg.to, wait["rn3"])
                ki4.sendText(msg.to, wait["rn4"])
                ki5.sendText(msg.to, wait["rn5"])
                ki6.sendText(msg.to, wait["rn6"])
                ki7.sendText(msg.to, wait["rn7"])
                ki8.sendText(msg.to, wait["rn8"])
                ki9.sendText(msg.to, wait["rn9"])
                ki10.sendText(msg.to, wait["rn10"])
#-----------------------------------------------------------speed

            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["pap"])
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#-----------------------------------------------
            elif msg.text.lower() == wait["sq"]+' sayang':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == 'pinky':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                                             
#-----------------------------------------------
            elif msg.text.lower() == 'backup':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == 'sf come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif wait["rn1"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif wait["rn2"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif wait["rn3"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif wait["rn4"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif wait["rn5"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif wait["rn6"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
            elif wait["rn7"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif wait["rn8"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif wait["rn9"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif wait["rn10"]+" in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == wait["sq"]+' bye':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "\nTanks For " + ginfo.creator.displayName + "")
                        ki2.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki3.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki4.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki5.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki6.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki7.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "\nTanks For " + ginfo.creator.displayName + "")
                        ki8.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki9.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki10.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text.lower() == 'pulang':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "\nTanks For " + ginfo.creator.displayName + "")
                        ki.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki3.leaveGroup(msg.to)
                        ki4.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki4.leaveGroup(msg.to)
                        ki5.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki5.leaveGroup(msg.to)
                        ki6.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki6.leaveGroup(msg.to)
                        ki7.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "\nTanks For " + ginfo.creator.displayName + "")
                        ki7.leaveGroup(msg.to)
                        ki8.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki8.leaveGroup(msg.to)
                        ki9.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki9.leaveGroup(msg.to)
                        ki10.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn1"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn2"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn3"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn4"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn5"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn6"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
            elif wait["rn7"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn8"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn9"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["rn10"]+" bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
#-----------------------------------------------
            elif "Papay" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye😘 " + str(ginfo.name) + "\nTanks For " + ginfo.creator.displayName + "")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif wait["sq"]+" key" in msg.text:
                ki.sendText(msg.to,"""      􀜁􀇔􏿿􀜁􀇔􏿿 SATRIA SELF [SF] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Sf1 in]\n􀜁􀇔􏿿[1name:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Sf1 Gift]\n􀜁􀇔􏿿[Sf1 bye]\n\n   
  
        
  
☆ S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃ B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆



""")
                ki2.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿 SATRIA SELF [SF] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Sf2 in]\n􀜁􀇔􏿿[2name:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Sf2 Gift]\n􀜁􀇔􏿿[Sf2 bye]\n\n     
        
  

☆ S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃ B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆


""")
                ki3.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿 SATRIA SELF [SF] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Sf3 in]\n􀜁􀇔􏿿[3name:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Sf3 Gift]\n􀜁􀇔􏿿[Sf3 bye]\n\n     
        
  


☆ S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃ B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆

""")
                ki4.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿 SATRIA SELF [SF] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Sf4 in]\n􀜁􀇔􏿿[4name:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Sf4 Gift]\n􀜁􀇔􏿿[Sf4 bye]\n\n     
        
  

☆ S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃ B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆


""")
                ki5.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿 SATRIA SELF [SF] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Sf5 in]\n􀜁􀇔􏿿[5name:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Sf5 Gift]\n􀜁􀇔􏿿[Sf5 bye]\n\n     
        
  
☆ S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃ B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆



""")
                ki6.sendText(msg.to,"""     􀜁􀇔􏿿􀜁􀇔􏿿 SATRIA SELF [SF] 􀜁􀇔􏿿􀜁􀇔􏿿  \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Sf6 in]\n􀜁􀇔􏿿[6name:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Sf6 Gift]\n􀜁􀇔􏿿[Sf6 bye]\n\n     
        
  
☆ S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃T̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃R̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḭ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ã̷̶̷̰̰̰̰̃̃̃̃̃̃̃ ̶̷̰̰̃̃̃̃S̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃Ḛ̷̶̷̶̷̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃L̷̶̷̶̷̰̰̰̰̰̰̃̃̃̃̃̃̃̃̃̃̃̃F̷̶̷̰̰̰̰̃̃̃̃̃̃̃̃ B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆



""")
#================================================
            elif msg.text.lower() == 'welcome':
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#=======================================

#==============================================================================#
            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═══════List Friend═══════"
                for ids in kontak:
                    msgs+="\n%i• %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Friend═══════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═══════List Member═══════-"
                for ids in group:
                    msgs+="\n%i• %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Member═══════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═══════List FriendMid═══════"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═══════List FriendMid═══════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═══════List Blocked═══════"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═══════List Blocked═══════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═══════List Grup═══════"
                for ids in kontak:
                    msgs+="\n%i• %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═══════List Grup═══════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
            elif "Auto add" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.findAndAddContactsByMids(mi_d)
                cl.sendText(msg.to,"Success Add all")
            elif "Pm cast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Broadcast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Broadcast ", "")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt +"\n\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName))
										 
#========================================
#===============================================
            elif "Sayang say " in msg.text:
				bctxt = msg.text.replace("Sayang say ","")
				ki12.sendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
            elif "Sms: " in msg.text:
                if msg.from_ in admin:
                    cond = msg.text.split(" ")
                    target = int(cond[1])
                    text = msg.text.replace("Mengirim Kepada: " + str(target) + "\nIsi Pesan: ","")
                    try:
                        cl.findAndAddContactsByMid(target)
                        cl.sendText(target,"Ada Pesan Untukmu: \n" + text + "\n\n~Pesan Berakhir~")
                        cl.sendText(msg.to,"Berhasil mengirim pesan")
                    except:
                        cl.sendText(msg.to,"Gagal mengirim pesan, mungkin midnya salah")

            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki7.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki8.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki9.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki10.sendText(msg.to,"Ping 􀜁􀇔􏿿")
#=============================================
            elif "Kepo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#===============================================
            elif wait["SetKey"]+"Sp" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "Progress...\n")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s " % (elapsed_time))
                ki.sendText(msg.to, "%s " % (elapsed_time))
                ki2.sendText(msg.to, "%s " % (elapsed_time))
                ki3.sendText(msg.to, "%s " % (elapsed_time))
                ki4.sendText(msg.to, "%s " % (elapsed_time))
                ki5.sendText(msg.to, "%s " % (elapsed_time))
                ki6.sendText(msg.to, "%s " % (elapsed_time))
                ki7.sendText(msg.to, "%s " % (elapsed_time))
                ki8.sendText(msg.to, "%s " % (elapsed_time))
                ki9.sendText(msg.to, "%s " % (elapsed_time))
                ki10.sendText(msg.to, "%s " % (elapsed_time))
#===============================================
            elif msg.text in ["Tess","Debug speed"]:
                cl.sendText(msg.to, "Waiting procesion...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif msg.text in ["zzz","Bot speed"]:
                cl.sendText(msg.to, "Waiting your processing...")
                start = time.time()
                time.sleep(0.00009)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif "Speed respon" in msg.text:
                cl.sendText(msg.to, "Tunggu...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"				
            elif "Turunin" in msg.text:
                cl.sendText(msg.to, "Sek lurr")
                start = time.time()
                time.sleep(0.02)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu"
#==========================================
            #elif "Tban " in msg.text:
                #cmd = msg.text.replace("Tban ","")
                #if cmd == "on":
                    #if mimic["status"] == False:
                        #mimic["status"] = True
                        #cl.sendText(msg.to,"Reply Message on")
                    #else:
                        #cl.sendText(msg.to,"Sudah on")
                #elif cmd == "off":
                    #if mimic["status"] == True:
                        #mimic["status"] = False
                        #cl.sendText(msg.to,"Reply Message off")
                    #else:
                        #cl.sendText(msg.to,"Sudah off")

            elif ("Tban:on " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        talkban["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Tunban:on " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del talkban["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Tbanlist"]:
                        if talkban["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target Tban user\n"
                            for mi_d in talkban["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Tban target " in msg.text:
                        if talkban["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                talkban["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
#==============================================================================#
            elif wait["SetKey"]+"Tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
#-----------------------------------------------
            elif msg.text in ["Cipok","Colek","Tagall"]:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif wait["rn1"]+" tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki.sendMessage(msg)
            elif wait["rn2"]+" tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki2.sendMessage(msg)
            elif wait["rn3"]+" tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki3.sendMessage(msg)
            elif wait["rn4"]+" tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki4.sendMessage(msg)
            elif wait["rn5"]+" tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki5.sendMessage(msg)
            elif wait["rn6"]+" tag" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki6.sendMessage(msg)

            elif msg.text.lower() == wait["SetKey"]+'lurking':
                cl.sendText(msg.to,"「Lurking help」\n\n●Lurk on/off\n●Lurkers")
            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '>>>Lurkers Detector F150<<<\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
            
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")


            elif msg.text.lower() == wait["SetKey"]+'mimic':
                cl.sendText(msg.to,"「Mimic help」\n\n●Mimic on/off\n●Micadd @\n●Micdel @\n●Miclist")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
#--------------------------------------------------------
#Script Google Image Search
            elif wait["SetKey"]+"Gimage:" in msg.text:
                      googl = msg.text.replace(wait["SetKey"]+"Gimage:","")
                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl
                      raw_html = (download_page(url))
                      items = []
                      items = items + (_images_get_all_items(raw_html))
                      path = random.choice(items)
                      try:
                          start = timeit.timeit()
                          cl.sendImageWithURL(msg.to,random.choice(items))
                      except Exception as e:
                          cl.sendText(msg.to,str(e))
#--------------------------------------------------------
#Script Wikipedia Search
            elif wait["SetKey"]+'wikipedia:' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(wait["SetKey"]+"wikipedia:","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#--------------------------------------------------------
#Script Youtube Search
            elif wait["SetKey"]+"youtube:" in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#--------------------------------------------------------
#Script Instagram
            elif wait["SetKey"]+"Ig info:" in msg.text:
                try:
                    instagram = msg.text.replace(wait["SetKey"]+"Ig info:","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "=====INSTAGRAM INFO USER=====\n"
                    details = "\n=====INSTAGRAM INFO USER====="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif wait["SetKey"]+"Ig pict: " in msg.text:
                try:
                    instagram = msg.text.replace(wait["SetKey"]+"Ig pict: ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))                	
            elif wait["SetKey"]+"Ig link:" in msg.text:
                try:
                    instagram = msg.text.replace(wait["SetKey"]+"Ig link:","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    cl.sendText(msg.to,  link)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))   	
            elif wait["SetKey"]+"Ig pictl:" in msg.text:
                cari = msg.text.replace(wait["SetKey"]+"Ig pictl:","")
                try:
                    respon = requests.get(cari+"?__a=1")
                    data = respon.json()
                    ig_url = data['graphql']['shortcode_media']['display_url']
                    cl.sendImageWithURL(msg.to,ig_url)
                except:
                        cl.sendText(msg.to,"Error")
            elif wait["SetKey"]+"Ig vidl:" in msg.text:
                cari = msg.text.replace(wait["SetKey"]+"Ig vidl:","")
                try:
                    respon = requests.get(cari+"?__a=1")
                    data = respon.json()
                    ig_url = data['graphql']['shortcode_media']['video_url']
                    cl.sendVideoWithURL(msg.to,ig_url)
                except:
                        cl.sendText(msg.to,"Error")
            elif msg.text in ["time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                client.sendText(msg.to, rst)
            elif "Ig bio " in msg.text:
                    try:
                        instagram = msg.text.replace("Ig bio ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Biography : "+bioIG
                        cl.sendImageWithURL(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif wait["SetKey"]+"Ig bio:" in msg.text:
                arg = msg.text.split(" ");
                nk0 = msg.text.replace(wait["SetKey"]+"Ig bio:","")
                nk1 = nk0.rstrip("  ")
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"       「Succes」\n「Fitur」: Instagram Bio  \n「Account Name」: @" + nk0 + "\n「Bio」: " + str(bio))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig aguzz_gangga")
            elif wait["SetKey"]+"3:" in msg.text:
                try:
                    twitter = msg.text.replace(wait["SetKey"]+"3:","")
                    html = requests.get('https://twitter.com/' + twitter)
                    soup = BeautifulSoup(html.text, 'html5lib')
                    name = data[0].get(".ProfileHeaderCard-nameLink").split() #data[0].get('content').split()
                    cl.sendText(msg.to, name)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif wait["SetKey"]+"Tw link:" in msg.text:
                try:
                    twitter = msg.text.replace(wait["SetKey"]+"Tw link:","")
                    html = requests.get('https://www.twitter.com/' + twitter + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    link = "Link: " + "https://www.twitter.com/" + twitter
                    cl.sendText(msg.to,  link)
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))                     
#「Succes」\n「Fitur」: Add Blocklist\n「Account Name」: " + _name
#--------------------------------------------------------
#Script Voice note Google
            elif msg.text.lower() == wait["SetKey"]+'voice':
                cl.sendText(msg.to,"「Voice help」\n\n●Vn-af \n●Vn-sq \n●Vn-ar \n●Vn-hy \n●Vn-bn \n●Vn-ca \n●Vn-zh \n●Vn-zhcn \n●Vn-zhtw \n●Vn-zhyue \n●Vn-hr \n●Vn-cs \n●Vn-da \n●Vn-nl \n●Vn-en \n●Vn-enau \n●Vn-enuk \n●Vn-enus \n●Vn-eo \n●Vn-fi \n●Vn-fr \n●Vn-de \n●Vn-el \n●Vn-hi\n●Vn-hu \n●Vn-is\n●Vn-id \n●Vn-it \n●Vn-jp \n●Vn-km\n●Vn-ko \n●Vn-la \n●Vn-lv \n●Vn-mk \n●Vn-no") 
            elif wait["SetKey"]+"Vn:" in msg.text:
                say = msg.text.replace(wait["SetKey"]+"Vn:","")
                contact = cl.getContact(msg.from_)
                cName = contact.displayName
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                	
            elif "Vn-af " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-af ","")
                 tts = gTTS(psn, lang='af', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-sq " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-sq ","")
                 tts = gTTS(psn, lang='sq', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ar " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-ar ","")
                 tts = gTTS(psn, lang='ar', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hy " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hy ","")
                 tts = gTTS(psn, lang='hy', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-bn " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-bn ","")
                 tts = gTTS(psn, lang='bn', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ca " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-ca ","")
                 tts = gTTS(psn, lang='ca', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zh " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zh ","")
                 tts = gTTS(psn, lang='zh', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhcn " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zhcn ","")
                 tts = gTTS(psn, lang='zh-cn', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhtw " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zhtw ","")
                 tts = gTTS(psn, lang='zh-tw', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-zhyue " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-zhyue ","")
                 tts = gTTS(psn, lang='zh-yue', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hr " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hr ","")
                 tts = gTTS(psn, lang='hr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-cs " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-cs ","")
                 tts = gTTS(psn, lang='cs', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-da " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-da ","")
                 tts = gTTS(psn, lang='da', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-nl " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-nl ","")
                 tts = gTTS(psn, lang='nl', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-en " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-en ","")
                 tts = gTTS(psn, lang='en', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enau " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-enau ","")
                 tts = gTTS(psn, lang='en-au', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enuk " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-enuk ","")
                 tts = gTTS(psn, lang='en-uk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-enus " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-enus ","")
                 tts = gTTS(psn, lang='en-us', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-eo " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-eo ","")
                 tts = gTTS(psn, lang='eo', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-fi " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-fi ","")
                 tts = gTTS(psn, lang='fi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-fr " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-fr ","")
                 tts = gTTS(psn, lang='fr', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-de " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-de ","")
                 tts = gTTS(psn, lang='de', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-el " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-el ","")
                 tts = gTTS(psn, lang='el', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hi " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hi ","")
                 tts = gTTS(psn, lang='hi', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-hu " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-hu ","")
                 tts = gTTS(psn, lang='hu', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-is " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-is ","")
                 tts = gTTS(psn, lang='is', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-id " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-id ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-it " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-it ","")
                 tts = gTTS(psn, lang='it', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-jp " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-jp ","")
                 tts = gTTS(psn, lang='ja', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-km " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-km ","")
                 tts = gTTS(psn, lang='km', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-ko " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-ko ","")
                 tts = gTTS(psn, lang='ko', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-la " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-la ","")
                 tts = gTTS(psn, lang='la', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-lv " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-lv ","")
                 tts = gTTS(psn, lang='lv', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-mk " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-mk ","")
                 tts = gTTS(psn, lang='mk', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "Vn-no " in msg.text:
              if msg.from_ in admin:
                 psn = msg.text.replace("Vn-no ","")
                 tts = gTTS(psn, lang='no', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
#--------------------------------------------------------
#Script Play & Download Music Google = JOOX
            elif wait["SetKey"]+"Musik:" in msg.text:
                try:
                    songname = msg.text.replace(wait["SetKey"]+"Musik:","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
#--------------------------------------------------------
#Script Lyric Music Google = JOOX
            elif wait["SetKey"]+"Lirik:" in msg.text:
                try:
                    songname = msg.text.replace(wait["SetKey"]+"Lirik:","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#--------------------------------------------------------
#Script Search Google
            elif wait["SetKey"]+"Google:" in msg.text:
                    a = msg.text.replace(wait["SetKey"]+"Google:","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "https://www.google.co.jp/search?q=" + b)
            elif wait["SetKey"]+"Test:" in msg.text:
                    a = msg.text.replace(wait["SetKey"]+"Test:","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "https://www.google.com/search?q=" + b)                    
#--------------------------------------------------------
#Search,Add and Steal By Id and Mid
            elif wait["SetKey"]+"Searchid:" in msg.text:
                msgg = msg.text.replace(wait["SetKey"]+'Searchid: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)   
            elif wait["SetKey"]+"AddId:" in msg.text:
                msgg = msg.text.replace(wait["SetKey"]+'AddId: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.findAndAddContactsByUserid(msgg) 
                    cl.sendMessage(msg)                       
                    findAndAddContactsByUserid
            elif wait["SetKey"]+"Searchmid:" in msg.text:
                key = msg.text[-33:]
                msg.contentType = 13
                msg.contentMetadata = {'mid': key}
                contact = cl.getContact(key)
                cl.sendMessage(msg)
            elif wait["SetKey"]+"AddMid:" in msg.text:
                msgg = msg.text.replace(wait["SetKey"]+'AddMid: ','')
                key = msg.text[-33:]
                msg.contentType = 13
                msg.contentMetadata = {'mid': key}
                contact = cl.getContact(key)
                cl.findAndAddContactsByMid(msgg)
                cl.sendMessage(msg)                         
            elif wait["SetKey"]+"Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace(wait["SetKey"]+"Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass                
            elif wait["SetKey"]+"Midcover:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+"Midcover:","")
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif wait["SetKey"]+"Mid @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass                         
            elif wait["SetKey"]+"Midbio:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+"Midbio:","")
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                try:
                    cl.sendText(msg.to,"Bio :\n" + contact.statusMessage)
                except:
                    pass  
            elif wait["SetKey"]+"Midname:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+"Midname:","")
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                try:
                    cl.sendText(msg.to,"Bio :\n" + contact.displayName)
                except:
                    pass                  
            elif "About" in msg.text: 
                if msg.from_ in admin:
                	cl.sendText(msg.to,"「Aʙᴏᴜᴛ Bᴏᴛ」\nSf Sᴇʟғʙᴏᴛ Eᴅɪᴛɪᴏɴ♪\nTɪᴍᴇ: " + datetime.today().strftime('%H:%M:%S') + " \n\n「Bᴏᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ」\n╠═════════════════════\n  ❂͜͡➣ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ ɪɴ: 01-12-2017\n  ❂͜͡➣ Bᴏᴛ Uᴘʟɪɴᴋ ʙʏ: SaTtria \n「 ▶ line://ti/p/~satria_hk」\n  ☸ Bᴏᴛ Usᴇʀɴᴀᴍᴇ:"+ wait["sq"]+"\nKey:"+wait["SetKey"]+"  ☸ Exᴘɪʀᴇᴅ ᴅᴀᴛᴇ: 01-05-2019\n  ☸ Iɴ ᴅᴀʏs: 300+ ᴅᴀʏs\n╠═════════════════════\n「Cᴏɴᴛᴀᴄᴛ Pᴇʀsᴏɴᴀʟ」\n「 ▶ ID LINE: line://ti/p/~satria_hk」\n\n ʀᴇᴠᴏʟᴜᴛɪᴏɴ ℬᴏᴛ")

#--------------------------------------------------------
#Set Key Info
            elif msg.text in [wait["SetKey"]+"Help",wait["SetKey"]+"help"]:
                if wait["SetKey"]: md = "╔═══════════════════\n║ Gunakan Kata Awalan「%s」 \n║Untuk Menggunakan Fitur Bot\n" % (wait["SetKey"])
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Gimage:[Judul]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Gimage:[Judul]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Wikipedia:[Judul]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Wikipedia:[Judul]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Youtube:[Judul]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Youtube:[Judul]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig info:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig info:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Musik:[Song Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Musik:[Song Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Lirik:[Song Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Lirik:[Song Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Google:[Text]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Google:[Text]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig check:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig check:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig bio:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig bio:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig pict:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig pict:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig pictl:[Link]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig pictl:[Link]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig vidl:[Link]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig vidl:[Link]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ig link:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ig link:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Vn:[Text]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Vn:[Text]\n" % (wait["SetKey"])
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Searchid:[Id]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Searchid:[Id]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Searchmid:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Searchmid:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 AddId:[Id]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ AddId:[Id]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 AddMid:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ AddMid:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Checkmid:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Checkmid:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Midcover:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Midcover:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Midpict:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Midpict:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Midbio:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Midbio:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Midname:[Mid]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Midname:[Mid]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getinfo[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getinfo[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getbio[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getbio[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getmid[@tag]\n" % (wait["SetKey"])
                else: md+=""╠❂͜͡➣ Getmid[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getcontact[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getcontact[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getpict[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getpict[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getcover[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getcover[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getpicturl[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getpicturl[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Getcoverurl[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Getcoverurl[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Myname:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Myname:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Mybio:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Mybio:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Myname\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Myname\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Mybio\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Mybio\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Mypict\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Mypict\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Mycover\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Mycover\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Mypicturl\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Mypicturl\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Mycoverurl\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Mycoverurl\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Friendlist\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Friendlist\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Glist/Glist2\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Glist/Glist2\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Copy[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Copy[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Copy name[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Copy name[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Copy bio[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Copy bio[@tag]\n"
                if wait["Key"] True: md+="╠❂͜͡➣「%s」 Copy pict[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Copy pict[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Copy cover[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Copy cover[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Gn:[Name]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Gn:[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ourl/Curl\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ourl/Curl\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Gpict\n" % (wait["SetKey"])   
                else: md+="╠❂͜͡➣ Gpict\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Gpicturl\n" % (wait["SetKey"])   
                else: md+="╠❂͜͡➣ Gpicturl\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Gpict[Name]\n" % (wait["SetKey"])   
                else: md+="╠❂͜͡➣ Gpict[Name]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Tagall\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Tagall\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Lurks on/off\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Lurks on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Lurkers\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Lurkers\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Spam?\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Spam?\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Set spam:[Text]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Set spam:[Text]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Spam:10-50[@tag]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Spam:10-50[@tag]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Spam [on/off] [jmlh] [text]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Spam [on/off] [jmlh] [text]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Set pap:[Link]\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Set pap:[Link]\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Pap\n" % (wait["SetKey"])  
                else: md+="╠❂͜͡➣ Pap\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Ifconfig\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Ifconfig\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 System\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ System\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Kernel\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Kernel\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Cpu\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Cpu\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Translate\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Translate\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 voice\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ voice\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 mimic\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ mimic\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Gift\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Gift\n"
                if wait["Key"] == True: md+="╠❂͜͡➣「%s」 Backup\n" % (wait["SetKey"])
                else: md+="╠❂͜͡➣ Backup\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Wc on/off\n"
                else: md+="╠❂͜͡➣ Wc on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Update welcome:\n"
                else: md+="╠❂͜͡➣ Update welcome\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Check welcome\n"
                else: md+="╠❂͜͡➣ Check welcome\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Protecton/off\n"
                else: md+="╠❂͜͡➣ Protect on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Qr on/off\n"
                else: md+="╠❂͜͡➣ Qr on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Blockinvite on/off\n"
                else: md+="╠❂͜͡➣ Blockinvite on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Namelock on/off\n"
                else: md+="╠❂͜͡➣ Namelock on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Steal on/off\n"
                else: md+="╠❂͜͡➣ Steal on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Notag on/off\n"
                else: md+="╠❂͜͡➣ notag on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Respon: on/off\n"
                else: md+="╠❂͜͡➣ Respon: on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Chatbot on/off\n"
                else: md+="╠❂͜͡➣ Chatbot on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Autorein: on/off\n"
                else: md+="╠❂͜͡➣ Autorein: on/off\n"
                if wait["Key"] == True: md+="╠❂͜͡➣ Backup on/off\n"
                else: md+="╠❂͜͡➣ Backup on/off\n"
                cl.sendText(msg.to,md + "╚═══════════════════")
                
            elif msg.text in ["Help"]:
                cl.sendText(msg.to," ❂SELFBOT V.1❂\n\nUser Prefix「" + str(wait["SetKey"]) +"」  to use the Bot(s)\nPrefix is Case sensitive but the\ncommands is not\n\n❂͜͡➣" + str(wait["SetKey"]) + "Help1 [MENU PENGHIBUR]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Help2 [MENU ID & MID]" + "\n❂͜͡➣" + str(wait["SetKey"]) +  "Help3 [MENU GET AKUN]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Help4 [MENU PROFILE]" +  "\n❂͜͡➣" + str(wait["SetKey"]) +  "Help5 [Menu Grup]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Help6 [Menu Contact]" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Set" + "\n❂͜͡➣" + str(wait["SetKey"]) + "Status")
            elif msg.text in ["Key?"]:
                cl.sendText(msg.to,"My Set Keyword: 「" + str(wait["SetKey"]) + "」")
            elif "SetKey:" in msg.text:
                wait["SetKey"] = msg.text.replace("SetKey:","")
                cl.sendText(msg.to,"Set Key changed")                
#--------------------------------------------------------
#Script Get
            elif wait["SetKey"]+"Getcoverurl" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Cover link」\n" + str(cu))
                except:
                    cl.sendText(msg.to,"\n[homePicture]\n" + str(cu))
            elif wait["SetKey"]+"Getpicturl" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Picture link」\nhttps://obs.line-scdn.net/" + contact.pictureStatus)
                except:
                    cl.sendText(msg.to,"[profilePicture]\nhttps://obs.line-scdn.net/" + contact.pictureStatus)                   
            elif wait["SetKey"]+"Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttps://obs.line-scdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
            elif wait["SetKey"]+"Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif wait["SetKey"]+"Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Name:\n[" + contact.displayName  + "]")
                except:
                    cl.sendText(msg.to,"Name:\n[" + contact.displayName  + "]")
            elif wait["SetKey"]+"Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Bio」\n\n「" + contact.statusMessage + "」")
                except:
                    cl.sendText(msg.to,"「Bio」\n\n「" + contact.statusMessage + "」")        
            elif wait["SetKey"]+"Getmid" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"「Mid」\n\n「" + contact.mid + "」")
                except:
                    cl.sendText(msg.to,"「Mid」\n\n「" + contact.mid + "」")                  
            elif wait["SetKey"]+"Getcover @" in msg.text:
                 print "[Command]dp executing"
                 _name = msg.text.replace(wait["SetKey"]+"Getcover @","")
                 _nametarget = _name.rstrip(' ')
                 gs = cl.getGroup(msg.to)
                 targets = []
                 for g in gs.members:
                     if _nametarget == g.displayName:
                         targets.append(g.mid)
                 if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                 else:
                     for target in targets:
                         try:
                             contact = cl.getContact(target)
                             cu = cl.channel.getCover(target)
                             path = str(cu)
                             cl.sendText(msg.to,"Loading Cover... || " +  _name )
                             cl.sendImageWithURL(msg.to, path)
                         except:
                             pass
                 print "[Command]dp executed"    
            elif wait["SetKey"]+"Getpict @" in msg.text:
                 print "[Command]dp executing"
                 _name = msg.text.replace(wait["SetKey"]+"Getpict @","")
                 _nametarget = _name.rstrip(' ')
                 gs = cl.getGroup(msg.to)
                 targets = []
                 for g in gs.members:
                     if _nametarget == g.displayName:
                         targets.append(g.mid)
                 if targets == []:
                     cl.sendText(msg.to,"Contact not found")
                 else:
                     for target in targets:
                         try:
                             contact = cl.getContact(target)
                             path = "https://obs.line-scdn.net/" + contact.pictureStatus
                             cl.sendText(msg.to,"Loading Pict... || " +  _name )
                             cl.sendImageWithURL(msg.to, path)
                         except:
                             pass
                 print "[Command]dp executed"                 
            elif wait["SetKey"]+"Set pap:" in msg.text:
                wait["Pap"] = msg.text.replace(wait["SetKey"]+"Set pap:","")
                cl.sendText(msg.to,"Pap Has Ben Set To")
            elif msg.text in [wait["SetKey"]+".Pap",wait["SetKey"]+"Pap"]:
                cl.sendImageWithURL(msg.to,wait["Pap"])
#--------------------------------------------------------
            elif wait["SetKey"]+"Gpict" in msg.text:
                group = cl.getGroup(msg.to)
                path ="https://obs.line-scdn.net/" + group.pictureStatus
                cl.sendText(msg.to,"Loading....")
                cl.sendImageWithURL(msg.to, path)
            elif wait["SetKey"]+"Gpicturl" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif wait["SetKey"]+"Gpict:" in msg.text:
                saya = msg.text.replace(wait["SetKey"]+'Gpict:','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            elif wait["SetKey"]+"Setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Checkpoint checked!")
                print "@setview"
            elif wait["SetKey"]+"Viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------------------------------------
#Script Spam
            elif wait["SetKey"]+"Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace(wait["SetKey"]+"Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
            elif wait["SetKey"]+"Spam @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"          
            elif wait["SetKey"]+"Spam:10 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:10 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"    
            elif wait["SetKey"]+"Spam:15 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:15 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"    
            elif wait["SetKey"]+"Spam:20 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:20 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"                           
            elif wait["SetKey"]+"Spam:25 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:25 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"                           
            elif wait["SetKey"]+"Spam:30 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:30 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"  
            elif wait["SetKey"]+"Spam:35 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:35 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"                              
            elif wait["SetKey"]+"Spam:40 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:40 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"Start Spam")
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"       
            elif wait["SetKey"]+"Spam:50 @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spam:50 @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))
                       cl.sendText(g.mid,(wait["spam"]))

                       cl.sendText(msg.to, "Spam Succes")
                       print "Done spam"       
            elif msg.text in [wait["SetKey"]+"Spam?"]:
                cl.sendText(msg.to,"Spam saat ini telah ditetapkan sebagai berikut:\n\n" + str(wait["spam"]))
            elif wait["SetKey"]+"Set spam:" in msg.text:
                wait["spam"] = msg.text.replace(wait["SetKey"]+"Set spam:","")
                cl.sendText(msg.to,"spam changed")
            elif wait["SetKey"]+"Spam add:" in msg.text:
                wait["spam"] = msg.text.replace(wait["SetKey"]+"Spam add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
            elif wait["SetKey"]+"Spam:" in msg.text:
                strnum = msg.text.replace(wait["SetKey"]+"Spam:","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
            elif wait["SetKey"]+"Spamtag @" in msg.text:
                _name = msg.text.replace(wait["SetKey"]+"Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass                    
#--------------------------------------------------------
#Script Copy Profile
            elif wait["SetKey"]+"Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Contact profile")
                                except Exception as e:
                                    print e
            elif wait["SetKey"]+"Copy pict @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy pict @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.clonePictureProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Picture profile")
                                except Exception as e:
                                    print e                                    
            elif wait["SetKey"]+"Copy cover @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy cover @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneCoverProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Cover profile")
                                except Exception as e:
                                    print e                                
            elif wait["SetKey"]+"Copy name @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy name @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneNameProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Name profile")
                                except Exception as e:
                                    print e  
            elif wait["SetKey"]+"Copy bio @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace(wait["SetKey"]+"Copy bio @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneStatusProfile(target)
                                    cl.sendText(msg.to, "Succes Copy Bio profile")
                                except Exception as e:
                                    print e                                           
            elif msg.text in [wait["SetKey"]+"Backup"]:
                try:
                    cl.updateDisplayPicture(kembali.pictureStatus)
                    cl.updateProfile(kembali)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
#--------------------------------------------------------
#
#--------------------------------------------------------
#============Mimic Start=========#
            elif (wait["SetKey"]+"Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif (wait["SetKey"]+"Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in [wait["SetKey"]+"Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif wait["SetKey"]+"Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace(wait["SetKey"]+"Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif wait["SetKey"]+"Mimic " in msg.text:
                cmd = msg.text.replace(wait["SetKey"]+"Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
#--------------------------------------------------------
#
#--------------------------------------------------------
#Block
            elif wait["SetKey"]+"Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace(wait["SetKey"]+"Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Succes")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                   except:
                                       cl.sentText(msg.to,"Succes")

	    elif wait["SetKey"]+"Scbl:on" in msg.text:
	        wait["wblacklist"] = True
	    	cl.sendText(msg.to,"Block Send contact Active")

	    elif wait["SetKey"]+"Scubl:on" in msg.text:
	    	wait["dblacklist"] = True
	    	cl.sendText(msg.to,"Unblock Send contact Active")
            elif wait["SetKey"]+"Bl @" in msg.text:
                if msg.toType == 2:
                    print "@Block by mention"
                    _name = msg.text.replace(wait["SetKey"]+"Bl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"    「Succes」\n「Fitur」: Add Blocklist\n「Account Name」: " + _name)
                                except:
                                    cl.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Admin Detected~")
#--------------------------------------------------------
            elif msg.text in [wait["SetKey"]+"Blist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"===[Blocklist User]===\n"+mc)

#--------------------------------------------------------
            elif wait["SetKey"]+"Ubl @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                    _name = msg.text.replace(wait["SetKey"]+"Ubl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"    「Succes」\n「FITUR」: Unblocklist\n「Account Name」: " + _name)
                            except:
                                cl.sendText(msg.to,"    「Succes」\n「FITUR」: Unblocklist\n「Account Name」: " + _name)
#--------------------------------------------------------
#Script Speed
            elif msg.text in ["Speed","Sp","speed","Debug speed"]:
                start = time.time()
                cl.sendText(msg.to, "「 Debug Speed」\nSpeed is STARTING♪")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「 Debug Speed」\nSpeed is STARTING♪\n%sseconds􏿿" % (elapsed_time))
#--------------------------------------------------------
#Script Kick
            elif "Uk " in msg.text:
                  if msg.from_ in admin:
                       ulti0 = msg.text.replace("Uk ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
	    elif "Vk " in msg.text:
		if 'MENTION' in msg.contentMetadata.keys()!= None:
		    names = re.findall(r'@(\w+)', msg.text)
		    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		    mentionees = mention['MENTIONEES']
		    print mentionees
		    for mention in mentionees:
			cl.kickoutFromGroup(msg.to,[mention['M']])
#--------------------------------------------------------
#Script Tagall
            elif msg.text.lower() in ["aa"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                    cnt = Message()
                    cnt.text = "Done : " + str(jml) +  " Members"
                    cnt.to = msg.to
                    cl.sendMessage(cnt)     
#--------------------------------------------------------
#Script System
            elif msg.text.lower() ==  wait["SetKey"]+'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() ==  wait["SetKey"]+'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() ==  wait["SetKey"]+'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() ==  wait["SetKey"]+'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#--------------------------------------------------------
#
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': wait["creator"]}
                cl.sendMessage(msg)
            elif wait["SetKey"]+"Set ct:" in msg.text:
                wait["creator"] = msg.text.replace(wait["SetKey"]+"Set ct:","")
                cl.sendText(msg.to,"Creator Has Ben Set To")
            elif msg.text in [wait["SetKey"]+"Ct",wait["SetKey"]+"ct"]:
                cl.sendImageWithURL(msg.to,wait[""])
#===============================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#------------------------------------------------------------------------------------
        #if op.type == 26:
            #msg=op.message
            #if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	#text = msg.text
            	#if text is not None:
            		#cl.sendText(msg.to,text)
            	#else:
            		#if msg.contentType == 7:
            			#msg.contentType = 7
            			#msg.text = None
            			#msg.contentMetadata = {
            							 	 #"STKID": "6",
            							 	 #"STKPKGID": "1",
            							 	 #"STKVER": "100" }
            			#cl.sendMessage(msg)
            		#elif msg.contentType == 13:
            			#msg.contentType = 13
            			#msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			#cl.sendMessage(msg)
#===========================================
#===========================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#==============================================================================#

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            

        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like"


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)