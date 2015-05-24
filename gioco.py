#!/usr/bin/ python
# -*- coding: utf-8 -*-
import os 
os.system("clear")
print "Pulitica"
print "Il gioco in cui devi entrare in parlamento e vincere le elezioni!"
print "Basato su 'Fuga col malloppo'
import random
turno = 1
elettori = 15
flop = 0
sindaci = 45
ele1 = 50
ele2 = 40
eleap = 5
parlamento = ele1 + ele2 + eleap + elettori
# deputati = 50
print """ Benvenuto. L'assemblea del Partito Indipendente Milanese ti ha nominato Presidente. Siamo un piccolo partito con un peso minimo nella politica milanese, ma ti abbiamo scelto per far crescere il nostro partito e renderlo uno dei primi. Il nostro obiettivo è di eleggere il Capo dello Stato"""
print " Gioco creato da Sciking"
tuonome = raw_input("Come ti chiami, Presidente?: ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def poss():
	print "L'Indipendente di Milano"
	global elettori
	global flop
	global ele1
	global ele2
	global parlamento
	global eleap
	global sindaci
	#global deputati
	poss = random.randint(1,25)
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
		parlamento = ele1+ele2+eleap+elettori
		print elettori, "nostri deputati al Parlamento su", parlamento
		gioco()
	elif poss == 5:
		print "Voto nella Dichiarazione di Guerra: Il tuo partito è favorevole, il popolo apprezza"
		elettori = elettori + 3
		ele1 = ele1 - 4
		ele2 = ele2 + 1
		gioco()
	elif poss == 6:
		print "
	elif poss == 7:
		print "Il tuo fornitore sammarinese ti fa degli sconti per l'abbassamento dell'IVA locale. Prendi il 10% dei tuoi soldi"
		soldi = soldi*1.10
		gioco()
	elif poss == 8:
		print "Aumenta l'IVA. Perdi il 3 % dei tuoi soldi"
		gioco()
	elif poss == 9:
		print "Vieni recensito da un blog famoso e ottieni molti nuovi ordini!"
		soldi = soldi*1.5
		gioco()
	elif poss == 10:
		print "Paghi 5000€ un noto blogger per ottenere una buona recensione"
		soldi = soldi - 50000
	elif poss == 11:
		print "Un uomo travestito da panino che fa versi da scimmia vicino a", nome,"fa divertire i turisti"
		gioco()
	elif poss == 12:
		print "Vai in un postribolo d'alto bordo con un tuo fornitore. Spendi 1500€"
		soldi = soldi - 1500
		gioco()
	elif poss == 13:
		print "Trovi 688€ davanti al negozio"
		soldi = soldi + 688
		gioco()
	elif poss == 14:
		print "Tuo figlio vince la gara di rutti in dialetto indetta dalla scuola"
		gioco()
	elif poss == 15:
		print "Ottieni un rimborso IVA di 2500€"
		soldi = soldi + 2500
		gioco()
	elif poss == 16:
		print "Hai immatricolato male il veicolo, vieni multato dalla Polizia"
		soldi = soldi*0.97
		gioco()
	elif poss == 17 and evadi < 40:
		print "Sei stato denunziato per attività scorrette"
		print "Sei multato per 100000€"
		soldi = soldi - 100000
		gioco()
	elif poss == 18 and evadi > 50:
		print "Hai vinto un premio di stato di 25000€"
		soldi = soldi + 25000
		gioco()
	elif poss == 19:
		print "Vinci 1000 € alla lotteria"
		soldi = soldi +1000
		gioco()
	elif poss == 20:
		print "Fallisci investimenti. Perdi il 30% dei tuoi soldi"
		soldi = soldi*0.7
		gioco()
	else:
		gioco()
	gioco()
	
def gioco():
	global turno
	global elettori
	global ele1
	global ele2
	global eleap
	global sindaci
	global parlamento
	print "Turno", turno
	print "hai", elettori, "elettori"
	print "Parlamentari", elettori, "/", parlamento
	print "Sindaci", sindaci, "/250"
	turno = turno +1 
	poss()
gioco()		
