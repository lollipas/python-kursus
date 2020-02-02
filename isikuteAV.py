from statistics import mean
def isikuteAV(m):
    f=open("isikud.txt", "r")
    v=open("vastus.txt", "r+")
    
    if m < 20:
        print("Andmed puuduvad", file=v)

    vtulp=[]

    for line in f:
        h = line.split("\t")
        vtulp.append(h[6])

    #Listi ümbertegemine int
    conv = list(map(int, vtulp))    

    filterlist=[]
    count = 0
    for i in conv : 
         if i < m : 
             count = count + 1
             filterlist.append(i)

    #Keskmise arvutamine
    avg = mean(filterlist)

    #Faili kirjutamine
    print("Inimeste arv kes on noorem kui m on :", count, file=v)
    print("Nende keskmine vanus on :", round(avg), file=v)

    for line in v:
        print(line)

    f.close()
    v.close()
    

    
isikuteAV(30)