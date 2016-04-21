#!C:\xampp\perl\bin\perl.exe

use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

print "Content-type: text/html\n\n";

print<<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<title>Libri - Libronline</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
	<meta http-equiv="Content-Script-Type" content="text/javascript"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta name="title" content="" />
	<meta name="description" content="Home page del sito del progetto" />
	<meta name="keywords" content="libraria Padova" />
	<meta name="language" content="italian it" />
	<meta name="author" content="" />
	<link href="style.css" rel="stylesheet" type="text/css" media="screen"/>
	<link rel="stylesheet" href="printstyle.css" type="text/css" media="print"/>	
	<link rel="stylesheet" href="mobilestyle.css" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)"/>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Fredoka+One%7cShadows+Into+Light+Two%7cCherry+Cream+Soda%7cCinzel+Decorative" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="javascript/libri.js"></script>
</head>
<body>
	<div id="header">
		<span id="logo"></span>
		<h1> Libronline</h1>
		<h2> il tuo libro a portata di mano ovunque sei</h2>
	</div>
		<div id="main">
			<div id="menu">
				<ul>
					<li><a href="index.html" tabindex="0">Home</a></li>
					<li>Libri</li>
					<li><a href="contatti.html"  tabindex="1">Contatti</a></li>	
					<li><a href="registrazione.html" tabindex="2">Registrati</a></li>
					<li><a href="login.html" tabindex="3">Entra</a></li>
				</ul>
			</div>
		<div id="contenuto">
		<div id="path">
			Ti trovi in: <a href="index.html" xml:lang="en">Home</a> » Libri
		</div>
			EOF

sub createSession() {
		$session = new CGI::Session();
		$session->param('pwd', $password);
}


sub getPwd() {
	$session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
		}	
 	else {
		my $pwd = $session->param('pwd');
		return $pwd;
		}
}

sub destroySession() {
$session = CGI::Session->load() or die $!;
$SID = $session->id();
$session->close();
$session->delete();
$session->flush();
}		

# modifica

$page = new CGI;
createSession();
$password=getPwd();

if(!$password){

	my $submit=$page->param('submit');  
	if($submit){
	
		$password=$page->param('pwd'); 
		if($password eq "admin"){
			print "<h1>BENVENUTO</h1>";
			}
		else
			{print "<h1>ERRORE</h1>";}
		}
		
	else{
	
print<<EOF;
		<div id="ricerca">
			<form id="ciao" action="#" method="post" onsubmit="return libri()">
				<fieldset>
					<legend>Ricerca</legend>
					<label id="Rtitolo"  for="titolo">Titolo:</label>
					<input type="text" name="titolo" id="titolo" onblur="#" />
					
					<label id="Rautore" for="autore">Autore:</label>
					<input type="text" name="autore" id="autore" onblur="#" />
				
					<label id="Rgenere" for="genere">Genere:</label>
					<input type="text" name="genere" id="genere" onblur="#" />
												
					<input type="submit" name="submit" id="submit" value="Cerca"/>
					<input type="reset" name="reset" id="reset" value="Reset"/>
				</fieldset>		
			</form>
		</div>
EOF
	
	}
}

else{

	print "<h1>LOGGED</h1>";

}

print<<EOF;		
		
		<div class="libro">
			<img class="immagini" src="immagini/allegiant.jpg" alt="Copertina Allegiant"/>
			<h1>Descrizione:</h1>
			<p> Allegiant è un romanzo di fantascienza per giovani adulti del 2013 di Veronica Roth, terzo libro della serie iniziatasi 
			con Divergent. È stato pubblicato negli Stati Uniti nell'ottobre 2013, mentre in Italia è uscito il 18 marzo 2014.</p>
			<p>A differenza dei due romanzi precedenti, questo si caratterizza per l'alternanza di capitoli seguenti il punto di vista 
			di Tris o di Tobias, mantenendo tale impostazione fin quasi alla fine.</p>
			<p><a href = "ebook/Allegiant.pdf"> Scarica Allegiant.pdf </a>(1,56 MB)</p>
		</div>
		<div class="libro">
			<img class="immagini" src="immagini/insurgent.jpg" alt="Copertina Insurgent" />
			<h1>Descrizione:</h1>
			<p> Insurgent è un romanzo di fantascienza distopica per giovani adulti del 2012 di Veronica Roth, secondo libro della 
			serie iniziata con Divergent. È stato pubblicato negli Stati Uniti il 1º maggio 2012 e in Italia, per la De Agostini, 
			il 30 novembre 2013. </p>
			<p>Il romanzo riparte esattamente da dove si era interrotto l'ultimo capitolo di Divergent.</p>
			<p><a href = "ebook/Insurgent.pdf"> Scarica Insurgent.pdf </a> (2,02 MB)</p>
		</div>
		<div class="libro">
			<img class="immagini" src="immagini/Divergent.jpg" alt="Copertina Divergent"/>
			<h1>Descrizione:</h1>
			<p> Divergent è un romanzo di fantascienza per ragazzi del 2011 di Veronica Roth, primo capitolo dell'omonima
			trilogia. Pubblicato in America il 3 maggio 2011, è uscito in Italia per la De Agostini il 22 marzo 2012.</p>
			<p>Il romanzo è una distopia per ragazzi ambientata in un futuro non specificato in cui gli esseri umani hanno 
			posto fine alle guerre dividendosi autonomamente in fazioni e svolgendo ognuno il mestiere più consono alle 
			proprie naturali inclinazioni.</p>
			<p><a href = "ebook/Divergent.pdf"> Scarica Divergent.pdf </a>(1,31 MB)</p>
		</div>
		</div>
		</div>
	<div id="footer">
	via ugo bassi libreria libronline
	</div>
</body>
</html>
EOF
