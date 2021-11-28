def MenuProfilsdeslecteurs():
    print("+--------------------------------------------------------+")
    print("|       -  Menu Gestion des profils des lecteurs -       |")
    print("|                                                        |")
    print("|              1 : Afficher des livres                   |")
    print("|              2 : Ajouter un lecteur                    |")
    print("|              3 : Afficher un lecteur                   |")
    print("|              4 : Modifier un lecteur                   |")
    print("|              5 : Supprimer un lecteur                  |")
    print("+--------------------------------------------------------+")
    choixCheck=False
    while choixCheck==False:
        choix=input("          !! Rentrez le numéro du menu voulu !!           \n")
        if choix in [str(i) for i in range(1,6)]:
            choixCheck=True
    return choix

    
def AjouterDesNouvellesLignes(fichier,tableauDesLignes):
    f = open(fichier,'r')
    tableauSauvegardeLignes = []
    for ele in f.readlines():
        tableauSauvegardeLignes.append(ele)
    f.close()
    if len(tableauSauvegardeLignes) > 0:
        tableauSauvegardeLignes[-1] = tableauSauvegardeLignes[-1] + '\n'
    f = open(fichier,'w')
    for ele in tableauSauvegardeLignes :
        f.write(ele)
    for ele in tableauDesLignes:
        f.write(ele)
    f.close()


def showBooks(books):
    print("+--------------------------------------------------------+")
    print("|                     Liste des livres                   |")
    print("+--------------------------------------------------------+")
    print('')
    f = open(books,"r")
    counter = 0
    for ele in f.readlines() :#readlines renvoit une liste qui contient les lines de f
        counter += 1
        print(str(counter)+' - ',ele[:-1]) #le dernier elements de la liste est \n
    f.close()


def addReaders():
    readers = 'readers.txt'
    print('\n','-'*7,'Ajouter un lecteur','-'*7,'\n')
    f = open(readers,"r")
    tableau_sauvegarde = []
    for line in f :
        tableau_sauvegarde.append(line)
    f.close()

    pseudo = input("Quel est ton pseudo ? : ")
    while type(pseudo) != type('Hello World'):
        pseudo = input("Quelle est ton pseudo ?, attention tu dois donner une chaîne de caractère. ")

    genre_check = False
    while genre_check == False:
        genre = input("Quel est ton genre ? ( 1.homme / 2.femme / 3.peu importe) : ")
        if genre == '1' or genre == '2' or genre == '3':
            genre_check = True

    age_check = False
    while age_check == False:
        print("Quel est ton âge ? : ")
        print("1. <= 18 ans,\n2. Entre 18 ans et 25 ans,\n3. > 25 ans\n",end='')
        age = input()
        if age == '1' or age == '2' or age == '3':
            age_check = True 

    style_lecture_check = False 
    while style_lecture_check == False :
        print("Le style de lecture\n1. Science-fiction\n2. Biographie\n3. Horreur\n4. Romance\n5. Fable\n6. Histoire\n7. Comédie") 
        style_lecture = input('\nQuel est ton style de lecture ? : ')
        tableau = []
        for i in range(1,8):
            tableau.append(str(i))
        if style_lecture in tableau:
            style_lecture_check = True 
    print('')
    AjouterDesNouvellesLignes('readers.txt',[pseudo+','+genre+','+age+','+style_lecture])
    showBooks('books.txt')
    tableauLivreLus = [] # Ce tableau stock tout les livres que l'utilisateur à lus
    tableauLivreLus.append(pseudo) # ici je mets le pseudo dans le but de pouvoir ensuite juste ajouter le tableau comme une nouvelle ligne de booksread
    ToutesLesRepPossibles = [str(i)for i in range(1,nombreDeLivres('books.txt')+1) ]
    check = False
    while check == False:
        livreLus = input("\nQuels livres avez-vous déjà lus ?('stop' pour terminer la saisie) :") # stock un livre que l'uti a lu
        if livreLus == 'stop':
            check = True
        elif livreLus in ToutesLesRepPossibles:
            tableauLivreLus.append(livreLus)
            ToutesLesRepPossibles.remove(livreLus) # Un livre ne peut avoir été lu 2x    print("L'utilisateur a bien été ajouté !")
    tableauLivreLus = ','.join(tableauLivreLus)
    AjouterDesNouvellesLignes('booksread.txt',tableauLivreLus)
def nombreDeLivres(books):
    f = open(books,'r')
    taille = len(f.readlines())
    f.close()
    return taille
def AfficherUnLecteur():
    print('\n','-'*7,'Afficher un lecteur','-'*7,'\n')
addReaders()