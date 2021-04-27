import threading
import requests
import time
from pushbullet import Pushbullet
from tkinter import *
from tkinter.ttk import Combobox
import hashlib
import os.path
import webbrowser
import tkinter
import ctypes, sys


active = 0
b = 0
if os.path.exists(r"C:\config.txt"):
    global key
    try:
    
        file = open(r"C:\config.txt","r")
        data = file.readlines()
        b = 1
        key = data[0][:-1]
        PUBkey = data[1]
        file.close()
    
    except IndexError:
        print("Нет одного/нескольких Api-ключей")

window = Tk()
window.title("'Лучший' бот по трейдингу на csgomarket")
window.resizable(False, False)

def openBrowserMarkt(event):
    webbrowser.open_new(r"https://market.csgo.com/docs-v2")
def openBrowserBullet(event):
    webbrowser.open_new(r"https://www.pushbullet.com/#settings/account")
    

def addoning():
    def savekeys():
        global key
        global PUBkey
        try:
            file = open(r"C:\config.txt","w")
            Mapi = Markt.get().replace(" ","")
            Papi = Bullet.get()

            file.write(Mapi)
            file.write("\n")
            file.write(Papi)
            file.close()
            
        except PermissionError:
            print("Недостаточно прав, запустите от имени администратора")
            quit()


        
    addon = Toplevel()
    addon.title("Дополнительные возможности")
    addon.overrideredirect(False)
    addon.resizable(False, False)
    addon.transient(window)
    
    Markt = Entry(addon, width=5)
    Bullet = Entry(addon, width=5)

    
    Bullet.insert(0,PUBkey)
    Markt.insert(0, key)
    
    labA = Label(addon, text = "MarketApi:",bg="black",fg="red")
    labB = Label(addon, text = "PushAPI:",bg="black",fg="red")
    butA = Button(addon, text ="Update",command=savekeys)

    labA.grid(column=0,row=1)       #### Обновление Api - ключей
    Markt.grid(column=1,row=1)
    labB.grid(column=2,row=1)
    Bullet.grid(column=3,row=1)
    butA.grid(column=4,row=1)

    link1 = Label(addon, text="Market api url",fg="blue",bg="yellow", cursor="hand2")
    link1.bind("<Button-1>",openBrowserMarkt)
    link1.grid(column=0,row=2)

    link2 = Label(addon, text="PushBullet api url",fg="blue",bg="yellow", cursor="hand2")
    link2.bind("<Button-1>",openBrowserBullet)
    link2.grid(column=2,row=2,)
    
    Label(addon, text = "      ").grid(column=1,row=2)

    labAddon = Label(addon, text = "notification:",bg="black",fg="red")
    but8= Button(addon, text = "check", command = notification)
    but8.grid(column=1,row=0)
    labAddon.grid(column=0,row=0)

        
combo = Combobox(window)
combo2 = Combobox(window)
combo3 = Combobox(window)
combo4 = Combobox(window)

name = "s"
        
####################################################################################################################################
def start():
    global lab6
    try:
        ping = requests.get('https://market.csgo.com/api/v2/ping?key='+key).json()
        lab6= Label(window,text=str(ping["success"]), bg="gray",fg="purple")
    
        combo3["values"] = "Тут будут цены",
        combo3.current(0)
    
        combo2["values"] = "Нажмите Check",
        combo2.current(0)

        combo["values"] = "Выберите оружие",
        combo.current(0)
        combo['values'] = ("AK-47 | ","AUG | ","AWP | ","Bayonet | ","Bowie Knife | ","Butterfly Knife | ", "Classic Knife | ", "CZ75-Auto | ","Desert Eagle | ","Dual Berettas | ",
        "Falchion Knife | ","FAMAS | ","Five-SeveN | ","Flip Knife | ","G3SG1 | ","Galil AR | ","Glock-18 | ","Gut Knife | ", "Huntsman Knife | ","Karambit | ","M249 | ", "M4A1-S | ",
        "M4A4 | ","M9 Bayonet | ", "MAC-10 | ","MAG-7 | ","MP5-SD | ","MP7 | ", "MP9 | ", "Navaja Knife | ","Negev | ", "Nomad Knife | ","Nova | ","P2000 | ","P250 | ", "P90 | ", "Paracord Knife | ",
        "PP-Bizon | ","R8 Revolver | ","Sawed-Off | ","SCAR-20 | ", "SG 553 | ", "Shadow Daggers | ","Skeleton Knife | ", "SSG 08 | ","Stiletto Knife | ","Survival Knife | ","Talon Knife | ","Tec-9 | ",
        "UMP-45 | ","Ursus Knife | ", "USP-S | ", "XM1014 | ")
    except:
        start()

t3 = threading.Thread(target = start)

t3.start()
t3.do_run = False

############################### Comraring prices #################################################################

def price_f6(names):
    
    valG = [".",]
    value = []
    urlsteam = 'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name='+names
    url = 'https://market.csgo.com/api/v2/search-item-by-hash-name-specific?key='+key+'&hash_name='+names
    
    try:
        
        gun = requests.get(url+' (Factory New)' ).json()
        gunsteam = requests.get(urlsteam+' (Factory New)' ).json()

        pricesteam = gunsteam
        print(pricesteam["median_price"])
        price = gun["data"]
    
        value = "Прямо с завода ",
        valG = valG + list(value)
        value = "."
        valG = valG + list(value)
        for i in range(4):
        
            value = str(price[i]["price"]/100),  
            valG = valG + list(value)
            combo3["values"]= valG
        combo3.current(0)
    except IndexError:
        
        value = "Нет предмета",
        valG = valG + list(value)
        combo3["values"]= valG
    

        
    try:
        
        time.sleep(0.35)
        gun = requests.get(url+' (Minimal Wear)' ).json()
        price = gun["data"]
    
        value = "Немного поношенное ",
        valG = valG + list(value)
        value = "."
        valG = valG + list(value)
    
        for i in range(4):
        
            value = str(price[i]["price"]/100),
            valG = valG + list(value)
            combo3["values"]= valG
    except IndexError:
        
        value = "Нет предмета",
        valG = valG + list(value)
        combo3["values"]= valG


    try:    
        time.sleep(0.35)
        gun = requests.get(url+' (Well-Worn)' ).json()
        price = gun["data"]
    
        value = "Поношенное ",
        valG = valG + list(value)
        value = "."
        valG = valG + list(value)
    
        for i in range(4):
        
            value = str(price[i]["price"]/100), 
            valG = valG + list(value)
            combo3["values"]= valG
            
    except IndexError:
        
        value = "Нет предмета",
        valG = valG + list(value)
        combo3["values"]= valG
        
        
    try:
        
        time.sleep(0.35)
        gun = requests.get(url+' (Field-Tested)' ).json()
        price = gun["data"]
    
        value = "После полевых испытаний ",
        valG = valG + list(value)
        value = "."
        valG = valG + list(value)
    
        for i in range(4):
        
            value = str(price[i]["price"]/100), 
            valG = valG + list(value)
            combo3["values"]= valG
            
    except IndexError:
        
        value = "Нет предмета",
        valG = valG + list(value)
        combo3["values"]= valG
        
        
    try:
        
        time.sleep(0.35)
        gun = requests.get(url+' (Battle-Scarred)' ).json()
        price = gun["data"]
    
        value = "Закалённое в боях ",
        valG = valG + list(value)
        value = "."
        valG = valG + list(value)
    
        for i in range(4):
        
            value = str(price[i]["price"]/100), 
            valG = valG + list(value)
            combo3["values"]= valG
            
            
    except IndexError:
        
        value = "Нет предмета",
        valG = valG + list(value)
        combo3["values"]= valG

        
### Geting information about trade that you need send
def GetTradeInfo():
    url = "https://market.csgo.com/api/v2/trade-request-give-p2p-all?key="+key
    request = requests.get(url).json()

### Geting information about trade that you need take
def TakeTradeInfo():
    url = "https://market.csgo.com/api/v2/trade-request-take?key="+key
    request = requests.get(url).json()


    
                                                               
### Request of buying item                                                           
def TakeItems():
    url = "https://market.csgo.com/api/v2/trade-request-take?key="+key
    request = requests.get(url).json()
    

####### Check balance

def balance():
    global lab11
    try:
        lab11= Label(window,bg="gray",fg="purple",width = 5)
        lab11.grid(column=3,row=1)
        urlmoney = 'https://market.csgo.com/api/v2/get-money?key='+key
        request = requests.get(urlmoney).json()
        print("Баланс: " + str(request["money"]))
        lab5= Label(window, text = "balance: ",bg = "black",fg="red")
        lab11.config(text = str(request["money"]))
    
        lab5.grid(column=2,row=1)
    except Exception:
        lab11.config(text = "False")
        



######## using by "selling" (sends notification to Pushbullet)

def notification():
    pb = Pushbullet(PUBkey)
    push = pb.push_note("S","Accept")
    print("уведомление создано")
    print(push)
    
######## using by "selling_mode" (Checks if trade avaible)

def selling():
    
    urlTrade ="https://market.csgo.com/api/ItemRequest/out/1/?key="+key
    while active == 1:
            
        try:
                           
            acceptGive = requests.get(urlTrade).json()
            print("Оффер готов: ",acceptGive["success"])
            
            if acceptGive["success"] == True:
                notification()
                time.sleep(6)
                GetTradeInfo()
            else: 
                time.sleep(6)
        except Exception:
                    
            print("Ошибка #1")
            continue
    
        
######## turn on sales

def pinging():
    urlping ="https://market.csgo.com/api/v2/ping?key="+key
    
    while active == 1:
        try:
            ping = requests.get(urlping).json()["success"]
            print("Продажи включены: ", ping)


            
            lab6.config(text=str(ping))
            time.sleep(6)
            
        except:
            print("Ошибка #2")
            continue
            # Ошибка в отправке запроса на включение трейда
    
######## Saling mode

def selling_mode():
    t2 = threading.Thread(target=selling)
    t1 = threading.Thread(target=pinging)
    
    t2.start()
    t1.start()

    t2.join()
    t1.join()
    
####### Refresh inventory

def checkInv():
    global values
    global combo2
    val = [".",]
    valid = []
    url = "https://market.csgo.com/api/v2/update-inventory/?key="+key
    urlinv = 'https://market.csgo.com/api/v2/my-inventory/?key='+key
    
    updated = requests.get(url).json()
    inventory = requests.get(urlinv).json()
    inv = str(inventory['items'])
       
    print("инвентарь обновился: ", updated)

    for i in inventory['items']:
        values = i['market_hash_name'],
        valuesID=i["id"],
        valid = list(valuesID)
        
        val = val + list(values) + valid + list(".")
        combo2["values"]= val
    combo2.current(0)

###### using by "checkInv"

def sellgun():
    currency = "RUB"
    ids = str(combo2.get())
    price = str(ent1.get())
    price = str(int(price) * 100)
    urls = "https://market.csgo.com/api/v2/add-to-sale?key="+key+"&id="+ids+"&price="+price+"&cur="+currency
    sell = requests.get(urls).json()
    
    lab9= Label(window, text = "Success: "+str(sell["success"]),bg="gray",fg="purple")
    lab9.grid(column=7,row=2)

def clicked():
    name = combo.get()
    name = str(name)
    price_f6(name)

def acton():
    print("Продажи включены!!!")
    global active
    active = 1
    lab6.grid(column=3,row=3)

    selling_mode()
    
    

def actOff():
    global active
    print("Продажи выключены!!!")
    lab6.config(text="offline")
    active = 0

def closing():
    quit()  
     

but1= Button(window, text = "Узнать цену по предмету", command=clicked)
but2= Button(window, text = "Press", command =balance)
but3= Button(window, text = "Check", command =checkInv)
but4= Button(window, text = "sell", command = sellgun)
but5= Button(window, text = "On", command = acton)
but6= Button(window, text = "Off", command= actOff)
but7= Button(window, text = "EXIT", command = closing)
#but8= Button(addon, text = "check notification", command = notification)
but9= Button(window, text = "Расширенные возможности", command = addoning)


lab1= Label(window, text = "                 Узнать баланс                    ", bg="black", fg="red")
lab2= Label(window, text = " Посмотреть инвентарь и продать ", bg="black", fg="red")
lab3= Label(window, text = "               Продажи на сайте               ", bg="black",fg="red")
lab4= Label(window, text = "_________________________________________",fg="red")
lab5= Label(window, text = "balance: ",bg = "black",fg="red")
#lab6.grid(column=3,row=3)
lab7= Label(window, text = "id: ",bg="black", fg="red")
lab8= Label(window, text = "price: ",bg="black", fg="red")
#lab9= Label(window, text = "Success: "+sell[success],bg="black",fg="red")
labX= Label(window, text = "Guns: ",bg="black",fg="red")
lab44= Label(window, text = "_________________________________________",fg="red")

ent1= Entry(window, width=5)

but1.grid(column=1, row=0)      #### 1 строка
combo.grid(column=0, row=0)
combo3.grid(column=3,row=0)
combo4.grid(column=4,row=0)
labX.grid(column=2,row=0)

but2.grid(column=1,row=1)       #### 2 строка
lab1.grid(column=0,row=1)
lab5.grid(column=2,row=1)

but3.grid(column=1,row=2)       #### 3 строка
but4.grid(column=6,row=2)  
lab2.grid(column=0,row=2)
lab7.grid(column=2,row=2)
lab8.grid(column=4,row=2)
combo2.grid(column=3,row=2)
ent1.grid(column=5,row=2)
#lab9.grid(column=7,row=2)



lab3.grid(column=0,row=3)       #### 4 строка
but5.grid(column=1,row=3)
but6.grid(column=2,row=3)
#lab6.grid(column=3,row=3)#### находится в 228 строке файла

lab44.grid(column=0,row=4)      #### 5 строка

but9.grid(column=0,row=5)       #### 6 строка

lab4.grid(column=0,row=6)       #### 7 строка

but7.grid(column=0,row=7)       #### 8 строка

######## Доп. Возможности

### Переписать Api ключи

### Проверить Уведомления

#but8= Button(addon, text = "check notification", command = notification)
#but8.grid(column=0,row=0)

window.mainloop()
