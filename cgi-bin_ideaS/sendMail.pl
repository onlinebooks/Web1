#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);

use Net::SMTP::SSL;

my $page=new CGI;
my $indirizzo=$page->param('email');
my $oggetto=$page->param('oggetto');
my $contenuto=$page->param('messaggio');

my $ckindirizzo=($indirizzo=~m/^([\w\-\+\.]+)\@([\w\-\+\.]+)\.([\w\-\+\.]+)$/);
my $ckoggetto=($oggetto=~m/^(.{2,})$/);
my $ckcontenuto=($contenuto=~m/^(.{5,})$/);

if($ckindirizzo && $ckoggetto && $ckcontenuto){&invia($indirizzo,$oggetto,$contenuto);}
else{
	print "Content-type: text/html\n\n";
	&stampaHeader();
	
print '<div id="contatti">
	<h1>Dove trovarci e come Contattarci</h1>
		<div class="info">
		
			 <div class="form_interna">
				<div id="menu1">
				<ul>
					<li> Indirizzo: Via Ugo Bassi, Padova, (PD) Italia </li>
					<li> Telefono: 049 1234728 </li>
					<li> E-mail: studioideaweb@gmail.com </li>
				</ul>
				</div>
			</div>
		</div>
				<form id="mail" action="sendMail.pl" method="post"><fieldset><legend>Invio posta</legend>';
		if($ckindirizzo){print "<label for='email'>Email:</label><br />
					<input type='text' size='20' id='email' name='email' value=\"$indirizzo\" /> <br />";}
		else{print "<label for=\"email\" class='erroreForm'>Email: inserire un indirizzo valido</label><br />
					<input type=\"text\" size=\"20\" id=\"email\" name=\"email\" /> <br />";}
		if($ckoggetto){print "<label for=\"oggetto\">Oggetto:</label><br />
					<input type=\"text\" id=\"oggetto\" size=\"20\" name=\"oggetto\" value=\"$oggetto\" /> <br />";}
		else{print "<label for=\"oggetto\" class='erroreForm'>Oggetto: inserire almeno 2 caratteri</label><br />
					<input type=\"text\" id=\"oggetto\" size=\"20\" name=\"oggetto\" /> <br />";}
		if($ckcontenuto){print "<label for=\"messaggio\">Messaggio:</label><br />
					<textarea name=\"messaggio\" id=\"messaggio\" rows=\"10\" cols=\"60\" >$contenuto</textarea>  <br/>";}
		else{print "<label for=\"messaggio\" class='erroreForm'>Messaggio: inserire testo di almeno 5 caratteri</label><br />
					<textarea name=\"messaggio\" id=\"messaggio\" rows=\"10\" cols=\"60\" ></textarea>  <br/>";}			
					
		print '<input type="submit" id="submit" value="Invia" />
				</fieldset></form>
	</div>
	<div id="contenitore-contatti">
			<div class="servizio-contatti">
				<h2>Finotello Luca</h2>
				<p>Laureato presso il dipartimento di matematica di Padova ad indirizzo informatica.</p>';
	print "<p>All'interno dell'azienda si occupa di rispodere e di chiarire ogni dubbio dei clienti.</p>";
	print '</div>
			<div class="servizio-contatti">
			<h2>Scaglione Stefano</h2>
				<p>Laureato presso il dipartimento di matematica di Padova ad indirizzo informatica.</p>';
	print "<p> Il suo ruolo nell'azienda è quello di illustrare ai nostri amatissimi clienti le varie componenti di cui è strutturato il loro futuro sito web. </p>";
	print '</div>
			<div class="servizio-contatti">
			<h2>Zaidan Gino</h2>
				<p>Laureato presso il dipartimento di matematica di Padova ad indirizzo informatica</p>
			</div>
			<div class="servizio-contatti">
			<h2>Bizzaro Francesco</h2>
				<p>Laureato presso il dipartimento di matematica di Padova ad indirizzo informatica.</p>
			</div>
		</div>';

	&stampaFooter();
}

sub invia{
my $indirizzo=$_[0];
my $oggetto=$_[1];
my $contenuto=$_[2];

my $smtp = Net::SMTP::SSL->new('smtp.gmail.com',
                    Port=> 465,
                    Timeout => 10,
                    Hello=>'smtp.gmail.com'
                    );
#print $smtp->domain,"\n";
my $sender = "studioideaweb\@gmail.com";
my $password = "francescoginolucastefano";
$smtp->auth ( $sender, $password ) or die "could not authenticate\n";
my $receiver = "studioideaweb\@gmail.com";

$smtp->mail($sender);
$smtp->to($receiver);
$smtp->data();
$smtp->datasend("To: <$receiver> \n");
$smtp->datasend("From: <$sender> \n");
$smtp->datasend("Content-Type: text/html \n");
$smtp->datasend("Subject: $oggetto");
$smtp->datasend("\n");
$smtp->datasend("<br/>Mittente $indirizzo<br/><br/>$contenuto");
$smtp->dataend();
$smtp->quit();

print "Content-type: text/html\n\n";

&stampaHeader();
print "<div id='esitoMail'><h1>Invio Mail</h1><p>La mail è stata inviata con successo. Le risponderemo a breve all'indirizzo di posta indicato.</p>
<a href='../contatti.html'>Torna a Contatti</a></div>";
&stampaFooter();
}

sub stampaHeader{
print<<EOF
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"  xml:lang="it" lang="it">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta http-equiv="Content-Script-Type"content="text/javascript"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta name="title" content="" />
	<meta name="description" content="Home page del sito del progetto" />
	<meta name="keywords" content="" />
	<meta name="language" content="italian it" />
	<meta name="author" content="" />
	<link href="../style.css" rel="stylesheet" type="text/css" media="all"/>
	<link rel="icon" href="" type="image/png" />
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	<link rel="icon" href="../resources/favicon.gif" type="image/gif" />
	 <script src="../javascript/menu-responsive.js" type="text/javascript"></script>
	<title>Contatti - IDEA Studio Web</title>
</head>
<body onload="abilitamenu();">
<div id="header">
	<div id="path">
		<p> Ti trovi in:  <a href="../index.html"><span xml:lang="en">Home </span></a>&gt;&gt; Contatti</p>
	</div>
	<div id="nav">
		<div id="logo">
				<a href="../index.html" accesskey="g" tabindex="0">IDEA <span>Studio Web</span></a>
		</div>
		
		<div id="menu">
			
			<ul id="nav-menu">
			<li><a href="../index.html"  xml:lang="en" tabindex="1">Home</a></li>
			<li><a href="../work.html"  xml:lang="en" tabindex="2">Work</a></li>
			<li><a href="feedback.cgi"  xml:lang="en" tabindex="3">Feedback</a></li>
			<li><a href="news.cgi"  xml:lang="en" tabindex="4">News</a></li>
			<li>Contatti</li>
			<li><a href="../listino.html"  tabindex="5">Listino</a></li>
		</ul>
		</div>
	</div>
</div>
	
<div id="main">


	<!-- inizio intestazione -->
		<div id="intestazione-contatti">
			
			<div id="contenitore-testo">
				<h1>Sempre connessi</h1>
			</div>
			<div id="contenitore-immagine">
				<img src="../resources/contattiPicture.jpg" alt="contatti su sfondo verde" usemap="#slider" />

<map name="slider" id="slider">
  <area shape="rect" coords="0,0,450,380" alt="Vai alla sezione News" title="Vai alla sezione News" href="news.cgi"/>
  <area shape="rect" coords="700,0,1366,380" alt="Vai alla sezione Listino" title="Vai alla sezione Listino" href="../listino.html"/>
</map>
			</div>
			
		</div>
		<!-- fine intestazione -->
EOF

}

sub stampaFooter{
print<<EOF
</div>
<div id="footer">
		<p>Via Ugo Bassi, Padova, Italia - Telefono: 049 1234728 - E-mail: studioideaweb\@gmail.com</p>
<a href="Amministratore.cgi" id="accessoAmm" title="link alla zona riservata di amministrazione">Area di Amministrazione</a>
</div>
</body>
</html>
EOF

}

