def pikimsona():

  
   
    sonad=[]
        
    for i in range(5):
        s = input("sisestage mingi sõna (lõpetamiseks tühik) => ")
        sonad.append(s)       



    def sort(s):
     return len(s)

    
    f=sonad.sort(key=sort)
    
    
    print(sonad[4])
    
    l=len(sonad[4])
    print("tahti selles lauses:")
    print(l)
    
pikimsona()
