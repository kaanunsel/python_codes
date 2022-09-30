import random

while True:
    satır_a = [0,0,0]
    satır_b = [0,0,0]
    satır_c = [0,0,0]
    sutun_1 = [0,0,0]
    sutun_2 = [0,0,0]
    sutun_3 = [0,0,0]
    sıralar = [satır_a,satır_b,satır_c,sutun_1,sutun_2,sutun_3]

    a1 = satır_a[0]
    a2 = satır_a[1]
    a3 = satır_a[2]
    b1 = satır_b[0]
    b2 = satır_b[1]
    b3 = satır_b[2]
    c1 = satır_c[0]
    c2 = satır_c[1]
    c3 = satır_c[2]

    tumu = satır_a + satır_b + satır_c
    kontrol = (sum(satır_a) + sum(satır_b) + sum(satır_c)) == 45 and len(tumu) == len(set(tumu))
    while(kontrol == False):
        for i in range(0,3):
            for k in range(0,3):
                sıralar[i][k] = random.randint(1,9)
        tumu = satır_a + satır_b + satır_c
        kontrol = (sum(satır_a) + sum(satır_b) + sum(satır_c)) == 45 and len(tumu) == len(set(tumu))
         
    print(f"'{satır_a[0]}'  '{satır_a[1]}'  '{satır_a[2]}'  \n'{satır_b[0]}'  '{satır_b[1]}'  '{satır_b[2]}'  \n'{satır_c[0]}'  '{satır_c[1]}'  '{satır_c[2]}'")

    cevap = input("Yeni matrix ürretmek için A'yı, programı sonlandırmak için B'yi tuşlayınız.")
    if(cevap.lower()== "a"):
        continue
    elif(cevap.lower()== "b"):
        break
    else:
        break
    
