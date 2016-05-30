#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;
require 'functions.pl';

print "Content-type: text/html\n\n";

sub printContenuto{
	print"<div id='contenuto_regole'>
				<h2> Norme di funzionamento del servizio di prestito</h2>
				<dl id='listService'>
					<dt>Iscrizione al servizio di prestito</dt>
						<dd>
						Per poter accedere ai servizi di prestito occorre registrarsi al sito web fornendo un indirizzo email corretto e una propria password. 
						Ogni account verrà confermato solo dopo il ritiro di una tessera, con codice identificativo, presso la sede della biblioteca.
						Gli account che non verranno confermati entro 15 giorni dalla registrazione verranno cancellati.
						La tessera verrà rilasciata previa compilazione di un apposito modulo ed esibizione di un documento di identità. Per gli utenti minorenni
						tale modulo dovrà essere sottoscritto da uno dei genitori.
						Il prestito è personale e non può essere trasferito ad altri.
						L'utente è responsabile della buona conservazione del materiale prestatogli e della riconsegna entro il termine di scadenza.
						</dd>
					<dt>Prenotazioni</dt>
						<dd>
						Le prenotazioni possono essere effettuate o dal catalogo web presente nel sito o direttamente presso la sede della biblioteca.
						Ciascun utente può effettuare un numero massimo di 5 prenotazioni contemporaneamente. Tutte le prenotazioni supplementari saranno automaticamente cancellate.
						</dd>

					<dt>Durata e quantità</dt>
						<dd>
						Ciascun utente può avere in prestito contemporaneamente non più di 10 opere.
						Un singolo prestito ha durata di 28 giorni.
						</dd>

					<dt>Restituzione</dt>
						<dd>
						I libri in prestito devono essere restituiti presso la sede della biblioteca entro la data di scadenza. La mancata riconsegna dei libri nei termini previsti comporta l’adozione automatica di provvedimenti sospensivi dal servizio di prestito.
						</dd>

				
				</dl>
	
	</div>";
}

#need $title $description $keywords
printHead('Servizi - Biblioteca di Portobuffolè','Pagina relativa ai servizi offerti dalla biblioteca comunale di Portobuffolè','biblioteca Portobuffolè servizi');

printBody("Servizi");
