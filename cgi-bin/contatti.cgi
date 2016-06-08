#!perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;
use CGI qw(:standard);
use XML::LibXML;
#use Net::SMTP::SSL;
require 'functions.pl';

my $page = CGI->new;
my $session = CGI::Session->new( undef, $page, { Directory => '/tmp' } )
  or die CGI::Session->errstr;

print $session->header(-charset => 'UTF-8');

sub printContenuto{
	my @controlli;
	if($page->param("submit")){
		my $nome=$page->param("nome");
		if(!$nome){$controlli[0]="nv";}
		else{$controlli[0]="v";}
		my $email=$page->param("email");
		my $checkEmail=($email=~m/^([\w\-\+\.]+)\@([\w\-\+\.]+)\.([\w\-\+\.]+)$/);
		if(!$email || !$checkEmail){$controlli[1]="nv";}
		else{$controlli[1]="v";}
		my $messaggio=$page->param("messaggio");
		if(!$messaggio){$controlli[2]="nv";}
		else{$controlli[2]="v";}
		my $size = @controlli;
		my $v=0;
		for (my $i=0; $i < $size; $i++){
			if($controlli[$i] eq "v"){$v=$v+1;}
		}
		if($v eq $size){
		#invia($nome,$email,$messaggio);
		print "
		<p id='confermaInvioMail'>Email inviata con successo! Riceverai presto risposta.</p>
		<h2>Dove trovarci</h2>
				
				<p>La biblioteca si trova in Piazza Vittorio Emanuele II a Portobuffole (TV) ed è aperta da martedì a venerdì dalle 9.00 alle 13.00 e  dalle 14.30 alle 18.30. Il sabato dalle 9.00 alle 13.00.</p>
				
				<h2>Come contattarci</h2>
				<p>Chiama il numero 0422 850020 oppure invia una email compilando i dati qui sotto</p>
				
				<form id='formContatti' action='contatti.cgi' method='post' onsubmit='return contatti()'>
					<fieldset><legend>Compila i dati</legend>
						<label for='nome'>Nome</label><input type='text' name='nome' id='nome'/>
						<label for='email'><span xml:lang='en'>Email</span></label><input type='text' name='email' id='email'/>
						<label for='messaggio'>Messaggio</label><textarea rows='10' cols='50' name='messaggio' id='messaggio'></textarea>
						<input type='submit' name='submit' id='submit' value='Invia'/>
					</fieldset>
				</form>
		";
		}
		else{
			print"
			<h2>Dove trovarci</h2>
				<p>La biblioteca si trova in Piazza Vittorio Emanuele II a Portobuffole (TV) ed è aperta da martedì a venerdì dalle 9.00 alle 13.00 e  dalle 14.30 alle 18.30. Il sabato dalle 9.00 alle 13.00.</p>
				
				<h2>Come contattarci</h2>
				<p>Chiama il numero 0422 850020 oppure invia una email compilando i dati qui sotto</p>
				<form id='formContatti' action='contatti.cgi' method='post' onsubmit='return contatti()'>
					<fieldset><legend>Compila i dati</legend>";
			if($controlli[0]eq "nv"){print"<label for='nome' class='erroreInserimento'>Nome non inserito correttamente</label><input type='text' id='nome'  name='nome' value=\"$nome\" />";}
			else {print"<label for='nome'>Nome</label><input type='text' id='nome'  name='nome' value=\"$nome\" />";}
			if($controlli[1]eq "nv"){print"<label for='email' class='erroreInserimento'>Inserire una <span xml:lang='en'>email</span> valida</label><input type='text' id='email'  name='email' value=\"$email\" />";}
			else {print"<label for='email'><span xml:lang='en'>Email</span></label><input type='text' id='email'  name='email' value=\"$email\" />";}
			if($controlli[2]eq "nv"){print"<label for='messaggio' class='erroreInserimento'>Messaggio non inserito correttamente</label><textarea rows='10' cols='50' name='messaggio' id='messaggio' >$messaggio</textarea>";}
			else {print"<label for='messaggio'>Messaggio</label><textarea rows='10' cols='50' name='messaggio' id='messaggio' >$messaggio</textarea>";}
			print"
			<input type='submit' name='submit' id='submit' value='Invia'/>
					</fieldset>
				</form>
			";
		}
	
	}
	else{
	print"
	<h2>Dove trovarci</h2>
				<p>La biblioteca si trova in Piazza Vittorio Emanuele II a Portobuffole (TV) ed è aperta da martedì a venerdì dalle 9.00 alle 13.00 e  dalle 14.30 alle 18.30. Il sabato dalle 9.00 alle 13.00.</p>
				
				<h2>Come contattarci</h2>
				<p>Chiama il numero 0422 850020 oppure invia una email compilando i dati qui sotto</p>
				<form id='formContatti' action='contatti.cgi' method='post' onsubmit='return contatti()'>
					<fieldset><legend>Compila i dati</legend>
						<label for='nome'>Nome</label><input type='text' name='nome' id='nome'/>
						<label for='email'><span xml:lang='en'>Email</span></label><input type='text' name='email' id='email'/>
						<label for='messaggio'>Messaggio</label><textarea rows='10' cols='50' name='messaggio' id='messaggio'></textarea>
						<input type='submit' name='submit' id='submit' value='Invia'/>
					</fieldset>
				</form>
	
	";
	}

}

#need $title $description $keywords
printHead('Contatti - Biblioteca di Portobuffolè','Pagina relativa ai contatti del sito della biblioteca comunale di Portobuffolè','contatti biblioteca Portobuffolè');

printBody("Contatti",$session);