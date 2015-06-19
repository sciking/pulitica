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
mandatop = 0
nome = ""
flop = 0
soldi = 100000000
possib = [-100000, - 75000, -50000, 0, 50000, 100000, 250000, 500000, 750000, 1000000] #9 elementi 0-9
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
gloca = 1
nomi = ["Mario","Alessio","Patrick","Lumbardo","Maria Augusta","Rin Michela","Rita","Altiero","Cesara","Giorgia","Francesco Ferdinando","Vittoria","Italia","Francesca Beatrice","Linus","Bartolo","Ariel","Gaetano","Alcide","Salvatore","Fermo","Giuliano","Domenico","Albano","Celere","Giulio Cesare","Valeria","Nicoletta","Ekaternia Giorgia","Jason Ambrogio","Alessia","Emilia","Selena","Ermenegilda","Teodolinda","Erminio","Beniamino","Zebo","Bambin","Nazario","Paoletto","Glorioso","Gilberto","Helmut","Lotario","Arnaldo","Mauro Lupo","Teodorico","Noemi","Giulia","Adelaide","Roberta","Candace","Pier Giorgio","Andrea","Virgilio","Dante","Nazareno Michele","Ezechele","Alluro","Victoria","Agnese","Adelaide","Elvezia","Amanda","Iustizia","Caterina","Martina","Fiorenza","Melissa","Antioco","Barisone","Lucio","Cornelio","Peppone","Gastone","Genoveffo","Giasone","Gavino","Arnold","Cassio","Vercingetorice","Nerone","Anzolo","Tiberio","Mariello","Amerigo","Ernesto","Adamo","Karol","Manfredi","Rotario","Antonello","Alessandro","Michele","Amado","Nikolai","Egidio","Tracaro","Arcangelo","Duomo","Attanasio","Garrumo","Giandomenico","Ciociaro","Giorgio","Licio","Calogero","Mona","Germano","Ugo","Matteo","Attilio","Teodorico","Crescenzo","Arimanno","Floriano","Baldassarre","Berto","Roso","Catalino","Tromlino","Ambroeus","Francesco","Abbondio","Nunzio","Gerardo","Silvio","Alberto","Gianni","Teresio","Ambrogio","Anselmo","Giovese","Amintore","Italo","Arcibaldo","Justinià","Danjuro","Bortolo","Augusto","Piergastone","Diego","Giulio","Giuàn","Azeglio","Adolfo","Benito","Natale","Nazareno","Jorji"]
cognomi = ["Brambilla","Fumagalli","Rossi","dell'Incoronata","Schulzi","Fabero","Kofler","Coffiere","Verdi","Capellaro","da Pirla","Almirante","Casadei","Tettamanzi","Pessotti","Mastranzo","Nasdrovie","Dalle Colonie","Bono","Rovatacchini","Bianchi","Bernasca","Salvino","Porcu","Lefevre","Thompson","Vagneri","Sojuzzi","La Foppa","Dervalaporta","Sforza","Visconti","De Medici","Ottone","Di Calino","Aromano","Megrato","Suscrofa","Lazzaroni","Formaggi","Giamboni","Della Libertà","Di Pioltello","Feltrinelli","Zaccuri","Scoeura","Caselli","Wagner","Bottazzi","Guadone","de Brescello","Prestinée","Caterborino","Mariano","Eleatico","Ploeuf","Taleano","Loserbiddio","Berlinguer","Ol Careàs","Pisaelfoeuc","Puteo","Diletta","Vlocci","Prondella","Mangiagalli","Cordileone","De Nicola","Battisti","Terione","Milanese","Muratore","Scipoti","Auffo","Insinavìi","Veneranda Fabbrica","Scapece","Rensi","Bosse","Cetipaga","Dellinfermi","Legnano","Werrant","Scarpa","Soccuso","Varvaro","Lonbarto","Mascio","Togliatti","Tramaglino","Ienneri","Kowalsky","Tomat","Muzzo","Putin","Ostuni","Latarga","Narodna","Piattirotti","Colleone","Mandi","Fanfani","Corsi","Romano","Perottini","Torvalds","da Giussano","Mantaro","Asburgo","Sala","Passalapalla","Plebfiore","Vaccini","De Stefano","Pizza","Rotino","Spoeusa","Alfulo","Cappi","Di Piero","Altissimo","Maroni","Olsone","Popov","Sensi","Bellotti","Conti","Invernizzi","Nicolello","Legramandi","Olivetti","Vignana","Carminati","Zennaro","Savoia","Figliodigesù","De Gianfiö","Ferrero","Colombo","Lombardi","Basile","Degasperi","Culot","Toccaferro","Lafica","Granlaüradur","Fantozzi","Nagotta","Mosconi","Perazzini","Mussolesi","Schavòn"]
sd = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
ss = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
premier = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
si = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
pa = ["Partito Liberale", "Lega Milanese", "Unione Popolare","Partito Sociale Liberale","Movimento Federale del Lavoro", "Movimento delle Libertà", "Casa Riformista", "Il Lume della Ragione","Partito di Sua Maestà il Maiale","Destra per l'Italia Unita","Liberali d'Emilia Romagna","Uomo Qualunque","Destra Latina","Patrito contro le Pantofole", "Casa delle Riforme", "Föra di ball! Milano Libera","Destra Piemontese","Destra Arcobaleno","Movimento Fascio Repubblicano","Partito Socialista Federale","Milano Bene di Tutti",]
pb = ["Milano Rossa", "Partito Ecologista", "Lega dei Contadini", "Partito per le frontiere aperte","Alleanza di Democrazia","Sinistra Triveneta", "Progressismo è Democrazia", "Rivoluzione Popolare","Civiltà Umana","Democrazia Pastafariana","Socialisti Marchigiani","Movimento del Panino","Cattolici di Sinistra per l'Europa", "MoviMento Quattro Soli", "Equità nelle ricchezze", "Alleanza di Sinistra","Lega Popolare Slava","Microfono Civico","Monarchia & Popolo","Lotta Milano","Democrazia Cattolica Socialista",]
apar = ["Unione dei Radicali", "Giustizia di Destra", "Libertà Comunista", "Movimento Letterario","Partito della Scienza","Guardia dei Contadini","Dio e Popolo","Coalizione dei Deisti","Partito Evropa Vnita ",]
destra = pa[random.randint(0,20)]
sinistra =  pb[random.randint(0,20)]
leggi = ["contro l'omofobia", "per l'introduzione del lombardo nelle scuole", "contro la ciarlataneria", "per la democrazia diretta", "contro l'obbligo militare", "per l'allungamento dell'obbligo scolastico","per creare un testo all'Inno Nazionale","per proibire la Lingua Inglese","per la beatificazione di Freddie Mercury","per aumentare le pensioni","per abolire la canapa a Milano", "contro le pantofole", "per la sicurezza scolastica", "per l'abolizione del reato di stupro","per l'insegnamento del russo","per diminuire l'età pensionabile","per ufficializzare la lingua piemontese","per collegare Milano a Varese via Navigli","per collegare via fiume Milano e Ivrea","per aumentare le pene ai pedofili","per eliminare ogni limitazione alla Sperimentazione animale","contro il populismo","contro il bigottismo","per creare nuove lupanari","per migliorare l'omologazione delle auto","contro la Boemia","per introdurre le sputacchiere","contro le epidemie","per limitare i fenomeni migratori","per creare una rete sociale di stato","per migliorare le armi dei ghisa","per esportare la piadina romagnola nel mondo","contro il software a pagamento","per favorire le vaccinazioni","contro la tastiera QWERTY","contro i giocatori stranieri del folball","contro le adolescenti truccate","per costruire una Reggia Presidenziale a Codigoro","contro il plagio", "per l'illegalità del popolarismo", "per i diritti civili","per abolire le religioni", "per creare la Regione Autonoma Emiliana", "per l'istituzione delle regioni","contro il reato di furto con scasso","contro le mense sporche", "per abolire  i videogiochi violenti","per l'elezione diretta del Premier","contro il veganismo","contro le infiltrazioni malavitose nelle amministrazioni locali","contro l'estremismo religioso","contro il complottismo","per abbassare le tasse indirette","per migliorare gli ospedali","per abolire i giornali erotici","per la prevenzione dell'obesità","contro chi indossa pantaloncini osceni con gli stivali","per migliorare i canili","contro il gioco del lotto","per far fare all'offelee el so mestée","contro i debiti dello stato","contro l'astensionismo","per favorire l'Italia Unita","contro le dogane interne","contro le riforme","per dedicare una statua ad Alberto da Giussano","per conquistare Caporetto","per controllare le case farmaceutiche","contro i fanatismi religiosi","per abolire Babbo Natale","contro i centri sociali","per toglere l'IMVA al pane","contro il latte scaduto","per migliorare i rapporti con il San Marino","contro la crescita zero","per introdurre le scuole in lingua regionale","per l'introduzione del matrimionio incestuoso","per l'ufficializzazione della lingua lombarda","contro la prostituzione minorile","per incentivare la coltivazione dell'erburìn","per favorire le biciclette","per tutelare le minoranze","contro i politici locali corrotti","contro i danè falsi","per introdurre le mescite a Milano","per evitare la diffusione dei pidocchi","per la liberalizzazione delle droghe leggere","contro i computer sovraprezzati","per tutelare la pasta","contro le pseudoscienze","per abolire l'omeopatia","per mettere i cani in parlamento per aumentare la produttività","in favore del monossido di diidrogeno","per togliere ogni limitazione agli OGM","per sostenere chi parla dumà el lumbaart","per favorire il dialetto ticines","per favorire il lavoro minorile","contro le cooperative","per abolire le tasse agricole","per introdurre il proporzionale puro","contro lo sbarramento","per eliminare le barriere architettoniche","per favorire l'onanimso nei giovini ambrosiani","contro le armi da fuoco","per introdurre la tessera sanitaria elettronica","per abbassare la maggiore età a 16 anni","per abolire il canone televisivo","contro le cure ciarlatane","per abolire il Senato Sovracomunale","per aprire un centro di integrazione per gli immigrati","per dare un premio di 500 Ambrogi ai collezionisti","contro le droghe pesanti","per promuovere la cura dalla ludopatia","contro i prof politicizzati","per ridurre l'inquinamento","per favorire le lobby del tabacco","per costruire una statua della Perottina a Pregnana","per tutelare il risotto alla milanese","per aumentare le ore di educazione sessuale","per punire la bestemia","per aumentare il tasso di natalità","contro i negozi taiwanesi","per mettere Sant'Ambrogio sui 10 Ambrogi","per fare una statua a Sant'Anselmo da Baggio","per il laicismo","contro i nomi stranieri","per creare un sistema operativo di stato","per tassare il parquet dei 25%","per evitare le malattie trasmesse dai migranti","contro l'inimicizia tra Bergamo e Brescia","per abolire le scarpe col tacco","per diminuire le tasse","per aumentare le pene per omicidio stradale","per insegnare la buona educazione ai bambini","contro il nomadismo","per le pari opportunità","per lo ius soli","per alzare il prezzo delle sigarette","per mettere nuove misure di sicurezza ai danè","per contrastare il razzismo","per introdurre la prigione per vandalismo","per aiutare i milanesi prima degli altri","per la limitazione delle armi bianche","per migliorare l'esercito di milizia","per aumentare l'autonomia federale alla Repubblica Friulana","contro le nudità all'Idroscalo","per introdurre la lingua veneta nelle scuole","contro le droghe","contro il software proprietario","contro la pirateria informatica","per le adozioni ai single e ai gay","per la libera associazione della Sicilia a Milano","per il disarmamento dei ghisa","contro le droghe leggere","Per regolare l'immigrazione dall'Est Europa","Per l'introduzione dei Permessi d'Accesso","per introdurre le console da videogioco a scuola","contro il gimnopodismo","per l'eliminazione delle zanzare","per fornire ai cittadini buoni gratis per il postribolo.","per proibire l'alcole","per aumentare i finanziamenti alle scuole","per abolire le scuole private", "contro le sculacciate",]
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
while nome == "":
	nome = raw_input("Come ti chiami, Presidente?: ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def poss():
	global elettori
	global flop
	global ele1
	global deputati
	global r
	global deps
	global premier
	global depd
	global depa
	global ss
	global soldi
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
	poss = random.randint(1,60)
	if poss == 1:
		print "Sindaco delle Liste Locali diserta nel Partito Indipendente"
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
			soldi = soldi - 100000
		elettori = elettori + 3
		ele1 = ele1 + 3
		ele2 = ele2 - 3
		eleap = eleap + random.randint(-3,3)
		gioco()
	elif poss == 6:
		print "Arrestato un nostro sindaco!"
		print "Perderemo sicuramente elettorato!"
		sindaci = sindaci - 1
		elettori = elettori -2
		ele1 = ele1 + 1
		ele2 = ele2 + 1
		gioco()
	elif poss == 7:
		print "Una nostra mozione al Parlamento per diminuire le tasse passa! Il Popolo è soddisfatto."
		elettori = elettori + 2
		sindaci = sindaci + 1
		ele1 = ele1 + random.randint(-2,2)
		ele2 = ele2 + random.randint(-2,2)
		eleap = eleap + random.randint(-1,1)
		soldi = soldi - 500000
		gioco()
	elif poss == 8:
		print "Deputato PIM si masturba in piazza"
		print nome, "tenta di salvare in extremis: 'Nulla sia coperto, \n voteremo si alla richiesta di arresto"
		elettori = elettori + random.randint(-4, 1)
		ele1 = ele1 + 1
		ele2 = ele2 + 1
		gioco()
	elif poss == 9:
		print "Fast Food: E' rivincita \n Roberto Vicentino: Fa bene, se moderato"
		gioco()
	elif poss == 10:
		print "La prostituzione legale è legge, grazie a noi"
		sindaci = sindaci - 1
		elettori = elettori + 6 #prima era 8... suvvia, non siamo così puttanieri :D
		ele1 = ele1 + random.randint(-2,2)
		ele2 = ele2 + random.randint(-2,2)
		eleap = eleap + random.randint(-2,2)
		soldi = soldi + 100000
		gioco()
	elif poss == 11:
		print "I giudici riescono a condannare l'imputato della strage di 3 anni fa: Ergastolo!"
		gioco()
	elif poss == 12:
		print "OGM consentiti, è legge. I sindaci non approvano la legge unanime"
		elettori = elettori +1
		sindaci = sindaci + random.randint(-1,1)
		soldi = soldi - 50000
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
		ele1 = ele1 + random.randint(-2,3)
		ele2 = ele2 + random.randint(-2,3)
		eleap = eleap + random.randint(-2,3)
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
			ele1 = ele1 + 1
			ele2 = ele2 - 1
		elif destra == "Unione Popolare":
			print "Sinistra e PIM unanimi, ma l'UP ha dubbi ambientali"
			ele2 = ele2 + 2
			elettori = elettori + 1
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
		print nome,"multato per 5000 Ambrogi, il segretario condannato a 6 mesi"
		elettori = elettori - 6
		ele1 = ele1 + 2
		ele2 = ele2 + 3
		eleap = eleap + 1
		soldi = soldi + 5000
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
		soldi = soldi - 5000
		elettori = elettori + 3
		gioco()
	elif poss == 34:
		print "Milano vince i campionati mondiali del folball!" #per chi non lo sapesse el folball è il calcio in milanese
		soldi = soldi + 50000
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
		print "Governo approva mozione del Consiglio Tecnico: Stanziati 1 milioni di Ambrogi contro il cancro"
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
		soldi = soldi - 1000000
		gioco()
	elif poss == 43:
		print "Retata a Cesano Boscone"
		if turno%2 == 0:
			print "Arrestato", ss
			if ss == premier:
				ss = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
				premier = ss
			else:
				ss = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
			ele2 = ele2 - 10
		elif turno%5 == 0:
			if si == premier:
				si = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
				premier = si
			else:
				si = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
			elettori = elettori - 10
		else:
			print "Arrestato", sd
			if sd == premier:
				sd = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
				premier = sd
			else:
				sd = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
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
		soldi = soldi - 100000
		gioco()
	elif poss == 45:
		print "Partito Indipendente e", destra, "alleate per qualche mese"
		ele1 = ele1 + 5
		elettori = elettori + 5
		gioco()
	elif poss == 46:
		print "Partito Indipendente ingloba partiti minori, ma gli elettori non ci stanno"
		deputati = deputati + depa
		depa = 0
		elettori = elettori -4
		ele1 = ele1 + 2
		ele2 = ele2 +2
		gioco()
	elif poss == 47:
		ka = random.randint(1,3)
		if ka == 1:
			print nome, "beccato a chiedere foto pè biott alle ragazze"
			print "Poi vi passo le foto, sdrammatizza"
		if ka == 2:
			print ss, "mostra per errore immagini porno in presentazione"
			print "Elettori", sinistra, "divertiti sdrammatizzano"
		if ka == 3:
			print sd, "iscritto a sito di spanking"
			print "Deputato", destra, "sdrammatizza"
		gioco()
	elif poss == 48:
		print "Arrestati 15 deputati! Elettorato generale a picco!"
		deps = deps - 5
		depd = depd - 5
		deputati = deputati - 5
		depa = depa + 15
		ele1 = ele1 - 15
		ele2 = ele2 - 15
		eleap = eleap + 5
		elettori = elettori - 15
		gioco()
	elif poss == 49:
		if turno%2 == 0:
			print "Referendum Straordinario"
			print "Corte suprema approva richiesta", apar[random.randint(0,8)] + ", si voterà oggi"
			raw_input("Premi invio per continuare")

			referendum()
		else:
			print "Nuova legge per favorire l'Internet\n Accordo multipartitico"
			ele1 = ele1 + 4
			ele2 = ele2 + 4
			eleap = eleap + 1
			elettori = elettori + 4
			
	elif poss == 50:
		print "Politici milanesi: I più onesti."
		ele1 = ele1 + 5
		ele2 = ele2 + 5
		elettori = elettori + 5
		eleap = eleap + 2
		gioco()
	elif poss == 51:
		if turno %4 == 0:
			kade = random.randint(1,4)
			if kade == 1:
				print "Liste minori entrano nel PIM"
				elettori = elettori + eleap
				eleap = 0
			elif kade == 2:
				print "Liste minori entrano nel", destra
				ele1 = ele1 + eleap
				eleap = 0	
			elif kade == 3:
				print "Liste minori entrano nel", sinistra
				ele2 = ele2 + eleap
				eleap = 0
			elif kade == 4:
				print "Milano,", random.randint(1,5),"in Europa per le scuole!"
			else:
				print "Crisi: Effetti diminuiti in pochi mesi"
		else:
			print "Milano: Motore economico dell'Italia"
		gioco()
	elif poss == 52:
		print "Olimpiadi: L'Italia Unita vince il medagliere"
		gioco()
	elif poss == 53:
		print "Politici milanesi in testa all'Unità Europea"
		ele1 = ele1 + 4
		ele2 = ele2 + 4
		eleap = eleap + 2
		elettori = elettori + 4
		gioco()
	elif poss == 54:
		if turno%2 == 0:
			print "Scandalo a Milano"
			print "Grande azienda paga mazzette per leggi favorevoli, coinvolti tutti i partiti"
			print "Arrestato", nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)] ,", presidente della società"
			ele1 = ele1 - 20
			ele2 = ele2 - 20
			eleap = eleap - 10
			elettori = elettori - 20
		else:
			print "Partiti sempre più amici, gli elettori aumentano"
			ele1 = ele1 + 3
			ele2 = ele2 + 3
			eleap = eleap + 1
			elettori = elettori + 3		
		gioco()
	elif poss == 55:
		print "L'energia di Milano è sempre più verde"
		if premier == ss:
			ele2 = ele2 + 5
		if premier == sd:
			ele1 = ele1 + 5
		if premier == nome or premier == si:
			elettori = elettori + 5
		elettori = elettori + 2
		ele1 = ele1 + 2
		ele2 = ele2 + 2
		eleap = eleap + 1
		gioco()
	elif poss == 56:
		print "Astensionismo sempre più alto, Capo dello Stato fa appello"
		ele1 = ele1 - 3
		ele2 = ele2 - 3
		eleap = eleap - 1
		elettori = elettori - 3	
	elif poss == 57: #qua si perdono i danè :D
		lum = random.randint(1,6)
		if lum == 1:
			print "Scandalo Malasanità: Milano risarcirà due milioni"
			soldi = soldi - 2000000
		elif lum == 2:
			print "Milano: Scuole costose. Tagli annunciati ma spese alte"
			soldi = soldi - 500000
		elif lum == 3:
			print "Stato perde causa: Pagherà 25000Å"
			soldi = soldi - 25000
		elif lum == 4:
			print "Rovigo: Nuove zone industriali \nGuadagno alla lunga, ma per ora sol soldi"
			soldi = soldi - 100000
		elif lum == 5 and random.randint(1,10) > 8:
			print "Energie Pulite: Multati per 1 milione"
			soldi = soldi - 1000000
			gioco()
		elif lum == 5:
			print "Milano restituisce titoli di stato: Non vi è guadagno"
			soldi = soldi - 10000
		elif lum == 6:
			print "Esposizione universale: Persi 100000Å"
			soldi = soldi - 100000
		gioco()
	elif poss == 58: #qui si guadagnano i danè invece :D
		luma = random.randint(1,6)
		if luma == 1:
			print "Scie idriche: Milano vince causa contro sostenitori"
			soldi = soldi + 100000
		elif luma == 2:
			print "Friuli ricchissimo: Una parte va a Milano"
			soldi = soldi + 250000
		elif luma == 3:
			print "Politici milanesi: I più produttivi. E lo stato vince premio"
			soldi = soldi + 25000
		elif luma == 4:
			print "Nuove zone industriali vicino Ferrara fruttano"
			soldi = soldi + 250000
		elif luma == 5 and random.randint(1,10) > 8:
			print "Farmaceutica multata: Iniettava acqua in cambio di denaro"
			soldi = soldi + 1500000
			gioco()
		elif luma == 5:
			print "Investimenti azzeccati e Milano vince mezzo milione"
			soldi = soldi + 500000
		elif luma == 6:
			print "Esposizione universale: Ci sono guadagni"
			soldi = soldi + 25000
		gioco()			
	elif poss == 59:
		print "Milano vince il premio 'Città mondiale dell'Anno'"
		elettori = elettori + 1
		ele1 = ele1 + 1
		ele2 = ele2 + 1
		gioco()
	elif poss == 60:
		print "I quartieri degradati a Milano sono troppo, per l'elettorato"
		elettori = elettori - 2
		ele1 = ele1 - 2
		ele2 = ele2 - 2
		eleap = eleap - 1
		gioco()
			
	gioco()
def referendum():
	os.system("clear")
	global elettori
	global soldi
	global ele1 
	global ele2
	print "PLEBISCITO - STRUMENTO DI DEMOCRAZIA DIRETTA"
	quesiti = ["per l'abolizione della detenzione preventiva","per l'adozione indifferenziata a coppie omo ed eterosessuali","contro l'insegnamento della  matematica","per l'illegalità delle pantofole","per inserire l'obbligo vaccinale totale","per espellere gli immigrati clandestini","per migliorare gli accordi con la Polonia","per chiedere una licenza ai prestiné","per usare gli aerei nei trasporti interurbani","contro la guida del telefono","per abolire il parquet","per adottare ufficialmente la grafia moderna del milanese","contro l'alleanza con la Provenza","per migliorare i cessi pubblici","per comperare nuove corriere Neopleb","contro l'affolamento carcerario","per arrestare i corrotti","per diminuire i postriboli","per limitare i farmaci psicotropi","per limitare l'altezza dei tacchi a 8 centimetri","per tutelare il limoncello","contro l'antiscienza","per sbattere in galera gli antivaccinisti","per abbattere le scuole private con una ruspa","contro la prostituzione nelle strade","per abolire il monopolio telefonico della SET","per finanziare la squadra del folball","contro l'inquinamento ambientale","per abolire le norme antibestemmia","contro la malavita","per legalizzare l'uso alimentare del gatto","per abolire il software proprietario","contro il fumo di sigaretta","per il nucleare nella Repubblica Milanese","contro le religioni","contro la malasanità","per far valere le lauree europee a Milano","per creare la Provincia di Vanzaghello","per avere i taxi gialli","contro il tetano","per l'abolizione dei licei","per abolire gli inni comunali","per abolire i numeri 668 a pagamento","per diminuire il costo di iscrizione alle poste","contro le droghe","per aumentare le libertà personali","per introdurre la prevenzione delle malattie sessuali a spese dello stato","contro il gioco d'azzardo","per istituire una Regione del Canavese","per tutelare le gondole a Cmâc"]
	random.shuffle(quesiti)
	print "Quesito", quesiti[1]
	sceltak = ["si","no"]
	sceltaq = raw_input("Si o No?")
	sceltav = sceltak[random.randint(0,1)]
	sceltad = sceltak[random.randint(0,1)]
	sceltas = sceltak[random.randint(0,1)]
	sceltaq = sceltaq.lower()
	if sceltaq != "si" and sceltaq != "no":
		sceltaq = "no"
	print "Scelta PIM:", sceltaq
	print "Scelta", destra, ":", sceltad
	print "Scelta", sinistra, ":", sceltas
	if sceltav == "si":
		if sceltaq == "si":
			elettori = elettori + 3
		if sceltad == "si":
			ele1 = ele1 + 3
		if sceltas == "si":
			ele2 = ele2 + 3
	else:
		if sceltaq != "si":
			elettori = elettori + 3
		if sceltad != "si":
			ele1= ele1 + 3
		if sceltas != "si":
			ele = ele2 + 3
	del quesiti[1]
	print "Il popolo ha scelto", sceltav
	raw_input("Premi Invio per continuare")
	soldi = soldi - 100000
	os.system("clear")
	poss()
		

def gioco():
	global turno
	global elettori
	global ele1
	global ele2
	global eleap
	global sindaci
	global soldi
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
	global mandatop
	print " \n \n"
	"""if turno%4 == 0:
		if turno > 15 and elettori > 15:
		print "La campagna elettorale è impo"""
	if turno%5 == 0:
		deputati = elettori*parlamento/(elettori+ele1+ele2+eleap)# elettori : totale = x : parlamento
		depd = ele1*parlamento/(elettori+ele1+ele2+eleap)
		deps = ele2*parlamento/(elettori+ele1+ele2+eleap)
		depa = eleap*parlamento/(elettori+ele1+ele2+eleap)
		sindaci = elettori*4000/(elettori+ele1+ele2+eleap)
		if parlamento/deputati < 2 and flop < 2 and decas == 0:
			print """Salve signor presidente. Siamo riusciti ad eleggere il Capo dello Stato e abbiamo scelto Lei come nostro nuovo Capo. Governi bene in questi due anni!"""
			print "Onori al Capo dello Stato", nome, "!"
			mandatop = mandatop + 1
			print "Mandato:", mandatop
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
		elif parlamento/(deps+depa) <2:
			print "L'Indipendente di Milano \n Sinistra al Governo, ma coalizzata"
			premier = ss
		elif parlamento/(deputati+depa) <2:
			print "L'Indipendente di Milano \n Siamo al Governo, ma coalizzati"
			if caput == 0:
				premier = nome
			else:
				premier = si
		elif parlamento/(depd+depa) <2:
			print "L'Indipendente di Milano \n Destra al Governo, ma coalizzata"
			premier = sd
		else:
			print "Nessun eletto: Capo dello Stato nomina governo tecnico"
			premier = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
	entrate = possib[random.randint(0,9)]
	uscite = possib[random.randint(0,9)]
	if turno%2 == 0:
		uscite = uscite + 750000
	bilancio = entrate - uscite
	soldi = soldi + bilancio
	print "Hai", soldi, "Å \t Bilancio", bilancio
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
		r = random.randint(1,2)
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
		destra = pa[random.randint(0,20)]
		ele1 = 15
	if ele2 < 5:
		sinistra =  pb[random.randint(0,20)]
		ele2 = 15
	if eleap < 0 or depa < 0:
		eleap = 0
		depa = 0
	if turno%25 == 0:
		sd = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
		ss = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
		si = nomi[random.randint(0,150)]+ " " + cognomi[random.randint(0,150)]
	if turno%4 == 0:
		gloc = elettori*18/(elettori+ele1+ele2+eleap)
		coeffi = [0.5,0.75,1,1.25]
		coeff = coeffi[random.randint(0,3)]
		gloca = int(gloc*coeff)
	if turno%10 == 0 and turno > 9:
		referendum()
		
	os.system("clear")
	poss()
gioco()		# computerblog.ga no alle pantofole :D
