import random


def loendennik():
    ennik=()
    arvud1=[]
    arvud2=[]
    arvud3=[]
    for i in range(5):
        
        r = random.randint(0,5)
        arvud1.append(r)
        r2=random.randint(-5,0)
        arvud2.append(r2)


    
    arvud1=tuple(arvud1)
    arvud2=tuple(arvud2)
    arvud3=arvud1+arvud2
    print(arvud3)

    
    e=arvud3.count(0)
            

        
    print("Selles ennikus nullide arv on: ", e)
loendennik()
