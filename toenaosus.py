def toenaosus():
    list('list')
    ['1','2','3','4','5','6','7']
    
    
    s=int(input("sisesta silmade summa => "))
    
    mitu = 0
    for i in list:
        for j in list:
            for k in list:
                if i+j+k == s:mitu+=1
    p=mitu/6**3
    print("Tõenäosus on", round(p, 2))

toenaosus()
