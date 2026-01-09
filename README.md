Ce projet consiste en le développement d’un jeu de type Othello en Python, intégrant une interface graphique interactive réalisée à l’aide de la bibliothèque Tkinter. L’objectif principal est de proposer une implémentation complète du jeu, incluant la gestion des règles officielles, des interactions utilisateur et de plusieurs modes de jeu.

Le plateau de jeu est modélisé sous la forme d’une grille 8×8, représentée par une structure matricielle. Chaque case peut contenir un pion noir, blanc ou être vide. La logique du jeu repose sur l’identification des coups valides, définis par la possibilité de retourner au moins un pion adverse dans l’une des huit directions possibles. Cette détection est assurée par un parcours directionnel systématique autour de la case jouée, garantissant le respect strict des règles d’Othello.

Le programme propose deux modes de jeu distincts :

* un mode 1 contre 1, permettant à deux joueurs humains de s’affronter,
* un mode joueur contre ordinateur, dans lequel l’ordinateur sélectionne automatiquement un coup valide de manière aléatoire.
  Le changement de mode entraîne une réinitialisation complète de la partie afin de garantir un état de jeu cohérent.

Plusieurs fonctionnalités avancées viennent enrichir l’expérience utilisateur. Le bouton Undo permet d’annuler le dernier coup joué, en restaurant à la fois la position du pion et les pions retournés lors de ce coup. Le bouton Passer le tour gère les situations où aucun coup valide n’est disponible ; si les deux joueurs passent consécutivement leur tour, la partie prend fin automatiquement. Un bouton Revenge permet de relancer une partie depuis l’état initial, tandis que l’option Ragequit ferme immédiatement l’application.

L’interface graphique offre un retour visuel clair : affichage dynamique du plateau, indication du joueur courant, mise en évidence des coups possibles et animation du retournement des pions. Le score est mis à jour en temps réel à partir du comptage des pions présents sur la grille.

Ce projet met en évidence des compétences solides en programmation Python, en algorithmique, en programmation orientée objet, ainsi qu’en gestion d’événements graphiques. Il illustre la capacité à concevoir un jeu complet, intégrant logique métier, interface utilisateur et gestion rigoureuse des états de jeu.
