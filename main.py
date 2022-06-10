# This is a sample Python script.
#import end as end
import random

import yfinance as yf
import json
import ctypes
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#print(datafromjsonfile[1]['ticker'])

#for i in datafromjsonfile:
 #   print(i['ticker'])

choix = '0'
tickerexists = 0
maxIscorrect = 0
minIscorrect = 0


updategraph = 1

while choix != 'q' and choix != 'Q':
    jsonfileWL = open('data.json', 'r+') # fichier Json watchlist
    datafromjsonfile = json.load(jsonfileWL)
    print ( "Veuillez chosir une option \n" 
           "1- Afficher les donnés de ma watchlist \n"
           "2- Ajouter un élément à ma watchlist \n"
           "3- supprimer un élement dans la watchlist \n"
           "q- Quitter \n " )
    choix = input()
    if (choix == '1'):

        jsonfileWL = open('data.json', 'r+')  # fichier Json watchlist
        datafromjsonfile = json.load(jsonfileWL)
        print ("Veuillez entrer l'élément dans votre watchlist à obsérver")

        cpt = 0

        for i in datafromjsonfile:
          print(f"{cpt}-  {i['ticker']} ")
          cpt += 1

        input = input()

        print(f"affichage de : {datafromjsonfile[int(input)]['ticker']}")


        #plt.plot(105, 200, 'o')
        #fig = pylab.gcf()
        #fig.canvas.set_window_title('AAPL')
       # xpoints = np.array([0, 6])


        #plt.plot(xpoints)
        #plt.show()
        x= 1
        ticker = yf.Ticker(datafromjsonfile[int(input)]['ticker'])
        info = ticker.info
        x_numberlist = [x]
        y_numberlist = [info['regularMarketPrice']]
        while updategraph == 1:







           print( info['regularMarketPrice'])



           plt.plot(x_numberlist, y_numberlist, 'ro-')
           #plt.plot(x, info['regularMarketPrice']+ 1 , 'o')
           plt.draw()
           plt.pause(0.00000001)
           plt.clf()

           for i  in datafromjsonfile:
               if i['max']< info['regularMarketPrice']:
                    Mbox('Alerte ', f'La valeur de {i["ticker"]} a dépassé son max : {i["max"]}', 0)

               if i['min'] > info['regularMarketPrice']:
                   Mbox('Alerte ', f'La valeur de {i["ticker"]} est en dessous de son min  : {i["min"]}', 0)

           x += 1
           ticker = yf.Ticker(datafromjsonfile[int(input)]['ticker'])
           info = ticker.info

           temp = info['regularMarketPrice'] # + random.randint(1 , 6 )
           y_numberlist.append( temp )
           x_numberlist.append(x)


           # plt.clear()
           #xpoints = np.array([0 +x, 6 +x])
           #ypoints = np.array([0 +x, 250 +x] )
           #
           #print(x)
           #plt.plot(xpoints, ypoints)
           #plt.show()
          # plt.clear()
           # Mbox('Alerte ', 'Your text', 0)

    if (choix == '3'):


          jsonfileWL = open('data.json', 'r+')  # fichier Json watchlist
          datafromjsonfile = json.load(jsonfileWL)
          print("Veuillez entrer l'élément dans votre watchlist à supprimer")

          cpt = 0

          for i in datafromjsonfile:
              print(f"{cpt}-  {i['ticker']} ")
              cpt += 1

          inputt = input()


          print(f"symbole à supprimer  : {datafromjsonfile[int(inputt)]['ticker']}")
          jsonfileWL.truncate(0)
          jsonfileWL.seek(0)
          datafromjsonfile.pop(int(inputt))
          json.dump(datafromjsonfile, jsonfileWL)
          jsonfileWL.close()



    if (choix == '2'):
        print('Veuillez Entrer le Symbole boursier à ajouter dans votre liste ')
        _ticker = input()
        for i in datafromjsonfile:
          if i['ticker'] == _ticker:
              tickerexists = 1

        if tickerexists == 1 :
            print("Symbole boursier existe dèja dans votre watchlist \n")
        else:
         for t in [_ticker]:
             ticker = yf.Ticker(_ticker)
             info = None
             try:
                 info = ticker.info
                 if info['regularMarketPrice'] == None :
                  print("Symbole boursier Introuvable")

                 else :

                     while maxIscorrect == 0:
                       print(f"Veuillez entrer la valeur maximale de l'Action, Actuelle : {info['regularMarketPrice']}"  )
                       maxi = input()
                       if (float(maxi) > info['regularMarketPrice']):
                           maxIscorrect  = 1
                       else:
                           print("la valeur maximale devrait être supérieur au prix actuel de l'Action")
                     while minIscorrect == 0:
                       print(f"Veuillez entrer la valeur minimale de l'Action, Actuelle : {info['regularMarketPrice']}"  )
                       mini = input()
                       if (float(mini) < info['regularMarketPrice']):
                           minIscorrect  = 1
                       else:
                           print("la valeur minimale devrait être inférieur au prix actuel de l'Action")


                     datatosave = {'ticker':_ticker,
                                   'max': float(maxi),
                                   'min': float(mini)}

                     jsonfileWL.truncate(0)
                     jsonfileWL.seek(0)
                     datafromjsonfile.append(datatosave)
                     json.dump(datafromjsonfile, jsonfileWL)
                     jsonfileWL.close()

                     print(f"Le symbole boursier {t} a été ajouté à votre liste : {datatosave}")
             except Exception as e :
                 print("Impossible d'ajouter ce symbole boursier à votre watchlist : " + e)
                 continue

    tickerexists = 0
    maxIscorrect = 0
    minIscorrect = 0




    # Got the info of the ticker, do more stuff with it

    # Got the info of the ticker, do more stuff with it


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
