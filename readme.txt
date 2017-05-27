___________________________________
______ A quoi sert ce projet ______

je prend régulièrement des notes au format .txt.
j'utilise une mise en page qui me permet de facilement me retrouver dans mes notes
j'utilise aussi le format html.

ces scripts transforment un fichier .txt contenant du texte mis en page en texte html
ils sont écris en python 2


___________________________________
______ composition du projet ______

deux scripts:
  dpowers_txt.py
  dpowers_html.py

un fichier d'exemple pour les tester, dpowers-la-maison.txt

________________________ dpowers_txt ________________________

dependances:
	le module os de python
	le module sys de python

ce script peut etre appele dans d'autres scripts
si vous ne voulez que rajouter des majuscules dans un texte:
	python dpowers_txt.py fichier

contient les variables globales:

path_root	chemin du dossier "user", qui contient bureau et documents
path_desktop	chemin du bureau
path_document	chemin du dossier "document"
dico_raccourcis
		dictionnaire stoquant les raccourcis et les chemins correspondant
		raccourci : chemin/complet

vous devez les modifier afin de les adapter a votre ordinateur
vous pouvez rajouter d'autres variables

contient les fonctions:

chemin = raccourcis (chemin)
	action:
		les chemins de fichiers peuvent etre ecris avec des raccourcis.	b/fichier.txt
		cette fonction remplace le raccourci par le chemin entier.	C://user/bureau/fichier.txt
		vous pouvez rajouter vos propres chemins de dossier
	argument: le chemin
	retourne: le chemin entier

texte = lire (fichier)
	ouvrir un fichier .txt, recuperer le texte dans une chaine de caractere
	argument: le nom du fichier, avec le chemin
	retourne: le texte

ecrire (fichier, texte, mode ='w')
	ecrire un texte au format str dans un fichier
	arguments:
		- le fichier
		- le texte
		- le mode d'ecriture
	retourne: rien
	si mode = w, le texte precedement ecris dans le fichier est efface
	si mode = a, on ecris le nouveau texte a la suite de celui deja ecris

texte = majuscule (texte)
	rajouter des majuscules dans un texte au format str
	argument: un texte au format str
	retourne: le texte avec des majuscules apres les points
	pour eviter d'avoir une majuscule apres un point, ecrire deux espaces
		coucou. vous allez bien ?	va devenir	Coucou. Vous allez bien ?
		coucou.  vous allez bien ?	va devenir	Coucou. vous allez bien ?
		le double espace est transforme en espace simple


________________________ dpowers_html ________________________

dependances:
	le module os de python
	le module sys de python
	le module dpowers_txt de deborah-powers

utiliser le script:
	python dpowers_html.py fichier.txt [fichier.css]

contient les fonctions:

texte = creer_liste (texte)
	argument: un texte au format str contenant des listes
	retourne: le texte dans lequel les listes ont ete transformees en liste non ordonnees html
	on peut faire des listes imbriquees.

texte = creer_table (texte)
	argument: un texte au format str contenant des tableaux
	retourne: le texte dans lequel les tableaux ont ete transformees en  tableaux html simples

texte = modif_texte (texte)
	argument: un texte au format str. le texte utilise ma mise en page
	retourne: le texte transforme en texte html. ma mise en page a ete transformee en balises.

txt_to_html (fichier_txt, fichier_css=None):
	arguments:
		un fichier .txt contenant un texte avec ma mise en forme
		(facultatif) un fichier .css contenant les styles a appliquer
	retourne: un fichier .html contenant le texte
