#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
#use CGI::Session;
require 'functions.pl';

print "Content-type: text/html\n\n";

sub printContenuto{
	print"<h2> Libri consigliati della settimana:</h2>

			<div class='contenitore-img'>
				<div class='immagine'>
					<img src='immagini/Divergent.jpg' alt='Copertina Divergent'/>
					<a href='#' class='bottone'>Scopri di pi&ugrave;</a>
				</div>
				<div class='immagine'>
					<img src='immagini/insurgent.jpg' alt='Copertina Insurgent'/>
					<a href='#' class='bottone'>Scopri di pi&ugrave;</a>
				</div>
				<div class='immagine'>
					<img src='immagini/allegiant.jpg' alt='Copertina Allegiant'/>
					<a href='#' class='bottone'>Scopri di pi&ugrave;</a>
				</div>
				<div class='immagine'>
					<img src='immagini/vale.jpeg' alt='Copertina Valentino'/>
					<a href='#' class='bottone'>Scopri di pi&ugrave;</a>
				</div>
				<div class='immagine'>
					<img src='immagini/anna_karenina.jpg' alt='Copertina Anna Karenina'/>
					<a href='#' class='bottone'>Scopri di pi&ugrave;</a>
				</div>
			</div>

			<h2>Le ultime novit&agrave; da non perdere!</h2>

			<div class='contenitore-img'>
				<div class='immagine'>
					<img src='immagini/delitto-e-castigo-dostoevskij.jpg' alt='Copertina Delitto e castigo'/>
				</div>
				<div class='immagine'>
					<img src='immagini/il-lungo-addio.jpg' alt='Copertina Il lungo addio'/>
				</div>
				<div class='immagine'>
					<img src='immagini/lovecraft_antologia.jpg' alt='Copertina Lovecraft'/>
				</div>
				<div class='immagine'>
					<img src='immagini/neve_di_primavera_mishima.png' alt='Copertina Neve di primavera'/>
				</div>
				<div class='immagine'>
					<img src='immagini/norwegian_wood.jpg' alt='Copertina Norwegian wood'/>
				</div>
			</div>";

}

#need $title $description $keywords
printHead('Home - Biblioteca di Portobuffolè','Home page del sito della biblioteca comunale di Portobuffolè','biblioteca Portobuffolè');

printBody("Home");


