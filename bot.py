import threading
import requests
import json
import time
from pushbullet import Pushbullet

PUBkey = "o.XA4cCFrk1CkRgY4HFk4oUffqLWFUql0C"
key = "9zwz7eDBiv67Bg0JdcsBoK4Zxw0rGgK"

###############################Поиск всех цен по названию предмета#################################################################

def price_f6():
    global name
    name = input("Введите название предмета из стима: " )
    url = 'https://market.csgo.com/api/v2/search-item-by-hash-name-specific?key='+key+'&hash_name='+name 
    gun = requests.get(url+' (Factory New)' ).json()
    price = gun["data"]
    
    try:
        print(".")
        print("               Цена предмета (Прямо с завода)")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
    except IndexError:
        print("нет предмета")
    time.sleep(0.66)

    gun = requests.get(url+' (Minimal Wear)').json()
    price = gun["data"]

    try:
        print(".")
        print("               Цена предмета (Немного поношенное)")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
        print(".")
    except IndexError:
        print("нет предмета")
    time.sleep(0.66)
    

    gun = requests.get(url+" (Well-Worn)").json()
    price = gun["data"]

    try:
        print("               Цена предмета (Поношенное)")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
        print(".")
    except IndexError:
        print("нет предмета")
    time.sleep(0.66)

    gun = requests.get(url+" (Field-Tested)").json()
    price = gun["data"]

    try:
        print("               Цена предмета (После Полевых Испытаний)")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
        print(".")
    except IndexError:
        print("нет предмета")
    time.sleep(0.66)

    gun = requests.get(url+" (Battle-Scarred)").json()
    price = gun["data"]
    
    try:
        print("               Цена предмета (Закалённое в боях)")
        print(".")
        print("Цена первого лота: ",  str(price[0]["price"])  .replace(' ', '')[:-2])
        print("Цена второго лота: ",  str(price[1]["price"])  .replace(' ', '')[:-2])
        print("Цена третьего лота: ",  str(price[2]["price"])  .replace(' ', '')[:-2])
        print("Цена четвертого лота: ",  str(price[3]["price"])  .replace(' ', '')[:-2])
    except IndexError:
        print("нет предмета")
    time.sleep(0.66)

def balance():
    urlmoney = 'https://market.csgo.com/api/v2/get-money?key='+key
    request = requests.get(urlmoney).json()
    print(request['success'])
    print(request['money'])

#checking inventory for items that you can sell

def checkInv():
    urlinv = 'https://market.csgo.com/api/v2/my-inventory/?key='+key
    inventory = requests.get(urlinv).json()
    inv = str(inventory['items'])

    for i in inventory['items']:
    
        print(i['market_hash_name'])
        print('цена: ',i['market_price'])
        print('')


def trade():
    global accept
    urltr ="https://market.csgo.com/api/ItemRequest/in/1/?key="+ key
    accept = requests.post(urltr).json()
    print(accept)

######## используется для "selling" (отправляет уведомление на pushbullet)

def notification():
    pb = Pushbullet(PUBkey)
    push = pb.push_note("S","Accept")
    print("уведомление создано")
    print(push)
    
######## Используется для "selling_mode" (отправляет запрос и проверяет на верность и если так, то отправляет уведомление на pushbullet)

def selling():

        urlTrade ="https://market.csgo.com/api/ItemRequest/in/1/?key="+ key
        
        while True:
            1==1
            acceptGive = requests.get(urlTrade).json()
            print("Оффер готов: ",acceptGive["success"])
            
            if acceptGive["success"] == True:
                notification()
                time.sleep(30)    
            else: 
                time.sleep(30)
        
######## Используется для "selling_mode" (отправляет запрос на включение продаж)

def pinging():
    while True:
        1==1
        
        url = 'https://market.csgo.com/api/v2/ping?key='+key
        ping = requests.get(url).json()
        
        print("Продаются вещи: ",ping["success"])
        time.sleep(130)


def selling_mode():
    t2 = threading.Thread(target=selling)
    t1 = threading.Thread(target=pinging)
    
    t2.start()
    t1.start()
    


