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
deputati = 50
print """ Benvenuto. L'assemblea del Partito Indipendente Milanese ti ha nominato Presidente. Siamo un piccolo partito con un peso minimo nella politica milanese, ma ti abbiamo scelto per far crescere il nostro partito e renderlo uno dei primi. Il nostro obiettivo è di eleggere il Capo dello Stato"""
print " Gioco creato da Sciking"
tuonome = raw_input("Come ti chiami, Presidente?: ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def poss():
	print "L'Indipendente di Milano"
	global elettori
	global flop
	global sindaci
	global deputati
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
			print "Elezioni Comunali: Buoni risultati, a noi 20 sindaci"
			sindaci = sindaci + 20
			gioco()
	elif poss == 3:
		print "Elezioni Comunali: Flop del nostro partito"
		soldi = sindaci - 10
		flop = flop + 1
		gioco()
	elif poss == 4:
		print "Rinnovo straordinario del nostro Parlamento"
		
		gioco()
	elif poss == 5:
		print "Riesci a truffare il fisco per 15000€, ma per evitare l'arresto fuggi in Svizzera."
		print "Benvenuto in Svizzera, signor", tuonome
		print "La polizia ha chiuso", nome, "al turno", turno
		soldi = soldi + 15000
		print "Hai ottenuto", soldi
		exit()
	elif poss == 6:
		print "Tenti di andare in Slovenia per ripulire soldi"
		print "Buongiorno signore"
		print "Lei è in stato di fermo"
		print "La polizia slovena arresta", tuonome,	"e fa chiudere", nome
		print "Sono stati sequestrati Euro", soldi
		exit()
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
	print nome, "di", tuonome, "- Sistema Informatico"
	print "Turno", turno
	print "Hai", ordtot, "ordini"
	spesa = random.randint(180,245)
	print "Ogni ordine ti frutta 200€. Tu per evadere un ordine ne spendi", spesa
	soldi = soldi + (nuovo * 200)
	try:
		while evadi <= 0:
			evadi = input("Quanti ordini vuoi evadere?")
	except SyntaxError or NameError:
		print "Errore!"
		os.system("clear")
		global soldi
		global nuovi
		os.system("clear")
		ordtot = ordtot - nuovi
		soldi = soldi - (nuovo*200)
		gioco()
	ordtot = ordtot-evadi
	soldi = soldi - (spesa*evadi)
	print "Ora hai", soldi, "Euro"
	svizzera = raw_input("Scrivi scappa e premi ok per scappare in Svizzera. Costerà 1/3 del tuo budget.: ")
	raw_input("Clicca su invio per continuare")
	turno = turno +1 
	if soldi < -2500:
		l = random.randint(1,6)
		if l == 3:
			print "sono un anonimo benefattore e salverò la tua azienda"
			soldi = 1000
			poss()
		else:
			print "Gendarmeria Fiscale. Lei è in arresto per fallimento"
			print "La Gendarmeria Fiscale ha chiuso", nome
			print tuonome, "viene scarcerato subito e non potrà avviare imprese per 5 anni"
			exit()
	while ordtot > evadi*6 or evadi < 30 and soldi > 50000:
		k =random.randint(1,10)
		print k 
		if k == 8:
			print "Buongiorno Polizia"
			print "Sono state segnalate irregolarità nel suo negozio"
			print "Lei è stato denunziato e il suo negozio verrà chiuso"
			print nome, "è stato chiuso al turno", turno, "dalla Polizia che ha sequestrato Euro", soldi
			print tuonome, "viene arrestato il giorno dopo dalla Polizia per truffa"
			exit()
		elif k == 2:
			print "Buongiorno Gendarmeria fiscale"
			print "Lei ha commesso reati fiscali!"
			print "Paga il 5% per coprire tutto"
			soldi = soldi*0.95
			raw_input("premi invio per continuare")
			os.system("clear")
			poss()
		else:
			os.system("clear")
			poss()
	else:
		os.system("clear")
		poss()
gioco()		
