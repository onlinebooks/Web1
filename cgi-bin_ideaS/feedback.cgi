#!/usr/bin/perl
use XML::LibXML;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Time::localtime;


print "Content-type: text/html\n\n";

print<<EOF;
 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">


<head>
	<title>Feedback - IDEA Studio Web</title>
	<meta http-equiv="Content-Type"content="text/html; charset=utf-8"/>
	<meta http-equiv="Content-Script-Type"content="text/javascript"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta name="title" content="" />
	<meta name="description" content="Pagina feedback del sito del progetto" />
	<meta name="keywords" content="web designer Padova" />
	<meta name="language" content="italian it" />
	<meta name="author" content="" />
	<link href="../style.css" rel="stylesheet" type="text/css" media="all"/>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	<link rel="icon" href="../resources/favicon.gif" type="image/gif" />
	<script src="../javascript/form-feedback.js" type="text/javascript"></script>
	 <script src="../javascript/menu-responsive.js" type="text/javascript"></script>
</head>
<body onload="abilitamenu()">

EOF

sub controllaForm{
		print "<span class=\"erroreForm\">*Campo non inserito</span>";	
	}

my $file='../data/commenti.xml';
my $parser=XML::LibXML->new();

my $doc=$parser->parse_file($file);


my $radice=$doc->getDocumentElement;

my $page = CGI->new;
my $submit=$page->param('submit');
my $nome;
my $ruolo;
my $commento;




if( $submit){
 $nome=$page->param('nome');
 $ruolo=$page->param('ruolo');
 $commento=$page->param('commento');
 if($nome && $ruolo && $commento){
 my $frammento="         <singolaTestimonianza>
             <Nome>$nome</Nome>
             <Lavoro>$ruolo</Lavoro>
             <Commento>\"$commento\"</Commento>
         </singolaTestimonianza>\n\n";
 my $nodo=$parser->parse_balanced_chunk($frammento);
 $radice->appendChild($nodo);}
 }

print<<EOF;


	<!-- inizio div header -->
	<div id="header">
	
		<!-- inizio div path -->
		<div id="path">
			Ti trovi in: <a href="../index.html" accesskey="g" title="vai alla home" tabindex="1"><span xml:lang="en">Home </span></a>&gt;&gt;<span xml:lang="en"> Feedback</span>
		</div>
		<!-- fine div path -->
		
		<!-- inizio div nav -->
		<div id="nav">
			<div id="logo">
				<a href="../index.html" title="vai alla home" tabindex="2">IDEA <span>Studio Web</span></a>
			</div>
			<div id="menu">
				
				<ul id="nav-menu">
					<li><a href="../index.html" title="vai alla home" xml:lang="en" tabindex="3">Home</a></li>
					<li><a href="../work.html" title="vai alla sezione work" xml:lang="en" tabindex="4">Work</a></li>
					<li xml:lang="en">Feedback</li>
					<li><a href="../cgi-bin/news.cgi" title="vai alla sezione news" xml:lang="en" tabindex="5">News</a></li>
					<li><a href="../contatti.html" title="vai alla sezione contatti" tabindex="6">Contatti</a></li>
					<li><a href="../listino.html" title="vai alla sezione listino" tabindex="7">Listino</a></li>
				</ul>
			</div>
		</div> 
		<!-- fine div nav -->
		
		
		
	</div>
	<!-- fine header -->
	
	
	<!-- inizio main -->
	<div id="main">
	
		<!-- inizio intestazione -->
		<div id="intestazione-feedback">
			
			<div id="contenitore-testo">
				<h1>Cosa dicono di Noi!</h1>
			</div>
			<div id="contenitore-immagine">
				<img src="../resources/feedbackPicture2.png" alt="sfondo con icona per social" usemap="#slider" />

<map name="slider" id="slider">
  <area shape="rect" coords="0,0,450,380" alt="Vai alla sezione Work" title="Vai alla sezione Work" href="../work.html"/>
  <area shape="rect" coords="700,0,1366,380" alt="Vai alla sezione News" title="Vai alla sezione News" href="news.cgi"/>
</map>
			</div>
			
		</div>
		<!-- fine intestazione -->
		
		<div id="contenitore-testimonianze">

EOF

$radice->setNamespace('http://www.ideastudioweb.com','x');
foreach my $singoloCommento ($doc->findnodes('//x:listaTestimonianze/singolaTestimonianza')) {
	
    my $nome = $singoloCommento->getElementsByTagName('Nome');
    my $lavoro = $singoloCommento->getElementsByTagName('Lavoro');
    my $commento = $singoloCommento->getElementsByTagName('Commento');
    utf8::encode($nome);
    utf8::encode($lavoro);
    utf8::encode($commento);
    
    print "<div class=\"singola-testimonianza\">
                <h1>".$nome."</h1>
                <h2>".$lavoro."</h2>
                <p>".$commento."</p>
                <hr></hr>
           </div>";
  }

print<<EOF;

		</div>
		
		<div id="div-form-testimonianze">
			
			<form id="form-testimonianze" action="feedback.cgi" method="post" onsubmit="return validazione()">
				<fieldset>
					<legend>Lasciaci un commento</legend>
					<label id="label-nome" for="nome" >Inserisci il tuo nome</label>

EOF

if($submit && !$nome){&controllaForm;}

print<<EOF;
					<br />
					<input type="text" name="nome" id="nome" value="$nome"/><br />
					<label id="label-ruolo" for="ruolo" >Inserisci il tuo ruolo nella societ&agrave; in cui lavori</label>
EOF

if($submit && !$ruolo){&controllaForm;}

print<<EOF;	

					<br />
					<input type="text" name="ruolo" id="ruolo" value="$ruolo"/><br />
					<label id="label-commento" for="commento">Inserisci il tuo commento</label>
EOF

if($submit && !$commento){&controllaForm;}

print<<EOF;

					<br />
					<textarea name="commento" id="commento" rows="10" cols="30">$commento</textarea><br />
					<input type="submit" name="submit" class="submit" value="Invia" />
				</fieldset>
			</form>
		</div>
	
	</div>
	<!-- fine main -->
	
	
	<!-- inizio footer -->
	<div id="footer">
		<p>Via Ugo Bassi, Padova, Italia - Telefono: 049 1234728 - E-mail: studioideaweb\@gmail.com</p>
<a href="Amministratore.cgi" id="accessoAmm" title="link alla zona riservata di amministrazione">Area di Amministrazione</a>
	</div>
	<!-- fine footer -->
	
</body>
<!-- fine body -->

</html>

EOF
 
 open(OUT,">$file");
print OUT $doc->toString;
close(OUT);

exit(0);
