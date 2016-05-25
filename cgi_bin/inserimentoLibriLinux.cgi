#!#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use XML::LibXML;
use CGI::Session;
#ppm install XML-LibXML

require 'functions.pl';

my $page=new CGI;

print "Content-type: text/html\n\n";

&printHead("Inserimento libri","","");

sub formInserimento{
	print "<h2>Inserimento libro nel catalogo della biblioteca</h2>
	<form action='inserimentoLibri.cgi' method='post'>
	<fieldset><legend>Inserimento libro</legend>
	<label for='isbn'>ISBN*</label><input type='text' name='isbn' id='isbn'/>
	<label for='titolo'>Titolo*</label><input type='text' name='titolo' id='titolo'/>
	<label for='sottotitolo'>Sottotitolo</label><input type='text' name='sottotitolo' id='sottotitolo'/>
	<fieldset><legend>Autore</legend>
	<label for='nomeAutore'>Nome*</label><input type='text' name='nomeAutore' id='nomeAutore'/>
	<label for='cognomeAutore'>Cognome*</label><input type='text' name='cognomeAutore' id='cognomeAutore'/>
	<label for='secondoNomeAutore'>Secondo nome</label><input type='text' name='secondoNomeAutore' id='secndoNomeAutore'/>
	</fieldset>
	<fieldset><legend>Informazioni editoriali</legend>
	<label for='lingua'>Lingua*</label><select name='lingua' id='lingua'>
		<option value='it'>Italiano</option>
		<option value='en'>Inglese</option>
	</select>
	<label for='anno'>Anno pubblicazione*</label><input type='text' name='anno' id='anno'/>
	<label for='casaEditrice'>Casa Editrice*</label><input type='text' name='casaEditrice' id='casaEditrice'/>
	<label for='edizione'>Edizione</label><input type='text' name='edizione' id='edizione'/>
	<label for='collana'>Collana</label><input type='text' name='collana' id='collana'/>
	<label for='annoEdizione'>Anno Edizione</label><input type='text' name='annoEdizione' id='annoEdizione'/>
	<label for='ristampa'>Ristampa</label><input type='text' name='ristampa' id='ristampa'/>
	</fieldset>
	<fieldset><legend>Dati libro</legend>
	<label for='trama'>Trama*</label><textarea name='trama' id='trama' cols='30' rows='15'></textarea>
	<label for='copertina'>Copertina</label><input type='file' name='copertina' id='copertina' accept='image/*'/>
	<!-- attributo accept non supportato da Explorer9 e versioni precedenti -->
	<label for='altImmagine'>Descrizione immagine</label><input type='text' name='altImmagine' id='altImmagine'/>
	</fieldset>
	<label for='quantita'>Quantita*</label><input type='quantita' name='quantita' id='quantita'/>
	<input type='submit' name='submit' id='submit' value='Memorizza'/>
	</fieldset>
	</form>";
}



my @controlli=(
	{
		parametro => "isbn",
		expr => "\\d{3}-\\d{1,7}-\\d{1,7}-\\d{1,7}-\\d{1}",
		valido => 1,
		mex => "Inserire il corretto codice ISBN del libro (con i caratteri -)",
		valore => "",
	},
	{
		parametro => "titolo",
		expr => ".{1,}",
		valido => 1,
		mex => "Inserire un titolo",
		valore => "",
	},
	{
		parametro => "sottotitolo",
		expr => ".{0,}",
		valido => 1,
		mex => "Inserire un sottotitolo o lasciare il campo vuoto",
		valore => "",
	},
	{
		parametro => "nomeAutore",
		expr => "\\w{1,30}",
		valido => 1,
		mex => "Inserire un nome",
		valore => "",
	},
	{
		parametro => "cognomeAutore",
		expr => "\\w{1,30}",
		valido => 1,
		mex => "Inserire un cognome",
		valore => "",
	},
	{
		parametro => "secondoNomeAutore",
		expr => "\\w{0,30}",
		valido => 1,
		mex => "Inserire un nome o lasciare il campo vuoto",
		valore => "",
	},
	{
		parametro => "anno",
		expr => "\\d{4}",
		valido => 1,
		mex => "Inserire un anno",
		valore => "",
	},
	{
		parametro => "casaEditrice",
		expr => "\\w{1,}",
		valido => 1,
		mex => "Inserire il nome della casa editrice",
		valore => "",
	},
	{
		parametro => "edizione",
		expr => "\\d{0,2}",
		valido => 1,
		mex => "Inserire il numero dell'edizione o lasciare il campo vuoto",
		valore => "",
	},
	{
		parametro => "collana",
		expr => "\\w{0,}",
		valido => 1,
		mex => "Inserire il nome della collana o lasciare il campo vuoto",
		valore => "",
	},
	{
		parametro => "annoEdizione",
		expr => "\\d{4}|\\d{0}",
		valido => 1,
		mex => "Inserire un anno o lasciare il campo vuoto",
		valore => "",
	},
	{
		parametro => "ristampa",
		expr => "\\d{4}|\\d{0}",
		valido => 1,
		mex => "Inserire un anno o lasciare il campo vuoto",
		valore => "",
	},
	{
		parametro => "trama",
		expr => ".{10,}",
		valido => 1,
		mex => "Inserire una descrizione di almeno 10 lettere",
		valore => "",
	},
	{
		parametro => "quantita",
		expr => "\\d{1,3}",
		valido => 1,
		mex => "Inserire un numero intero",
		valore => "",
	},
	);




# main ------------------------------------------------------------------------------------------------------
sub printContenuto{
	if($page->param("submit") eq "Memorizza"){
		my $k=checkForm($page,\@controlli);
		if(!$k){
			print "non valido";
		}
		else {
			my $lingua=$page->param('lingua');
			my $libro="<libro ISBN=\"$controlli[0]{valore}\" lang=\"$lingua\">
	<titolo>$controlli[1]{valore}</titolo>";
	if($controlli[2]{valore}){$libro=$libro."<sottotitolo>$controlli[2]{valore}</sottotitolo>";}
	$libro=$libro."<autore>
		<nome>$controlli[3]{valore}</nome>
		<cognome>$controlli[4]{valore}</cognome>";
	if($controlli[5]{valore}){$libro=$libro."<secondoNome>$controlli[5]{valore}</secondoNome>";}
	$libro=$libro."</autore>
	<annoPubblicazione>$controlli[6]{valore}</annoPubblicazione>
	<edizione>
		<casaEditrice>$controlli[7]{valore}</casaEditrice>";
		if($controlli[8]{valore}){$libro=$libro."<edizione>$controlli[8]{valore}</edizione>";}
		if($controlli[9]{valore}){$libro=$libro."<collana>$controlli[9]{valore}</collana>";}
		if($controlli[10]{valore}){$libro=$libro."<annoEdizione>$controlli[10]{valore}</annoEdizione>";}
		if($controlli[11]{valore}){$libro=$libro."<ristampa>$controlli[11]{valore}</ristampa>";}

	my $altImm=$page->param("altImmagine");
	if(!altImm){$altImm="nessuna descriz";}#da MODIFICARE!
	$libro=$libro."</edizione>
	<trama>$controlli[12]{valore}</trama>
	<copertina src=\"resources/libri/Norwegian_wood.png\" alt=\"$altImm\"/>
	<quantita>$controlli[13]{valore}</quantita>
	</libro>
	";
			inserimentoSuXML($libro,"libro",$controlli[0]{valore});
			print "fatto...";
		}
	}
	else{
		formInserimento();
	}
}

printBody("Inserimento Libri");
