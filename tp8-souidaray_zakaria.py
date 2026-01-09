#Zakaria Souidaray

#pour utiliser le programme il suffit de le lancer, puis vous pouvez commencer par defaut en 1vs1 avec un autre joueur (la case devient gris lorsque le mode est deja active) il suffit de cliquer sur les cases grille pour selectionner un coup. en appuyant sur CPU 9 vous pouvez jouer contre un ordi(lorsque quon change entre ces deux mode le jeux ce relance depuis le debut).
#Le bouton REVENGE sert a relancer une partie, passe le tour a passer le tour si les deux joueur passe leurs tour la partie est finis. le bouton Undo permet de revoir la dernier action et Ragequit? permet de quitter la fenetre. 
#Pour Finir Une Partie Il faut appuyer sur le bouton PasseLeTour

#ce que vous avez fait en plus ou en moins par rapport à l'énoncé:
#-je n'ai pas suivie les Conseils d'implémentation
#-je n'ai rien ajouter par rapport à l'énoncé.


import tkinter
from random import *

class Grille:
  def __init__(self,hauteur,largeur) :
    self.largeur=largeur
    self.hauteur=hauteur
    self.plateau=[]
    for y in range(self.hauteur):
      ligne=[]
      for x in range(self.largeur):
        ligne.append(0)
      self.plateau.append(ligne)
  
  def get(self,x,y):
    try:
      return self.plateau[y][x]
    except IndexError:
      pass

  def set(self,x,y,val):
    try:
      self.plateau[y][x]=val
      return {"x": x+1, "y":y+1, "pion": val}
    except IndexError as detail:
      print("Erreur en",x,y,":",detail)
      return None
  
  def afficher(self):
    largeur = self.largeur
    hauteur = self.hauteur
    for y in range(hauteur):
      for x in range(largeur):
        print(self.get(x,y),end=" ")
      print()



class PlateauOthello:
  def __init__(self) :
    self.grille = Grille(8,8)
    self.placer_pions()

  def placer_pions(self):
    self.grille.set(4, 4, 2)
    self.grille.set(3, 3, 2)
    self.grille.set(4, 3, 1)
    self.grille.set(3, 4, 1)


  def lister_coups_possibles(self,joueur):
    i=0
    liste=[]
    for elt in plateau.grille.plateau:
      i=i+1
      e=0
      for elt in elt:
        e=e+1
        coup = Coup(i,e,plateau,joueur)
        if coup.est_valide() == True:
          liste.append([i,e])  
    return liste

  def compter_pieces(self):
      i=0
      j=0
      for elt in plateau.grille.plateau:
        for elt in elt:
          if elt == 1:
            i=i+1
    
          elif elt == 2:
            j=j+1
      return [i,j]



      
 
plateau=PlateauOthello() 
 
class Coup:

  def __init__(self, xp,yp,plateau,joueur):
    self.xp= xp
    self.yp= yp
    self.plateau = plateau
    self.joueur= joueur

  def est_dans_grille (self):
    return 0 <= self.xp < self.plateau.grille.hauteur  and \
0 <= self.yp < self.plateau.grille.largeur 
  
  def case_est_libre(self):
    grille= self.plateau.grille
    return grille.get (self.xp, self.yp)==0

  def peut_retourner (self, dx, dy):
    largeur = self.plateau.grille.largeur
    hauteur = self.plateau.grille.hauteur
    grille = self.plateau.grille
    adversaire = 3 - self.joueur
    x= self.xp + dx
    y= self.yp + dy
    nb_adversaire =0
    while 0 <= x < largeur and 0 <= y < hauteur:
      case = grille.get (x , y)
      if case == adversaire :
        nb_adversaire += 1
      else:
        break 
      x += dx ; y += dy
    return nb_adversaire  > 0 and \
      0 <= x < largeur and 0 <= y < hauteur and \
      case == self.joueur 


  def est_valide (self):
    if not ( self.est_dans_grille() and self.case_est_libre()):
      return False
    for dx , dy in [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]:
      if self.peut_retourner(dx,dy):
        return True
    return False
  
  def lister_pions_a_retourner(self):
    grille = self.plateau.grille
    dx=self.xp
    dy=self.yp
    liste=[]
    for dx , dy in [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]:
      if self.peut_retourner(dx,dy):
        
        e=1
        while grille.get ((dx*e+self.xp) , (dy*e+self.yp)) != self.joueur :
          liste.append([dx*e+self.xp,dy*e+self.yp])
          e=e+1
    return liste

    
  
  def retourner_pions_de_liste(self,liste):
    grille = plateau.grille.plateau
    for elt in liste:
      x=elt[0]
      y=elt[1]
      g=grille[y]
      g[x]=self.joueur

class Coupj:
    def __init__(self,xp,yp,liste):
        self.xp= xp
        self.yp= yp
        self.liste = liste
        
    def methode_defaire(self, plateau):
        y= plateau[self.yp]
        y[self.xp]= 0
        liste = self.liste
        sous=liste[len(liste)-1]
        for elt in sous:
            x=elt[0]
            y=elt[1]
            g=plateau[y]
            g[x]= zone_dessin.round%2+1




def tout_dessiner(zone_dessin) :
  
  coucou()  
  r= 40
  zone_dessin.delete(tkinter.ALL)
  zone_dessin.create_rectangle (r/2, r/2, ((8*r) + (r/2)) , ((8*r) + (r/2)) , outline="black", fill="#ccc")
  e=0 
  while e <= plateau.grille.hauteur-1 :
    n=0
    while n <= plateau.grille.largeur-1 :
      
      x0 = r/2 + r*e
      y0 = r/2
      y1 = r/2 + r*(n+1)
      x1= r/2 + r*e
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")
      x0 = x1
      y0 = y1
      y1= r/2 + r*(n+1)
      x1= r/2 + r*(e+1)
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")
      x0 = x1
      y0 = y1
      x1 = r/2 + r*(e+1)
      y1 = r/2 + r*n
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")
      x0 = x1
      y0 = y1
      x1 = r/2 + r*e
      y1 = r/2 + r*n
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")

      n=n+1
    e=e+1
  

  zone_dessin.create_text(10, 5, text="Tour du Joueur1" , anchor="nw", tag= "blue")
  dessiner_pion(zone_dessin)


#def dessiner_pion est une fonction qui grace a la liste de la grille du plateau dessin les pions celon la position sur la matrice plateau
  
def dessiner_pion(zone_dessin) :
  plateau = zone_dessin.plateau
  grille=plateau.grille.plateau

  p=0
  for elt in grille:  
    o=0
    for elt in elt :
      if elt == 2: 
        r=40
        e=0 
        while e <= plateau.grille.largeur-1 :
          n=0
          while n <= plateau.grille.hauteur-1 :
            if n == p and e == o:
              zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="white",width="2")
              
            n=n+1
          e=e+1
      elif elt == 1: 
        r=40
        e=0 
        while e <= plateau.grille.largeur-1 :
          n=0
          while n <= plateau.grille.hauteur-1 :
            if n == p and e == o:
              zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="black",width="2")
              
            n=n+1
          e=e+1
      o=o+1
    p=p+1


def bouton_appui(event):
  
  plateau = zone_dessin.plateau
  grille=plateau.grille.plateau
  r = 40
  round=zone_dessin.round

  offset_start_grille = (r/2) 

  n = plateau.grille.hauteur
  e = plateau.grille.largeur

  if(event.x >= offset_start_grille and
     event.x <= (plateau.grille.largeur*r) + offset_start_grille and
     event.y >= offset_start_grille and 
     event.y <= (plateau.grille.hauteur*r) + offset_start_grille):
    #on verifie si le clique est dans le tableau 
    e = int((event.x + offset_start_grille) // r -1)
    n = int((event.y + offset_start_grille) // r -1)
    # ici on fait un -1 car ce sont des index et ils seront utilisé
    # pour acceder au case de la matrice
    x0 = r/2 + r*e
    y0 = r/2 + r*n
    y1 = r/2 + r*(n+1)  
    x1= r/2 + r*e
    zone_dessin.create_line(x0,y0,x1,y1, fill="red" )
    x0 = x1
    y0 = y1
    y1= r/2 + r*(n+1)
    x1= r/2 + r*(e+1)
    zone_dessin.create_line(x0,y0,x1,y1, fill="red")
    x0 = x1
    y0 = y1
    x1 = r/2 + r*(e+1)
    y1 = r/2 + r*n
    zone_dessin.create_line(x0,y0,x1,y1, fill="red")
    x0 = x1
    y0 = y1
    x1 = r/2 +r*e
    y1 = r/2 + r*n
    zone_dessin.create_line(x0,y0,x1,y1, fill="red")
    coup = Coup(e,n,plateau,round%2+1)
    zone_dessin.coup=coup.est_valide()
    g=grille[n]
    
    if coup.est_dans_grille() == True and coup.case_est_libre() == True and coup.est_valide()== True :
      if g[e]==1 or g[e]==2 :
        pass
      else:
        if round%2+1 == 1:
          zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="black",width="2")
          zone_dessin.pion_a_retourner.append(coup.lister_pions_a_retourner()) 
          
          coup.retourner_pions_de_liste(coup.lister_pions_a_retourner())
          zone_dessin.round=round+1
          zone_dessin.coor=[e,n]
          zone_dessin.liste_coups_jouer.append([e,n])
          

        elif round%2+1 == 2 :
          
          zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="white",width="2")
          zone_dessin.pion_a_retourner.append(coup.lister_pions_a_retourner())
          
          coup.retourner_pions_de_liste(coup.lister_pions_a_retourner())
          zone_dessin.round=round+1 
          zone_dessin.coor=[e,n]
          zone_dessin.liste_coups_jouer.append([e,n])
  
  coucou()

#lorsque vous relacher votre click droit cette fonction ce lance, ce qui mets dans le plateau le coup qui est jouer et change le tour du joueu. il faut savoir aussi que lorsque le bouton CPU 9 est activer elle permet aussi de faire jouer l'ordinateur.

def bouton_relacher(event):
  r=40
  grille=plateau.grille.plateau
  round=zone_dessin.round
  
  if zone_dessin.coup==True:
    lecoup = zone_dessin.coor
    x=lecoup[0]
    y=lecoup[1]
    g=grille[y]
    g[x]=2-round%2

    dessiner_pion(zone_dessin)
    fen_princ.after(0, animation)
    fen_princ.after(150, animation2)
    fen_princ.after(300, animation3)
    fen_princ.after(450, animation4)
    fen_princ.after(600, animation5)
    fen_princ.after(750, animation6)
    if round%2==0:
      zone_dessin.create_oval ((r/2)+r*x,(r/2)+r*(y+1),(r/2)+r*(x+1),(r/2)+r*y, outline="red", fill="white",width="2")
    else:
      zone_dessin.create_oval ((r/2)+r*x,(r/2)+r*(y+1),(r/2)+r*(x+1),(r/2)+r*y, outline="red", fill="black",width="2")

  if round%2 ==0:
    zone_dessin.delete("blue")
    zone_dessin.create_text(10, 5, text="Tour du Joueur1" , anchor="nw", tag="blue")

  else:

    zone_dessin.delete("blue")
    zone_dessin.create_text(10, 5, text="Tour du Joueur2" , anchor="nw", tag="blue")
  r = 40
  e=0
  n_ligs=plateau.grille.hauteur
  n_cols=plateau.grille.largeur
  while e <= n_ligs-1 :
    n=0
    while n <= n_cols-1 :

      x0 = r/2 + r*e
      y0 = r/2
      y1 = r/2 + r*(n+1)
      x1= r/2 + r*e
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")
      x0 = x1
      y0 = y1
      y1= r/2 + r*(n+1)
      x1= r/2 + r*(e+1)
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")
      x0 = x1
      y0 = y1
      x1 = r/2 + r*(e+1)
      y1 = r/2 + r*n
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")
      x0 = x1
      y0 = y1
      x1 = r/2 + r*e
      y1 = r/2 + r*n
      zone_dessin.create_line(x0,y0,x1,y1, fill="black")

      n=n+1
    e=e+1
  x="joueur2 à "
  if zone_dessin.ordinateur==1:
    cpu()
    x= "ordinateur à "


  a=plateau.compter_pieces()
  i=a[0]
  j=a[1]
  zone_dessin.create_text(10, 340, text="Joueur1 à "+str(i)+"point(s)" , anchor="nw", tag="blue")
  zone_dessin.create_text(210, 340, text=x+str(j)+"point(s)" , anchor="nw", tag="blue")

  dessiner_coup_possible(zone_dessin,plateau.lister_coups_possibles(zone_dessin.round%2+1))

#le bouton_undo est ce qui permet de revenir un coup avant. 

def bouton_undo () :
  
  z=zone_dessin.liste_coups_jouer
  ledernier=zone_dessin.liste_coups_jouer[len(z)-1]
  e=ledernier[0]
  n=ledernier[1]
  a=zone_dessin.pion_a_retourner
  
  coup=Coupj(e,n,a)
  coup.methode_defaire(plateau.grille.plateau)
  zone_dessin.delete(tkinter.ALL)
  tout_dessiner(zone_dessin)
  a.remove(a[len(a)-1])
  z.remove(z[len(z)-1])
  zone_dessin.round = zone_dessin.round%2+1
  if zone_dessin.round ==2:
    zone_dessin.delete("blue")
    zone_dessin.create_text(10, 5, text="Tour du Joueur1" , anchor="nw", tag="blue")
  else:
    zone_dessin.delete("blue")
    zone_dessin.create_text(10, 5, text="Tour du Joueur2" , anchor="nw", tag="blue")
  dessiner_coup_possible(zone_dessin,plateau.lister_coups_possibles(zone_dessin.round%2+1))
  coucou()
  
#def dessiner_coup_possible est ce qui permet de dessiner des croix sur toute les zone ou le joueur peux jouer

def dessiner_coup_possible(zone_dessin,a):
  zone_dessin.delete("green")
  r=40
  for elt in a:
    e=elt[0]
    n=elt[1] 
    zone_dessin.create_line ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, fill="green",tag="green")
    zone_dessin.create_line ((r/2)+r*e,(r/2)+r*n,(r/2)+r*(e+1),(r/2)+r*(n+1), fill="green", tag="green")

#def deuxjoueur() est ce qui me permet de changer de mode pour faire des session joueur contre joueur

def deuxjoueur():
  zone_dessin.ordinateur=0
  zone_dessin.joueur=1 
  print("octogone")
  joueur_or_cpu()
  boutonrecommencer()

#def ordinateur() et ce qui permet une fois activer de jouer contre l'ordinateur 

def ordinateur():
  zone_dessin.ordinateur=1
  zone_dessin.joueur=0
  print("vs cpu")
  joueur_or_cpu()
  boutonrecommencer()


# def cpu() est le programme qui permet a lordinateur de jouer un coup au hazard

def cpu():
  r=40
  grille=plateau.grille.plateau
  if zone_dessin.coup==True and plateau.lister_coups_possibles(2) != []:
    zone_dessin.round=zone_dessin.round%2+1
    couppossible=plateau.lister_coups_possibles(zone_dessin.round)
    a=randint(0,len(couppossible)-1)
    p=couppossible[a]
    e=p[0]
    n=p[1]
    g=grille[n]
    g[e]=2
  
    zone_dessin.liste_coups_jouer.append([e,n])
    coup = Coup(e,n,plateau,2)
    zone_dessin.pion_a_retourner.append(coup.lister_pions_a_retourner())
    coup.retourner_pions_de_liste(coup.lister_pions_a_retourner())
    dessiner_pion(zone_dessin)
    zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="red", fill="white",width="2")
    zone_dessin.delete("blue")
    zone_dessin.create_text(10, 5, text="Tour du Joueur1" , anchor="nw", tag="blue")
  else:
    passe_le_tour()

# permet de passer le tour, si les deux jouers passe leurs tour alors la partie est finis. noté qui est possible de passer son tour que lorsqu'on a pas de coup possible à jouer.

def passe_le_tour():
  zone_dessin.nbdepassetour=zone_dessin.nbdepassetour+1
  if plateau.lister_coups_possibles(zone_dessin.round%2+1) != []:
    print ("tu dois jouer")
    zone_dessin.nbdepassetour=0
  else:
    if zone_dessin.nbdepassetour == 2:
      print("fin de le partie")
      a=plateau.compter_pieces()
      i=a[0]
      j=a[1]
      x="joueur2 à gagner "
      if zone_dessin.ordinateur==1:
        x= "ordinateur à gagner"
      boutonrecommencer()
      if i>j :
        zone_dessin.create_text(140, 340, text="Joueur1 à gagner" , anchor="nw", tag="blue")
      elif i<j:
        zone_dessin.create_text(140, 340, text=x , anchor="nw", tag="blue")
      else :
        zone_dessin.create_text(140, 340, text="egalité" , anchor="nw", tag="blue")
      
    else:
      zone_dessin.round=zone_dessin.round%2+1
      if zone_dessin.round%2 ==0:
        zone_dessin.delete("blue")
        zone_dessin.create_text(10, 5, text="Tour du Joueur1" , anchor="nw", tag="blue")
      else:
        zone_dessin.delete("blue")
        zone_dessin.create_text(10, 5, text="Tour du Joueur2" , anchor="nw", tag="blue")
  dessiner_coup_possible(zone_dessin,plateau.lister_coups_possibles(zone_dessin.round%2+1))

#ce qui me permet de relancer une partie depuis le debut

def boutonrecommencer():
  zone_dessin.nbdepassetour=0
  list=zone_dessin.liste_coups_jouer
  
  while len(list) != 0 :
      z=zone_dessin.liste_coups_jouer
      ledernier=zone_dessin.liste_coups_jouer[len(z)-1]
      e=ledernier[0]
      n=ledernier[1]
      a=zone_dessin.pion_a_retourner
      coup=Coupj(e,n,a)
      coup.methode_defaire(plateau.grille.plateau)
      zone_dessin.delete(tkinter.ALL)
      tout_dessiner(zone_dessin)
      a.remove(a[len(a)-1])
      z.remove(z[len(z)-1])
      zone_dessin.round = zone_dessin.round%2+1
      if zone_dessin.round ==2:
        zone_dessin.delete("blue")
        zone_dessin.create_text(10, 5, text="Tour du Joueur1" , anchor="nw", tag="blue")
      else:
        zone_dessin.delete("blue")
        zone_dessin.create_text(10, 5, text="Tour du Joueur2" , anchor="nw", tag="blue")
  
  plateau.grille.plateau =[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
  zone_dessin.round = 0
  tout_dessiner(zone_dessin)
  dessiner_coup_possible(zone_dessin,plateau.lister_coups_possibles(1))
  coucou()

# toute les fonction animation  sont la pour animer le changement de couleur des pions a retourner

def animation():
  r=40
  z=zone_dessin.pion_a_retourner
  ledernier=zone_dessin.pion_a_retourner[len(z)-1]
  for elt in ledernier:
    e=elt[0]
    n=elt[1]
    if zone_dessin.round%2 == 1:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="white",width="2")
    else:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="black",width="2")
def animation2():
  r=40
  z=zone_dessin.pion_a_retourner
  ledernier=zone_dessin.pion_a_retourner[len(z)-1]
  for elt in ledernier:
    e=elt[0]
    n=elt[1]
    if zone_dessin.round%2 == 1:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e+10,(r/2)+r*(n+1),(r/2)+r*(e+1)-10,(r/2)+r*n, outline="#ccc", fill="white",width="2")
    else:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e+10,(r/2)+r*(n+1),(r/2)+r*(e+1)-10,(r/2)+r*n, outline="#ccc", fill="black",width="2")

def animation3():
  
  r=40
  z=zone_dessin.pion_a_retourner
  ledernier=zone_dessin.pion_a_retourner[len(z)-1]
  for elt in ledernier:
    e=elt[0]
    n=elt[1]
    if zone_dessin.round%2 == 1:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e+20,(r/2)+r*(n+1),(r/2)+r*(e+1)-20,(r/2)+r*n, outline="#ccc", fill="white",width="2")
    else:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e+20,(r/2)+r*(n+1),(r/2)+r*(e+1)-20,(r/2)+r*n, outline="#ccc", fill="black",width="2")

def animation4():
  r=40
  z=zone_dessin.pion_a_retourner
  ledernier=zone_dessin.pion_a_retourner[len(z)-1]
  for elt in ledernier:
    e=elt[0]
    n=elt[1]
    if zone_dessin.round%2 == 1:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e+20,(r/2)+r*(n+1),(r/2)+r*(e+1)-20,(r/2)+r*n, outline="#ccc", fill="black",width="2")
    else:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e+20,(r/2)+r*(n+1),(r/2)+r*(e+1)-20,(r/2)+r*n, outline="#ccc", fill="white",width="2")


def animation5():
  r=40
  z=zone_dessin.pion_a_retourner
  ledernier=zone_dessin.pion_a_retourner[len(z)-1]
  for elt in ledernier:
    e=elt[0]
    n=elt[1]
    if zone_dessin.round%2 == 1:
      zone_dessin.create_oval ((r/2)+r*e+10,(r/2)+r*(n+1),(r/2)+r*(e+1)-10,(r/2)+r*n, outline="#ccc", fill="black",width="2")
    else:
      zone_dessin.create_oval ((r/2)+r*e+10,(r/2)+r*(n+1),(r/2)+r*(e+1)-10,(r/2)+r*n, outline="#ccc", fill="white",width="2")
def animation6():
  
  r=40
  z=zone_dessin.pion_a_retourner
  ledernier=zone_dessin.pion_a_retourner[len(z)-1]
  for elt in ledernier:
    e=elt[0]
    n=elt[1]
    if zone_dessin.round%2 == 1:
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="black",width="2")
    else :
      zone_dessin.create_rectangle ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n , outline="black", fill="#ccc")
      zone_dessin.create_oval ((r/2)+r*e,(r/2)+r*(n+1),(r/2)+r*(e+1),(r/2)+r*n, outline="#ccc", fill="white",width="2")




fen_princ = tkinter.Tk()      # Init tkinter et crée fenêtre principale

xmax = 360 ; ymax = 360
zone_dessin = tkinter.Canvas(fen_princ, bg="white", width=xmax, height=ymax)

frame_top = tkinter.Frame(fen_princ)
frame_top.pack(anchor=tkinter.NW)



b_coucou = tkinter.Button(frame_top, text="Undo", command=bouton_undo)

# ceci me permet de griser le bouton undo quand il y a pas de coup jouer

def coucou():
  if zone_dessin.liste_coups_jouer ==[]:
    b_coucou.config(state=tkinter.DISABLED)
  else :
    b_coucou.config(state=tkinter.NORMAL)









b_coucou.pack(side=tkinter.LEFT)


button = tkinter.Button(frame_top, text="RAGEQUIT?", fg="red",command=fen_princ.destroy)

button.pack(side=tkinter.LEFT)

buttoncpu = tkinter.Button(frame_top, text="CPU 9", fg="red",command=ordinateur)

buttoncpu.pack(side=tkinter.LEFT)

buttonjoueur = tkinter.Button(frame_top, text="1vs1 Octogone", fg="red",command=deuxjoueur)

buttonjoueur.pack(side=tkinter.LEFT)

passeletour = tkinter.Button(frame_top, text="PasserLeTour?", fg="red",command=passe_le_tour)

passeletour.pack(side=tkinter.LEFT)


bouttonrecommencer = tkinter.Button(frame_top, text="REVENGE?", fg="red",command=boutonrecommencer)
bouttonrecommencer.pack(side=tkinter.LEFT)

# ceci me permet de grisser les cases jouer ou ordinateur quand elles sont selectionner

def joueur_or_cpu():
  if zone_dessin.joueur == 1:
    buttonjoueur.config(state=tkinter.DISABLED)
    buttoncpu.config(state=tkinter.NORMAL)
  elif zone_dessin.ordinateur == 1 :
    buttoncpu.config(state=tkinter.DISABLED)
    buttonjoueur.config(state=tkinter.NORMAL)


zone_dessin.pack()            # Accroche la zone de dessin dans la fenêtre
zone_dessin.nbdepassetour=0
zone_dessin.ordinateur=0
zone_dessin.joueur=1
zone_dessin.plateau=plateau 
zone_dessin.liste_coups_jouer=[]
zone_dessin.pion_a_retourner=[]
zone_dessin.round = 0



plateau=zone_dessin.plateau
zone_dessin.coup = bouton_appui
tout_dessiner(zone_dessin)
dessiner_coup_possible(zone_dessin,plateau.lister_coups_possibles(zone_dessin.round%2+1))
joueur_or_cpu()





zone_dessin.bind('<Button-1>', bouton_appui )
zone_dessin.bind('<ButtonRelease-1>' , bouton_relacher)

zone_dessin.mainloop()
zone_dessin.destroy()  