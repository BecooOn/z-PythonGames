import time
import random
from colorama import init, Fore, Style
from IPython.display import HTML
from termcolor import colored, cprint


def blink_string(input_str, duration_seconds = 0.5, blink_count = 3):
    init(autoreset= True)  # Colorama'nin renk ayarlarini otomatik sifirlamak icin
    
    for i in range(blink_count):
        print(Fore.WHITE + input_str, end = "\r", flush = True)  # "\r" sizi ayni satirda satir basina getirir. 
        time.sleep(duration_seconds)  # duration_seconds kadar bekleyecek.
        print(' ' * len(input_str), end='\r', flush=True)
        time.sleep(duration_seconds/3)
    print(input_str)
    
def blink_sayac(input_str):
    init(autoreset=True)  # Colorama'nin renk ayarlarini otomatik sifirlamak icin
    
    print(input_str, end='')
    
    for count in range(3,0,-1):
        print(Fore.WHITE  + " " + str(count), end = '', flush = True)
        time.sleep(0.5)  # 0.8 saniye bekleyecek
        print(end='\b\b')  # ekrana yazdigi count u silecek. 
        time.sleep(0.5)  # 0.8 saniye bekleyecek
        
    print("\r" + " "*len(input_str))  # '\r' ile satir basina geliyoruz ve input_str uzunlugu kadar bos string ekliyoruz. 
    
    
    
    
cprint("Taş-Kağıt-Makas Oyunu: \n", "blue", attrs=['bold'])

liste = ["TAŞ", "KAĞIT", "MAKAS"]

kazanan = [("TAŞ", "MAKAS"), ("KAĞIT","TAŞ"), ("MAKAS","KAĞIT")]

puan_dict = {"rakip 1" : 0, "rakip 2" : 0}

tebrik_emoji = "\U0001F38A\U0001F389\U0001F38A\U0001F44F\U0001F44F" 
berabere_emoji = "\U0001f640\U0001f640\U0001f640\U0001f640"

isim1 = input("Birinci yarismacinin ismini giriniz: ").upper()
isim2 = input("Ikinci yarismacinin ismini giriniz: ").upper()

while True:
    limit = input("Oyun kaçta bitsin? ")
    if limit.isnumeric():
        limit = int(limit)
        break
        
while ((puan_dict["rakip 1"] < limit) and (puan_dict["rakip 2"]< limit)):
    
    blink_sayac("3sn Sonra Tas kagit makas secimleri yapilacak:")
    
    rakip1 = liste[random.randint(0,2)]
    rakip2 = liste[random.randint(0,2)]
    
    if (rakip1, rakip2) in kazanan:
        
        puan_dict["rakip 1"] += 1
        
        display(HTML(f"{isim1} : <font color = 'red'>{rakip1}  <===>  {isim2} : <font color = 'blue'>{rakip2} </font> Bu el kazanan : {isim1} {tebrik_emoji}"))
        print()
        blink_string(f'Puan durumu: {isim1} : {puan_dict["rakip 1"]} - {isim2} : {puan_dict["rakip 2"]}', 0.8, 2)
        print()
        time.sleep(1) 
    elif (rakip2, rakip1) in kazanan:
        puan_dict["rakip 2"] += 1
        display(HTML(f"{isim1} : <font color = 'red'>{rakip1}  <===>  {isim2} : <font color = 'blue'>{rakip2} </font> Bu el kazanan : {isim2} {tebrik_emoji}"))
        print()
        blink_string(f'Puan durumu: {isim1} : {puan_dict["rakip 1"]} - {isim2} : {puan_dict["rakip 2"]}', 0.8, 2)
        print()
        time.sleep(1) 
    else:
        display(HTML(f"{isim1} : <font color='cyan'>{rakip1}</font> - {isim2} : <font color='cyan'>{rakip2} </font>  Aynı seçim!!{berabere_emoji}\n"))
        

if puan_dict["rakip 1"] == limit:
    kazanan = isim1
else:
    kazanan = isim2
display(HTML(f"<font color='darkred'> <b> Oyun sona erdi.. <br>  Oyunu Kazanan : {kazanan}</b></font>"))


