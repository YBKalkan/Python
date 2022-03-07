while(1):
    v = int(input("Vize Notu  : "))
    f = int(input("Final Notu : "))
    bn = int(v * 0.3 + f * 0.7 + 0.5)
    print("Başarı Notu =", bn, end=' ')
    if bn >= 60:
        print("(başarılı)")
    else:
        print("(başarısız), final sınavından en az", round((60 - (v*0.3))/0.7),  "almalıydı")
        b = int(input("Bütünleme Notu : "))
        bn = int(v * 0.3 + b * 0.7 + 0.5)
        print("Başarı Notu =", bn, end=' ')
        if bn >= 60:
            print("(başarılı)")
        else:
            print("(başarısız), bütünleme sınavından en az", round((60 - (v*0.3))/0.7),  "almalıydı")
    print()
