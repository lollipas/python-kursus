def rootsilaud():
    road=('P, L, Kl, Kn, Ka')

    for i in road:
        print(i)

    #road[3]=('Kaste') - ei ole lubatud

    road=list(road)
    print(road)

    road[4]='UUS TOIT'
    road[5]='UUS TOIT 2'

    road=tuple(road)
rootsilaud()
