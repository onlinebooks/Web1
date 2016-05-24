#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;

my $page=new CGI;

print "Content-type: text/html\n\n";

my $npag=$page->param("numPagine");
if(&checkPag($npag)){
	my $base=&calcola($page,$npag);
	my $upper=2*$base;
	&stampaPag($base,$upper);
	}
else{
	&stampaErrore($page);
	}


sub calcola{
	my $page=$_[0];
	my $npag=$_[1];
	my $database=$page->param("database");
	my $admin=$page->param("admin");
	my $ecommerce=$page->param("ecommerce");
	my $blog=$page->param("blog");
	my $dinamico=$page->param("dinamico");
	my $responsive=$page->param("responsive");
	my $accessibilita=$page->param("accessibilita");
	my $seo=$page->param("seo");
	my $social=$page->param("social");
	my $mantenimento=$page->param("mantenimento");
	my $costo=300+150*$npag;
	if($database){$costo=$costo+600;}
	if($admin){$costo=$costo+150;}
	if($ecommerce){$costo=$costo+750;}
	if($blog){$costo=$costo+350;}
	if($dinamico){$costo=$costo+500;}
	if($responsive){$costo=$costo+500;}
	if($seo){$costo=$costo+350;}
	if($social){$costo=$costo+50;}
	if($mantenimento){$costo=$costo+200;}
	if($accessibilita){$costo=$costo+($costo*0.05);}
	return $costo;
}

sub checkPag{
my $npag=$_[0];
return $npag=~m/^([123456789][0123456789]{0,})$/;
}

sub stampaIntestazione{
 print<<EOF

<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<link rel="stylesheet" href="../style.css" type="text/css" />
	<title>Listino - IDEA Studio Web</title>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	 <link rel="icon" href="resources/favicon.gif" type="image/gif" />
	<meta name="author" content="cesco" />
	<meta name="description" content="I prezzi di IDEA Studio web" />
	<meta name="keywords" content="listino,idea,studio,web,Padova" />
	<script type="text/javascript" src="javascript/listino.js"></script>
	<script src="../javascript/menu-responsive.js" type="text/javascript"></script>
</head>

<body onload="abilitamenu();">

<div id="header">

	<div id="path">Ti trovi in: <a href="../index.html" accesskey="g" tabindex="1" xml:lang="en">Home</a> &gt;&gt; Listino </div>
	
	<div id="nav">
	
	<div id="logo">
				<a href="../index.html" tabindex="2">IDEA <span>Studio Web</span></a>
			</div>	
	
	<div id="menu">
		
		<ul id="nav-menu">
			<li><a href="../index.html" xml:lang="en" tabindex="3">Home</a></li>	
			<li><a href="../work.html" xml:lang="en" tabindex="4">Work</a></li>
			<li><a href="feedback.cgi" xml:lang="en" tabindex="5">Feedback</a></li>
			<li><a href="news.cgi" xml:lang="en" tabindex="6">News</a></li>
			<li><a href="../contatti.html" tabindex="7">Contatti</a></li>		
			<li>Listino</li>		
					
		</ul>
	</div>
	</div> 
	
</div>

<div id="main">
	
	<div id="intestazione-listino">
		<div id="contenitore-testo">
				<h1>Chiedi un preventivo, è gratis</h1>
			</div>
			<div id="contenitore-immagine">
				<img src="../resources/listinoPicture.jpg" alt="sfondo rappresentante un cartellino dei prezzi" usemap="#slider"/>

<map name="slider" id="slider">
  <area shape="rect" coords="0,0,450,380" alt="Vai alla sezione Contatti" title="Vai alla sezione Contatti" href="../contatti.html"/>
  <area shape="rect" coords="700,0,1366,380" alt="Vai alla Home" title="Vai alla Home" href="../index.html"/>
</map>
				
			</div>	
	</div>	
	
	<ul id="navigazione">
	<li><a href="#infoPrezzi" class="navigazione" title="link alle informazioni sui preventivi">INFORMAZIONI SUL PREVENTIVO</a></li>	
	<li><a href="#vociPreventivo" class="navigazione" title="link alla spiegazione delle caratteristiche di un sito">CARATTERISTICHE DEI SITI</a></li>	
	<li><a href="#ricercaPrezzo" class="navigazione" title="link al form per il calcolo del prezzo">STIMA IL COSTO DEL TUO SITO</a></li>
	</ul>
EOF

}

sub stampaInfo{
print<<EOF

   <div id="infoPrezzi">
	<!-- div id="introPreventivo"-->
	<h2>Chiedi un preventivo gratis</h2>
	<p>Richiedi una <strong>consulenza gratuita</strong> per iniziare a progettare il tuo sito, è semplice: basta andare nella sezione 
	<a href="../contatti.html">contatti</a>. In breve tempo analizzeremo le tue esigenze e ti forniremo un preventivo, senza impegno.</p>
	<p>Ogni sito richiede particolari tecnologie e deve essere progettato in maniera accurata, per fornire in maniera ottimale le funzionalità che 
	lo caratterizzano. Questo ne determina la complessità e i costi di produzione. Di seguito sono elencate le 
	<strong>opzioni principali</strong> che andiamo a considerare nella fase di progettazione. Con la stesura del preventivo si
	fisseranno le linee guida del progetto ed il relativo costo.</p>
   </div>

   <div id="vociPreventivo">
	<h3>Perché quel prezzo?</h3><a href="#header" class="navigazione" title="torna a inizio pagina">torna a inizio pagina</a>
	<dl>
	<dt>Quantità di pagine</dt>
		<dd>Siti di grandi dimensioni comportano la necessità di un lavoro accurato di <em>progettazione</em>, per selezionare 
		le aree logiche principali e definire interfacce consistenti. Il costo cresce in modo lineare con la grandezza del sito.</dd>
	<dt xml:lang="en">Database</dt>
		<dd>Se si vogliono raccogliere dati dagli utenti, per poi analizzarli in modo efficente, è spesso utile (se non necessario) 
		configurare una base di dati. A seconda della tecnologia impiegata (es. <span xml:lang="en">mysql</span>, <span xml:lang="en">oracle</span>,
		<span xml:lang="en">mongoDB</span>) possono essere richiesti 
		costi aggiuntivi.</dd>
	<dt>Area amministrativa</dt>
		<dd>Se si vogliono fornire funzionalità privilegiate per gli amministratori del sito, sarà necessario costruire un'intera 
		area il cui accesso sarà condizionato da una precedente fase di <span xml:lang="en">login</span>. Questo comporta una progettazione più sofisticata 
		del sito.</dd>
	<dt xml:lang="en">E-commerce</dt>
		<dd>Per i siti di <span xml:lang="en">e-commerce</span> deve essere garantita una maggiore affidabilità, 
		sopratutto per quanto riguarda il pagamento 
		<span xml:lang="en">on-line</span> e la selezione della merce. I dati degli utenti devono inoltre essere custoditi in sicurezza. Ne consegue una 
		responsabilità maggiore da parte dello sviluppatore.</dd>	
	<dt xml:lang="en">Blog</dt>
		<dd>Per inserire un <span xml:lang="en">blog</span> si ha spesso la necessità di un <span xml:lang="en">database</span>. 
		Ma oltre a questo è richiesto un certo quantitativo
		di lavoro nello sviluppo di una interfaccia adatta all'interazione attiva con l'utente, e sopratutto all'attuazione 
		di meccanismi di sicurezza che controllino l'input ricevuto.</dd>
	<dt>Sito dinamico</dt>
		<dd>Una pagina <abbr xml:lang="en" title="hypertext markup language">html</abbr> statica (il cui contenuto è fissato) 
		viene semplicemente inviata dal <span xml:lang="en">server</span> a fronte di una richiesta.
		Una pagina dinamica invece deve essere &quot;creata al volo&quot; nel momento in cui risultasse necessaria. Andrà 
		pertanto gestito il meccanismo di creazione.</dd>
	<dt>Sito <span xml:lang="en">responsive</span></dt>
		<dd>Un sito <span xml:lang="en">responsive</span> si deve adattare ad ogni schermo in cui viene visualizzato, sia che si tratti di un
		<span xml:lang="en">desktop</span>, di un <span xml:lang="en">tablet</span>, o di uno <span xml:lang="en">smartphone</span>. Per 
		questo motivo la gestione del <span xml:lang="en">layout</span> aumenterà in complessità.</dd>
	<dt>Massima accessibilità</dt>
		<dd>Tutti i siti di qualità dovrebbero curare molto l'aspetto dell'accessibilità - è uno dei nostri
		<a href="../work.html">principi</a>. Tuttavia questo ha un costo, poichè per garantirla c'è la necessità di analizzare 
		ogni elemento presente nella pagina con occhio critico.</dd>
	<dt><abbr xml:lang="en" title="Search Engine Optimization">SEO</abbr></dt>
		<dd>Apparire fra i primi risultati di una ricerca è un aspetto cruciale per il successo di un sito. Avere buoni contenuti serve
		a raggiungere questo scopo, ma potrebbe non bastare. Per migliorare la valutazione che le proprie pagine ricevono dai motori
		di ricerca esistono diverse euristiche. La qualità del codice è molto rilevante.</dd>
	<dt xml:lang="en">Social Media Integration</dt>
		<dd>Il traffico di rete generato dai <span xml:lang="en">social network</span> è in continua crescita, tanto che 
		<a href="http://www.facebook.com" title="link al sito esterno Facebook" xml:lang="en">Facebook</a> 
		ha superato <a href="http://www.google.com" title="link al sito esterno Google" xml:lang="en">Google</a> 
		per traffico di rete. Avere una pagina dedicata in vari siti sociali aumenta la probabilità di essere visti.</dd>
	<dt>Manutenzione</dt>
		<dd>Un sito web necessita di essere manutenuto nel tempo. Deve aggiornarsi, evolversi e tutto senza che vengano a formarsi problemi
		di incompatibilità con versioni precedenti. Per migliorare questa fase serve che il codice sia leggibile e strutturato in maniera chiara... con
		più attenzione di un sito fermo.</dd>
	</dl>
   </div>
EOF

}

sub stampaChiusura{
print<<EOF

	</div>	
	
</div><!-- fine del main -->




<!-- inizio footer -->
	<div id="footer">
		<p>Via Ugo Bassi, Padova, Italia - Telefono: 049 1234728 - E-mail: ideawebstudio\@gmail.com</p>
<a href="Amministratore.cgi" id="accessoAmm" title="link alla zona riservata di amministrazione">Area di Amministrazione</a>

	</div>
	<!-- fine footer -->

</body>
</html>
EOF

}

sub stampaForm{
my $err=$_[0];
my $page=$_[1];
my $database=$page->param("database");
my $admin=$page->param("admin");
my $ecommerce=$page->param("ecommerce");
my $blog=$page->param("blog");
my $dinamico=$page->param("dinamico");
my $responsive=$page->param("responsive");
my $accessibilita=$page->param("accessibilita");
my $seo=$page->param("seo");
my $social=$page->param("social");
my $mantenimento=$page->param("mantenimento");

if($database){$database="checked=\"checked\""}
if($admin){$admin="checked=\"checked\""}
if($ecommerce){$ecommerce="checked=\"checked\""}
if($blog){$blog="checked=\"checked\""}
if($dinamico){$dinamico="checked=\"checked\""}
if($responsive){$responsive="checked=\"checked\""}
if($accessibilita){$accessibilita="checked=\"checked\""}
if($seo){$seo="checked=\"checked\""}
if($social){$social="checked=\"checked\""}
if($mantenimento){$mantenimento="checked=\"checked\""}

if($err==0){
$database="";
$admin="";
$ecommerce="";
$blog="";
$dinamico="";
$responsive="";
$accessibilita="";
$seo="";
$social="";
$mantenimento="";
}

print '<div id="ricercaPrezzo">
		<h2>Stima il costo</h2><a href="#header" class="navigazione" title="torna a inizio pagina">torna a inizio pagina</a>
		<div id="costo">
		<p>Siti semplici (1-10 pagine) possono venire a costare dai 400€ ai 10000€ nella media. Siti più complessi (più di 10 pagine e con una
		programmazione rilevante) tra i 10000€ e i 25000€.</p>
		<p>Compilando il form sottostante è possibile stimare il costo per la realizzazione del proprio sito, in base alle 
		caratteristiche che si vogliono richiedere. Questo prezzo è solamente una stima: il prezzo reale verrà concordato mediante il preventivo.</p>
		</div>
		<form id="preventivo" action="listino-prezzo.cgi" method="post" onsubmit="return calcolaPrezzo();">
			<fieldset>
				<legend>Indica le funzionalità richieste</legend>
				<fieldset><legend>Struttura</legend>
				<label id="labelnumPagine" ';
if($err){print 'class="erroreForm" for="numPagine">Quante pagine avrà il sito? Numero intero >0';}
else{print 'for="numPagine">Quante pagine avrà il sito?';}
print<<EOF

				</label>
				<input type="text" name="numPagine" id="numPagine" onBlur="checkNpag();" />
				
				<input type="checkbox" class="checkb" name="database" id="database" $database />	
				<label for="database">Ho bisogno di un <span xml:lang="en">database</span> per la gestione 
				e l'analisi dei dati</label>			
				
				<input type="checkbox" class="checkb" name="admin" id="admin" $admin />
				<label for="admin">Ho bisogno di una sezione amministrativa</label>	
				
				<input type="checkbox" class="checkb" name="ecommerce" id="ecommerce" $ecommerce />
				<label for="ecommerce">Ho bisogno di un sito di <span xml:lang="en">e-commerce</span></label>	
				
				<input type="checkbox" class="checkb" name="blog" id="blog" $blog />	
				<label for="blog">Ho bisogno di inserire un blog</label>	
					
				</fieldset>
				
				<fieldset><legend>Caratteristiche opzionali</legend>
				
				<input type="checkbox" class="checkb" name="dinamico" id="dinamico" $dinamico />
				<label for="dinamico">Ho bisogno di un sito dinamico</label>	
				
				<input type="checkbox" class="checkb" name="responsive" id="responsive" $responsive />	
				<label for="responsive">Ho bisogno di un sito <span xml:lang="en">responsive</span></label>	
				
				<input type="checkbox" class="checkb" name="accessibilita" id="accessibilita" $accessiblita />
				<label for="accessibilita">Ho bisogno di garantire la massima accessibilità a tutte le categorie 
				di utenti</label>	
						
				</fieldset>
				
				<fieldset><legend xml:lang="en">Findability</legend>
				
				<input type="checkbox" class="checkb" name="seo" id="seo" $seo />
				<label for="seo" xml:lang="en">Search engine optimization</label>	

				<input type="checkbox" class="checkb" name="social" id="social" $social />
				<label for="social" xml:lang="en">Social media integration</label>	
										
				</fieldset>
				
				<fieldset><legend>Manutenzione</legend>
				
				<input type="checkbox" class="checkb" name="mantenimento" id="mantenimento" $mantenimento />
				<label for="mantenimento">Ho bisogno che il sito venga manutenuto e aggiornato nel tempo</label>	
								
				</fieldset>
				
				<input type="submit" name="submit" id="submit" value="Calcola"/>
			</fieldset>		
		</form>	

EOF

}

sub stampaErrore{
my $page=$_[0];
&stampaIntestazione();
print'<div id="stimaPrezzo"><h2>Stima del prezzo</h2><p id="Risultato">Errore di inserimento: inserisci un numero intero maggiore di 0 nella
	casella per il numero di pagine.</p></div>';
&stampaInfo();
&stampaForm(1,$page);
&stampaChiusura();

}

sub stampaPag{
my $base=$_[0];
my $upper=$_[1];
&stampaIntestazione();
print "	<div id=\"stimaPrezzo\"><h2>Stima del prezzo</h2><p id=\"Risultato\">Il prezzo stimato per la realizzazione del tuo sito è fra 
	<strong>$base€ e $upper€</strong></p></div>";
&stampaInfo();
&stampaForm(0,$page);
&stampaChiusura();
}
