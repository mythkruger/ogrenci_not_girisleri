#coder by kruger
def not_hesapla(satir):
    satir=satir[:-1] #satırlar arası boşluğu mantıksal hata oluşmasın diye yok ettik
    liste= satir.split(":")

    ogrenciadi=liste[0]
    notlar=liste[1]

    notlar=liste[1].split(",")
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama =(not1+not2+not3)/2
    harf="0"
    if ortalama>90:
        harf="AA"
    elif ortalama>=85 and ortalama<=89:
        harf="BA"
    elif ortalama>=65 and ortalama<=84:
        harf="CC"
        #şartları devam ettirmiyorum mantık aynı
    return ogrenciadi+": "+harf+ " \n"
def kayıt_sil():
    with open("sinav_notları.txt","r") as deletefile:
        satırlar= deletefile.readline()
        liste=[]
        for satır in satırlar:
            liste.append(not_gir(satır))

def ortalamaları_oku():
    with open("sinav_notları.txt","r") as file: #r means "read"
        for satir in file:
            print(not_hesapla(satir))
def not_gir():
    ad   = input("öğrenci adı:")
    soyad = input("öğrenci soyadı:")
    not1 = input("not1:")
    not2 = input("not2:")
    not3 = input("not3:")

    file= open("sinav_notları.txt","a")
    file.write(ad+" "+soyad+":"+not1+" ,"+not2+" ,"+not3+"\n")

def not_kayıt():
    with open("sinav_notları.txt","r") as file:
        list=[]

        for i in file:
            list.append(not_hesapla(i))
        with open("sonuclar.txt","w") as filesonuc:
            for i in list:
                filesonuc.write(i)



while True:
    islem=input("1-notları oku\n2-notları gir\n3-notları kayıt et\n4-kayıt sil\n5-cıkıs\n")
    if islem=="1":
        ortalamaları_oku()

    elif islem=="2":
        not_gir()

    elif islem=="3":
        not_kayıt()

    elif islem=="4":
        kayıt_sil()
    else:
        break