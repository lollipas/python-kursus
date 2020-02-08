
#TEE HILJEM OIGESTI


def tahtedearv():
        e=input("Sisestage tekst siia => ")

        tekst={'sonad': e}

        if 'sonad' in tekst:
            print("Võti on olemas")
        else: print("None")
     
        if e.isalpha():
             print(len(tekst['sonad']))
        else: print("Kasuta tähti!")
tahtedearv()
