isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]

soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

liste = list(zip(isimler,soyisimler))

def eşleştirme(demet):
    return demet[0] + "\t" + demet[1]


liste2 = list(map(eşleştirme,liste))

for i in liste2:
    print(i)