#!/usr/bin/ python
# -*- coding: utf-8 -*-
import os 
os.system("clear")
print "Pulitica"
print "Il gioco in cui devi entrare in parlamento e vincere le elezioni!"
print "Basato su 'Fuga col malloppo'"
import random
turno = 1
elettori = 15
flop = 0
sindaci = 45
ele1 = 50
deputati = 15
ele2 = 40
eleap = 5
leggi = ["contro l'omofobia", "per l'introduzione del lombardo nelle scuole", "contro la ciarlataneria", "per la democrazia diretta", "contro l'obbligo militare", "per l'allungamento dell'obbligo scolastico", "contro le pantofole", "per la sicurezza scolastica", "per l'abolizione del reato di stupro", "per l'illegalità del comunismo"]
parlamento = ele1 + ele2 + eleap + elettori
# deputati = 50
print """ Benvenuto. L'assemblea del Partito Indipendente Milanese ti ha nominato Presidente. Siamo un piccolo partito con un peso minimo nella politica milanese, ma ti abbiamo scelto per far crescere il nostro partito e renderlo uno dei primi. Il nostro obiettivo è di eleggere il Capo dello Stato"""
print " Gioco creato da Sciking"
nome = raw_input("Come ti chiami, Presidente?: ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def poss():
	print "L'Indipendente di Milano"
	global elettori
	global flop
	global ele1
	global deputati
	global ele2
	global parlamento
	global eleap
	global sindaci
	#global deputati
	poss = random.randint(1,20)
	if poss == 1:
		print "Sindaco del Patrito liberale diserta nel Partito Indipendente"
		sindaci = sindaci + 1
		gioco()
	elif poss == 2:
		if elettori > 35:
			print "Elezioni Comunali: Eletti molti sindaci e il Sindaco di Milano!"
			sindaci = sindaci+ 25
			gioco()
		else:
			print "Elezioni Comunali: Flop del nostro partito"
			soldi = sindaci - 10
			flop = flop + 1
			gioco()
	elif poss == 3:
			print "Elezioni Comunali: Buoni risultati, a noi 20 sindaci"
			sindaci = sindaci + 20
			gioco()
	elif poss == 4:
		print "Rinnovo straordinario del nostro Parlamento"
		parlamento = (ele1+ele2+eleap+elettori)-10
		deputati = elettori
		print elettori, "nostri deputati al Parlamento su", parlamento
		gioco()
	elif poss == 5:
		print "Voto nella Dichiarazione di Guerra: Il tuo partito è favorevole, il popolo apprezza"
		elettori = elettori + 3
		ele1 = ele1 - 4
		ele2 = ele2 + 1
		gioco()
	elif poss == 6:
		print "Arrestato un nostro sindaco!"
		print "Perderemo sicuramente elettorato!"
		sindaci = sindaci - 2
		elettori = elettori -2 
		gioco()
	elif poss == 7:
		print "Una nostra mozione al Parlamento per diminuire le tasse passa! Il Popolo è soddisfatto."
		elettori = elettori + 2
		sindaci = sindaci + 3
		gioco()
	elif poss == 8:
		print "Alleanza con un partito minore. Ottieniamo i loro sindaci e i loro elettori."
		elettori = elettori + (eleap/2)
		sindaci = sindaci + 4
		gioco()
	elif poss == 9:
		print "Alleanza con un partito Svizzero. Sindaci felici ma elettori meno."
		sindaci = sindaci + 2
		elettori = elettori - 1
		gioco()
	elif poss == 10:
		print "La prostituzione legale è legge, grazie a noi"
		elettori = elettori + 8
		gioco()
	elif poss == 11:
		print "I giudici riescono a condannare l'imputato della strage di 3 anni fa: Ergastolo!"
		gioco()
	elif poss == 12:
		print "OGM consentiti, è legge. I sindaci non approvano la legge unanime"
		elettori = elettori +1
		sindaci = sindaci +2
		gioco()
	elif poss == 13:
		print "Noi contro i sindaci"
		print "Per i sindaci, diminiure i loro poteri è deleterio, ma gli elettori apprezzano"
		elettori = elettori + 5
		sindaci = sindaci - 4
		gioco()
	elif poss == 14:
		print "Parlamento: È flop"
		print "Pochissimi elettori per noi alle parlamentari"
		elettori = elettori - 5
		sindaci = sindaci - 1
		flop = flop + 1
		gioco()
	elif poss == 15:
		print "Grazie a noi la libertà sopravive"
		print "La satirà sarà ancora libera"
		elettori = elettori +2
		gioco()
	elif poss == 16:
		print "Guerra in Arabia", nome, ": 'Si tratti con diplomazia'"
		elettori = elettori + 2
		gioco()
	elif poss == 17:
		print "Alea iacta est"
		print "Finalmente alleati, cosa ne penserà l'elettorato?"
		elettori = elettori + random.randint(-2,3)
		gioco()
	elif poss == 18:
		print "Rivolte: I Ghisa antisommossa gestiscono benissimo la situazione"
		if parlamento/deputati < 2 and turno%2 == 0:
			elettori = elettori + 2
		gioco()
	elif poss == 19:
		print "L'Ambasciatore a Barcellona è Indipendente!"
		elettori = elettori + 2
		sindaci = sindaci - 1
		gioco()
	elif poss == 20:
		print "I nostri sindaci sono i peggiori, dice uno studio"
		elettori = elettori - random.randint(1,4)
		gioco()
	gioco()
	
def gioco():
	global turno
	global elettori
	global ele1
	global ele2
	global eleap
	global sindaci
	global nome
	global flop
	global parlamento
	global deputati
	print ""
	print ""
	print ""
	if turno%5 == 0:
		deputati = elettori
		if parlamento/deputati < 2 and flop < 2:
			print """Salve signor presidente.
Lei non ci serve più come presidente. Siamo riusciti ad eleggere il Capo dello Stato e abbiamo scelto Lei come nostro nuovo Capo. Governi bene in questi due anni!"""
			print "Onori al Capo dello Stato", nome, "!"
			exit()
			#capostato()
		elif parlamento/deputati < 2:
			print "Salve, Presidente. Abbiamo eletto il nostro nuovo presidente. Aumenterà i nostri elettori."
			elettori = elettori + 10
			sindaci = sindaci + 10
	if parlamento/deputati < 2 and turno%2 == 0:
		print "Hai eletto il governo!"
		flop = 0
		elettori = elettori + 3
	print "Turno", turno
	print "hai", elettori, "elettori"
	print "Parlamentari", deputati, "/", parlamento
	print "Sindaci", sindaci, "/250"
	print "LEGGE DEL GIORNO:"
	r = random.randint(1,9)
	print "legge", leggi[r]
	scelta = raw_input("Vuoi approvare la legge?")
	scelta = scelta.lower
	if scelta == "si":
		elettori = elettori + random.randint(-4,4)
		ele1 = ele1 + random.randint(-4,4)
		ele2 = ele2 + random.randint(-4,4)
		eleap = eleap + random.randint(-4,4)
	else:
		elettori = elettori + random.randint(-3,3)
		ele1 = ele1 + random.randint(-3,3)
		ele2 = ele2 + random.randint(-3,3)
		eleap = eleap + random.randint(-3,3)
	opzioni = ["si", "no", "si", "no"]
	j = random.randint(0,3)
	opz = opzioni[j]
	if opz == "si":
		print "Legge approvata!"
		elettori = elettori + 1
		#del legge[r]
	else:
		print "Legge respinta"
		elettori = elettori - 1

	turno = turno +1 
	if sindaci > 240:
		print "Grazie Presidente, vogliamo mandarti in campo! Hai vinto, possediamo quasi tutti i comuni ora. Abbiamo eletto il Capo Dello Stato con maggioranza dei comuni e sei tu l'attuale Capo dello Stato. Governa bene!"
		exit()
		
	if flop > 5:
		print "Hai sbagliato troppe volte, mi spiace. Sei licenziato"
		exit()
	os.system("clear")
	poss()
gioco()		
