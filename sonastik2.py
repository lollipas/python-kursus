sonad={}


def sonastik2(sonastik):
    
    
    while True:
        sona=input("Sisestage mingi sõna inglisekeeles => ")
        
        if sona=="":
            print("Tühi tekst. Programmi lõpp");break
            
        if sona in sonad:
           tolge=sonad[sona]
        else:
            sonad[sona]=input("nüüd tõlgi! =>")
           
sonastik2(sonad)
print(sonad)
