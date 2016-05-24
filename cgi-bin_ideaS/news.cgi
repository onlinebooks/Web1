#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use Time::localtime;

require "News-Funzioni/stampaHtml.pl";
require "News-Funzioni/ricerca.pl";
require "News-Funzioni/notizie.pl";

my $page=new CGI;


#caricamento file xml
my $fileNotizie="../data/news.xml";
my $parser=XML::LibXML->new()||die("Errore nella creazione del parser");
my $doc=$parser->parse_file($fileNotizie)|| die("Errore nell'apertura del file xml");
my $radice=$doc->getDocumentElement();

print "Content-type: text/html\n\n";

#stampa intestazione html della pagina
&stampaIntestazione;

if($page->param("cerca")=="Cerca" && length($page->param("queryNews"))>0){
	#si effettua una ricerca
	&ricerca($page->param("queryNews"),$radice);
	}
elsif($page->param("dettagli")){
	#è richiesto il testo completo di una notizia
	&mostraDettagli($page->param("dettagli"),$radice);	
	}
elsif($page->param("anno")){
	#sono richieste le notizie di un anno specifico
	&stampaNotizieAnno($page->param("anno"),$radice);	
	}
else{#caso standard: mostra le ultime 10 notizie pubblicate
	&stampaNotizie($radice);	
	}

#creazione colonna di ricerca e chiusura della pagina
&casellaRicerca;
&stampaFine;



