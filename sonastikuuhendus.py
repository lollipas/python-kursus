def sonastikuuhendus():
     d={'mark': 'Ford', 'mudel': 'Mustang'}
     d2={'aasta': 1964}
     d3={}
     for x in d:
         d3.update(d)
         d3.update(d2)
     print(d3)

      
sonastikuuhendus()
