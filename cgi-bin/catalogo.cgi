#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;
use CGI qw(:standard);
use XML::LibXML;
require 'functions.pl';

my $page = CGI->new;
my $session = CGI::Session->new( undef, $page, { Directory => '/tmp' } )
  or die CGI::Session->errstr;

print $session->header(-charset => 'UTF-8');



sub sezioneLibri{
	print "<h2>Catalogo della biblioteca</h2>
	<form action='catalogo.cgi' method='post' id='formContatti'>
	<fieldset><legend>Ricerca</legend>
	<label for='casellaRicerca'>Cerca</label><input type='text' name='casellaRicerca' id='casellaRicerca'/>	
	<input type='checkbox' id='show-elenco' name='show-elenco'/><label for='show-elenco' id='label-show-elenco'>Ricerca avanzata</label>
	<ul id='elenco'>
	<li><label for='titoloLibro'>Titolo</label><input type='text' name='titoloLibro' id='titoloLibro'/></li>
	<li><label for='autore'>Autore</label><input type='text' name='autore' id='autore'/></li>
	<li><label for='genere'>Genere</label><input type='text' name='genere' id='genere'/></li>
	</ul>	
	<input type='submit' name='submit' id='submit' value='Cerca'/>
	</fieldset>
	</form><div id='risultatiRicerca'>
	<dl><dt>Titolo</dt>
		<dd class='libro'>
		<img src='immagini/Divergent.jpg' alt='Copertina Divergent'/>
		<h3>Autore</h3>
		<h4>Genere</h4>
		<div class='trama'>trama..</div>		
		</dd>
	</dl>
	</div>";
	}

sub printContenuto{
	sezioneLibri();
}

&printHead("Catalogo libri","Catalogo della biblioteca, in cui è possibile cercare un libro","Ricerca, Libro, Catalogo");
printBody("Catalogo della biblioteca",$session);
