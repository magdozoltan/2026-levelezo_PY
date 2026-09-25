def korszamlalas (kor):
    while kor < 65:
        kor += 1
        if kor == 52:
            continue
        print(kor)
        if kor == 55:
            break
    else:
        print('nyugger')
    print('Vége')
    return kor

# porogramfutás
kor = 56
print('Nyugdíj: ', korszamlalas(kor))

felhasznalo_kora = 20 #int(input('Hány éves vagy: '))
if felhasznalo_kora < 18:
    print('gyerek')
elif felhasznalo_kora < 30:
    print('Ifjú')
elif felhasznalo_kora <65:
    print('Felnőtt')
else:
    print('Nyugger')