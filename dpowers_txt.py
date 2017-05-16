#!/usr/bin/python2.6
# modules python
import os
from sys import argv


help ="""
dependances:
	le module os de python
	le module sys de python
contient trois fonctions:

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

ce script peut etre appele dans d'autres scripts
si vous ne voulez que rajouter des majuscules dans un texte:
	python dpowers_txt.py fichier
"""

def lire (fichier):
	""" ouvrir un fichier .txt, recuperer le texte dans une chaine de caractere
	argument: le nom du fichier, avec le chemin
	retourne: le texte
	"""
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
	texte = texte.strip()	# preparer le texte pour le rendre plus clair
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


