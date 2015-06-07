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
r = 1
sindaci = 300
difficile = "abc" 
ele1 = 50
decas = 0
ele2 = 40
altripaesi = ["Impero di Roma","Puglia","Lazio e Campania","Stato della Chiesa"]
eleap = 5
dichiarazionipol = ["Creeremo il sistema presidenziale"]
dichiarazionieco = ["Abbasseremo le tasse"]
dichiarazionieti = ["Si all'aborto incondizionato","La vera vittoria non è introdurre il matrimonio gay, ma abolirlo per tutti!" ]
dichiarazionialtro = ["Milano vincerà i mondiali del folball!"]
gloc = elettori*18/(elettori+ele1+ele2+eleap)
gloca = int(gloc*random.random())
nomi = ["Mario","Alessio","Gaetano","Alessandro","Michele","Giorgio","Matteo","Silvio","Alberto","Gianni","Teresio","Ambrogio","Anselmo","Giovese","Bortolo","","Piergastone","Diego","Giulio","Giuàn","Azeglio","Adolfo","Benito","Natale","Nazareno",""]
cognomi = ["Brambilla","Fumagalli","Rossi","Verdi","Pessotti","Bianchi","Bernasca","Salvino","Sensi","Bellotti","Conti","Invernizzi","Nicolello","Legramandi","Olivetti","Vignana","Carminati","Colombo","Lombardi","Basile","Degasperi","Culot","Toccaferro","Perazzini","Mussolesi","Schavòn"]
sd = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
ss = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
premier = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
si = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
pa = ["Partito Liberale", "Lega Milanese", "Unione Popolare", "Movimento delle Libertà", "Casa Riformista", "Il Lume della Ragione","Patrito contro le Pantofole con Michele Redeisci", "Casa delle Riforme", "Föra di ball! Milano Libera"]
pb = ["Milano Rossa", "Partito Ecologista", "Lega dei Contadini", "Partito per le frontiere aperte", "Progressismo è Democrazia", "Rivoluzione Popolare", "MoviMento Quattro Soli", "Equità nelle ricchezze", "Alleanza di Sinistra"]
destra = pa[random.randint(0,8)]
sinistra =  pb[random.randint(0,8)]
leggi = ["contro l'omofobia", "per l'introduzione del lombardo nelle scuole", "contro la ciarlataneria", "per la democrazia diretta", "contro l'obbligo militare", "per l'allungamento dell'obbligo scolastico","per creare un testo all'Inno Nazionale","per proibire la Lingua Inglese","per la beatificazione di Freddie Mercury","per aumentare le pensioni","per abolire la canapa a Milano", "contro le pantofole", "per la sicurezza scolastica", "per l'abolizione del reato di stupro","per l'insegnamento del russo","per diminuire l'età pensionabile","per ufficializzare la lingua piemontese","per collegare Milano a Varese via Navigli","per collegare via fiume Milano e Ivrea","per creare una rete sociale di stato","per migliorare le armi dei ghisa","per esportare la piadina romagnola nel mondo","per costruire una Reggia Presidenziale a Codigoro","contro il plagio", "per l'illegalità del popolarismo", "per i diritti civili","per abolire le religioni", "per creare la Regione Autonoma Emiliana", "per l'istituzione delle regioni","contro il reato di furto con scasso","contro le mense sporche", "per abolire i videogiochi violenti","per l'elezione diretta del Premier","contro il veganismo","contro le infiltrazioni malavitose nelle amministrazioni locali","contro l'estremismo religioso","contro il complottismo","per abbassare le tasse indirette","per migliorare gli ospedali","per abolire i giornali erotici","per la prevenzione dell'obesità","per l'introduzione del matrimionio incestuoso","per l'ufficializzazione della lingua lombarda","contro la prostituzione minorile","per aprire un centro di integrazione per gli immigrati","per dare un premio di 500 Ambrogi ai collezionisti","contro le droghe pesanti","per promuovere la cura dalla ludopatia","contro i prof politicizzati","per ridurre l'inquinamento","per favorire le lobby del tabacco","per costruire una statua della Perottina a Pregnana","per tutelare il risotto alla milanese","per aumentare le ore di educazione sessuale","per punire la bestemia","per abolire le scarpe col tacco","per diminuire le tasse","per aumentare le pene per omicidio stradale","per insegnare la buona educazione ai bambini","contro il nomadismo","per le pari opportunità","per lo ius soli","per alzare il prezzo delle sigarette","per mettere nuove misure di sicurezza ai danè","per contrastare il razzismo","per introdurre la prigione per vandalismo","per aiutare i milanesi prima degli altri","per la limitazione delle armi bianche","per migliorare l'esercito di milizia","per aumentare l'autonomia federale alla Repubblica Friulana","contro le nudità all'Idroscalo","per introdurre","contro le droghe","contro il software proprietario","contro la pirateria informatica","per le adozioni ai single e ai gay","per la libera associazione della Sicilia a Milano","per il disarmamento dei ghisa","contro le droghe leggere","Per regolare l'immigrazione dall'Est Europa","Per l'introduzione dei Permessi d'Accesso","per introdurre le console da videogioco a scuola","contro il gimnopodismo","per l'eliminazione delle zanzare","per fornire ai cittadini buoni gratis per il postribolo.","per proibire l'alcole","per aumentare i finanziamenti alle scuole","per abolire le scuole private", "contro le sculacciate",]
emergenza = tuple(leggi)
parlamento = 220
deputati = elettori*parlamento/(elettori+ele1+ele2+eleap)# elettori : totale = x : parlamento
depd = ele1*parlamento/(elettori+ele1+ele2+eleap)
deps = ele2*parlamento/(elettori+ele1+ele2+eleap)
depa = eleap*parlamento/(elettori+ele1+ele2+eleap)
# deputati = 50
print """ Benvenuto. L'assemblea del Partito Indipendente Milanese, visti i tuoi eccellenti 10 anni di carriera tutta nel PIM, ti ha nominato Presidente. Siamo un piccolo partito con un peso minimo nella politica milanese, ma ti abbiamo scelto per far crescere il nostro partito e renderlo uno dei primi. Il nostro obiettivo è di eleggere il Capo dello Stato. Ricorda che noi siamo la terza sponda: A metà tra la sinistra e la destra. Conserva questo ideale, ma non dimenticarlo: Il mondo cambia."""
print " Gioco creato da Sciking"
#difficile = raw_input("Vuoi giocare in modalità facile, medio o difficile? ")
#difficile = difficile.lower()
nome = raw_input("Come ti chiami, Presidente?: ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def poss():
	global elettori
	global flop
	global ele1
	global deputati
	global r
	global ss
	global sd
	global si
	global turno
	global ele2
	global leggi
	global parlamento
	global eleap
	global sindaci
	"""if turno > 50 and difficile == "difficile":
		print "Il gioco è finito!"
		exit()
	if turno > 100 and difficile == "medio":
		print "Il gioco è finito!"
		exit()
	if turno > 150 and difficile == "facile":
		print "Il gioco è finito!"
		exit()"""
	"""print "RILASCIA UNA DICHIARAZIONE"
	print "1)", dichiarazionepol[random.randint(0,1)]""" #selezione random
	opzioni = ["si", "no", "si", "no", "no","si"]
	j = random.randint(0,5)
	opz = opzioni[j]
	if opz == "si":
		print "Legge approvata! \n \n"
		elettori = elettori + 1
		del leggi[r] #decommentare quando ci saranno molte leggi
	else:
		print "Legge respinta\n \n"
		elettori = elettori - 1
	
	print "L'Indipendente di Milano"
	#global deputati
	random.shuffle(leggi) #dovrebbe mescolare ad mentulam canis la lista ma el va minga trop ben...
	poss = random.randint(1,45)
	if poss == 1:
		print "Sindaco del Patrito liberale diserta nel Partito Indipendente"
		sindaci = sindaci + 1
		gioco()
	elif poss == 2:
		if elettori > 35:
			print "Elezioni Comunali: Eletti molti sindaci e il Sindaco di Milano!"
			sindaci = sindaci+ 3
			flop = flop - 1
			gioco()
		else:
			print "Elezioni Comunali: Flop del nostro partito"
			sindaci = sindaci - 4
			flop = flop + 1
			gioco()
	elif poss == 3:
			print "Elezioni Comunali: Buoni risultati, a noi altri 5 sindaci"
			sindaci = sindaci + 5
			gioco()
	elif poss == 4:
		print "Scandalo Scommesse nel Calcio"
		print destra,"e Partito Indipendente non ne sono dentro"
		elettori = elettori + 3	
		ele1 = ele1 + 3
		ele2 = ele2 - 5
		gioco()
	elif poss == 5:
		print "Voto nella Dichiarazione di Guerra: Il tuo partito è favorevole, il popolo apprezza"
		if turno % 2 == 0:
			print "Non vi sarà guerra con", altripaesi[random.randint(0,3)], "però"
		else:
			print "Sarà guerra con", altripaesi[random.randint(0,3)]
		elettori = elettori + 3
		ele1 = ele1 + 3
		ele2 = ele2 - 3
		gioco()
	elif poss == 6:
		print "Arrestato un nostro sindaco!"
		print "Perderemo sicuramente elettorato!"
		sindaci = sindaci - 1
		elettori = elettori -2
		gioco()
	elif poss == 7:
		print "Una nostra mozione al Parlamento per diminuire le tasse passa! Il Popolo è soddisfatto."
		elettori = elettori + 2
		sindaci = sindaci + 1
		ele1 = ele1 - 2
		ele2 = ele2 + 2
		gioco()
	elif poss == 8:
		print "Deputato PIM si masturba in piazza"
		print nome, "tenta di salvare in extremis: 'Nulla sia coperto, \n voteremo si alla richiesta di arresto"
		elettori = elettori + random.randint(-4, 1)
		gioco()
	elif poss == 9:
		print "Fast Food: E' rivincita \n Roberto Vicentino: Fa bene, se moderato"
		gioco()
	elif poss == 10:
		print "La prostituzione legale è legge, grazie a noi"
		sindaci = sindaci - 1
		elettori = elettori + 6 #prima era 8... suvvia, non siamo così puttanieri :D
		gioco()
	elif poss == 11:
		print "I giudici riescono a condannare l'imputato della strage di 3 anni fa: Ergastolo!"
		gioco()
	elif poss == 12:
		print "OGM consentiti, è legge. I sindaci non approvano la legge unanime"
		elettori = elettori +1
		sindaci = sindaci + random.randint(-1,1)
		gioco()
	elif poss == 13:
		print "Noi contro i sindaci"
		print "Per i sindaci, diminiure i loro poteri è deleterio, ma gli elettori apprezzano"
		elettori = elettori + 3
		sindaci = sindaci - 2
		gioco()
	elif poss == 14:
		print "Parlamento: È flop"
		print "Pochissimi elettori per noi alle parlamentari"
		elettori = elettori - 3
		sindaci = sindaci - 1
		flop = flop + 1
		gioco()
	elif poss == 15:
		print "Grazie a noi la libertà sopravive"
		print "La satirà sarà ancora libera"
		elettori = elettori +2
		flop = flop - 1
		gioco()
	elif poss == 16:
		print "Guerra al terrorismo.", nome, ": 'Si usi l'atomica'"
		elettori = elettori + 2
		sindaci = sindaci - 1 
		gioco()
	elif poss == 17:
		print "Guardia Liberale entra nel PIM"
		print "L'organizzazione non è ben vista a Milano, ma ha molti votanti"
		elettori = elettori + random.randint(-2,3)
		gioco()
	elif poss == 18:
		print "Rivolte: I Ghisa antisommossa gestiscono benissimo la situazione"
		if parlamento/deputati < 2:
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
		ele1 = ele1 + 2
		ele2 = ele2 + 2
		gioco()
	elif poss == 21:
		print "Segretario", sinistra, ":'gay nei forni'"
		print "Elettori a picco, noi e le destre di certo non siamo tristi"
		ele2 = ele2 - 6
		ele1 = ele1 + 3
		elettori = elettori + 3
		gioco()
	elif poss == 22:
		print "Arrestata moglie del presidente del", destra
		ele1 = ele1 - 2
		ele2 = ele2 + 2
		gioco()
	elif poss == 23:
		print nome, "inciampa e urla 'mad***a troia'"
		print "Forse non è così male..."
		elettori = elettori + random.randint(-1,3)
		ele2 = ele2 + 1
		ele1 = ele1 - 1
		gioco()
	elif poss == 24:
		print "Destra spaccata: Nasce nuovo movimento"
		print "Ne beneficia specialmente", sinistra
		ele1 = ele1 - 8
		ele2 = ele2 + 4
		eleap = eleap + 1
		elettori = elettori + 3
		gioco()
	elif poss == 25:
		print "Elettori sempre più attivi"
		print "Astensionsimo incredibilmente basso"
		ele1 = ele1 + random.randint(1,5)
		ele2 = ele2 + random.randint(1,5)
		eleap = eleap + random.randint(1,5)
		elettori = elettori + random.randint(1,5)
		gioco()
	elif poss == 26:
		print sinistra, "beccata ad accettare mazzette"
		print "Arrestato il segretario: Elettori a picco."
		ele2 = ele2 - random.randint(8,12)
		ele1 = ele1 + random.randint(4,6)
		elettori = elettori + random.randint(4,6)
		gioco()
	elif poss == 27:
		print "Scie idriche: Non sono una minaccia"
		if sinistra == "MoviMento Quattro Soli":
			print "Noi e le destre lo abbiamo detto, ma", sinistra, "grida al complotto"
			elettori = elettori + 1
		elif destra == "Unione Popolare":
			print "Sinistra e PIM unanimi, ma l'UP ha dubbi ambientali"
			ele2 = ele2 + 2
		else:
			print "Partiti concordano unanimi"
		gioco()
	elif poss == 28:
		print "Scandalo nel", destra, ": Manomissioni di farmaci per soldi"
		print "Il PM chiede 9 anni di reclusione per il loro presidente"
		ele1 = ele1 - random.randint(8,12)
		ele2 = ele2 + random.randint(4,6)
		elettori = elettori + random.randint(4,6)
		gioco()
	elif poss == 29:
		print "Giornata nera del PIM: Corruzione, adulterazioni e contrabbando"
		print nome,"multato per 3000 Ambrogi, il segretario condannato a 6 mesi"
		elettori = elettori - 6
		ele1 = ele1 + 2
		ele2 = ele2 + 3
		eleap = eleap + 1
		gioco()
	elif poss == 30:
		print "Fiera del Cosplay a Milano: Partecipa divertito l'Ambasciatore dell'Impero del Giappone"
		print nome, ": 'Bello vedere le nuove generazioni appassionate alla cultura orientale'" #kurumo te lo dedico <3
		gioco()
	elif poss == 31:
		print "Giustino Ciucci a Milano: I Giovani non si recheranno al voto" 
		print "Molto colpiti i partiti che puntano sui giovani"
		ele1 = ele1 - 2
		ele2 = ele2 - 3
		eleap = eleap - 1
		elettori = elettori - 2
		gioco()
	elif poss == 32:
		print "Pena di morte incostituzionale: Noi l'abbiamo detto"
		elettori = elettori + 2
		gioco()
	elif poss == 33:
		print "Droga Leun, nuova piaga: I Partiti uniti per combatterla"
		print "Summit tra", nome,",",ss," e ", sd, "per creare provvedimenti contro le droghe"	
		ele1 = ele1 + 3
		ele2 = ele2 + 3
		eleap = eleap + 1
		elettori = elettori + 3
		gioco()
	elif poss == 34:
		print "Milano vince i campionati mondiali del folball!" #per chi non lo sapesse el folball è il calcio in milanese
	elif poss == 35:
		print "Movimenti in rete: Elettori molto confusi"
		ele1 = ele1 - random.randint(-3,3)
		ele2 = ele2 + random.randint(-3,3)
		elettori = elettori + random.randint(-3,3)
		gioco()
	elif poss == 36:
		print "Segretario Partito Vegan Animalaro: Si spetimenti sui politici"
		print "Candidato Comico dell'anno:", sd, "annunzia querela" #in un paese ideale i vari "STOP VIVISEZZIONE" sarebbero candidati allo stesso premio
		gioco()
	elif poss == 37:
		print "Cura Di Vacio, parlamento approva mozione: Inefficace"
		print "Ma gli elettori non ci credono"
		ele1 = ele1 - 3
		ele2 = ele2 - 3
		eleap = eleap - 1
		elettori = elettori - 3
		gioco()
	elif poss == 38:
		print "Truffa: Mozione del PIM e di", sinistra, "aumenta le pene per truffa a incapaci"
		ele1 = ele1 - 4
		ele2 = ele2 + 3
		eleap = eleap - 1
		elettori = elettori + 2
		gioco()
	elif poss == 39:
		print "Scandalo a Vimodrone"
		if turno%2 == 0:
			print "Sindaco", sinistra, "accetta mazzetta da 20'000 Ambrogi per campo sportivo"
			ele1 = ele1 + 3
			ele2 = ele2 - 5
			elettori = elettori + 2
			gioco()
		else:
			print "Sindaco", destra, "accetta mazzetta da 35'000 Ambrogi per l'ospedale"
			ele1 = ele1 - 5
			ele2 = ele2 + 2
			elettori = elettori - 3
			gioco()
	elif poss == 40:
		print "Governo salva il condannato a morte in Arabia"
		print "Sconterà tre anni a Milano"
		if premier == sd:
			ele1 = ele1 + 3
		if premier == ss:
			ele2  = ele2 + 3
		if premier == nome:
			elettori = elettori + 3
		gioco()
	elif poss == 41:
		print "Corte Friulana: Bestemmia diritto fondamentale"
		print "Chiesto al parlamento di abolire ogni legge contro la bestemmia"
		gioco()
	elif poss == 42:
		print "Governo approva mozione del Consiglio Tecnico: Stanziati 10 milioni di Ambrogi contro il cancro"
		if premier == sd:
			ele1 = ele1 + 4
		if premier == ss:
			ele2  = ele2 + 4
		if premier == nome:
			elettori = elettori + 4
		else:
			ele1 = ele1 + 1
			ele2 = ele2 + 1
			elettori = elettori + 1
		gioco()
	elif poss == 43:
		print "Retata a Cesano Boscone"
		if turno%2 == 0:
			print "Arrestato", ss
			ss = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
			ele2 = ele2 - 10
		elif turno%5 == 0:
			print "Arrestato", si
			si = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
			elettori = elettori - 10
		else:
			print "Arrestato", sd
			sd = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
			ele1 = ele1 - 10
		gioco()
	elif poss == 44:
		print "Olimpiadi: Saranno a Milano"
		if premier == sd:
			ele1 = ele1 + 4
		if premier == ss:
			ele2  = ele2 + 4
		if premier == nome:
			elettori = elettori + 4
		else:
			ele1 = ele1 + 1
			ele2 = ele2 + 1
			elettori = elettori + 1
		gioco()
	elif poss == 45:
		print "Partito Indipendente e", destra, "alleate per qualche mese"
		ele1 = ele1 + 5
		elettori = elettori + 5
		gioco()
		
	gioco()
	
def gioco():
	global turno
	global elettori
	global ele1
	global ele2
	global eleap
	global sindaci
	global r
	global gloc
	global gloca
	global emergenza
	global nome
	global flop
	global deps
	global depa
	global premier
	global depd
	global ss
	global decas
	global sd
	global si
	global sinistra
	global destra
	global parlamento
	global leggi
	global deputati
	print " \n \n"
	if turno%5 == 0:
		deputati = elettori*parlamento/(elettori+ele1+ele2+eleap)# elettori : totale = x : parlamento
		depd = ele1*parlamento/(elettori+ele1+ele2+eleap)
		deps = ele2*parlamento/(elettori+ele1+ele2+eleap)
		depa = eleap*parlamento/(elettori+ele1+ele2+eleap)
		sindaci = elettori*4000/(elettori+ele1+ele2+eleap)
		if parlamento/deputati < 2 and flop < 2 and decas != 0:
			print """Salve signor presidente. Siamo riusciti ad eleggere il Capo dello Stato e abbiamo scelto Lei come nostro nuovo Capo. Governi bene in questi due anni!"""
			print "Onori al Capo dello Stato", nome, "!"
			caput = 1
			decas = 1 #a milano solo un mandato per volta, quindi...
			#capostato()
		elif parlamento/deputati < 2:
			print "Salve, Presidente. Abbiamo eletto il nostro nuovo presidente. Aumenterà i nostri elettori."
			elettori = elettori + 10
			sindaci = sindaci + 3
			caput = 0
			decas = 0
		else:
			caput = 0
			decas = 0
	if turno%5 == 0:
		#calcola chi è al governo
		if parlamento/deputati < 2:
			print "Hai eletto il governo!"
			flop = 0
			elettori = elettori + 3
			if caput == 0:
				premier = nome
			else:
				premier = si
				print "Nominato premier il nostro segretario"
		elif parlamento/depd < 2:
			print "L'Indipendente di Milano \n Destra al Governo"
			ele1 = ele1 + 3
			premier = sd
		elif parlamento/deps < 2:
			print "L'Indipendente di Milano \n Sinistra al governo"
			ele2 = ele2 + 3
			premier = ss
		else:
			print "Nessun eletto: Capo dello Stato nomina governo tecnico"
			premier = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
		
	print "Turno", turno
	print "Capo del Governo:", premier
	print "hai", elettori, "elettori"
	print "Parlamentari Partito Indipendente:", deputati, "/", parlamento
	print "Parlamentari", destra, ":" ,depd, "/", parlamento
	print "Parlamentari", sinistra, ":",deps, "/", parlamento
	print "Parlamentari misti:", depa, "/", parlamento
	print "Sindaci", sindaci, "/4000"
	print "Gov.Locali:", gloca, "/18"
	print "Altri:"
	print "Elettori", destra, ":", ele1
	print "Elettori", sinistra, ":", ele2
	print "LEGGE DEL GIORNO:"
	try:
		r = random.randint(1,6)
		print "Legge", leggi[r]
	except:
		leggi = list(emergenza)
	scelta = raw_input("Vuoi approvare la legge?")
	scelta = scelta.lower
	if scelta == "si":
		elettori = elettori + random.randint(-4,4)
		ele1 = ele1 + random.randint(-4,4)
		ele2 = ele2 + random.randint(-4,4)
		eleap = eleap + random.randint(-2,2)
	else:
		elettori = elettori + random.randint(-3,3)
		ele1 = ele1 + random.randint(-3,3)
		ele2 = ele2 + random.randint(-3,3)
		eleap = eleap + random.randint(-1,1)

	turno = turno +1
		
	if flop > 5 and turno > 25:
		print "Hai sbagliato troppe volte, mi spiace. Sei licenziato \n"
		print "L'Indipendente di Milano \n", nome, "fallisce, ma sarà Sindaco"
		exit()
	if elettori < 2:
		elettori = 10
		flop = flop + 1
	if ele1 < 5:
		destra = pa[random.randint(0,5)]
		ele1 = 15
	if ele2 < 5:
		sinistra =  pb[random.randint(0,5)]
		ele2 = 15
	if eleap < 0:
		eleap = 0
	if turno%25 == 0:
		sd = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
		ss = nomi[random.randint(0,25)]+ " " + cognomi[random.randint(0,25)]
	if turno%4:
		gloc = elettori*18/(elettori+ele1+ele2+eleap)
		coeff = random.random()
		if coeff < 0.5:
			gloca = int(gloc*coeff)
		else:
			gloca = int(gloc*0.5)
		
	os.system("clear")
	poss()
gioco()		# computerblog.ga no alle pantofole :D
