def bir():
    sm = 500
    sf = 20
    ciro = 5000

    counter = 0
    while (ciro <= 500000):
        sm = sm+20
        sf = sf+10
        ciro = ciro+(sm*sf)
        counter = counter+1

    yil =counter/12
    print("Şirketin Cirosu, 500 bin Tl yi ",counter," ay (yani ",round(yil,2)," yıl)","sonra geçer")

def iki():
    stok = 10000
    counter = 0
    while(stok > 0):
        #her ay...
        stok = (stok-500)+100
        counter = counter +1
    print("İşletme Stokları ",counter," ay sonra sıfırlanır. Yani",counter+1,". ayda")

def uc():
    print("3 bölümünden kalan sayıların Toplamı")
    kalanlar = 0
    
    while True:
        sayi = int(input("Sayı Giriniz : "))
        if(sayi > 0 ):
            kalanlar = kalanlar+(sayi%3)
        else:
            break
        
    print("Girilen Sayıların 3 ile bölümünden kalanların toplamı =",kalanlar)

        
while True:
    state  = int(input("Ödev Numarası Giriniz (1-5):"))  
    try:
        if(state == 1):
            bir()
        elif(state == 2):
            iki()
        elif(state == 3 ):
            uc()
        elif(state == 4 ):
            dort()
        elif(state == 5 ):
            bes()
    except  KeyboardInterrupt:
        exit()  
