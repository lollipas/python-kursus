sonad={'wolf': 'hunt', 'rabbit': 'kuulik', 'lamb': 'tall', 'cock': 'kukk',
           'rat': 'rott', 'badger': 'mager', 'hen': 'kana', 'fox': 'rebane',
           'pig': 'siga', 'bear': 'karu', 'deer': 'hirv', 'elk': 'poder',
           'foal': 'varss', 'piglet': 'porsas', 'monkey': 'ahv', 'turkey': 'kalkun',
           'horse': 'hobune', 'tiger': 'tiiger', 'lion': 'lovi', 'sheep': 'lammas',
           'beaver': 'kobras', 'mouse': 'hiir', 'cow': 'lehm',
           'dog': 'koer', 'cheetah': 'gepard', 'hedgehong': 'siil',
           'elephant': 'elevant', 'hare': 'janes', 'cat': 'kass'}


def sonastik1(sonad):
    
    while 1:
        sona=input("Sisestage sõna mida tahate tõlkida! (Katkestamiseks vajutage space)=> ")

        if sona == " ":
            print("Tühi tekst. Programm sulgub");break
            
        else:
            if sona in sonad:
                tolge=sonad[i]
                print(tolge)
            for i in sonad:

                if sonad[i] == sona:
                    print(sona)

                
            else: print("Väärtust pole")
    
    


    

sonastik1(sonad)
