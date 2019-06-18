db = open("data.mac", "r+", encoding="UTF-8")
dr = db.read()
accounts = []

for i in range(len(dr.split("\n"))):
    accounts.append(dr.split("\n")[i].split(":"))

def write():
    str = ""
    for i in range(len(accounts)):
        if i < len(accounts) - 1:
            str += ":".join(accounts[i]) + "\n"
        else:
            str += ":".join(accounts[i])
    g = open("data.mac", "w")
    g.write(str)
    g.close()

while True:
    print("***************************************\n"
          "                Merhaba!\n"
          "***************************************")
    print("1. Yönetici Girişi\n2. Kullanıcı Girişi")
    giris = int(input("Lütfen Giriş Türünü Seçiniz: "))
    if giris == 1:
        print("Yönetici Paneli Girişi\n")
        a = int(input("Lütfen Yönetici Numaranızı Giriniz: "))
        adminState = "false"
        admin = []
        for i in range(len(accounts)):
            if (int(accounts[i][0]) == a and accounts[i][1] == "1"):
                adminState = "true"
                admin = accounts[i]
        if adminState == "true":
            b = int(input("Lütfen Şifrenizi Giriniz: "))
            if admin[3] == str(b):
                while True:
                    print(
                        "Hoşgeldiniz {}.\n1. Kullanıcıları Görüntüle\n2. Kullanıcı Ekle\n3. Kullanıcı Sil\n4. Yöneticileri Görüntüle\n5. Yönetici Ekle\n6. Yönetici Sil\n7. Çıkış".format(
                            admin[2]))
                    f = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz: "))
                    if f == 1:
                        for i in range(len(accounts)):
                            if accounts[i][1]=="0":
                                print("ID: '{}' Ad: '{}' Şifre: '{}' Bakiye: '{}'\n".format(accounts[i][0],accounts[i][2],accounts[i][3],accounts[i][4]))
                    elif f == 2:
                        kullanıcıekle = str(input("Lütfen Oluşturmak İstediğiniz Kullanıcı Adını Giriniz: "))
                        kullanıcısifre = str(input("Lütfen Kullanıcı İçin Parola Belirleyiniz: "))
                        accounts.append([str(len(accounts) + 1), "0", str(kullanıcıekle), str(kullanıcısifre), "0"])
                        write()
                    elif f == 3:
                        kullanıcısil = int(input("Lütfen Silmek İstediğiniz Kullanıcı ID'yi Giriniz: "))
                        for i in range(len(accounts)):
                            if accounts[i][0] == str(kullanıcısil):
                                accounts.pop(i)
                        write()
                    elif f == 4:
                        for i in range(len(accounts)):
                            if accounts[i][1]=="1":
                                print("ID: '{}' Ad: '{}' Şifre: '{}' Bakiye: '{}'\n".format(accounts[i][0],accounts[i][2],accounts[i][3],accounts[i][4]))
                    elif f == 5:
                        yoneticiekle = str(input("Lütfen Oluşturmak İstediğiniz Yönetici Adını Giriniz: "))
                        yoneticisifre = int(input("Lütfen Yönetici İçin Parola Belirleyiniz: "))
                        accounts.append([str(len(accounts) + 1), "1", str(yoneticiekle), str(yoneticisifre), "0"])
                        write()
                    elif f == 6:
                        yoneticisil = int(input("Lütfen Silmek İstediğiniz Yönetici ID'yi Giriniz: "))
                        for i in range(len(accounts)):
                            if accounts[i][0] == str(yoneticisil):
                                accounts.pop(i)
                        write()
                    elif f == 7:
                        print("Çıkış Yapılıyor.")
                        break
    elif giris == 2:
        print("Kullanıcı Paneli Girişi\n")
        c = int(input("Lütfen Kullanıcı Numaranızı Giriniz: "))
        userState = "false"
        user = []
        id = 0
        for i in range(len(accounts)):
            if (int(accounts[i][0]) == c):
                userState = "true"
                user = accounts[i]
                id = i
        if userState == "true":
            d = int(input("Lütfen Şifrenizi Giriniz: "))
            if user[3] == str(d):
                while True:
                    print(
                        "Hoşgeldiniz {}.\n1. Para Yatır\n2. Para Çek\n3. Para Gönder\n4. Bakiye Görüntüle\n5. Çıkış".format(
                            user[2]))
                    e = int(input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz: "))
                    if e == 1:
                        parayatırma = int(input("Lütfen Yatırmak İstediğiniz Tutarı giriniz: "))
                        accounts[id][4] = str(int(accounts[id][4]) + parayatırma)
                        write()
                    elif e == 2:
                        paracekme = int(input("Lütfen Çekmek İstediğiniz Tutarı giriniz: "))
                        money = int(accounts[id][4]) - paracekme
                        if money >= 0:
                            accounts[id][4] = str(int(accounts[id][4]) - paracekme)
                            print("Para çekme işleminiz gerçekleşmiştir.")
                            write()
                        else:
                            print("Bakiyeniz Yetersiz.")
                    elif e == 3:
                        paragonderhesap = int(input("Lütfen Para Transferi için Hesap No Giriniz: "))
                        check = "false"
                        targetAccount = 0
                        for i in range(len(accounts)):
                            if accounts[i][0] == str(paragonderhesap):
                                check = "true"
                                targetAccount = i
                        if check == "true":
                            paragondermiktar = int(input("Lütfen Para Transferi için Miktar Giriniz: "))
                            if int(user[4]) - paragondermiktar >= 0:
                                user[4] = str(int(user[4]) - paragondermiktar)
                                accounts[targetAccount][4] = str(int(accounts[targetAccount][4]) + paragondermiktar)
                                print("Para transferiniz gerçekleşmiştir!")
                                write()
                            else:
                                print("Bakiye yetersiz!")
                        else:
                            print("Hesap bulunamadı!")
                    elif e == 4:
                        print("Bakiyeniz {} TL'dir.".format(user[4]))
                    elif e == 5:
                        print("Çıkış Yapılıyor.")
                        break
            else:
                print("Hatalı Giriş Yaptınız!")
                break