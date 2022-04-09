def dortgen_alan_hesapla_v1(x, y):
    print("-"*20)
    alan = x * y;
    print("Dörtgenin alanı: ", alan)
    print("-"*20)

    
def daire_alan_hesapla_v1(r):
    pi=3.14
    print("-"*20)
    alan = pi*r*r
    print("Dairenin alanı: ", alan)
    print("-"*20)

def dortgen_alan_hesapla_v2(x, y):
    print("-"*20)
    x = x*x
    y = y*y
    alan = x * y;
    print("Dörtgenin alanı: ", alan)
    print("-"*20)

def daire_alan_hesapla_v2(r):
    pi=3.14
    r = r*r
    print("-"*20)
    alan = pi*r**2
    print("Dairenin alanı: ", alan)
    print("-"*20)
    
while True:
    print("1-)Dortgen alan hesapla v1")
    print("2-)Daire alan hesapla v1")
    print("3-)Dortgen alan hesapla v2")
    print("4-)Daire alan hesapla v2") 
    a=int(input("Islem seciniz: "))
    
    if a==1:
        a=int(input("Uzun kenarı giriniz: "))
        b=int(input("Kısa kenarı giriniz: "))
        dortgen_alan_hesapla_v1(a, b)
    elif a==2:
        a=int(input("Yarı capı giriniz: "))
        daire_alan_hesapla_v1(a)
    elif a==3:
        a=int(input("Uzun kenarı giriniz: "))
        b=int(input("Kısa kenarı giriniz: "))
        dortgen_alan_hesapla_v2(a, b)
    elif a==4:
        a=int(input("Yarı capı giriniz: "))
        daire_alan_hesapla_v2(a)
    else:
        break
    
print("aaa")
    