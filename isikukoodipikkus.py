def isikukood():

    ik=open("IK.txt", "r")
    

    Lisikukood = 11
    iktulp=[]
    nimtulp=[]
    
    for line in ik:
        h = line.split("\t")
        iktulp.append(h[0])
        nimtulp.append(h[1])

  

    
    

    i = input("sisestage oma isikukood => ")
    Linput= len(i)
    
    if(Lisikukood > Linput):
      print("Vigane kood - pikkus on vale. Päringu lõpp")
    
     

isikukood()
