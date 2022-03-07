import random

birimler  = ["ikiyüz", "yüz", "elli", "yirmi", "on"]
degerler  = [200, 100, 50, 20, 10, 0]
miktarlar = [100, 100, 100, 100, 100]

kisi, zaman = 0, 480 # sabah 8:00'da başlayacak
while True:
##    miktar = random.randrange(10, 2000, 10)
    miktar = int(random.gammavariate(2, 30)) * 10 + 10 # 200-500 TL arası daha çok para çeken olsun diye
    zaman += random.randint(1, 15)
    if kisi % 10 == 0:
        yatıran = random.randint(0, 9)
    if kisi % 10 == yatıran:
        kisi += 1
        print("%d. kişi %d TL yatıracak (saat: %02d:%02d)" % (kisi, miktar, zaman//60, zaman%60))
        print("alınan  : ", end="")
        for i in range(5):
            if miktar >= degerler[i] and miktar >= 5 * degerler[i+1]:
                print(miktar // degerler[i], "adet", birimler[i], end=", ")
                miktarlar[i] += miktar // degerler[i]
                miktar %= degerler[i] 
    else:
        kisi += 1
        print("%d. kişi %d TL çekecek (saat: %02d:%02d)" % (kisi, miktar, zaman//60, zaman%60))
        print("verilen : ", end="")
        for i in range(5):
            if miktar >= degerler[i] and miktar >= 5 * degerler[i+1]: # önce büyük banknotlar tükenmesin diye
                if miktarlar[i] >= miktar // degerler[i]:
                    print(miktar // degerler[i], "adet", birimler[i], end=", ")
                    miktarlar[i] -= miktar // degerler[i]
                    miktar %= degerler[i] 
                elif miktarlar[i]:
                    print(miktarlar[i], "adet", birimler[i], end=", ")
                    miktar -= miktarlar[i] * degerler[i] 
                    miktarlar[i] = 0

    print("\b\b.\nkalan   : ", end="")
    for i in range(5):
        print(miktarlar[i], "adet", birimler[i], end=", ")
    print("\b\b.\n")

    if (sum(miktarlar) == 0):
        print("--- para bitti ---")
        break

input()
