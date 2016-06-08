#!perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use XML::LibXML;
use CGI::Session;
use File::Basename;
#ppm install XML-LibXML

require 'functions.pl';

my $page=new CGI;

print "Content-type: text/html\n\n";

&printHead("Inserimento libri","","");

sub formInserimento{
	print "<h2>Inserimento libro nel catalogo della biblioteca</h2>
	<form action='inserimentoLibri.cgi' method='post' enctype='multipart/form-data'>
	<fieldset><legend>Inserimento libro</legend>
	<label for='isbn'>ISBN*</label><input type='text' name='isbn' id='isbn'/>
	<label for='titoloL'>Titolo*</label><input type='text' name='titoloL' id='titoloL'/>
	<label for='sottotitolo'>Sottotitolo</label><input type='text' name='sottotitolo' id='sottotitolo'/>
	<fieldset><legend>Autore</legend>
	<label for='nomeAutore'>Nome*</label><input type='text' name='nomeAutore' id='nomeAutore'/>
	<label for='cognomeAutore'>Cognome*</label><input type='text' name='cognomeAutore' id='cognomeAutore'/>
	<label for='secondoNomeAutore'>Secondo nome</label><input type='text' name='secondoNomeAutore' id='secondoNomeAutore'/>
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
	<label for='quantita'>Quantita*</label><input type='text' name='quantita' id='quantita'/>
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
		parametro => "titoloL",
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
	{#3
		parametro => "nomeAutore",
		expr => "\\w{1,30}",
		valido => 1,
		mex => "Inserire un nome",
		valore => "",
	},
	{#4
		parametro => "cognomeAutore",
		expr => "\\w{1,30}",
		valido => 1,
		mex => "Inserire un cognome",
		valore => "",
	},
	{#5
		parametro => "secondoNomeAutore",
		expr => "\\w{0,30}",
		valido => 1,
		mex => "Inserire un nome o lasciare il campo vuoto",
		valore => "",
	},
	{#6
		parametro => "anno",
		expr => "\\d{4}",
		valido => 1,
		mex => "Inserire un anno",
		valore => "",
	},
	{#7
		parametro => "casaEditrice",
		expr => "\\w{1,}",
		valido => 1,
		mex => "Inserire il nome della casa editrice",
		valore => "",
	},
	{#8
		parametro => "edizione",
		expr => "\\d{0,2}",
		valido => 1,
		mex => "Inserire il numero dell'edizione o lasciare il campo vuoto",
		valore => "",
	},
	{#9
		parametro => "collana",
		expr => "\\w{0,}",
		valido => 1,
		mex => "Inserire il nome della collana o lasciare il campo vuoto",
		valore => "",
	},
	{#10
		parametro => "annoEdizione",
		expr => "\\d{4}|\\d{0}",
		valido => 1,
		mex => "Inserire un anno o lasciare il campo vuoto",
		valore => "",
	},
	{#11
		parametro => "ristampa",
		expr => "\\d{4}|\\d{0}",
		valido => 1,
		mex => "Inserire un anno o lasciare il campo vuoto",
		valore => "",
	},
	{#12
		parametro => "trama",
		expr => ".{10,}",
		valido => 1,
		mex => "Inserire una descrizione di almeno 10 lettere formattata in html (con i paragrafi contenuti in tag &lt;p&gt;)",
		valore => "",
	},
	{#13
		parametro => "quantita",
		expr => "\\d{1,3}",
		valido => 1,
		mex => "Inserire un numero intero",
		valore => "",
	},
	);

sub checkImage{
	my $page=$_[0];
	if(!$page->param("copertina")){return 1;}
	if($page->param("altImmagine") =~ /.{1,}/){return 1;}
	return 0;
}

sub formRitrasmesso{
	my $page=$_[0];
	my @controlli=@{$_[1]};
	print "<h2>Inserimento libro nel catalogo della biblioteca</h2>
	<form action='inserimentoLibri.cgi' method='post' enctype='multipart/form-data'>
	<fieldset><legend>Inserimento libro</legend>";
	if(!$controlli[0]{valido}){
		print "<label for='isbn' class='erroreInserimento'>ISBN* - $controlli[0]{mex}</label>
		<input type='text' name='isbn' id='isbn' value=\"$controlli[0]{valore}\"/>";
	}
	else{
		print "<label for='isbn'>ISBN*</label>
		<input type='text' name='isbn' id='isbn' value=\"$controlli[0]{valore}\"/>";
	}
	if(!$controlli[1]{valido}){
		print "<label for='titoloL' class='erroreInserimento'>Titolo* - $controlli[1]{mex}</label>
		<input type='text' name='titoloL' value=\"$controlli[1]{valore}\" id='titoloL'/>";
	}
	else{
		print "<label for='titoloL'>Titolo*</label>
		<input type='text' value=\"$controlli[1]{valore}\" name='titoloL' id='titoloL'/>";
	}
	if(!$controlli[2]{valido}){
		print "<label for='sottotitolo' class='erroreInserimento'>Sottotitolo - $controlli[2]{mex}</label>
		<input type='text' name='sottotitolo' value=\"$controlli[2]{valore}\" id='sottotitolo'/>";
	}
	else{
		print "<label for='sottotitolo'>Sottotitolo</label>
		<input type='text' name='sottotitolo' value=\"$controlli[2]{valore}\" id='sottotitolo'/>";
	}
	print "<fieldset><legend>Autore</legend>";
	if(!$controlli[3]{valido}){
		print "<label for='nomeAutore' class='erroreInserimento'>Nome* - $controlli[3]{mex}</label>
		<input type='text' name='nomeAutore' value=\"$controlli[3]{valore}\" id='nomeAutore'/>";
	}
	else{
		print "<label for='nomeAutore'>Nome*</label>
		<input type='text' name='nomeAutore' value=\"$controlli[3]{valore}\" id='nomeAutore'/>";
	}
	if(!$controlli[4]{valido}){
		print "<label for='cognomeAutore' class='erroreInserimento'>Cognome* - $controlli[4]{mex}</label>
		<input type='text' name='cognomeAutore' value=\"$controlli[4]{valore}\" id='cognomeAutore'/>";
	}
	else{
		print "<label for='cognomeAutore'>Cognome*</label>
		<input type='text' name='cognomeAutore' value=\"$controlli[4]{valore}\" id='cognomeAutore'/>";
	}
	if(!$controlli[5]{valido}){
		print "<label for='secondoNomeAutore' class='erroreInserimento'>Secondo nome - $controlli[5]{mex}</label>
		<input type='text' name='secondoNomeAutore' value=\"$controlli[5]{valore}\" id='secondoNomeAutore'/>";
	}
	else{
		print "<label for='secondoNomeAutore'>Secondo nome</label>
		<input type='text' name='secondoNomeAutore' value=\"$controlli[5]{valore}\" id='secondoNomeAutore'/>";
	}
	my $linguaSelezionata=$page->param("lingua");
	print "</fieldset>
	<fieldset><legend>Informazioni editoriali</legend>
	<label for='lingua'>Lingua*</label><select name='lingua' value=\"$linguaSelezionata\" id='lingua'>
		<option value='it'>Italiano</option>
		<option value='en'>Inglese</option>
	</select>";
	if(!$controlli[6]{valido}){
			print "<label for='anno' class='erroreInserimento'>Anno pubblicazione* - $controlli[6]{mex}</label>
			<input type='text' name='anno' value=\"$controlli[6]{valore}\" id='anno'/>";
	}
	else{
			print "<label for='anno'>Anno pubblicazione*</label>
			<input type='text' name='anno' value=\"$controlli[5]{valido}\" id='anno'/>";
	}
	if(!$controlli[7]{valido}){
		print "<label for='casaEditrice' class='erroreInserimento'>Casa Editrice* - $controlli[7]{mex}</label>
		<input type='text' name='casaEditrice' value=\"$controlli[7]{valore}\" id='casaEditrice'/>";
	}
	else{
		print "<label for='casaEditrice'>Casa Editrice*</label>
		<input type='text' name='casaEditrice' value=\"$controlli[7]{valore}\" id='casaEditrice'/>";
	}
	if(!$controlli[8]{valido}){
		print "<label for='edizione' class='erroreInserimento'>Edizione - $controlli[8]{mex}</label>
		<input type='text' name='edizione' value=\"$controlli[8]{valore}\" id='edizione'/>";
	}
	else{
		print "<label for='edizione'>Edizione</label>
		<input type='text' name='edizione' value=\"$controlli[8]{valore}\" id='edizione'/>";
	}
	if(!$controlli[9]{valido}){
	print "<label for='collana' class='erroreInserimento'>Collana - $controlli[9]{mex}</label>
	<input type='text' name='collana' value=\"$controlli[9]{valore}\" id='collana'/>";
	}
	else{
		print "<label for='collana'>Collana</label>
		<input type='text' name='collana' valore=\"$controlli[9]{valore}\" id='collana'/>";
	}
	if(!$controlli[10]{valido}){
		print "<label for='annoEdizione' class='erroreInserimento'>Anno Edizione - $controlli[10]{mex}</label>
		<input type='text' name='annoEdizione' value=\"$controlli[10]{valore}\" id='annoEdizione'/>";
	}
	else{
		print "<label for='annoEdizione'>Anno Edizione</label>
		<input type='text' name='annoEdizione' value=\"$controlli[10]{valido}\" id='annoEdizione'/>";
	}
	if(!$controlli[11]{valido}){
		print "<label for='ristampa' class='erroreInserimento'>Ristampa - $controlli[11]{mex}</label>
		<input type='text' name='ristampa' value=\"$controlli[11]{valore}\" id='ristampa'/>";
	}
	else{
		print "<label for='ristampa'>Ristampa</label>
		<input type='text' name='ristampa' value=\"$controlli[11]{valore}\" id='ristampa'/>";
	}
	print "</fieldset>
	<fieldset><legend>Dati libro</legend>";
	if(!$controlli[12]{valido}){
	print "<label for='trama' class='erroreInserimento'>Trama* - $controlli[12]{mex}</label>
	<textarea name='trama' id='trama' cols='30' rows='15'>$controlli[12]{valore}</textarea>";
	}
	else{
	print "<label for='trama'>Trama*</label>
	<textarea name='trama' id='trama' cols='30' rows='15'>$controlli[12]{valore}</textarea>";
	}
	my $imgInserita=$page->param("copertina");
	my $altInserito=$page->param("altImmagine");
	if(!checkImage($page)){
		print "<label for='copertina' class='erroreInserimento'>Copertina</label>
		<input type='file' name='copertina' id='copertina' accept='image/*'/>
		<label for='altImmagine' class='erroreInserimento'>Descrizione immagine - Inserire una descrizione o non scegliere immagini</label>
		<input type='text' name='altImmagine' value=\"$altInserito\" id='altImmagine'/>";
	}
	else{
		print "<label for='copertina'>Copertina</label>
		<input type='file' name='copertina' id='copertina' value=\"$imgInserita\" accept='image/*'/>
		<label for='altImmagine'>Descrizione immagine</label>
		<input type='text' name='altImmagine' value=\"$altInserito\" id='altImmagine'/>";
	}
	print "</fieldset>";
	if(!$controlli[13]{valido}){
		print "<label for='quantita' class='erroreInserimento'>Quantita* - $controlli[13]{mex}</label>
		<input type='text' name='quantita' value=\"$controlli[13]{valore}\" id='quantita'/>";
	}
	else{
		print "<label for='quantita'>Quantita*</label>
		<input type='text' name='quantita' value=\"$controlli[13]{valore}\" id='quantita'/>";
	}
	print "<input type='submit' name='submit' id='submit' value='Memorizza'/>
	</fieldset>
	</form>";
}


# main ------------------------------------------------------------------------------------------------------
sub printContenuto{
	if($page->param("submit") eq "Memorizza"){#se si sta facendo submit
		my $inputValidi=checkForm($page,\@controlli);
		if( !$inputValidi || !checkImage($page) ){
			formRitrasmesso($page,\@controlli);
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

			# upload immagine
			$CGI::POST_MAX = 1024 * 5000;
			my $safe_filename_characters = "a-zA-Z0-9_.-";
			my $upload_dir = "../Public_html/resources/copertineLibri";
			my $filename = $page->param("copertina");
			if ( !$filename ){
				print $page->header ( );
				print "C'è stato un errore nel caricamento del file. Prova a caricare un file più piccolo.";
				exit;
			}
			my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
			$filename = $name . $extension;
			$filename =~ tr/ /_/;
			$filename =~ s/[^$safe_filename_characters]//g;
			if ( $filename =~ /^([$safe_filename_characters]+)$/ ){
				$filename = $1;
			}
			else{
				die "Filename contains invalid characters";
			}
			my $upload_filehandle = $page->upload("copertina");
			my $nomeImmagine=$upload_dir."/".$filename;
			open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
			binmode UPLOADFILE;
			while ( <$upload_filehandle> ){
				print UPLOADFILE;
			}
			close UPLOADFILE;
			# fine upload immagine

			my $altImm=$page->param("altImmagine");
			if(!altImm){$altImm="nessuna descriz";}#da MODIFICARE!
			$libro=$libro."</edizione>
			<trama>$controlli[12]{valore}</trama>
			<copertina src=\"$nomeImmagine\" alt=\"$altImm\"/>
			<quantita>$controlli[13]{valore}</quantita>
			</libro>
			";
			inserimentoSuXML($libro,"libro",$controlli[0]{valore});
			print "fatto...";
		}
	}
	else{# se non si sta facendo submit
		formInserimento();
	}
}

printBody("Inserimento Libri");