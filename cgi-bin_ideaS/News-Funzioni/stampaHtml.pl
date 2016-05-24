
#----------------------------------------------------
#	stampaIntestazione() 
#	stampaFine()
#----------------------------------------------------

sub stampaIntestazione{
#CREA IL CODICE HTML DI INTESTAZIONE DELLA PAGINA
print<<EOF
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<link rel="stylesheet" href="../style.css" type="text/css" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<title>News - IDEA Studio Web</title>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	 <link rel="icon" href="../resources/favicon.gif" type="image/gif" />
	<meta name="author" content="Francesco" />
	<meta name="description" content="Le ultime notizie di IDEA Studio web" />
	<meta name="keywords" content="news,idea,studio,web, Padova" />
	<meta http-equiv="Content-Script-Type"content="text/javascript"/>
	<script src="../javascript/news.js" type="text/javascript"></script>
	<script src="../javascript/menu-responsive.js" type="text/javascript"></script>
</head>

<body onload="abilitamenu();">

<div id="header">

	<div id="path">Ti trovi in: <a href="../index.html" accesskey="g" tabindex="1" title="vai alla home" xml:lang="en">Home</a> &gt;&gt; <span xml:lang="en">News</span> </div>
	
	<div id="nav">
	
	<div id="logo">
				<a href="../index.html" title="vai alla home" tabindex="2">IDEA <span>Studio Web</span></a>
			</div>	
	
	<div id="menu">
		
		<ul id="nav-menu">
			<li><a href="../index.html"  title="vai alla home" xml:lang="en" tabindex="3">Home</a></li>
			<li><a href="../work.html"  title="vai alla sezione work" xml:lang="en" tabindex="4">Work</a></li>
			<li><a href="feedback.cgi" title="vai alla sezione feedback" xml:lang="en" tabindex="5">Feedback</a></li>
			<li><span xml:lang="en">News</span></li>
			<li><a href="../contatti.html" title="vai alla sezione contatti" tabindex="6">Contatti</a></li>
			<li><a href="../listino.html" title="vai alla sezione listino" tabindex="7">Listino</a></li>		
		</ul>
	</div>
	</div> 
	
</div>

<div id="main">
	
	<div id="intestazione-news">
		<div id="contenitore-testo">
				<h1>Le nostre imprese, le nostre idee</h1>
			</div>
			<div id="contenitore-immagine">
				<img src="../resources/newsPicture2.png" alt="sfondo per sezione notizie" usemap="#slider" />

<map name="slider" id="slider">
  <area shape="rect" coords="0,0,450,380" alt="Vai alla sezione Feedback" title="Vai alla sezione Feedback" href="feedback.cgi"/>
  <area shape="rect" coords="700,0,1366,380" alt="Vai alla sezione Contatti" title="Vai alla sezione Contatti" href="../contatti.html"/>
</map>
			</div>	
	</div>	
<ul id="navigazione">
	<li><a href="#contenitoreNews" class="navigazione" title="link alle informazioni della pagina">NOTIZIE</a></li>	
	<li><a href="#ricerca" class="navigazione" title="link al form di ricerca">CERCA UNA NOTIZIA</a></li>
	</ul>
	
EOF
}

sub stampaFine{
#CHIUDE LA PAGINA HTML
print<<EOF

</div><!-- fine del main -->




<!-- inizio footer -->
	<div id="footer">
		<p>Via Ugo Bassi, Padova, Italia - Telefono: 049 1234728 - E-mail: studioideaweb\@gmail.com</p>

  <a href="Amministratore.cgi" id="accessoAmm" title="link alla zona riservata di amministrazione">Area di Amministrazione</a>

	</div>
	<!-- fine footer -->

</body>
</html>
EOF
}

return 1;
