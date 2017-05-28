#!/usr/bin/python2.6
# modules python
import os
from sys import argv


help ="""
dependances:
	le module os de python
	le module sys de python

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
	objectif: ouvrir un fichier .txt, recuperer le texte dans une chaine de caractere
	argument: le nom du fichier, avec le chemin
	retourne: le texte

ecrire (fichier, texte, mode ='w')
	objectif: ecrire un texte au format str dans un fichier
	arguments:
		- le fichier
		- le texte
		- le mode d'ecriture
	retourne: rien
	si mode = w, le texte precedement ecris dans le fichier est efface
	si mode = a, on ecris le nouveau texte a la suite de celui deja ecris

texte = majuscule (texte)
	objectif: rajouter des majuscules dans un texte au format str
	argument: un texte au format str
	retourne: le texte avec des majuscules apres les points
	pour eviter d'avoir une majuscule apres un point, ecrire deux espaces
		coucou. vous allez bien ?	va devenir	Coucou. Vous allez bien ?
		coucou.  vous allez bien ?	va devenir	Coucou. vous allez bien ?
		le double espace est transforme en espace simple

str_nb = float_to_str (nb)
	objectif: simplifier les nombres qui seront ecris, afin d'en faciliter la lecture. 10.0836 --> "10.1", 10.002 --> 10
	action:
		transforme un nombre, int ou float en str
		les float sont arrondi a la premiere decimale
	argument: le nombre
	retourne: la chaine de carcteres correspondant au nombre
	l'arrondi vaut 1

ce script peut etre appele dans d'autres scripts
si vous ne voulez que rajouter des majuscules dans un texte:
	python dpowers_txt.py fichier
"""


""" ____________________________________ quelques raccourci ____________________________________



faciliter l'ecriture des noms de fichiers lorsque l'on utilise l'un des scripts dependant de celui-ci
vous pouvez rajouter vos propres racourcis
"""

path_root = 'C:\Users\user\\'
path_desktop = os.path.join (path_root, 'desktop') +os.sep
path_document = os.path.join (path_root, 'Documents') +os.sep

dico_raccourcis ={
'r/': path_root,
'b/': path_desktop,
'd/': path_document
}


""" ____________________________________ les fonctions ____________________________________ """


def raccourcis (chemin):
	""" action:
		les chemins de fichiers peuvent etre ecris avec des raccourcis.	b/fichier.txt
		cette fonction remplace le raccourci par le chemin entier.	C://user/bureau/fichier.txt
		vous pouvez rajouter vos propres chemins de dossier
	argument: le chemin
	utilise le dictionnaire dico_raccourcis
	retourne: le chemin entier
	"""
#	le chemin est ecrit normalement
	if path_root in chemin: return chemin
#	le chemin est un raccourci
	if chemin[:2] in dico_raccourcis.keys():
		chemin = chemin.replace (chemin[:2], dico_raccourcis [chemin[:2]])
	return chemin

def lire (fichier):
	""" ouvrir un fichier .txt, recuperer le texte dans une chaine de caractere
	argument: le nom du fichier, avec le chemin
	retourne: le texte
	"""
#	si le chemin du fichier contient un raccourci
	fichier = raccourcis (fichier)
#	si le fichier n'ai pas trouve, renvoyer un texte vide
	if not os.path.isfile (fichier):
		print 'pas de fichier'
		print fichier[:60]
		return ""
#	ouvrir le fichier et recuperer le texte au format str
	texteBrut = open (fichier, 'r')
	texte = texteBrut.read()
	texteBrut.close()
#	preparer le texte pour faciliter ses futures tranformations
	texte = texte.replace ('\r', "")
	texte = texte.strip()
	return texte

def ecrire (fichier, texte, mode ='w'):
	"""
	ecrire un texte au format str dans un fichier
	arguments:
		- le fichier
		- le texte
		- le mode d'ecriture
	retourne: rien
	si mode = w, le texte precedement ecris dans le fichier est efface
	si mode = a, on ecris le nouveau texte a la suite de celui deja ecris
	"""
#	si le chemin du fichier contient un raccourci
	fichier = raccourcis (fichier)
#	preparer le texte pour le rendre plus clair
	texte = texte.strip()
	texte = texte.replace ('\r', "")
#	pas de texte, ""
	if not texte:
		print 'rien a ecrire'
		return
#	si le fichier existe et qu'on veut conserver l'ancien texte
	if mode == 'a' and os.path.isfile (fichier): texte ='\n'+ texte
#	ouvrir le fichier et ecrire le texte
	texteBrut = open (fichier, mode)
	texteBrut.write (texte)
	texteBrut.close()

def majuscule (texte):
	""" rajouter des majuscules dans un texte au format str
	argument: un texte au format str
	retourne: le texte avec des majuscules apres les points
	pour eviter d'avoir une majuscule apres un point, ecrire deux espaces
		coucou. vous allez bien ?	va devenir	Coucou. Vous allez bien ?
		coucou.  vous allez bien ?	va devenir	Coucou. vous allez bien ?
		le double espace est transforme en espace simple
	"""
#	mettre le texte en forme pour simplifier sa transformation
	while '\n\n' in texte: texte = texte.replace ('\n\n', '\n')
	while '_____' in texte: texte = texte.replace ('_____', '____')
#	rajouter des majuscules en debut de texte
	texte = texte[0].upper() + texte[1:]
#	"dictionnaire" des majuscule prenant en compte les accents
	accents =( ('a','A'), ('\xe0','A'), ('b','B'), ('c','C'), ('\xe7','\xc7'), ('d','D'), ('e','E'), ('\xe8','E'), ('\xe9','E'), ('\xea','E'), ('\xeb','E'), ('f','F'), ('g','G'), ('h','H'), ('i','I'), ('\xee','I'), ('\xef','I'), ('j','J'), ('k','K'), ('l','L'), ('m','M'), ('n','N'), ('o','O'), ('\xf4','\xe4'), ('p','P'), ('q','Q'), ('r','R'), ('s','S'), ('t','T'), ('u','U'), ('v','V'), ('w','W'), ('x','X'), ('y','Y'), ('z','Z') )
#	liste des points, des chaines de caracteres suivies par une majuscule
	points =( '\n', '. ', '! ', '? ', ': ', '\t- ', '\n____ ', '\n--- ', '\n---- ', '\n_ ')
#	rajouter les majuscules apres chaque point
	for p in points:
		for i,j in accents: texte = texte.replace (p+i, p+j)
#	transformer les doubles espaces
	while '  ' in texte: texte = texte.replace ("  ", " ")
	artefacts =( ('> ','>'), ('\n ','\n'), (' \n','\n'), ('Http','http') )
	for i,j in artefacts: texte = texte.replace (i,j)
	return texte

def float_to_str (nb):
	""" objectif: simplifier les nombres qui seront ecris, afin d'en faciliter la lecture. 10.0836 --> "10.1", 10.002 --> 10
	action:
		transforme un nombre, int ou float en str
		les float sont arrondi a la premiere decimale
	argument: le nombre
	retourne: la chaine de carcteres correspondant au nombre
	l'arrondi vaut 1
	"""
#	arrondir les float
	if type (nb) == float: nb = round (nb,1)
#	convertir le nb en str
	nb = str (nb)
#	transformer 10.0000 en 10
	nb = nb.rstrip ('0')
	nb = nb.rstrip ('.')
	return nb


""" ____________________________________ les actions ____________________________________ """


# on appele ce script dans un autre script
if argv[0] != 'dpowers_txt.py': pass
# mettre des majuscules dans un texte
elif len (argv) >=2:
	fichier = argv[1]
	texte = lire (fichier)
	texte = majuscule (texte)
	ecrire (fichier, texte, 'w')
# le nom du fichier n'a pas ete donne
else: print help


