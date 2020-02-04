import math
def funktsioonilahend(a,b,n):

      xloend=[]
      yloend=[]
      h = (b-a)/n
      v=open("asdf.txt", "w")

      if a < b:
         print("A peab olema väiksem")

      
      for i in range(0, n+1):
         tehe =  a + h*i
         tehe2=pow((tehe - 1), 3)/3
         tehe3= 4*tehe - 1
         tehe4= 3 *math.sin(tehe) + pow(math.cos(tehe), 2)

         if(tehe <= -1.8 ):
             print(round(tehe2, 3))

         if(-1.8 < tehe < 2):
             print(round(tehe3, 3))

         if(tehe >= 2):
             print(round(tehe4, 3))

         yloend.append(tehe)
         print(yloend)       

funktsioonilahend(-3,3,24)