#!usr/bin/perl


use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

require 'functions.pl';


print "Content-type: text/html\n\n";

sub printContenuto{
	
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

}

#need $title $description $keywords
printHead('Catalogo - Biblioteca di Portobuffolè','pagina catalogo del sito della biblioteca comunale di Portobuffolè','catalogo biblioteca Portobuffolè');

printBody("Catalogo");
