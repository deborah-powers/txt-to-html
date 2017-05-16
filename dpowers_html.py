#!/usr/bin/python2.6
# modules python
import os
from sys import argv
# modules dpowers
import dpowers_txt as fl

help ="""
dependances:
	le module os de python
	le module sys de python
	le module dpowers_txt de deborah-powers
contient plein de fonctions:

texte = creer_liste (texte)
	argument: un texte au format str contenant des listes
	retourne: le texte dans lequel les listes ont ete transformees en liste non ordonnees html
	on peut faire des listes imbriquees.
	exemple de liste:
je vais faire mes courses:
	lait
	oeuf
	legumes
		haricots verts
		carottes
	yaourt
voila, j'ai tout trouve.
_____________________________________________________________________________________________


texte = creer_table (texte)
	argument: un texte au format str contenant des tableaux
	retourne: le texte dans lequel les tableaux ont ete transformees en  tableaux html simples
	exemple de tableau:
les cadeaux de Noel:
Huguette	un pull quitch
Sebastien	un stylo
Jean-Marc	un souvenir des dernieres vacances
j'espere que je n'ai oublie personne

texte = modif_texte (texte)
	argument: un texte au format str. le texte utilise ma mise en page
	retourne: le texte transforme en texte html. ma mise en page a ete transformee en balises.
	exemple de texte:

____________________
____ chapitre 1 ____

quelle est la mise en page a utiliser


____ sous-chapitre 11 ____

inclure une image
img	fichier/image.jpg


____ sous-chapitre 12 ____

creer un tableau
case11	case12	case13
case21	case22	case23


____ sous-chapitre 13 ____

creer une liste
	element 1
	element 2
		element 21
		element 22
	element 3

____________________
____ chapitre 2 ____

les sous chapitres

____ sous-chapitre 2 ____

--- sous-chapitre 3 ---

---- sous-chapitre 4 ----

comment ajouter une barre horizontale
____
une ligne d'au moins quatre underscores
_____________________________________________________________________________________________


txt_to_html (fichier_txt, fichier_css=None):
	arguments:
		un fichier .txt contenant un texte avec ma mise en forme
		(facultatif) un fichier .css contenant les styles a appliquer
	retourne: un fichier .html contenant le texte

utiliser le script:
	python dpowers_html.py fichier.txt [fichier.css]
"""

# balises
balises =( (' ____\n', '</h1>\n'), ('\n____\n____ ', '\n<h1>'), ('\n____ ', '\n<h2>'), ('\n--- ', '\n<h3>'), (' ---\n', '</h3>\n'), ('\n---- ', '\n<h4>'), (' ----\n', '</h4>\n'), ('\n____\n', '\n<hr>\n'), ('\nImg\t', "\n<img src='") )
balises_internes = ('span', 'em', 'i', 'strong', 'b')
balises_externes = ('div', 'ul', 'table', 'math', 'figure')
balises_medianes = ('p', 'li', 'tr', 'figcaption', 'h1', 'h2', 'h3', 'h4', 'hr', 'img')


def creer_liste (texte):
	"""
	argument: un texte au format str contenant des listes
	retourne: le texte dans lequel les listes ont ete transformees en liste non ordonnees html
	on peut faire des listes imbriquees.
	exemple de liste:
je vais faire mes courses:
	lait
	oeuf
	legumes
		haricots verts
		carottes
	yaourt
voila, j'ai tout trouve.
	"""
#	ajouter les balises ouvrantes des elements de la liste
	texte = '\n'+ texte +'\n'
	texte = texte.replace ('\n\t', '\n<li>')
#	separer les lignes pour permettre leurs transformation
	list_chn = texte.split ('\n')
	lc= range (len( list_chn))
#	rajouter les balises fermantes
	for l in lc:
		if '<li>' in list_chn[l]: list_chn[l] = list_chn[l] +'</li>'
	lc= range (1, len( list_chn) -1)
#	rajouter les balises ouvrantes et fermantes delimitant la liste, <ul/>. reperer les listes imbriquees.
	for l in lc:
		if '<li>' in list_chn[l]:
#			compter le niveau d'imbrication (n) de l'element list_chn[l]
			n=0
			while '<li>'+n*'\t' in list_chn[l]: n+=1
			n-=1
			if '<li>'+n*'\t' in list_chn[l]:
#				debut de la liste (ou sous-liste), mettre le <ul>
				if '<li>'+n*'\t' not in list_chn[l-1]: list_chn[l] = '<ul>'+ list_chn[l]
#				fin de la liste (ou sous-liste), mettre le </ul>
				if '<li>'+n*'\t' not in list_chn[l+1]:
					while n >-1:
						if '<li>'+n*'\t' not in list_chn[l+1]: list_chn[l] = list_chn[l] + '</ul>'
						n-=1
#	reunir les lignes
	texte ='\n'.join (list_chn)
#	mettre le texte au propre
	texte = texte.strip ('\n')
	while '<li>\t' in texte: texte = texte.replace ('<li>\t', '<li>')
	while '<ul>\t' in texte: texte = texte.replace ('<ul>\t', '<ul>')
	return texte

def creer_table (texte):
	"""
	argument: un texte au format str contenant des tableaux
	retourne: le texte dans lequel les tableaux ont ete transformees en  tableaux html simples
	exemple de tableau:
les cadeaux de Noel:
Huguette	un pull quitch
Sebastien	un stylo
Jean-Marc	un souvenir des dernieres vacances
j'espere que je n'ai oublie personne
	"""
#	separer les lignes pour permettre leurs transformation
	list_chn = texte.split ('\n')
	len_chn = len (list_chn)
	d=-1 ; c=-1 ; i=0
	while i< len_chn:
#		rechercher une table
		d=-1 ; c=-1
		if d==-1 and c==-1 and '\t' in list_chn[i]:
			c= list_chn[i].count ('\t')
			d=i ; i+=1
		while list_chn[i].count ('\t') ==c: i+=1
		c=i-d
#		une table a ete trouve
		if c>1 and d>0:
			rtable = range (d,i)
			for j in rtable:
#				entre les cases
				list_chn[j] = list_chn[j].replace ('\t', '</td><td>')
#				bordure des cases
				list_chn[j] = '<tr><td>' + list_chn[j] +'</td></tr>'
#			les limites de la table
			list_chn[d] = '<table>\n' + list_chn[d]
			list_chn[i-1] = list_chn[i-1] +'\n</table>'
		i+=1
	texte ='\n'.join (list_chn)
	return texte

def modif_texte (texte):
	"""
	argument: un texte au format str. le texte utilise ma mise en page
	retourne: le texte transforme en texte html. ma mise en page a ete transformee en balises.
	exemple de texte:

____________________
____ chapitre 1 ____

quelle est la mise en page a utiliser


____ sous-chapitre 11 ____

inclure une image
img	fichier/image.jpg


____ sous-chapitre 12 ____

creer un tableau
case11	case12	case13
case21	case22	case23


____ sous-chapitre 13 ____

creer une liste
	element 1
	element 2
		element 21
		element 22
	element 3

____________________
____ chapitre 2 ____

les sous chapitres

____ sous-chapitre 2 ____

--- sous-chapitre 3 ---

---- sous-chapitre 4 ----

comment ajouter une barre horizontale
____
une ligne d'au moins quatre underscores
	"""
#	ajouter les majuscules
	texte = '\n'+ texte +'\n'
	texte = fl.majuscule (texte)
#	transformer la mise en page en balises
	for i,j in balises:
		if i in texte: texte = texte.replace (i,j)

#	ajustement pour les titres 2 et les images
	list_chn = texte.split ('\n')
	lc= range (len (list_chn))
	for i in lc:
		if '<h2>' in list_chn[i]: list_chn[i] = list_chn[i].replace ('</h1>', '</h2>')
		elif '<img' in list_chn[i]: list_chn[i] = list_chn[i] +"'/>"
	texte = '\n'.join (list_chn)
#	les tableaux et les listes
	if '\n\t' in texte: texte = creer_liste (texte)
	if '\t' in texte: texte = creer_table (texte)

#	nettoyer le texte pour faciliter la suite des transformations
	texte = texte.strip()
	texte = texte.replace ('\t', "")
	while '\n\n' in texte: texte = texte.replace ('\n\n', '\n')
	while '  ' in texte: texte = texte.replace ('  ', ' ')

#	rajouter les <p/>
	texte = texte.replace ('\n', '</p><p>')
	texte = texte.replace ('></p><p><', '><')
	texte = texte.replace ('></p><p>', '><p>')
	texte = texte.replace ('</p><p><', '</p><')
#	rajouter d'eventuel <p/> s'il n'y a pas de balise en debut ou fin de texte
	if '<' not in texte[0:3]: texte = '<p>'+ texte
	if '>'not in texte[-3:]: texte = texte +'</p>'

#	mettre en forme les balises pour clarifier le texte
	for b in balises_externes:
		texte = texte.replace ('<'+b+' ', '\n\t<'+b+' ')
		texte = texte.replace ('<'+b+'>', '\n\t<'+b+'>')
		texte = texte.replace ('</'+b+'>', '\n\t</'+b+'>')
	for b in balises_medianes:
		texte = texte.replace ('><'+b, '>\n<'+b)
		texte = texte.replace ('</'+b+'><', '</'+b+'>\n<')
	return texte


def txt_to_html (fichier_txt, fichier_css=None):
	"""
	arguments:
		un fichier .txt contenant un texte avec ma mise en forme
		(facultatif) un fichier .css contenant les styles a appliquer
	retourne: un fichier .html contenant le texte
	"""
#	transformer le texte en texte html
	texte = fl.lire (fichier_txt)
	texte = modif_texte (texte)
#	titre du fichier
	f= fichier_txt.rfind (os.sep) +1	# reperer le debut du nom du fichier
	titre = fichier_txt[f:-4]
#	creer le contenu du fichier html
	contenu_html = """<!DOCTYPE html><html><head>
<title>%s</title>
</head><body>
%s
</body></html>""" %( titre, texte)
#	si un fichier css a ete precise
	if fichier_css:
		feuille_style = "<link rel='stylesheet' href='%s'>\n" % fichier_css
		f= contenu_html.find ('</head>')
		contenu_html = contenu_html[:f] + feuille_style + contenu_html[f:]
#	creer le fichier html
	fichier_html = fichier_txt[:-4] +'.html'
	fl.ecrire (fichier_html, contenu_html, 'w')





# on appele ce script dans un autre script
if argv[0] != 'dpowers_html.py': pass
# transformer un texte simple en texte html
elif len (argv) >=2:
	fichier = argv[1]
	fichier_css =None
	if len (argv) >=3: fichier_css = argv[2]
	txt_to_html (fichier, fichier_css)
# le nom du fichier n'a pas ete donne
else: print help


