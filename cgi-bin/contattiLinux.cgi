#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
#use CGI::Session;
require 'functions.pl';

print "Content-type: text/html\n\n";

sub printContenuto{
print "	<h2>Dove trovarci</h2>
				<p>La biblioteca si trova in Piazza Vittorio Emanuele II a Portobuffole (TV) ed è aperta da martedì a venerdì dalle 9.00 alle 13.00 e  dalle 14.30 alle 18.30. Il sabato dalle 9.00 alle 13.00.</p>
				
				<h2>Come contattarci</h2>
				<p>Chiama il numero 0422 850020 oppure invia una email compilando i dati qui sotto</p>
				<form id='formContatti' caction='inserimentoLibri.cgi' method='post'>
					<fieldset><legend>Compila i dati</legend>
						<label for='nome'>Nome</label><input type='text' name='nome' id='nome'/>
						<label for='email'>Email</label><input type='text' name='email' id='email'/>
						<label for='messaggio'>Messaggio</label><textarea rows='10' cols='50' name='messaggio' id='messaggio'></textarea>
						<input type='submit' name='submit' id='submit' value='Invia'/>
					</fieldset>
				</form>
		</div>";
}

printHead('Contatti - Biblioteca di Portobuffolè','pagina contatti biblioteca di Portobuffolè','contatti biblioteca Portobuffolè');
printBody("contatti");
