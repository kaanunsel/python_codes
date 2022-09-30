print("Hoşgeldiniz. Bugün burada size 3 soru soracağız. \nHer doğru cevapta 5 puan kazanacak, her yanlış cevapta ise 3 puan kaybedeceksiniz.")
cevap_1 = input("Türkiye'nin başkenti hangi şehirdir? \nA)Adana  B)Eskişehir C)Ankara \n").capitalize()
puan = 0
if(cevap_1=="C"):
    puan = puan+5
    print("Tebrikler! Doğru bildiniz. \n PUANINIZ: ", puan)
else:
    puan = puan-3
    print("Yanlış yanıtladınız. Cevap Ankara olacaktı. \n PUANINIZ: ", puan)

cevap_2 = input("5 üzeri 3 kaçtır? \nA)25  B)125 C)625 \n").capitalize()
if(cevap_2=="B"):
    puan = puan+5
    print("Tebrikler! Doğru bildiniz. \n PUANINIZ: ", puan)
else:
    puan = puan-3
    print("Yanlış yanıtladınız. Cevap 125 olacaktı. \n PUANINIZ: ", puan)

cevap_3 = input("Karbon elementi en fazla kaç bağ yapar? \nA)4  B)3 C)2 \n").capitalize()
if(cevap_3=="A"):
    puan = puan+5
    print("Tebrikler! Doğru bildiniz. \n PUANINIZ: ", puan)
else:
    puan = puan-3
    print("Yanlış yanıtladınız. Cevap 4 olacaktı. \n PUANINIZ: ", puan)

print("Testin sonuna geldik. Toplam puanınız: ", puan)
input()
        