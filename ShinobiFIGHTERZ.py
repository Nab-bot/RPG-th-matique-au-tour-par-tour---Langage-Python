import random #On utilise cette bibliothèque au sein grande partie dans la génération d'ennemis, d'objects plus où moins aléatoires. 
import os #Cette bibliothèque permet effectuer des opérations à travers le système d'exploitation. Nous l'utilisons ici pour améliorer la navigation au sein du programme (essentiellement à travers nettoyerEcran)

#  ================================== GESTION VISUELLE DU JEU VIDEO ==============================

def nettoyerEcran():
    #La fonction de nettoiement des écrans sur Ios ou Windows. On a effectué des tests sur Linux et pas de soucis 
    os.system('cls' if os.name == 'nt' else 'clear')

def afficherTitreJeu():
    #Cette fonction permet d'afficher le titre du jeu. J'aimerais ajouter plus de détails visuels, mais ce sera pour plus tard. 
    nettoyerEcran()
    print("="*60)
    print("          SHINOBI FIGHTERZ ") #Le titre est dérivé du célèbre jeu de combat Dragon ball FIGHTERZ et du terme ninja en japonais qui est SHINOBI. 
    print("="*60)

def afficherSeparation():
    #A force de devoir à chaque mettre des séparation à la main à chaque fois, je me suis dit que ce serait mieux de créer une fonction qui vient tout prête avec un certain affichage. Comme ça on pourra l'appeler rapidement
    print(" " + "-"*50 + " ")


# ===================================== LANCEMENT DES MODES // =====================================  

def modeHistoire():
    #Lance mode histoire complet
    print("Lancement du mode HISTOIRE...")
    histoire = Histoire() #Il faut à tout pris créer un object pour utiliser les classes qu'on a créé ( comme en JAVA )
    histoire.menuHistoire() 


def modeArene():
    #Lance le mode arène complet
    print("Lancement du mode ARENE...")
    arene = Arene()
    arene.menuArene()


def retour(): 
    # Cette fonction est très utile pour confirmer le choix de retour des utilisateurs, A FAIRE EVOLUER 
    print("Retour au menu principal...")

def nouvellePartie(): 
    continuer = True
    while continuer :
        print("1- HISTOIRE")
        print("2- ARENE")
        print("3- RETOUR")
        try:
            choix = int(input("CHOIX : "))
        except ValueError:
            print("Erreur : vous devez entrer un nombre. ")
            choix = 0 #au cas où il y'a une valeur éronnée, le choix est initialisé a 0 et donc il ne pourra pas entrer dans le prochain if 
        if choix != 0: 
            if choix == 1:
                modeHistoire()
            elif choix == 2: 
                modeArene()
            elif choix == 3: 
                retour()
                continuer = False #On sort de la boucle uniquement en cas de retour pour quitter la nouvelle partie
            else : 
                print("Erreur, veuillez recommencer la saisie...")

def creerTechniquesDeBase():
        #Crée une liste de techniques de base pour le jeu
        techniques = []
        
        # Techniques offensives
        bouleFeu = Technique("Katon : Boule de feu suprême ", ["cheval", "tigre"], 20, 30, "offensive", "Feu")
        bouleFeu.ajouterDescription("Grande boule de feu destructrice")
        techniques.append(bouleFeu)
        
        multiClonage = Technique(" Ninpo : Multi Clonage", ["ram", "serpent", "tigre"], 15, 25, "offensive")
        multiClonage.ajouterDescription("Crée des clones pour attaquer l'ennemi")
        techniques.append(multiClonage)
        
        rasengan = Technique("Rasengan", ["ram", "serpent", "tigre", "dragon"], 35, 50, "offensive")
        rasengan.ajouterDescription("Sphère de chakra concentré dévastatrice")
        rasengan.changerRangRequis("Chunin")
        techniques.append(rasengan)
        
        # Techniques défensives
        murTerre = Technique("Doton : Mur de terre", ["serpent", "ram"], 18, 0, "defensive", "Terre")
        murTerre.ajouterDescription("Crée un mur de terre pour se protéger")
        techniques.append(murTerre)
        
        bouclierEau = Technique("Suiton : Bouclier d'eau", ["tigre", "boeuf"], 22, 0, "defensive", "Eau")
        bouclierEau.ajouterDescription("Bouclier d'eau qui absorbe les attaques")
        techniques.append(bouclierEau)
        
        # Techniques médicales
        soinBasique = Technique("Soin basique", ["boeuf", "serpent"], 25, 30, "medical")
        soinBasique.ajouterDescription("Soigne les blessures légères")
        techniques.append(soinBasique)
        
        return techniques

def trouverTechniqueParNom(nom, listeTechniques):
    for technique in listeTechniques:
        if technique.nom.lower() == nom.lower():
            return technique
    return None

#Le menu d'accueil du programme, le joueur peut à ce moment choisir de créer une nouvelle partie, charger une partie sauvegardé ou quitter le programme. Je préfère mettre le menu principal au sein d'une fonction car cela me permet de mieux lire mon code. 
def menuPrincipal():
    continuer = True
    while continuer:
        afficherTitreJeu()
        print(" " + "="*60)
        print(" " + " "*20 + "MENU PRINCIPAL")
        print(" " + "="*60)
        print(" "*15 + "1- JOUER ")
        print(" "*15 + "2- QUITTER")
        print(" " + "="*60)
        
        try:
            choix = int(input("  CHOIX : "))
        except ValueError:
            print("  Erreur : vous devez entrer un nombre.")
            input("Appuyez sur Entrée pour continuer...")
            choix = 0
        
        if choix != 0:
            if choix == 1:
                nouvellePartie()
            elif choix == 2:
                nettoyerEcran()
                print(" Merci d'avoir joué à Naruto RPG ! On se retrouvera pour la version graphique hihi..")
                print("Sayonara, ninja ! ")
                continuer = False
            else:
                print("  Erreur, veuillez recommencer la saisie...")
                input("Appuyez sur Entrée pour continuer...")



#Cette classe regroupe toutes les éléments nécessaires pour définir un ninja, il s'agit de sa carte d'identité. Elle comporte aussi des méthodes spécifiques qui permettent d'effectuer des actions basiques lors de combat attaque physique, recharge de chakra etc. 
class Ninja: 
    #Nous avons choisis d'utiliser des classes afin de pouvoir facilement structurer le jeu vidéo, il s'agit aussi d'une méthode qui nous est familière car elle est utilisé  au sein du cours de JAVA. De plus, une grande partie des sources référentielles ( autres jeux vidéos ) utilisent des classes lors du développement. 
    # La Classe Ninja permet ici de regrouper tous les éléments propres à chaque Ninja présent au sein du jeu. 
    def __init__(self,nom,pvMax=100,chakraMax= 100, endurance=100,spiritualite=100,rang="Genin"): #L'utilisation du init nous permet  ici d'assigner des valeurs aux différentes éléments de la classes quand celle-ci sera appelé (comme les constructeurs en java). Le premier rang qui est assigné est celui de Genin ( plus basse classe de ninja au sein de Naruto)

        self.nom = nom
        self.rang = rang

        #Il faut d'abord initialiser les statistiques maximales, sans ça c'est difficile de gérer les sorts de guérison. Ces statistiques sont utilisées comme références.
        self.pvMax = pvMax
        self.enduranceMax = endurance
        self.chakraMax = chakraMax
        self.spiritualiteMax = spiritualite     

        self.pvActuel = pvMax
        self.chakraActuel = chakraMax
        self.enduranceActuelle = endurance
        self.spiritualiteActuelle = spiritualite

      
        self.estVivant = True
        self.defenseActive = False
        self.bonusAttaque = 0  
 
        self.affinite = ""  #L'affinité est initialisé en étant vide et sera remplie par la suite 

        #Chaque Ninja dispose d'une liste de techniques propres à lui
        self.techniques = []
        self.inventaire = []

    #Cette fonction permet d'afficher le statut du Ninja, c'est essentiel lors des phases de combats 
    def afficherStatut(self): #Nota bene dev : Il faut toujours mettre le self au sein des méthodes d'une classe sinon on ne pourra pas utiliser les instances créées..
        #Cette fonction permet d'afficher l'état du Ninja à l'écran avec les données recueillis plus haut ( nom, rang, chakra etc.)      
        print(" --- STATUT DE " + self.nom + " ---") #simple on récupère le nom initialisé plus haut 
        print("PV: " + str(self.pvActuel) + "/" + str(self.pvMax)) #Les différentes données doivent êtres représentées en String si lors de l'affichage si elles ne le sont pas de base grace à la méthode str. C'est d'ailleurs ici qu'on voit l'utilité d'initialisé les pv max des ninja.
        print("Chakra: " + str(self.chakraActuel) + "/" + str(self.chakraMax))
        print("Endurance: " + str(self.enduranceActuelle) + "/" + str(self.enduranceMax))
        print("Spiritualité: " + str(self.spiritualiteActuelle) + "/" + str(self.spiritualiteMax))
        if self.affinite != "":
            print("Affinité: " + self.affinite) #L'affinité est très importante, car elle permet ensuite de voir quel type d'attaques le ninja doit utiliser pour maximiser ses dégats

#Cette fonction permet de gerer les attaques physiques ( Taijutsu dans Naruto ). Initialement, toutes les formes de Taijutsu avaient le même rendement en terme de dégâts. Cependant, j'ai voulu ajouter la possibilité de charger les attaques physiques avec du Chakra. Premièrement parce que cela permet d'avoir plus d'option en terme d'attaques ( sachant que les techniques offensives sont limitées à 1 par tour ) mais aussi car cela s'inscrit dans la lignée du manga Naruto     
    def attaquePhysique(self, ennemi):
        #On Verifie d'abord si le ninja est encore en vie.  
        if not self.estVivant:
            print(self.nom + " ne peut pas attaquer : il est vaincu.") #L'affichage du nom permettra à l'utilisateur d'identifier directement à qui le programme s'adresse plutôt qu'un "vous". 
            return #Le return va permettre de quitter la fonction directement sans afficher la suite qui présente les différentes options de dégats physiques
        if not ennemi.estVivant:
            print(ennemi.nom + " est déjà vaincu.")
            return 
        # Les dégats de base sont fixés à 20 points, à travers les différents test pour nous c'était le meilleur compromis pour assurer des combats ni tro
        degatsBase = 20
        degatsFinaux = degatsBase
        if getattr(self, "bonusAttaque", 0) > 0:
            degatsFinaux += self.bonusAttaque
            print("Bonus d'armement : +" + str(self.bonusAttaque) + " dégâts")
            self.bonusAttaque = 0
        coutChakra = 0
        descriptionAttaque = "attaque physiquement"

        # Ici on présente les renforcements de chakra
        print( self.nom + " prépare une attaque Taijutsu...")
        print("Dégâts de base : " + str(degatsBase))
        print("Chakra disponible : " + str(self.chakraActuel) + "/" + str(self.chakraMax))
        print("-"*30)
        print(" Renforcement chakra :")
        print("-"*30)
        print("1- Attaque normale (0 chakra)")
        print("2- Attaque renforcée (+10 dégâts pour 15 chakra)")
        print("3- Attaque puissante (+25 dégâts pour 30 chakra)")
        print("4- Attaque dévastatrice (+50 dégâts pour 55 chakra)")
        print("-"*30)
        
        #Cette section de code est assez importante, car elle représente l'un des nombreux choix que nous avons réalisés dans ce programme. En effet une mauvaise saisie est considérée comme une erreur punissable lors d'un combat. Notre objectif est d'apporter plus d'immersion à travers ce choix. 
        try:
            choix = int(input("Type d'attaque : "))
        except ValueError:
            choix = 1
    
        if choix == 2 and self.chakraActuel >= 15: #On vérifie que la quantité de chakra actuelle du ninja n'est pas inférieure au coût de l'attaque 
            degatsFinaux = degatsFinaux + 10 # aux dégats finaux (qui jusqu'à présent étaient égaux aux dégats de base) viennent s'additionner le bonus. Les points de dégats générés sont inférieurs au cout de chakra. Cette effet est intentionnel, cela mets plus d'accent sur la notion de contrôle du chakra lors d'un combat ( on ne peux pas juste spammer des attaques physiques puissantes car elles ont un coût). Aussi, j'aime beaucoup le fait que pour créer une attaque renforcée, une partie du chakra doit être perdue 
            coutChakra = 15  #Le cout total du chak
            descriptionAttaque = "frappe avec du chakra concentré"
        elif choix == 3 and self.chakraActuel >= 30:
            degatsFinaux = degatsFinaux + 25
            coutChakra = 30
            descriptionAttaque = "assène un coup puissant renforcé au chakra"
        elif choix == 4 and self.chakraActuel >= 60:
            degatsFinaux = degatsFinaux + 50 
            coutChakra = 50
            descriptionAttaque = "déchaîne une attaque dévastatrice imprégnée de chakra"
        elif choix != 1:
            if choix == 2 or choix == 3 or choix == 4:
                print("Pas assez de chakra ! Attaque normale utilisée.")
            else:
                print("(Choix erronée) Une attaque normale est utilisée car vous n'avez pas bien maitrisé votre chakra.")
        
        # Après avoir calculé le coût du chakra, ont doit le soustraire à la quantitié de chakra actuelle
        if coutChakra > 0:
            self.chakraActuel = self.chakraActuel - coutChakra
            print(self.nom + " " + descriptionAttaque + " ! (-" + str(coutChakra) + " chakra)")
        else:
            print(self.nom + " " + descriptionAttaque + " " + ennemi.nom + " !")
        
        # Pour appliquer les dégats, j'ai décider de créer une fonction séparée 
        ennemi.subirDegats(degatsFinaux)
        
        # Afficher le chakra restant si utilisé
        if coutChakra > 0:
            pourcentage = int((self.chakraActuel * 100) / self.chakraMax)
            if pourcentage >= 70:
                print("Chakra restant : " + str(self.chakraActuel) + "/" + str(self.chakraMax) + " (excellent)")
            elif pourcentage >= 40:
                print("Chakra restant : " + str(self.chakraActuel) + "/" + str(self.chakraMax) + " (correct)")
            elif pourcentage >= 20:
                print("Chakra restant : " + str(self.chakraActuel) + "/" + str(self.chakraMax) + " (faible)")
            else:
                print("Chakra restant : " + str(self.chakraActuel) + "/" + str(self.chakraMax) + " (critique !)")


    def subirDegats(self, degats):
        if degats < 0:
            degats = 0  #Pour ne pas avoir de dégats négatifs, on initialise toujours celui-ci à 0. J'ai eu des cas où certaines attaques finissaient par soigner l'adversaire à cause de certains malus 
        if self.defenseActive:
            degats = int(degats / 2) #Les dégats sont réduits de deux quand l'adversaire sont divisés par deux. Les dégats doivent êtres divisés par 3 aussi si l'attaque subit provient d'une affinité élémentaire inférieure ( ex : Les dégats d'une attaque feu sont réduits de 3 face à une défense "Eau")
            print(self.nom + " se défend ! Dégâts réduits de moitié.")
            self.defenseActive = False #La défense se désactive après le calcul des nouveaux dégats

        self.pvActuel = self.pvActuel - degats

        if self.pvActuel <= 0: #Très important, si on mets juste = à 0 cela pose problème car les pvActuels peuvent être inférieur à 0 en cas d'attaque ( ex : -20pPV après un Rasengan )
            self.pvActuel = 0 # Pour couvrir le cas mentionné juste en haut, on remet les pv à 0. 
            self.estVivant = False #Logique 
            print(self.nom + " subit " + str(degats) + " dégâts et est vaincu !")
        else:
            print(self.nom + " subit " + str(degats) + " dégâts. PV restants: " + str(self.pvActuel))

    def activerDefense(self):
        #Active la défense pour le prochain tour
        self.defenseActive = True

    def utiliserChakra(self, cout):
        #Vérifie si le ninja a assez de chakra et le consomme
        if self.chakraActuel >= cout:
            self.chakraActuel = self.chakraActuel - cout
            return True
        else:
            print(self.nom + " n'a pas assez de chakra ! (" + str(cout) + " requis, " + str(self.chakraActuel) + " disponible)")
            return False

    def rechargerChakra(self):
        #Initialisation des différents coûts pour un gain spécifique 
        coutEndurance = 20
        coutSpiritualite = 30
        gainChakra = 50
        
        # On vérifie si on a assez de ressources
        if self.enduranceActuelle >= coutEndurance and self.spiritualiteActuelle >= coutSpiritualite:
            # Recharge normale
            self.enduranceActuelle = self.enduranceActuelle - coutEndurance
            self.spiritualiteActuelle = self.spiritualiteActuelle - coutSpiritualite
            self.chakraActuel = self.chakraActuel + gainChakra
            if self.chakraActuel > self.chakraMax:
                self.chakraActuel = self.chakraMax
            print(self.nom + " recharge son chakra ! (+" + str(gainChakra) + " chakra)")
        else:
            # Recharge forcée avec perte de PV
            pertePv = 15
            gainRecharcheForcee = 25 #Vu qu'il s'agit d'une rechaque forcée les gains sont divisés par 2
            self.pvActuel = self.pvActuel - pertePv 
            
            # Ajouter chakra sans dépasser le maximum
            self.chakraActuel = self.chakraActuel + gainRecharcheForcee
            if self.chakraActuel > self.chakraMax:
                self.chakraActuel = self.chakraMax
                
            print(self.nom + " force la recharge ! (-" + str(pertePv) + " PV, +" + str(gainRecharcheForcee) + " chakra)")
            
            # Au cas où la recharge du chakra forcé entraine la suppression des derniers pv restant alors on considère que le personnage s'évanouit. Combat perdu 
            if self.pvActuel <= 0:
                self.pvActuel = 0
                self.estVivant = False
                print(self.nom + " s'épuise et s'évanouit !")

    def peutCombattre(self):
        #Vérifie si le ninja peut encore combattre#
        return self.estVivant

    def ajouterAffinite(self, element):
        #Ajoute une affinité élémentaire au ninja
        self.affinite = element
        print(self.nom + " a maintenant l'affinité " + element + " !")
    
    def changerRang(self, nouveauRang):
        ancienRang = self.rang
        self.rang = nouveauRang
        print(self.nom + " passe du rang " + ancienRang + " au rang de " + nouveauRang + " !")

# ===================================== GESTIONNAIRE DES TECHNIQUES =====================================
#Classe pour représenter une technique mudras et caractéristiques
class Technique:
 
    def __init__(self, nom, mudras, coutChakra, degats, typeTechnique, affinite=""): 
        #Informations de base de la technique
        self.nom = nom
        self.mudras = mudras  # Liste des mudras requis ex: ["cheval", "tigre"]
        self.coutChakra = coutChakra
        self.degats = degats
        self.typeTechnique = typeTechnique  # "offensive", "defensive", "medical"
        self.affinite = affinite  # "Feu", "Eau", "Terre", "Tonnerre", "Vent" ou vide( certaines techniques proviennent juste de la manipulation de chakra (ex : le Rasengan ))
        self.description = ""  # Description de la technique pour l'affichage, il s'agit d'un texte vide pour l'instant mais qui sera rempli en fonction de la technique
        self.rangRequis = "Genin"  # Rang minimum pour utiliser la technique. Cette fonctionnalité permet de ne pas avoir un personnage débutant avec une technique trop puissante..J'ai envie de créer un sens de progression au sein du programme 
    
    def afficherInfo(self):
        #Pour afficher les informations de la technique
        print(" --- TECHNIQUE: " + self.nom + " ---")
        print("Mudras: " + " + ".join(self.mudras)) #Permet d'afficher l'ensemble des mudra avec un + entre chacun pour la lecture 
        print("Coût chakra: " + str(self.coutChakra))
        print("Dégâts: " + str(self.degats))
        print("Type: " + self.typeTechnique)
        if self.affinite != "": #Lorsqu'il y'a une affinité, celle-ci doit être affiché 
            print("Affinité: " + self.affinite)
        print("Rang requis: " + self.rangRequis)
        if self.description != "":
            print("Description: " + self.description)
  
    
    def calculerDegats(self, ninjaUtilisateur):
        #Calcule les dégâts en tenant compte de l'affinité du ninja, si le ninja lance une technique qui dispose de son affinité alors il à droit a un bonus 
        degatsFinaux = self.degats
        
        #Ici on calcul les dégats supplémentaires générés par une technique offensive d'affinité similaire au joueur 
        if self.typeTechnique == "offensive":
            if ninjaUtilisateur.affinite != "" and ninjaUtilisateur.affinite == self.affinite:
            
                bonus = degatsFinaux * 25 / 100
                degatsFinaux = degatsFinaux + int(bonus)
                print("Bonus d'affinité " + self.affinite + " ! (+" + str(int(bonus)) + " dégâts)")
        
        return degatsFinaux
    
    def peutEtreUtilisee(self, ninjaUtilisateur):
        #Vérifie si le ninja peut utiliser cette technique en fonction de son rang 
        # Vérifier le chakra
        if ninjaUtilisateur.chakraActuel < self.coutChakra:
            print("Pas assez de chakra pour " + self.nom + " !")
            print("Requis: " + str(self.coutChakra) + ", Disponible: " + str(ninjaUtilisateur.chakraActuel))
            return False
        
        # Vérifier si le ninja est vivant
        if not ninjaUtilisateur.estVivant:
            print(ninjaUtilisateur.nom + " ne peut pas utiliser de technique : il est vaincu.")
            return False
        
        return True
    
    def ajouterDescription(self, description):
        #Ajoute une description à la technique
        self.description = description
    
    def changerRangRequis(self, nouveauRang):
        #Change le rang requis pour utiliser la technique
        self.rangRequis = nouveauRang


# ===================================== GESTIONNAIRE DE MUDRAS =====================================
#Cette classe permet de lister les différents gestes de mains (MUDRAS). On effectue aussi la validation des Mudras ici.
class GestionnaireMudras:
    
    def __init__(self):
        #Les différents mudras sont stockées au sein d'une liste sous formes de textes. Initialement, le nombre de signe était de 6...MAIS, encore une fois pour des raisons d'immersion nous avons choisis d'inclure les 12 signes basiques de l'univers de Naruto ( ce qui nous donne 4096 combinaisons ) 
        self.mudrasValide = [
            "ram", "serpent", "tigre", "cheval", "dragon", "boeuf", 
            "rat", "oiseau", "singe", "lievre", "chien", "coq"
        ]
    

    def mudraValide(self, mudra):
        m = mudra.lower()          # avant validation, on met le mudra à valider en minuscule 
        trouve = False             # on part du principe que ce n'est pas valide

        for i in self.mudrasValide: #On parcours la liste des 12 mudras valides 
            if i == m:
                trouve = True      
                break              # On sors de la boucle car on a vérif

        return trouve
    

    def validationSequence (self, technique, mudraSaisies):
        #Valide la séquence de Mudras saisie pour une technique donnée.
    
         # On nettoie la saisieen mettant tout en minuscule
        texte = mudraSaisies.lower()
        #On enlève les espace ( ex : cheval     +     tigre  devrait passer )
        texte = texte.replace(" ", "")

        
        morceaux = texte.split("+") #On découpe la chaine en morceau délimités par les +, les morceaux sont ensuite mit dans une liste 
        
        ##Pour stocker les Mudras saisis j'ai initialisé une autre liste finale
        listeMudras = []
        for m in morceaux:
            if m != "":#Des fois on a une erreur lorsque l'utilisateur tape deux "+" ( chien ++ cheval), donc on a un morceau de la liste qui dispose de "", là on demande au programme de continuer si jamais on tombe sur cette occurence
                listeMudras.append(m)

        ## parcours la liste de Mudra créé pour vérifier que chaque mudra existe
        for m in listeMudras:
            if not self.mudraValide(m):
                return False

        # On vérifie que le nombre de mudra de la liste correspond au meme nombre de mudra de la technique 
        if len(listeMudras) != len(technique.mudras):
            return False

        # 3) L'ordre doit correspondre
        i = 0
        while i < len(listeMudras):
            if listeMudras[i] != technique.mudras[i].lower():
                return False
            i = i + 1

        return True
    
    # ===================================== GESTION DES OBJETS  =====================================
class Objet:
    #Classe pour représenter un objet avec ses effets et caractéristiques
    def __init__(self, nom, typeObjet, effetPrincipal, valeur, description=""):
        #Informations de base
        self.nom = nom
        self.type = typeObjet  # On aura trois type d'objets : "consommable", "equipement", "special"
        self.effetPrincipal = effetPrincipal  #Ces objets peuvent avoir trois qualités principales : regain de PV, de chakra ou boost d'attaque. 
        self.valeur = valeur  # Puissance de l'effet
        self.description = description
        
        #Propriétés avancées
        self.rarete = "commun"  # commun, rare, legendaire
        self.utilisableCombat = True  # Peut être utilisé en combat
        self.effetsSecondaires = []  # Liste d'effets bonus
        
    def afficherInfo(self):

        print(" --- OBJET: " + self.nom + " ---")
        print("Type: " + self.type)
        print("Effet: " + self.effetPrincipal)
        if self.valeur > 0:
            print("Puissance: +" + str(self.valeur))
        print("Rareté: " + self.rarete)
        if self.description != "":
            print("Description: " + self.description)
        if not self.utilisableCombat:
            print(" Non utilisable en combat")
        print("")
    
    def peutEtreUtilise(self, ninja, enCombat=False):
        #Vérifie si l'objet peut être utilisé
        if enCombat and not self.utilisableCombat:
            print("Cet objet ne peut pas être utilisé en combat !")
            return False
            
        if not ninja.estVivant:
            print("Impossible d'utiliser un objet : ninja K.O.")
            return False
            
        return True
    
    def utiliser(self, ninja):
        #Cette fonction permet au ninja d'utiliser un des objets sur le ninja
        if not self.peutEtreUtilise(ninja):
            return False
            
        appliqueEffet = False
        
        if self.effetPrincipal == "soinPv":
            avant = ninja.pvActuel
            ninja.pvActuel = ninja.pvActuel + self.valeur
            if ninja.pvActuel > ninja.pvMax:
                ninja.pvActuel = ninja.pvMax
            gain = ninja.pvActuel - avant
            print(ninja.nom + " utilise " + self.nom + " et récupère " + str(gain) + " PV !")
            appliqueEffet = True
            
        elif self.effetPrincipal == "gainChakra":
            avant = ninja.chakraActuel
            ninja.chakraActuel = ninja.chakraActuel + self.valeur
            if ninja.chakraActuel > ninja.chakraMax:
                ninja.chakraActuel = ninja.chakraMax
            gain = ninja.chakraActuel - avant
            print(ninja.nom + " utilise " + self.nom + " et récupère " + str(gain) + " chakra !")
            appliqueEffet = True
            
        elif self.effetPrincipal == "gainEndurance":
            avant = ninja.enduranceActuelle
            ninja.enduranceActuelle = ninja.enduranceActuelle + self.valeur
            if ninja.enduranceActuelle > ninja.enduranceMax:
                ninja.enduranceActuelle = ninja.enduranceMax
            gain = ninja.enduranceActuelle - avant
            print(ninja.nom + " utilise " + self.nom + " et récupère " + str(gain) + " endurance !")
            appliqueEffet = True
            
        elif self.effetPrincipal == "gainSpiritualite":
            avant = ninja.spiritualiteActuelle
            ninja.spiritualiteActuelle = ninja.spiritualiteActuelle + self.valeur
            if ninja.spiritualiteActuelle > ninja.spiritualiteMax:
                ninja.spiritualiteActuelle = ninja.spiritualiteMax
            gain = ninja.spiritualiteActuelle - avant
            print(ninja.nom + " utilise " + self.nom + " et récupère " + str(gain) + " spiritualité !")
            appliqueEffet = True
            
        elif self.effetPrincipal == "soinComplet":
            ninja.pvActuel = ninja.pvMax
            ninja.chakraActuel = ninja.chakraMax
            ninja.enduranceActuelle = ninja.enduranceMax
            ninja.spiritualiteActuelle = ninja.spiritualiteMax
            ninja.estVivant = True
            print(ninja.nom + " utilise " + self.nom + " et récupère toutes ses forces !")
            appliqueEffet = True

        else:
            print("Effet d'objet non implémenté : " + self.effetPrincipal)
            return False
        
        for i in self.effetsSecondaires:
            self.appliquerEffetSecondaire(ninja, i)
            
        return appliqueEffet
    
    def appliquerEffetSecondaire(self, ninja, effet):
        if effet == "defenseTemporaire":
            ninja.defenseActive = True
            print("Bonus : Défense activée pour le prochain tour !")
        elif effet == "regeneration":
            print("Bonus : Régénération légère pendant 3 tours !") 
    
    def ajouterEffetSecondaire(self, effet):
        if effet not in self.effetsSecondaires:
            self.effetsSecondaires.append(effet)
    
    def changerRarity(self, nouvelleRarete):
        #Change la rarete de l'objet
        self.rarete = nouvelleRarete

def creerObjetsDeBase():
    objets = []
    # === OBJETS CONSOMMABLES ===
    
    #Pour les objets de type Soin 
    potionSoin = Objet("Potion de soin", "consommable", "soinPv", 30, "Petite potion commune à tous les shinobi qui soigne les blessures légères")
    objets.append(potionSoin)
    
    grandePotionSoin = Objet("Grande potion de soin", "consommable", "soinPv", 60,"Une potion puissante du clan Uzumaki qui soigne les blessures graves")
    grandePotionSoin.changerRarity("rare")
    objets.append(grandePotionSoin)
    
    # Pour les objets de type Chakra
    pilluleMilitaire = Objet("Pilule militaire", "consommable", "gainChakra", 30,"Pilule commune qui restaure rapidement le chakra")
    objets.append(pilluleMilitaire)
    
    piluleChakraSupreme = Objet("Pilule de chakra suprême", "consommable", "gainChakra", 60,"Pilule rare du clan Akimichi qui restaure massivement le chakra")
    piluleChakraSupreme.changerRarity("rare")
    objets.append(piluleChakraSupreme)
    
    # Endurance
    rationNinja = Objet("Ration de ninja", "consommable", "gainEndurance", 25,"Nourriture énergétique qui restaure l'endurance")
    objets.append(rationNinja)
    
    # Spiritualité 
    encensMediation = Objet("Encens de méditation", "consommable", "gainSpiritualite", 20,"Encens qui apaise l'esprit et restaure la spiritualité")
    objets.append(encensMediation)
    
    # === OBJETS SPÉCIAUX ===
    
    potionGuerriere = Objet("Potion du guerrier", "consommable", "soinPv", 25,"Potion qui soigne et renforce temporairement")
    potionGuerriere.ajouterEffetSecondaire("defenseTemporaire")
    potionGuerriere.changerRarity("rare")
    objets.append(potionGuerriere)
    
    # === EQUIPEMENT NINJA ===
    
    kunai = Objet("Kunai", "equipement", "boostAttaque", 5,"Couteau de lancer standard des ninjas")
    kunai.utilisableCombat = True 
    objets.append(kunai)
    
    shuriken = Objet("Fuma Shuriken", "equipement", "boostAttaque", 3,"Étoile de lancer traditionnelle")
    shuriken.utilisableCombat = True  
    objets.append(shuriken)
    
    return objets


def genererObjetAleatoire():

    objetBase = creerObjetsDeBase()
    rand = random.randint(1,100)
    if rand <= 60:
        objetsCommuns = []
        for objet in objetBase:
            if objet.rarete == "commun":
                objetsCommuns.append(objet)
        return random.choice(objetsCommuns)

    elif rand <= 85:
        objetsRares = []
        for objet in objetBase:
            if objet.rarete == "rare":
                objetsRares.append(objet)
        
        if len(objetsRares) > 0:
            return random.choice(objetsRares)
        else:
            return random.choice(objetBase)

    else:
        objetsLegendaires = []
        for objet in objetBase:
            if objet.rarete == "legendaire":
                objetsLegendaires.append(objet)
        
        if len(objetsLegendaires) > 0:
            return random.choice(objetsLegendaires)
        else:
            return random.choice(objetBase)



# =================== CLASSE DE GESTION DES COMBATS ===========================
#La classe la plus importante...la plus longue aussi....Cette classe permet de gérer les combats tours par tour du jeu. 
class Combat:
    def __init__(self, joueur, ennemi, techniquesDisponibles=None): #On initialise le constructeur avec les éléments principaux du combat : le joueur, l'ennemi et les techniques utilisées ( nécessaires lors de l'appel du constr)
        #Initialisation du combat
        self.joueur = joueur
        self.ennemi = ennemi
        self.techniquesDisponibles = techniquesDisponibles
        self.gestionnaireMudras = GestionnaireMudras() #Important pour utiliser les fonctions permettant de valider les mudras utilisées lors du combat 
        
        #État du combat
        self.tourActuel = 1
        self.combatTermine = False 
        self.vainqueur = None
        
        #Je n'ai pas envie d'avoir un jouer/ennemi qui puisse utiliser un nombre infini de techniques lors d'un tour.
        
        self.techniquesDefensiveUtilise = 0  # Max 2 par tour
        self.techniquesOffensiveUtilise = False  # Max 1 par tour
        self.techniquesMedicaleUtilise = 0  # Limiter le spam de soin
        
        #Lors de nos tests, on a eu un combat ou l'adversaire n'arrêtait pas d'utiliser des techniques médicales...Le combat était interminable, cette donnée va nous permettre de brider l'ennemi pour eviter cela ( donc une seule technique médicale par combat )
        self.maxSoinCombat = 1  # Maximum 1 soin par combat

        #Historique du combat pour affichage
        self.historique = []
        
    
    def afficherStatutCombat(self):
        #Affiche l'état actuel du combat. Vu qu'on est dans un jeu qui utilise l'invite de commande comme interface il nous faut bien présenter les différents statuts 
        nettoyerEcran()#Au sein de nos tests, j'ai remarqué qu'il était assez difficile de suivre le statut du Combat avec tout l'historique des actions en haut. On nettoie ici avec cette fonction ( c'est la raison principale pour laquelle nous utilisons la bibliothèque os )
        
        # Affichage du titre du combat 
        print("="*50)
        print("                   COMBAT NINJA ")
        print("                   TOUR " + str(self.tourActuel))
        print("="*50)

        afficherSeparation() 
        
        # Interface en deux colonnes
        print("JOUEUR: " + self.joueur.nom + " | ENNEMI: " + self.ennemi.nom)
        print("PV: " + str(self.joueur.pvActuel) + "/" + str(self.joueur.pvMax)  + " | PV: " + str(self.ennemi.pvActuel) + "/" + str(self.ennemi.pvMax))
        print("Chakra: " + str(self.joueur.chakraActuel) + "/" + str(self.joueur.chakraMax) + " | Chakra: " + str(self.ennemi.chakraActuel) + "/" + str(self.ennemi.chakraMax))
        print("Spiritualité : " + str(self.joueur.spiritualiteActuelle) + "/"+ str(self.joueur.spiritualiteMax)+" | Spiritualité : " + str(self.ennemi.spiritualiteActuelle)+" / " + str(self.ennemi.spiritualiteMax))
        print("Endurance : " + str(self.joueur.enduranceActuelle) + "/"+ str(self.joueur.enduranceMax)+" | Endurance : " + str(self.ennemi.enduranceActuelle)+" / " + str(self.ennemi.enduranceMax))
        print("Rang: " + self.joueur.rang + " | Rang: " + self.ennemi.rang)
        
        if self.joueur.affinite != "" or self.ennemi.affinite != "":
            print("Affinite: "+self.joueur.affinite+"| Affinite: "+self.ennemi.affinite)
        
        #Pour tracker les états défensifs de l'ennemi et du joueur, j'ai choisi de créer une liste qui ajoute les états défensif du joueur ou de l'ennemi après vérification
        etats = []
        if self.joueur.defenseActive: #Vérification de l'état grace à defenseActive
            etats.append( self.joueur.nom + " EN DÉFENSE")
        if self.ennemi.defenseActive:
            etats.append( self.ennemi.nom + " EN DÉFENSE")
        
        if etats:#On affiche le contenu de la liste et donc les personnes en état défensif 
            print(" ÉTATS SPÉCIAUX:")
            for etat in etats:
                print(etat)
        
        afficherSeparation() 

    
    def afficherMenuActions(self):
        #Affiche le menu des actions disponibles pour le joueur
        print(" ACTIONS DISPONIBLES:")
        print("1- Taijutsu")
        print("2- Utilisation de Ninjutsu / Genjustu")
        print("3- Utilisation de l'inventaire")
        print("4- Recharger chakra")
        print("5- Fuite ( Attention, une sanction sera prélevé en cas de fuite)")
        print("6- Afficher les Ninjutsu/Genjutsu disponibles")
        print("7- Terminer le tour") #Initialement je voulais que le tour se déclenche automatique après une action spécifique. Mais après des essais sur plusieurs amis on remarque qu'ils sont perdu...je préfère donc qu'ils aient le contrôlee sur la fin de leurs tours
        print("0- Abandonner le combat")

    def tourJoueur(self):
        if not self.joueur.estVivant:
            return False
        
        # Il faut réinitialiser les compteur au début de chaque tour
        self.techniquesDefensiveUtilise = 0
        self.techniquesOffensiveUtilise = False

        tourTermine = False
        while not tourTermine and not self.combatTermine:
            
            # Le début de chaque tour commence par un affichage du Statut du Combat
            self.afficherStatutCombat()
            
            # Afficher les limitations du tour
            print("ÉTAT DU TOUR:")
            #Les tests montrent que souvent les utilisateurs ne savent pas si ils ont déjà utilisés une technique offensive pendant le tour.Donc j'ai ajouté ce code 
            if self.techniquesOffensiveUtilise:
                print("Attaque offensive utilisée") 
            else:
                print(" Attaque offensive disponible")
            
            print(" Défenses utilisées : " + str(self.techniquesDefensiveUtilise) + "/2")
            
            afficherSeparation()
            
            # Menu d'actions
            self.afficherMenuActions()
            
            try:
                choix = int(input("  Choisissez une action : "))
            except ValueError:
                self.afficherErreur("Vous devez entrer un nombre.")
                continue
            
            # On traite ensuite l'entrée valide de l'utilisateur
            if choix == 1:
                if not self.techniquesOffensiveUtilise:
                    self.executerAction("TAIJUTSU")
                    self.joueur.attaquePhysique(self.ennemi) #Le joueur exécute son attaque sur l'ennemi, le tracker des techniques offensives s'active juste après 
                    self.techniquesOffensiveUtilise = True
                else:
                    self.afficherErreur("Vous avez déjà utilisé votre attaque offensive ce tour !")
            
            elif choix == 2:
                self.executerAction("NINJUSTU /GENJUTSU ")
                self.menuTechniques()
            
            elif choix == 3:
                self.executerAction("INVENTAIRE ")
                self.menuObjets()
            
            elif choix == 4:
                # Recharge chakra
                self.executerAction("RECHARGE CHAKRA")
                self.joueur.rechargerChakra()
                self.afficherChakraRestant()
            
            elif choix == 5:
                # Fuite
                self.executerAction("TENTATIVE DE FUITE")
                if self.tentativeFuite():
                    self.combatTermine = True
                    return False
            
            elif choix == 6:
                self.afficherTechnique()
            
            elif choix == 7:
                self.executerAction("FIN DU TOUR")
                print("Vous terminez votre tour.")
                tourTermine = True
            
            elif choix == 0:
          
                if self.confirmerAbandon():
                    self.combatTermine = True
                    self.vainqueur = self.ennemi
                    return False
            
            else:
                self.afficherErreur("Choix invalide !")

            if not self.ennemi.estVivant:
                self.combatTermine = True
                self.vainqueur = self.joueur
                return False
            
            if self.verifierTourComplete():
                self.executerAction("ACTIONS ÉPUISÉES")
                print("Toutes vos actions sont épuisées. Fin du tour.")
                tourTermine = True
            
            if not tourTermine:
                input(" Appuyez sur Entrée pour continuer...")
        
        return True

    
    def menuTechniques(self):
            #Menu pour choisir le type de technique
        if len(self.joueur.techniques) == 0:
            print("Vous ne connaissez aucun Ninjutsu...")
            return
        
        print(" " + "="*40)
        print("           NINJUTSU / GENJUTSU ")
        print("="*40)
        print("1- Ninjutsu offensifs")
        print("2- Ninjutsu défensifs") 
        print("3- Ninjutsu médicaux")
        print("0- Retour")
        
        try:
            choix = int(input("Type de technique : "))
        except ValueError:
            print("Erreur de saisie !")
            return
        
        if choix == 0:
            return
        elif choix == 1:
            self.menuTechniquesParType("offensive")
        elif choix == 2:
            self.menuTechniquesParType("defensive")
        elif choix == 3:
            self.menuTechniquesParType("medical")
        else:
            print("Choix invalide !")

    def menuTechniquesParType(self, typeTechnique):
        #Menu pour saisir les mudras d'un type de technique spécifique
        
        techniquesDuType = [] #On initialise une liste vide 
        for t in self.joueur.techniques:#On parcours l'ensemble des techniques du joueur 
            if t.typeTechnique == typeTechnique: #Une fois qu'on trouve une technique qui a aussi le même type que celui passé en argument alors on l'ajoute à la liste 
                techniquesDuType.append(t)
        
        if len(techniquesDuType) == 0: #Si aucune des techniques ne correspond au typeTechnique entré en argument alors le tableau est vide donc pas de technique de ce type
            print("Vous ne connaissez aucune technique " + typeTechnique + " !")
            return
        
        #Au cas où la technique est offensive, on doit d'abord vérifier qu'aucune autre technique n'a été utilisée au préalable. Pour les techniques défensives, on vérifies qu'on a pas dépassé le compteur
        if typeTechnique == "offensive" and self.techniquesOffensiveUtilise:
            print("Vous avez déjà utilisé votre attaque offensive ce tour !")
            return
        elif typeTechnique == "defensive" and self.techniquesDefensiveUtilise >= 2:
            print("Vous avez déjà utilisé vos 2 défenses ce tour !")
            return
        
        print(" --- TECHNIQUES " + typeTechnique.upper() + " ---")
        print("Techniques disponibles :")
        for technique in techniquesDuType: #On affiche l'ensemble des techniques à travers cette boucle 
            print("- " + technique.nom + " (" + " + ".join(technique.mudras) + ") - " + str(technique.coutChakra) + " chakra") 
        
        print(" Saisissez les mudras de la technique (ex: cheval+tigre)")
        print("Ou tapez 'retour' pour annuler")
        
        saisie = input("Mudras: ")
        saisie = saisie.strip()
        saisie = saisie.lower()
        
        if saisie == "retour" or saisie == "":
            return

        techniqueTrouve = None 
        for technique in techniquesDuType:
            if self.gestionnaireMudras.validationSequence (technique, saisie):
                techniqueTrouve = technique
                break
        
        if techniqueTrouve is not None:
            self.utiliserTechnique(techniqueTrouve)
        else:
            print("Séquence de mudras inconnue pour les techniques " + typeTechnique + " !")
            print("Vérifiez les mudras disponibles ci-dessus.")
          
        
    def utiliserTechnique(self, technique):
        # Il faut d'abord vérifier si la technique peut être utilisée, sinon on quitte la fonction avec un return 
        if not technique.peutEtreUtilisee(self.joueur):
            return

        #Si la technique peut être utilisée alors on consomme le chakr 
        self.joueur.utiliserChakra(technique.coutChakra)

        # Les techniques s'exécutent en fonction du type 
        if technique.typeTechnique == "offensive":
            degats = technique.calculerDegats(self.joueur)
            print(self.joueur.nom + " utilise " + technique.nom + " !")
            self.ennemi.subirDegats(degats)
            self.techniquesOffensiveUtilise = True

        elif technique.typeTechnique == "defensive":
            print(self.joueur.nom + " utilise " + technique.nom + " !")
            self.joueur.activerDefense()
            self.techniquesDefensiveUtilise += 1

        elif technique.typeTechnique == "medical":
            soin = technique.degats 
            print(self.joueur.nom + " utilise " + technique.nom + " !")
            nouveau = self.joueur.pvActuel + soin
            if nouveau > self.joueur.pvMax: #Il faut inclure un plafond pour ne pas que l'utilisateur se retrouve avec plus de pv que le maximum 
                self.joueur.pvActuel = self.joueur.pvMax
            else:
                self.joueur.pvActuel = nouveau
            print("+" + str(soin) + " PV récupérés !")

        self.afficherChakraRestant()


    def afficherChakraRestant(self):
    
        chakraActuel = self.joueur.chakraActuel
        chakraMax = self.joueur.chakraMax
        pourcentage = int((chakraActuel * 100) / chakraMax)
        
        if pourcentage >= 70:
            print("- " + self.joueur.nom + " dispose encore de beaucoup de chakra (" + str(chakraActuel) + "/" + str(chakraMax) + ")")
        elif pourcentage >= 40:
            print("- " + self.joueur.nom + " a un niveau de chakra correct (" + str(chakraActuel) + "/" + str(chakraMax) + ")")
        elif pourcentage >= 20:
            print("- " + self.joueur.nom + " manque de chakra (" + str(chakraActuel) + "/" + str(chakraMax) + ")")
        else:
            print("- " + self.joueur.nom + "  a peu de chakra restant ! (" + str(chakraActuel) + "/" + str(chakraMax) + ")")


    def menuObjets(self):#Permet d'afficher l'ensemble des objets de l'utilisateur lors du combat 
        
        if len(self.joueur.inventaire) == 0:#L'inventaire est vide au début de chaque partie de type Arène 
            print("Votre inventaire est vide !")
            return False

        print(" INVENTAIRE (objets utilisables en combat):")
        objetsUtilisables  = [] #L'ensemble des objets utilisables du joueur seront stockés au sein d'une liste 
        
        for i in range(len(self.joueur.inventaire)):#On parcours l'inventaire du joueur et on affiche les objets qui sont à sa disposition à l'écran 
            objet = self.joueur.inventaire[i]
            if isinstance(objet, Objet): #On doit d'abord vérifier que l'objet appartient bien à la classe objet 
                if objet.utilisableCombat:
                    objetsUtilisables.append((i, objet))
                    print(str(len(objetsUtilisables )) + ". " + objet.nom) #Il a fallu ajouter cette partie pour aussi d'afficher de copie d'un objet que l'utilisateur a 
                    if objet.valeur > 0:
                        print("   Effet: +" + str(objet.valeur) + " " + objet.effetPrincipal.replace("_", " "))
            else:
                if objet == "Pilule militaire":
                    objetsUtilisables .append((i, objet))
                    print(str(len(objetsUtilisables )) + ". " + str(objet))
        
        if len(objetsUtilisables ) == 0:
            print("Aucun objet utilisable en combat !")
            return False
        
        try:
            choix = int(input("Choisir un objet (Appuyez sur 0 pour retourner en arrière): "))
        except ValueError:
            print("Erreur : vous devez entrer un nombre.")
            return False
        
        if choix == 0:
            return False #On quitte le menu objet en cas de retour 
        if choix < 1 or choix > len(objetsUtilisables ):
            print("Choix invalide.")
            return False #Idem pour une mauvaise sélection d'obet 

        indexInventaire, objet = objetsUtilisables [choix - 1]
        
        #Finalement il faut aussi consommer l'objet et l'effacer de l'inventaire du joueur 
        if isinstance(objet, Objet):
            if objet.utiliser(self.joueur):
                if objet.type == "consommable":
                    del self.joueur.inventaire[indexInventaire]
                return True
        else:
            if objet == "Pilule militaire":
                avant = self.joueur.chakraActuel
                self.joueur.chakraActuel = self.joueur.chakraActuel + 30
                if self.joueur.chakraActuel > self.joueur.chakraMax:
                    self.joueur.chakraActuel = self.joueur.chakraMax
                gain = self.joueur.chakraActuel - avant
                print("Vous utilisez une Pilule militaire. +" + str(gain) + " chakra.")
                del self.joueur.inventaire[indexInventaire]
                return True
        
        return False

        
    def tentativeFuite(self):
        print(self.joueur.nom + " tente de fuir...")
        chancesFuite = random.randint(1, 100)

        if chancesFuite<= 70:
            print("Fuite réussie !")
            
            #La fuite entraine automatiquement la perte de loot. Honnêtement, je pense à laisser de côté l'abandon au profit de la fuite (le joueur ne peut pas abandonner un combat mais seulement fuir )
            if len(self.joueur.inventaire) > 0:
                i = random.randint(0, len(self.joueur.inventaire) - 1)
                objetPerdu = self.joueur.inventaire[i]
                print("Vous avez perdu : " + str(objetPerdu))
                # on enlève exactement cet objet-là
                del self.joueur.inventaire[i]
            else: #Si le joueur fuis alors qu'il n'a rien dans son inventaire alors il reçoit des sanctions : pour l'instant je calibre ça à de l'endurance et de la spiritualité mais je pense que je risque d'ajouter des sanctions sur les points de vie
                self.joueur.enduranceActuelle = self.joueur.enduranceActuelle - 10
                self.joueur.spiritualiteActuelle = self.joueur.spiritualiteActuelle - 10
                print("Vous perdez 10 points de spiritualité.")
                print("Vous perdez 10 points d'endurance.")
                if self.joueur.spiritualiteActuelle <= 0 or self.joueur.enduranceActuelle <= 0:
                    self.joueur.spiritualiteActuelle = 0
                    self.joueur.enduranceActuelle = 0 
                    print("...GAME OVER !")
                    self.joueur.estVivant = False
            
            return True
        else:
            print("Impossible de fuir !")
            return False
        


    def verifierTourComplete(self):
        #Permet de vérifier à chaque fois si le joueur n'a pas épuisé son lot de techniques défensives ou sa technique offensive
        offensiveEpuisee = self.techniquesOffensiveUtilise
        defensiveEpuisee = self.techniquesDefensiveUtilise >= 2
        return offensiveEpuisee and defensiveEpuisee
    


    def tourEnnemi(self):
        #Cette fonction permet de gérer ce qu'il se passe après le tour de l'utilisateur. On gère notre IA 
        if not self.ennemi.estVivant:#On vérifie d'abord si l'ennemi est vivant 
            return

        print(" --- TOUR DE " + self.ennemi.nom + " ---")
        #============================ CHANCES DE FUITE DE L'IA =================#
        # Si PV bas (moins de 45%), l'ennemi doit essayer de fuir ou se défendre
        pourcentagePv = (self.ennemi.pvActuel * 100) / self.ennemi.pvMax
        if pourcentagePv < 20:
            chanceFuite = random.randint(1,100)
            if chanceFuite <= 20:
                print(self.ennemi.nom + " tente de fuir...")
                if chanceFuite <= 10: #Les chances de fuite au départ étaient beaucoup trop élevées donc j'ai baissé celles-ci considérablement. 
                    print(self.ennemi.nom + " s'enfuit du combat !")
                    self.combatTermine = True
                    self.vainqueur = self.joueur
                    return
                else:
                    print(self.ennemi.nom + " n'arrive pas à fuir !")
            else:
                self.ennemi.activerDefense()
            
        #======================== CHANCES DE RECHARGE CHAKRA DE l'IA ============# 
        
        # Si le  chakra bas (moins de 30%), l'ennemi va essayer de recharger son chakra
        pourcentageChakra = (self.ennemi.chakraActuel * 100) / self.ennemi.chakraMax
        chanceRecharge = random.randint(1, 100)
        if pourcentageChakra < 30:
            if chanceRecharge <= 60:
                self.ennemi.rechargerChakra()
                return
        
        #===================== EXECUTION DES TECHNIQUES ( Pour changer les comportements de l'IA c'est ici )
        #Il faut d'abord récupérer les techniques de l'ennemi en fonction de leurs types. Ca nous donne plus de contrôle sur leurs actions
        techniquesOffensives = []
        techniquesDefensives = []
        techniquesMedicales  = []

        for t in self.ennemi.techniques:
            if t.typeTechnique == "offensive":
                techniquesOffensives.append(t)
            elif t.typeTechnique == "defensive":
                techniquesDefensives.append(t)
            elif t.typeTechnique == "medical":
                techniquesMedicales.append(t)

        actionChoisie = None
        
        

        #SI les PV sont très bas (< 30%) ET que l'ennemi peut se soigner alors il a 50% de chance de le faire 
        if pourcentagePv < 30 and self.peutUtiliserMedical(techniquesMedicales, pourcentagePv):
            chanceSoin = random.randint(1, 100)
            if  chanceSoin <= 50:
                actionChoisie = "medical"

        if actionChoisie is None and len(techniquesDefensives) > 0:
            chanceDefence = random.randint(1, 100)
            if chanceDefence <= 20:
                actionChoisie = "defensive"

        if actionChoisie is None and len(techniquesOffensives) > 0:
            chanceAttaque = random.randint(1, 100)
            if chanceAttaque <= 70:
                actionChoisie = "offensive"
    
        if actionChoisie is None:
            actionChoisie = "physique"

        #Après déterminé de l'action choisie, celle ci doit être exécutée, 
        if actionChoisie == "offensive":
            technique = random.choice(techniquesOffensives)#On sélectionne une technique offensive aléatoir dans le catalogue de l'ennemi.  
            if technique.peutEtreUtilisee(self.ennemi):
                print(self.ennemi.nom + " utilise " + technique.nom + " !")
                self.ennemi.utiliserChakra(technique.coutChakra)
                degats = technique.calculerDegats(self.ennemi)
                self.joueur.subirDegats(degats)
            else:
                self.attaquePhysiqueEnnemi()

        elif actionChoisie == "defensive":
            technique = random.choice(techniquesDefensives)
            if technique.peutEtreUtilisee(self.ennemi):
                print(self.ennemi.nom + " utilise " + technique.nom + " !")
                self.ennemi.utiliserChakra(technique.coutChakra)
                self.ennemi.activerDefense()
            else:
                self.attaquePhysiqueEnnemi()

        elif actionChoisie == "medical":
            technique = random.choice(techniquesMedicales)
            if technique.peutEtreUtilisee(self.ennemi):
                print(self.ennemi.nom + " utilise " + technique.nom + " !")
                self.ennemi.utiliserChakra(technique.coutChakra)
                soin = technique.degats
                self.ennemi.pvActuel = self.ennemi.pvActuel + soin
                if self.ennemi.pvActuel > self.ennemi.pvMax:
                    self.ennemi.pvActuel = self.ennemi.pvMax
                print(self.ennemi.nom + " se soigne de " + str(soin) + " PV !")

                self.  techniquesMedicaleUtilise += 1
                if self.  techniquesMedicaleUtilise >= self.maxSoinCombat:
                    print("(" + self.ennemi.nom + " ne peut plus se soigner dans ce combat)")
            else:
                self.attaquePhysiqueEnnemi()

        else:  # "physique"
            self.attaquePhysiqueEnnemi()
            
    def peutUtiliserMedical(self, techniquesMedicales, pourcentagePv):
        if len(techniquesMedicales) == 0:
            return False

        if self.  techniquesMedicaleUtilise >= self.maxSoinCombat:
            return False

        if pourcentagePv >= 50: #J'ai eu un cas où l'ennemi arrêtait pas de se soigner alors qu'il avait 80% de ses pv totaux. Donc pas de technique médicale tant qu'il n'a pas au moins 50% de pv en moins 
            return False
        
        for t in techniquesMedicales:
            if self.ennemi.chakraActuel >= t.coutChakra:
                return True

        return False


    def attaquePhysiqueEnnemi(self):
        degatsBase = 20
        degatsFinaux = degatsBase
        coutChakra = 0
        description = "attaque physiquement"
        
        
        pourcentageChakra = (self.ennemi.chakraActuel * 100) / self.ennemi.chakraMax
        
        if pourcentageChakra >= 80 and self.ennemi.chakraActuel >= 50:
            chanceCoup = random.randint(1,100)
            if chanceCoup <= 30:
                degatsFinaux += 50
                coutChakra = 50
                description = "déchaîne une attaque dévastatrice imprégnée de chakra"
        elif pourcentageChakra >= 60 and self.ennemi.chakraActuel >= 30:
            chanceCoup = random.randint(1,100)
            if chanceCoup <= 40:
                degatsFinaux += 25
                coutChakra = 30
                description = "assène un coup puissant renforcé au chakra"
        elif pourcentageChakra >= 40 and self.ennemi.chakraActuel >= 15:
            chanceCoup = random.randint(1,100)
            if  chanceCoup <= 55:
                degatsFinaux += 10
                coutChakra = 15
                description = "frappe avec du chakra concentré"
    
        if coutChakra > 0:
            self.ennemi.chakraActuel -= coutChakra
            print(self.ennemi.nom + " " + description + " ! (-" + str(coutChakra) + " chakra)")
        else:
            print(self.ennemi.nom + " " + description + " " + self.joueur.nom + " !")
        
        self.joueur.subirDegats(degatsFinaux)


    def verifierFinCombat(self):
        if not self.joueur.estVivant:
            self.combatTermine = True
            self.vainqueur = self.ennemi
            print(" " + self.joueur.nom + " est vaincu !")
            return True
        
        if not self.ennemi.estVivant:
            self.combatTermine = True
            self.vainqueur = self.joueur
            print(" " + self.ennemi.nom + " est vaincu !")
            return True
        
        return False
    
    def lancerCombat(self):
        print(" " + "="*60)
        print("             DEBUT DU COMBAT")
        print("         " + self.joueur.nom + " VS " + self.ennemi.nom)
        print("="*60)
        
        #Boucle principale du combat
        while not self.combatTermine:#Tant que le combat n'est oas terminé on répète cette boucle. A chaque tour on commence par afficher le statut du combat -> le joueur agi en premier, a la fin de son tour on vérifie si le combat n'est pas terminé  -> c'est au tour de l'ennemi, a la fin de son tour on vérifie encore qu'il n'y a pas de fin de combat -> On passe au tour suivant 
            self.afficherStatutCombat()
            if self.tourJoueur():
                #On vérifie d'abord si aucun des deux est mort, si c'est le cas alors c'est la fin du combat ( break)
                if self.verifierFinCombat() == True :
                    break
                
                self.tourEnnemi()
                
                if self.verifierFinCombat():
                    break
                
                #On passe ensuite au prochain tour 
                self.tourActuel = self.tourActuel + 1
                input(" Appuyez sur Entrée pour continuer...")
        
        #Affichage du résultat
        self.afficherResultat()
        return self.vainqueur
    
    def afficherResultat(self):
        #Affiche le résultat final du combat avec style
        nettoyerEcran() 
        print("="*60)
        print("                FIN DU COMBAT")
        print("="*60)
        
        if self.vainqueur == self.joueur:
            print("  VICTOIRE ! ")
            print(self.joueur.nom + " remporte le combat !")
        elif self.vainqueur == self.ennemi:
            print("  DÉFAITE ! ")
            print(self.ennemi.nom + " remporte le combat !")
        else:
            print("  MATCH NUL !")
        
        print("  STATUTS FINAUX:")
        print("─" * 30)
        print(self.joueur.nom + " : " + str(self.joueur.pvActuel) + "/" + str(self.joueur.pvMax) + " PV")
        print(self.ennemi.nom + " : " + str(self.ennemi.pvActuel) + "/" + str(self.ennemi.pvMax) + " PV")
        
        print("="*60)
        input(" Appuyez sur Entrée pour continuer...")


    def executerAction(self, nomAction):
        print("  " + nomAction + " ")
        afficherSeparation()

    def afficherErreur(self, message):
        print(" ERREUR: " + message)
        input("Appuyez sur Entrée pour continuer...")

    def confirmerAbandon(self):
        print(" ABANDONNER LE COMBAT ")
        choix = input("Êtes-vous sûr ? (oui/non): ").lower()
        return choix in ["oui", "o", "yes", "y"]

    def afficherTechnique(self):
        nettoyerEcran()
        print("="*50)
        print("            VOS TECHNIQUES ")
        print("="*50)
        
        if len(self.joueur.techniques) == 0:
            print("Vous ne connaissez aucune technique.")
            input(" Appuyez sur Entrée pour retourner au combat...")
            return
        
        # Grouper par type
        types = {"offensive": [], "defensive": [], "medical": []}
        for technique in self.joueur.techniques:
            if technique.typeTechnique in types:
                types[technique.typeTechnique].append(technique)
        
        # Afficher par type avec couleurs
        for typeNom, techniquesListe in types.items():
            if len(techniquesListe) > 0:
                if typeNom == "offensive":
                    print("  TECHNIQUES OFFENSIVES :")
                elif typeNom == "defensive":
                    print("  TECHNIQUES DÉFENSIVES :")
                else:
                    print("  TECHNIQUES MÉDICALES :")
                
                for technique in techniquesListe:
                    print("  • " + technique.nom)
                    print("    Mudras: " + " + ".join(technique.mudras))
                    print("    Chakra: " + str(technique.coutChakra))
                    if technique.typeTechnique == "offensive":
                        print("    Dégâts: " + str(technique.degats))
                    elif technique.typeTechnique == "medical":
                        print("    Soin: " + str(technique.degats) + " PV")
                    if technique.affinite:
                        print("    Affinité: " + technique.affinite)
                    print("")
        
        input("Appuyez sur Entrée pour retourner au combat...")

    # ===================================== GESTION DU MODE ARENE  =====================================

class Arene:
    
    def __init__(self):
        self.ninjaJoueur = None
        self.niveauArene = 1 #J'ai voulu intégrer une montée en terme de difficulté au sein du programme, le niveau de l'arène sert à ça 
        self.xpTotal = 0
        self.combatsGagnes = 0
        self.combatsPerdus = 0
        self.difficulte = "normal" 
        self.techniquesDisponibles = creerTechniquesDeBase()
        self.ennemisVaincus = []
        
    def creerNinjaPersonnalise(self):
        #Le mode arène doit pouvoir générer un protagoniste qui sera utilisé au sein du donjon
        print(" " + "="*50) #Effet d'habillage qu'il faudra harmoniser partout
        print("         CREATION DE VOTRE NINJA")
        print("="*50)
        
        nom = input("Nom de votre shinobi : ")
        if nom == "": 
            nom ="random"
        
        clans = { #Chaque clan dispose de statistiques spécifiques..je n'ai pas voulu créer trop de disparités pour le moment
            1: ("Uzumaki", 100, 100, 110, 100),  #Ces chiffres correspondent aux : pv, chakra, endurance, spiritualite
            2: ("Uchiha", 100, 100, 100, 110),
            3: ("Senju", 100, 100, 115, 100),
            4: ("Hyuga", 100, 100, 100, 110)
        }
       
        choixClanValide = False #On force l'utilisateur à choisir un clan
        while not choixClanValide: #On présente les différents clans et leurs attributs 
            print(" Choisissez votre clan :")
            print("1- Uzumaki (+10 endurance, techniques médicales)")
            print("2- Uchiha (+10 spiritualité, techniques feu)")
            print("3- Senju (+15 endurance, techniques terre/eau)")
            print("4- Hyuga (+10 spiritualité, techniques chakra pur)")
            try:
                choixClan = int(input("Votre choix (1-4) : "))
                if choixClan in clans:
                    nomClan, pv, chakra, endurance, spiritualite = clans[choixClan]
                    choixClanValide = True
                else:
                    print("Choix invalide ! Veuillez choisir entre 1 et 4.")      
            except ValueError:
                print("Erreur de saisie ! Veuillez entrer un nombre entre 1 et 4.")
                
        
        #En plus du clan, les joueurs doivent choisir une certaine affinité 
        print(" Choisissez votre affinité élémentaire :")
        print("1- Feu")
        print("2- Eau") 
        print("3- Terre")
        print("4- Tonnerre")
        print("5- Vent")
        affinites = {1: "Feu", 2: "Eau", 3: "Terre", 4: "Tonnerre", 5: "Vent",6:"Aucune"}
        
        try:
            choixAffinite = int(input("Votre choix (1-5) : "))
            affinite = affinites.get(choixAffinite, "Vent")#On récupère l'affinité choisie par le joueur
        except ValueError:
            affinite = "Aucune"

        #Création du ninja ! 
        self.ninjaJoueur = Ninja(nom, pvMax=pv, chakraMax=chakra, endurance=endurance, spiritualite=spiritualite, rang="Genin")
        self.ninjaJoueur.ajouterAffinite(affinite)
        
        # Techniques de départ selon le clan
        self.donnerTechniquesDepart(nomClan)
        
        print(" " + "="*50)
        print("         NINJA CREE AVEC SUCCES")
        print("="*50)
        print("Nom : " + self.ninjaJoueur.nom)
        print("Clan : " + nomClan)
        print("Affinité : " + affinite)
        print("Rang : " + self.ninjaJoueur.rang)
        print("XP : 0")
        print("Niveau Arène : 1")
        self.ninjaJoueur.afficherStatut()
        input(" Appuyez sur Entrée pour continuer...")
        
    def donnerTechniquesDepart(self, clan):
        #Chaque ninja dispose de techniques de base en fonction de son clan. Il faudrait inclure aussi une technique spéciale ( Kekkei Genkai ) utilisable uniquement par ce clan par la suite 
        techniquesBase = creerTechniquesDeBase()
        
        if clan == "Uzumaki":
            # Techniques médicales et endurance
            self.ninjaJoueur.techniques.append(techniquesBase[5])  # Soin basique
            self.ninjaJoueur.techniques.append(techniquesBase[1])  #  Multiclonage de Naruto
        elif clan == "Uchiha":
            # Techniques feu
            self.ninjaJoueur.techniques.append(techniquesBase[0])  # Boule de feu suprême 
            self.ninjaJoueur.techniques.append(techniquesBase[3])  # Mur de terre (défense)
        elif clan == "Senju":
            # Techniques terre/eau + endurance
            self.ninjaJoueur.techniques.append(techniquesBase[3])  # Mur de terre
            self.ninjaJoueur.techniques.append(techniquesBase[4])  # Bouclier eau
        elif clan == "Hyuga":
            # Techniques chakra pur + attaque physique renforcée
            self.ninjaJoueur.techniques.append(techniquesBase[1])  # Multiclonage
    
        
        print("Techniques de départ reçues !")
        
    def genererEnnemiAleatoire(self):
        
        nomsEnnemis = ["Bandit", "Zetsu Maléfique", "Samurai", "Shinobi", "Unité Spéciale", "Mercenaire", "Espion", "Monstre"] 
        village = ["Kumo","Kiri","Iwa","Suna","Konoha","Oto","Taki","Konoha"]
        nom = random.choice(nomsEnnemis)+ " de "+ random.choice(village) + " Niv." + str(self.niveauArene)
        
        #En fonction du niveau de l'arêne, les statistiques de l'ennemi s'adaptent. Je me suis dit que c'est un moyen simple de créer un semblant de difficulté accrue en fonction des niveaux 
        multiplicateur = 1.0
        niveau = 1
        while niveau < self.niveauArene:
            multiplicateur = multiplicateur + 0.2
            niveau = niveau + 1             
        pvBase = int(80 * multiplicateur)
        chakraBase = int(70 * multiplicateur)
        enduranceBase = int(80 * multiplicateur)
        spiritualiteBase = int(80 * multiplicateur)
        
        ennemi = Ninja(nom, pvMax=pvBase, chakraMax=chakraBase,
                    endurance=enduranceBase, spiritualite=spiritualiteBase)
        
        affinites = ["Feu", "Eau", "Terre", "Tonnerre", "Vent"]
        ennemi.ajouterAffinite(random.choice(affinites))
        
        techniquesDisponibles = creerTechniquesDeBase()
        
        
        techniquesOffensives = []
        techniquesDefensives = []
        techniquesMedicales  = []

        for i in techniquesDisponibles:
            if i.typeTechnique == "offensive":    
                techniquesOffensives.append(i)
            elif i.typeTechnique == "defensive":
                techniquesDefensives.append(i)
            elif i.typeTechnique == "medical":
                techniquesMedicales.append(i)
                
        
        if len(techniquesOffensives) > 0:
            techniqueOffensive = random.choice(techniquesOffensives) # On permet à l'ennemi d'avoir au moins 1 technique offensive
            ennemi.techniques.append(techniqueOffensive)
        
        
        techniquesRestantes = random.randint(1,3) #Un ennemi peut avoir 1 à 30 techniques supplémentaires 
        
        for i in range(techniquesRestantes):
            rand = random.randint(1, 100)
            if rand <= 60 and len(techniquesOffensives) > 0:
                technique = random.choice(techniquesOffensives)
                if technique not in ennemi.techniques: #On vérifie qu'on ne prend pas de doublons 
                    ennemi.techniques.append(technique)
            elif rand <= 90 and len(techniquesDefensives) > 0:
                technique = random.choice(techniquesDefensives)
                if technique not in ennemi.techniques:
                    ennemi.techniques.append(technique)
            elif len(techniquesMedicales) > 0:
                technique = random.choice(techniquesMedicales)
                if technique not in ennemi.techniques:
                    ennemi.techniques.append(technique)
        return ennemi

        
    def lancerCombatArene(self):
    
        print(" " + "="*50)
        print("         COMBAT D'ARENE - NIVEAU " + str(self.niveauArene))
        print("="*50)

        ennemi = self.genererEnnemiAleatoire()
        
        print("Adversaire généré :")
        ennemi.afficherStatut()
        
        input(" Appuyez sur Entrée pour commencer le combat...")
        
        # On appelle l'objet Combat à travers la classe dans -> combat 
        combat = Combat(self.ninjaJoueur, ennemi, self.techniquesDisponibles)
        vainqueur = combat.lancerCombat() #Lancement du combat calibré plus tôt 
        if vainqueur == self.ninjaJoueur:#Création du vainqueur
            self.gererVictoire(ennemi)
        else:
            self.gererDefaite()
            
        return vainqueur
        
    def gererVictoire(self, ennemiVaincus):
        print(" " + "="*50)
        print("             VICTOIRE !")
        print("="*50)
        
        self.combatsGagnes = self.combatsGagnes + 1
        self.ennemisVaincus.append(ennemiVaincus.nom)
        
        # Calcul de l'XP gagné après chaque victoire 
        xpGagne = 50 + (self.niveauArene * 10)
        self.xpTotal = self.xpTotal + xpGagne    
        print("XP gagné : " + str(xpGagne))
        print("XP total : " + str(self.xpTotal))
        
        # Vérifier montée de niveau
        xpRequis = self.calculerXPRequis()
        if self.xpTotal >= xpRequis:
            self.monterNiveau()
    
        self.donnerRecompensesAleatoires()
        
        # Calcul de la progression dans l'arène
        if self.combatsGagnes % 3 == 0:  # Tous les 3 combats
            self.niveauArene = self.niveauArene + 1
            print(" NIVEAU D'ARENE AUGMENTE !")
            print("Nouveau niveau : " + str(self.niveauArene))
            print("Vos opposants seront plus forts...")
        
        input(" Appuyez sur Entrée pour continuer...")
        
    def gererDefaite(self):
        #Gère les conséquences d'une défaite
        print(" " + "="*50)
        print("             DEFAITE...")
        print("="*50)
        
        self.combatsPerdus = self.combatsPerdus + 1
        
        # En cas de perte, le joueur perds de l'XP, il en perd pas énormément. Je ne veux pas d'effet de bloquage dans un niveau 
        if self.xpTotal >= 20:
            self.xpTotal = self.xpTotal - 20
            print("Vous perdez 20 XP...")
        
        # Soins partiels
        self.ninjaJoueur.pvActuel = self.ninjaJoueur.pvMax 
        self.ninjaJoueur.pvActuel = int(self.ninjaJoueur.pvActuel)
        self.ninjaJoueur.chakraActuel = self.ninjaJoueur.chakraMax / 2
        self.ninjaJoueur.chakraActuel = int(self.ninjaJoueur.chakraActuel)
        self.ninjaJoueur.estVivant = True
        
        print("Vous vous reposez et récupérez des forces...")
        print("XP total : " + str(self.xpTotal))
        
        input(" Appuyez sur Entrée pour continuer...")
        
    def calculerXPRequis(self):
        #Calcule l'XP requis pour le prochain niveau
        niveauActuel = self.obtenirNiveauActuel()
        niveauActuel = niveauActuel * 100
        return niveauActuel
        
    def obtenirNiveauActuel(self):
        #Calcule le niveau actuel basé sur l'XP
        niveauActuel = int(self.xpTotal / 100) + 1
        return niveauActuel
        
    def monterNiveau(self):
        #Gère la montée de niveau
        nouveauNiveau = self.obtenirNiveauActuel()
        
        print(" " + "="*30)
        print("    MONTEE DE NIVEAU !")
        print("    NIVEAU " + str(nouveauNiveau))
        print("="*30)
        
        # A chaque montée de niveau, le joueur peut utiliser des points à répartir pour prendre en niveau
        ptsDispo = 5
        
        print("Vous avez " + str(ptsDispo) + " points à répartir :")
        print("1- PV (+1 point = +5 PV max)")
        print("2- Chakra (+1 point = +3 Chakra max)")
        print("3- Endurance (+1 point = +2 Endurance)")
        print("4- Spiritualité (+1 point = +2 Spiritualité)")
        
        while ptsDispo > 0:
            print(" Points restants : " + str(ptsDispo))
            self.ninjaJoueur.afficherStatut()
            
            try:
                choix = int(input("Améliorer quelle stat (1-4) : "))
                points = int(input("Combien de points investir : "))
                
                if points > ptsDispo or points < 1:
                    print("Nombre de points invalide !")
                    continue
                    
                if choix == 1:
                    bonus = points * 5
                    self.ninjaJoueur.pvMax = self.ninjaJoueur.pvMax + bonus
                    self.ninjaJoueur.pvActuel = self.ninjaJoueur.pvActuel + bonus
                    print("+" + str(bonus) + " PV max !")
                elif choix == 2:  
                    bonus = points * 3
                    self.ninjaJoueur.chakraMax = self.ninjaJoueur.chakraMax + bonus
                    self.ninjaJoueur.chakraActuel = self.ninjaJoueur.chakraActuel + bonus
                    print("+" + str(bonus) + " Chakra max !")
                elif choix == 3:  
                    bonus = points * 2
                    self.ninjaJoueur.enduranceMax = self.ninjaJoueur.enduranceMax + bonus
                    self.ninjaJoueur.enduranceActuelle = self.ninjaJoueur.enduranceActuelle + bonus
                    print("+" + str(bonus) + " Endurance !")
                elif choix == 4: 
                    bonus = points * 2
                    self.ninjaJoueur.spiritualiteMax = self.ninjaJoueur.spiritualiteMax + bonus
                    self.ninjaJoueur.spiritualiteActuelle = self.ninjaJoueur.spiritualiteActuelle + bonus
                    print("+" + str(bonus) + " Spiritualité !")
                else:
                    print("Choix invalide !")
                    continue
                    
                ptsDispo = ptsDispo - points
                
            except ValueError:
                print("Erreur de saisie !")
        
        
        if nouveauNiveau % 3 == 0:  # Tous les 3 niveaux, le joueur peut apprendre une nouvelle technique
            self.apprendreTechniqueAleatoire()
            
        # Changement de rang
        if nouveauNiveau == 5:
            self.ninjaJoueur.changerRang("CHUNIN")
        if nouveauNiveau == 10:
            self.ninjaJoueur.changerRang("JONIN")
        if nouveauNiveau == 15:
            self.ninjaJoueur.changerRang("ANBU")
        if nouveauNiveau == 20: 
            self.ninjaJoueur.changerRang("HOKAGE")
            
    def apprendreTechniqueAleatoire(self):

        techniquesApprises = []
        for t in self.ninjaJoueur.techniques:
            techniquesApprises.append(t.nom)

        techniquePossibles = []
        for t in self.techniquesDisponibles:
            if t.nom not in techniquesApprises:
                techniquePossibles.append(t)
                
        if techniquePossibles:
            nouvelleTechnique = random.choice(techniquePossibles)
            self.ninjaJoueur.techniques.append(nouvelleTechnique)
            print(" NOUVELLE TECHNIQUE APPRISE !")
            nouvelleTechnique.afficherInfo()
            
    def donnerRecompensesAleatoires(self):
        #Cette fonction permet donner des récompenses aléatoire
        chanceObjet = random.randint(1,100)
        if chanceObjet <= 40:  # 40% de chance en 
            objet = genererObjetAleatoire()
            self.ninjaJoueur.inventaire.append(objet)
            print("Objet trouvé : " + objet.nom + " (" + objet.rarete + ")")
            
            # Affiche l'effet brièvement
            if objet.valeur > 0:
                print("Effet: +" + str(objet.valeur) + " " + objet.effetPrincipal.replace("_", " "))

            
    def afficherStatistiques(self):
        #Affiche les statistiques du joueur en arène
        print(" " + "="*50)
        print("         STATISTIQUES ARENE")
        print("="*50)
        print("Ninja : " + self.ninjaJoueur.nom)
        print("Niveau : " + str(self.obtenirNiveauActuel()))
        print("XP : " + str(self.xpTotal))
        print("XP pour niveau suivant : " + str(self.calculerXPRequis() - self.xpTotal))
        print("Niveau d'arène : " + str(self.niveauArene))
        print("Combats gagnés : " + str(self.combatsGagnes))
        print("Combats perdus : " + str(self.combatsPerdus))
        if self.combatsGagnes + self.combatsPerdus > 0:
            ratio = (self.combatsGagnes * 100) / (self.combatsGagnes + self.combatsPerdus)
            ratio = int(ratio)
            print("Taux de victoire : " + str(ratio) + "%")
        print("Techniques connues : " + str(len(self.ninjaJoueur.techniques)))
        print("Objets possédés : " + str(len(self.ninjaJoueur.inventaire)))
        
    def menuArene(self):
        if not self.ninjaJoueur:
            print("Aucun ninja créé ! Création en cours...")
            self.creerNinjaPersonnalise()
            
        continuer = True
        while continuer:
            print(" " + "="*50)
            print("              MODE ARENE")
            print("="*50)
            print("1- Combat d'arène")
            print("2- Voir statistiques")
            print("3- Voir ninja")
            print("4- Voir techniques")
            print("5- Gérer inventaire")
            print("6- Changer difficulté")
            print("7- Repos (soins complets)")
            print("0- Quitter l'arène")
            
            try:
                choix = int(input("CHOIX : "))
            except ValueError:
                print("Erreur : vous devez entrer un nombre.")
                choix = -1
                
            if choix != -1:
                if choix == 1:
                    if self.ninjaJoueur.estVivant:
                        self.lancerCombatArene()
                    else:
                        print("Votre ninja est K.O. ! Reposez-vous d'abord.")
                elif choix == 2:
                    self.afficherStatistiques()
                    input("Appuyez sur Entrée pour continuer...")
                elif choix == 3:
                    self.ninjaJoueur.afficherStatut()
                    input("Appuyez sur Entrée pour continuer...")
                elif choix == 4:
                    print(" Techniques connues :")
                    for technique in self.ninjaJoueur.techniques:
                        technique.afficherInfo()
                    input("Appuyez sur Entrée pour continuer...")
                elif choix == 5:
                    self.gererInventaire() 
                elif choix == 6:
                    self.changerDifficulte()
                elif choix == 7:
                    self.reposerNinja()
                elif choix == 0:
                    continuer = False
                    print("Vous quittez l'arène...")
                else:
                    print("Choix invalide !")
                    
    def changerDifficulte(self):
        #Change la difficulté de l'arène
        print(" Difficulté actuelle : " + self.difficulte)
        print("1- Normal (pas de timer, accès répertoire)")
        print("2- Difficile (timer 10s, pas de répertoire)")
        
        try:
            choix = int(input("Nouvelle difficulté (1-2) : "))
            if choix == 1:
                self.difficulte = "normal"
                print("Difficulté changée : NORMAL")
            elif choix == 2:
                self.difficulte = "difficile"
                print("Difficulté changée : DIFFICILE")
            else:
                print("Choix invalide.")
        except ValueError:
            print("Erreur de saisie.")
            
    def reposerNinja(self):
        #Repos complet du ninja
        self.ninjaJoueur.pvActuel = self.ninjaJoueur.pvMax
        self.ninjaJoueur.chakraActuel = self.ninjaJoueur.chakraMax
        self.ninjaJoueur.enduranceActuelle = self.ninjaJoueur.enduranceMax
        self.ninjaJoueur.spiritualiteActuelle = self.ninjaJoueur.spiritualiteMax
        self.ninjaJoueur.estVivant = True
        self.ninjaJoueur.defenseActive = False
        
        print("Repos complet effectué ! Toutes vos stats sont restaurées.")
        input("Appuyez sur Entrée pour continuer...")
    
    def utiliserObjetInventaire(self):
        #Utilise un objet depuis l'inventaire
        if len(self.ninjaJoueur.inventaire) == 0:
            print("Inventaire vide !")
            return
        
        try:
            numero = int(input("Numéro de l'objet à utiliser : "))
            if 1 <= numero <= len(self.ninjaJoueur.inventaire):
                objet = self.ninjaJoueur.inventaire[numero - 1]
                
                if isinstance(objet, Objet):
                    if objet.utiliser(self.ninjaJoueur):
                        # Retirer l'objet si c'est un consommable
                        if objet.type == "consommable":
                            del self.ninjaJoueur.inventaire[numero - 1]
                            print("Objet consommé et retiré de l'inventaire.")
                else:
                    # Ancien système pour compatibilité
                    print("Objet utilisé : " + str(objet))
                    del self.ninjaJoueur.inventaire[numero - 1]
                    
                input("Appuyez sur Entrée pour continuer...")
            else:
                print("Numéro invalide !")
        except ValueError:
            print("Erreur de saisie !")

    def gererInventaire(self):
        if len(self.ninjaJoueur.inventaire) == 0:
            print(" Votre inventaire est vide !")
            input("Appuyez sur Entrée pour continuer...")
            return
    
        continuer = True
        while continuer:
            print(" " + "="*40)
            print("            INVENTAIRE")
            print("="*40)
            
            for i in range(len(self.ninjaJoueur.inventaire)):
                objet = self.ninjaJoueur.inventaire[i]
                if isinstance(objet, Objet): 
                    print(str(i + 1) + ". " + objet.nom + " (" + objet.type + ")")
                    if objet.valeur > 0:
                        print("   Effet: +" + str(objet.valeur) + " " + objet.effetPrincipal.replace("_", " "))
                else: 
                    print(str(i + 1) + ". " + str(objet) + " (ancien)")
            
            print(" Actions :")
            print("1- Utiliser un objet")
            print("2- Voir détails d'un objet")
            print("0- Retour")
            try:
                choix = int(input("Choix : "))
                
                if choix == 0:
                    continuer = False
                elif choix == 1:
                    self.utiliserObjetInventaire()
                elif choix == 2:
                    self.voirDetailsObjet()
                else:
                    print("Choix invalide !")
                    
            except ValueError:
                print("Erreur de saisie !")

    def voirDetailsObjet(self):
        #Affiche les détails d'un objet
        if len(self.ninjaJoueur.inventaire) == 0:
            print("Inventaire vide !")
            return
        
        try:
            numero = int(input("Numéro de l'objet à examiner : "))
            if 1 <= numero <= len(self.ninjaJoueur.inventaire):
                objet = self.ninjaJoueur.inventaire[numero - 1]
                
                if isinstance(objet, Objet):
                    objet.afficherInfo()
                else:
                    print("Objet simple : " + str(objet))
                    
                input("Appuyez sur Entrée pour continuer...")
            else:
                print("Numéro invalide !")
        except ValueError:
            print("Erreur de saisie !")

class Histoire:
    #Classe pour gérer le mode histoire avec chapitres et progression narrative
    def __init__(self):
        self.ninjaJoueur = None
        self.chapitreActuel = 1
        self.chapitreTermines = []
        self.progressionTotale = 0
        self.dialogues_vus = []
        
        # Créer les chapitres
        self.chapitres = self.creerChapitres()
        
    def creerChapitres(self):
        #L'ensemble des chapitres sont stockés au sein d'un dictionnaire, la clé du dictionnaire représente le numéro du chapitre. Dans la valeur du dictionnaire, il existe un autre dictionnaire qui contient toutes les valeurs spécifiques du chapitre. 
        chapitres = {}
        
        chapitres[1] = {
            'titre': "L'Examen Genin",
            'description': "Neufs ans passés, le démon renard à neufs queues a attaqué Konoha...Le 4e hokage, grand héro du village, stoppa le carnage en scellant ce démon au sein du jeune Naruto. Orphelin et exclus par tous, Naruto s'enrole au sein de l'académin afin de devenir un grand Ninja et prouver sa valeur",
            'dialogueIntro': [
                "IRUKA : Naruto, c'est ton dernier examen pour devenir Genin. Tu as raté cet examin 3 fois déjà ! Il est temps que tu y mettent du sérieux..",
                "NARUTO : Je vous prouverais ma valeur Iruka-sensei ! Quelle est la mission à remplir cette fois-ci ? "
                "IRUKA : Tu devras affronter en duel singulier 3 élèves de l'académie des ninjas afin de remporter ton bandeau."
            ],
            'ennemis': [
                {'nom': 'Shikamaru Nara', 'niveau': 1, 'affinite': 'Vent'},
                {'nom': 'Shoji Akimichi', 'niveau': 1, 'affinite': 'Terre'},
                {'nom': 'Sasuke Uchiha ', 'niveau': 2, 'affinite': 'Feu'}
            ],
            'dialogueFin': [
                "IRUKA : Félicitations Naruto ! Tu es maintenant un Genin !",
                "NARUTO :...(pleure)Je vais devenir Hokage dattebayo !",
                "IRUKA :...Tu as encore beaucoup à apprendre. N'oublie pas que beaucoups de personnes te détesteront du fait que tu abrites Kyubi. A partir de demain tu intègre l'équipe 7 composé de Sakura Haruno et Sasuke Uchiha. Tu seras dirigé par Kakashi Hataké, le ninja copieur "
            ],
            'recompenses': {
                'xp': 100,
                'technique': 'Kage Bunshin no Jutsu',
                'objet': 'Bandeau de Konoha'
            }
        }
        

        chapitres[2] = {
            'titre': "Première Mission au Pays des vagues",
            'description': "L'Équipe 7 part pour sa première vraie mission. L'objectif de cette mission : escorter Izuna ( charpentier ) au sein de sa demeure",
            'dialogueIntro': [
                "KAKASHI : Votre première mission est d'escorter Izuna, je serais là en cas de soucis (continue à lire un roman).",
                "SASUKE : Tant que Naruto ne se met pas en travers de mon chemin..",
                "NARUTO : Je t'ai entendu Sasuke ! (grr)",
                "SAKURA : Calmez vous, au moins on sort du village !",
                "NARUTO : 'Oui, jespère qu'on va rencontrer des ninjas ennemis !"
            ],
            'ennemis': [
                {'nom': 'Mercenaires du Pays des Vagues', 'niveau': 2, 'affinite': 'Vent'},
                {'nom': 'Haku', 'niveau': 3, 'affinite': 'Vent'},
                {'nom': 'Zabuza', 'niveau': 4, 'affinite': 'Eau'}
            ],
            'dialogueFin': [
                "MARCHAND : Merci ninjas de Konoha ! Voici votre récompense.",
                "KAKASHI : Bon travail l'équipe 7. Vous progressez.",
                "NARUTO : Ils étaient plus coriaces que prévu...",
                "KAKASHI : Ne sous-estime jamais l'ennemi, Naruto."
            ],
            'recompenses': {
                'xp': 150,
                'technique': 'Rasengan',
                'objet': 'Kunai spécial'
            }
        }
        

        chapitres[3] = {
            'titre': "L'Invasion de Konoha",
            'description': "Le village est attaqué par les shinobi de Suna ! Défendez Konoha !",
            'dialogueIntro': [
                "ALARME : ALERTE ! Le village est attaqué !",
                "NARUTO : Quoi ?! Par qui ?? ",
                "KAKASHI : Tous les ninjas, défendez Konoha ! Naruto..tous les ninjas de rang supérieur sont mobilisés, je te charge de vaincre Gaara.",
                "NARUTO : Je ne laisserai personne détruire mon village !"
            ],
            'ennemis': [
                {'nom': 'Shinobi de Suna', 'niveau': 4, 'affinite': 'Terre'},
                {'nom': 'Kankuro', 'niveau': 5, 'affinite': 'Eau'},
                {'nom': 'Gaara', 'niveau': 6, 'affinite': 'Vent'}
            ],
            'dialogueFin': [
                "GAARA :...tu m'as vaincu..",
                "NARUTO : Personne ne touchera à mes amis !",
                "HOKAGE : Tu as le vrai esprit du feu, Naruto.",
                "NARUTO : Un jour, je protégerai ce village en tant qu'Hokage !"
            ],
            'recompenses': {
                'xp': 200,
                'technique': 'Multi-Clonage Supra',
                'objet': 'Médaille de Courage'
            }
        }
        
        return chapitres
    
    def creerNinjaHistoire(self):

        print(" " + "="*50)
        print("         MODE HISTOIRE")
        print("     INCARNEZ NARUTO UZUMAKI A TRAVERS LES DIFFERENTS ARCS DU MANGA CULTE ")
        print("="*50)
        self.ninjaJoueur = Ninja("Naruto Uzumaki", pvMax=120, chakraMax=110, endurance=130, spiritualite=100, rang="Genin")
        self.ninjaJoueur.ajouterAffinite("Vent")#Naruto est de type Vent au sein du Manga
        techniquesBase = creerTechniquesDeBase()
        self.ninjaJoueur.techniques.append(techniquesBase[1])  # Multi-Clonage
        # Objets de départ
        potion = Objet("Potion de soin", "consommable", "soinPv", 30)
        pilule = Objet("Pilule militaire", "consommable", "gainChakra", 30)
        self.ninjaJoueur.inventaire.append(potion)
        self.ninjaJoueur.inventaire.append(pilule)
        
        print(" Personnage créé :")
        self.ninjaJoueur.afficherStatut()
        print(" Techniques de départ :")
        for technique in self.ninjaJoueur.techniques:
            print("- " + technique.nom)
        
        input(" Appuyez sur Entrée pour commencer l'aventure...")
    
    def afficherDialogue(self, ligneDialogue):
        #Affiche un dialogue ligne par ligne
        for ligne in ligneDialogue:
            print(" " + ligne)
            input("   [Appuyez sur Entrée pour continuer...]")
    
    def creerEnnemiChapitre(self, infoEnnemi, nouveauChapitre):
            nom = infoEnnemi['nom']
            niveau = infoEnnemi['niveau']
            affinite = infoEnnemi['affinite']
            multiplicateur = 1 + (niveau - 1) * 0.3
            pvBase = int(90 * multiplicateur)
            chakraBase = int(80 * multiplicateur)
            enduranceBase = int(85 * multiplicateur)
            spiritualiteBase = int(85 * multiplicateur)

            ennemi = Ninja(nom, pvMax=pvBase, chakraMax=chakraBase,endurance=enduranceBase, spiritualite=spiritualiteBase)
            ennemi.ajouterAffinite(affinite)

            techniquesDisponibles = creerTechniquesDeBase()

            techniquesOffensives = []
            techniquesDefensives = []
            techniquesMedicales  = []

            for t in techniquesDisponibles:
                if t.typeTechnique == "offensive":
                    techniquesOffensives.append(t)
                elif t.typeTechnique == "defensive":
                    techniquesDefensives.append(t)
                elif t.typeTechnique == "medical":
                    techniquesMedicales.append(t)

            # Permet de garantir au moins 1 technique offensive
            if len(techniquesOffensives) > 0:
                techniqueOffensive = random.choice(techniquesOffensives)
                ennemi.techniques.append(techniqueOffensive)

            techniquesRestantes = 2

            for _ in range(techniquesRestantes):
                
                rand = random.randint(1, 100)
                
                if rand <= 70 and len(techniquesOffensives) > 0:
                    technique = random.choice(techniquesOffensives)
                    if technique not in ennemi.techniques:
                        ennemi.techniques.append(technique)
                elif rand <= 95 and len(techniquesDefensives) > 0:
                    technique = random.choice(techniquesDefensives)
                    if technique not in ennemi.techniques:
                        ennemi.techniques.append(technique)
                elif len(techniquesMedicales) > 0:
                    technique = random.choice(techniquesMedicales)
                    if technique not in ennemi.techniques:
                        ennemi.techniques.append(technique)
            return ennemi

    def lancerChapitre(self, numeroChapitre):
        if numeroChapitre not in self.chapitres:
            print("Chapitre introuvable !")
            return False
        
        chapitre = self.chapitres[numeroChapitre]
        
        print(" " + "="*60)
        print("         CHAPITRE " + str(numeroChapitre))
        print("         " + chapitre['titre'].upper())
        print("="*60)
        print(chapitre['description'])
        print("="*60)
        
        # Dialogue d'introduction
        print("  INTRODUCTION")
        self.afficherDialogue(chapitre['dialogueIntro'])
        
        # Combats contre tous les ennemis
        ennemisVaincus = 0
        for i, infoEnnemi in enumerate(chapitre['ennemis']):
            print(" " + "="*50)
            print("    COMBAT " + str(i + 1) + "/" + str(len(chapitre['ennemis'])))
            print("="*50)
            
            ennemi = self.creerEnnemiChapitre(infoEnnemi, numeroChapitre)
            
            print("Adversaire : " + ennemi.nom)
            ennemi.afficherStatut()
            
            input(" Appuyez sur Entrée pour commencer le combat...")
            
            # Combat
            combat = Combat(self.ninjaJoueur, ennemi, creerTechniquesDeBase())
            vainqueur = combat.lancerCombat()
            
            if vainqueur == self.ninjaJoueur:
                ennemisVaincus += 1
                print("  Ennemi vaincu ! (" + str(ennemisVaincus) + "/" + str(len(chapitre['ennemis'])) + ")")
                
                # Soins partiels entre les combats
                if i < len(chapitre['ennemis']) - 1:  # Pas le dernier combat
                    soin = 30
                    self.ninjaJoueur.pvActuel = min(self.ninjaJoueur.pvMax, 
                                                    self.ninjaJoueur.pvActuel + soin)
                    self.ninjaJoueur.chakraActuel = min(self.ninjaJoueur.chakraMax,
                                                        self.ninjaJoueur.chakraActuel + 20)
                    print("Naruto récupère un peu entre les combats... (+" + str(soin) + " PV, +20 chakra)")
                
                input("Appuyez sur Entrée pour continuer...")
            else:
                print("  DÉFAITE !")
                print("Naruto s'évanouit... Le chapitre recommence.")
                
                # Réinitialiser le ninja
                self.ninjaJoueur.pvActuel = self.ninjaJoueur.pvMax
                self.ninjaJoueur.chakraActuel = self.ninjaJoueur.chakraMax
                self.ninjaJoueur.estVivant = True
                
                input("Appuyez sur Entrée pour réessayer...")
                return self.lancerChapitre(numeroChapitre)  # Recommencer
        
        # Tous les ennemis vaincus - Chapitre terminé
        self.terminerChapitre(numeroChapitre, chapitre)
        return True
    
    def terminerChapitre(self, numeroChapitre, chapitre):
        #Termine un chapitre avec dialogue et récompenses
        print(" " + "="*60)
        print("         CHAPITRE TERMINÉ !")
        print("="*60)
        
        #Dialogue de fin
        print("  CONCLUSION")
        self.afficherDialogue(chapitre['dialogueFin'])
        
        #Récompenses
        print("  RÉCOMPENSES :")
        recompenses = chapitre['recompenses']
        
        #XP
        xpGagne = recompenses['xp']
        print(" XP gagné : " + str(xpGagne))
        self.progressionTotale += xpGagne
        
        # Technique
        if 'technique' in recompenses:
            nomTechnique = recompenses['technique']
            techniquesDisponibles = creerTechniquesDeBase()
            technique = trouverTechniqueParNom(nomTechnique, techniquesDisponibles)
            if technique and technique not in self.ninjaJoueur.techniques:
                self.ninjaJoueur.techniques.append(technique)
                print(" Nouvelle technique apprise : " + nomTechnique)
        
        # Objet
        if 'objet' in recompenses:
            nomObjet = recompenses['objet']
            if nomObjet == "Bandeau de Konoha":
                objet = Objet(nomObjet, "special", "symbole", 0, "Symbole de votre rang de Genin")
            elif nomObjet == "Kunai spécial":
                objet = Objet(nomObjet, "equipement", "boostAttaque", 5, "Kunai de qualité supérieure")
            elif nomObjet == "Médaille de Courage":
                objet = Objet(nomObjet, "special", "honneur", 0, "Médaille pour bravoure exceptionnelle")
            else:
                objet = Objet(nomObjet, "special", "mystere", 0, "Objet mystérieux")
            
            objet.changerRarity("rare")
            self.ninjaJoueur.inventaire.append(objet)
            print(" Objet reçu : " + nomObjet)
        
        # Soins complets
        self.ninjaJoueur.pvActuel = self.ninjaJoueur.pvMax
        self.ninjaJoueur.chakraActuel = self.ninjaJoueur.chakraMax
        self.ninjaJoueur.enduranceActuelle = self.ninjaJoueur.enduranceMax
        self.ninjaJoueur.spiritualiteActuelle = self.ninjaJoueur.spiritualiteMax
        self.ninjaJoueur.estVivant = True
        print(" Naruto récupère complètement !")
        
        # Marquer le chapitre comme terminé
        if numeroChapitre not in self.chapitreTermines:
            self.chapitreTermines.append(numeroChapitre)
    
        if numeroChapitre < len(self.chapitres):
            print("  Chapitre " + str(numeroChapitre + 1) + " débloqué !")
        else:
            print("  HISTOIRE TERMINÉE ! Félicitations !")
        
        input(" Appuyez sur Entrée pour continuer...")
    
    def afficherProgression(self):
        print(" " + "="*50)
        print("         PROGRESSION HISTOIRE")
        print("="*50)
        if self.ninjaJoueur: 
            print("Personnage : " + str(self.ninjaJoueur.nom ))
        else:
            print("Personnage : Aucun ")
        print("Chapitres terminés : " + str(len(self.chapitreTermines)) + "/" + str(len(self.chapitres)))
        print("Progression totale : " + str(self.progressionTotale) + " XP")
        
        print(" Chapitres :")
        for numero in range(1, len(self.chapitres) + 1):
            chapitre = self.chapitres[numero]
            if numero in self.chapitreTermines:
                statut = " TERMINÉ"
            elif numero == 1 or (numero - 1) in self.chapitreTermines:
                statut = " DISPONIBLE"
            else:
                statut = " VERROUILLÉ"
            
            print(str(numero) + ". " + chapitre['titre'] + " - " + statut)
        print(" " + "="*50)
    
    def menuHistoire(self):
        #Menu principal du mode histoire
        continuer = True
        while continuer:
            print(" " + "="*50)
            print("              MODE HISTOIRE")
            print("="*50)
            
            if not self.ninjaJoueur:
                print("1- Commencer l'histoire")
                print("0- Retour au menu principal")
            else:
                print("1- Continuer l'histoire")
                print("2- Voir progression")
                print("3- Voir personnage")
                print("4- Recommencer un chapitre")
                print("0- Retour au menu principal")
            
            try:
                choix = int(input("CHOIX : "))
            except ValueError:
                print("Erreur : vous devez entrer un nombre.")
                choix = -1
            
            if choix != -1:
                if choix == 1:
                    if not self.ninjaJoueur:
                        self.creerNinjaHistoire()
                        self.chapitreActuel = 1
                    self.continuerHistoire()
                elif choix == 2 and self.ninjaJoueur:
                    self.afficherProgression()
                    input("Appuyez sur Entrée pour continuer...")
                elif choix == 3 and self.ninjaJoueur:
                    self.ninjaJoueur.afficherStatut()
                    print(" Techniques :")
                    for technique in self.ninjaJoueur.techniques:
                        print("- " + technique.nom)
                    input("Appuyez sur Entrée pour continuer...")
                elif choix == 4 and self.ninjaJoueur:
                    self.menuRecommencerChapitre()
                elif choix == 0:
                    continuer = False
                    print("Retour au menu principal...")
                else:
                    print("Choix invalide !")
    
    def continuerHistoire(self):
        #Continue l'histoire au chapitre actuel
        if self.chapitreActuel > len(self.chapitres):
            print("Histoire terminée ! Félicitations !")
            input("Appuyez sur Entrée pour continuer...")
            return
        
        print(" Chapitre à jouer : " + str(self.chapitreActuel))
        print(self.chapitres[self.chapitreActuel]['titre'])
        
        choix = input("Voulez-vous jouer ce chapitre ? (oui/non) : ").lower()
        if choix in ["oui", "o", "yes", "y"]:
            if self.lancerChapitre(self.chapitreActuel):
                self.chapitreActuel += 1
    
    def menuRecommencerChapitre(self):
        self.afficherProgression()
        
        print(" Quel chapitre voulez-vous rejouer ?")
        print("0- Annuler")
        
        try:
            choix = int(input("Numéro du chapitre : "))
            
            if choix == 0:
                return
            elif 1 <= choix <= len(self.chapitres):
                if choix == 1 or (choix - 1) in self.chapitreTermines:
                    print("Lancement du chapitre " + str(choix) + "...")
                    self.lancerChapitre(choix)
                else:
                    print("Ce chapitre n'est pas encore débloqué !")
            else:
                print("Numéro de chapitre invalide !")
                
        except ValueError:
            print("Erreur de saisie !")
        
        input("Appuyez sur Entrée pour continuer...")

#==================================== DEBUT DU PROGRAMME ==========================================
print("Bienvenu dans l'arène jeune shinobi ! ")
menuPrincipal()
