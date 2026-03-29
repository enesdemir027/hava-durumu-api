import requests
from bs4 import BeautifulSoup
import time
import json

print("""
Hava Durumu Çekici
------------------
Bugün hava nasıl merak edenlere...
""")

sehir = input("şehir ismi girermisiniz? ")

print(f"\n{sehir} için hava aranıyor...")

try:
    url = f"https://wttr.in/{sehir}?format=%l:+%c+%t+%w+%h"
    istek = requests.get(url, timeout=8)
    
    if istek.status_code == 200:
        sonuc = istek.text.strip()
        print("\n" + "="*45)
        print(sonuc)
        print("="*45)
        
        with open("hava.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{time.ctime()} - {sehir}: {sonuc}\n")
            
        print("\nKaydedildi.")
    else:
        print("bağlantı sorunu var.")
        
except:
    print("olan dışı hata internet kontrol edermisin.")
