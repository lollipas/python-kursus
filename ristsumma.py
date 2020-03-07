def ristsumma(x):
   
    if x < 10:
        return x
    else:
        return x % 10 + ristsumma(x//10)

print(ristsumma(4789))
print(ristsumma(181))
print(ristsumma(1818371297218937912398))
        

        

    
    
