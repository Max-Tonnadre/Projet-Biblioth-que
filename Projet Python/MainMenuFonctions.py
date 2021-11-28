def AfficherMainMenu():
    print("+--------------------------------------------------------+")
    print("|                  -  Menu Principal -                   |")
    print("|                                                        |")
    print("|              1 : Profils des lecteurs                  |")
    print("|              2 : Visiter le dépôt des livres           |")
    print("|              3 : Recommandation                        |")
    print("+--------------------------------------------------------+")
    choixCheck=False
    while choixCheck==False:
        choix=input("          !! Rentrez le numéro du menu voulu !!           \n")
        if choix=="1" or choix=="2"or choix=="3" :
            choixCheck=True
    return choix