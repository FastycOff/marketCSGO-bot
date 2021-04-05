import requests
import json

key = "0ZOhGE1B47jm79qcL624pr3xHI6O81Q"

###############################Поиск всех цен по названию предмета#################################################################

def price_f6():
    global name
    name = input("Введите название предмета из стима: ")
    url = 'https://market.csgo.com/api/v2/search-item-by-hash-name-specific?key='+key+'&hash_name='+name
    
    gun = requests.get(url+' (Factory New)').json()
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
        
######################Не сделано(Нужно с api steam)
#def autoaccept():
    #urla = "https://market.csgo.com/api/v2/trade-request-give-p2p-all?key="+key # данные для создания всех трейдов
    #urlb = "" # запрос на передачу вещей
    #trade = requests.get(urla).json
    #print(trade)

###################Не сделано(Не работает)
#def steamprice():
    #urlsteam = "http://steamcommunity.com/market/priceoverview/?appid=570&market_hash_name="+name
    #steamp = requests.get(urlsteam)").json()
    #print(steamp)
def balance():
    urlmoney = 'https://market.csgo.com/api/v2/get-money?key='+key
    request = requests.get(urlmoney).json()
    
    print(request['success'])
    print(request['money'])
    import requests
    
def checkInv():
    urlinv = 'https://market.csgo.com/api/v2/my-inventory/?key='+key
    inventory = requests.get(urlinv).json()
    inv = str(inventory['items'])

    for i in inventory['items']:
    
        print(i['market_hash_name'])
        print('цена: ',i['market_price'])
        print('')

