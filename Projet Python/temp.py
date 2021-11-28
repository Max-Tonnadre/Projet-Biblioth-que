def modifyBookName(bookToChange):
    Booklist=[]
    bookDoc=open("books.txt","r")
    for line in bookDoc :            
        Booklist.append(line.replace("\n",""))
    Booklist.remove(bookToChange)#Nous avons maintenant une liste sans le livre à modifier 
    bookDoc.close()
    bookDoc=open("books.txt","w")
    for book in Booklist:
        bookDoc.write(book+"\n")
    bookDoc.write(input("Rentrez le nouveau nom de "+bookToChange))
    bookDoc.close()





def addBook():
    Booklist=[]
    bookDoc=open("books.txt","r")
    for line in bookDoc :              #J'ai favorisé cette méthode à readlines() pour me débarasser facilement des "\n"
        Booklist.append(line.replace("\n",""))
    bookToAdd=str(input("Rentres le nom du livres que tu veux ajouter :"))
    if bookToAdd in Booklist :
        print("Ce livres apparait déjà dans la liste des livres voulez vous le modifier ? 1 pour oui  2 pour non")
        bookDoc.close()
    else:
        bookDoc.close()
        bookDoc=open("books.txt","a")
        bookDoc.write('\n'+bookToAdd)
        print("Le livre à bien été ajouté à la liste des livres")
        bookDoc.close()
        

        
    
      




 