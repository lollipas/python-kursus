def aste(x):
    if x ==1:
        return "YES"
    elif x>1 and x<2:
        return "NO"
    else:
        return aste(x/2)


print(aste(16))
print(aste(256))
