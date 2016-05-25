#!perl

use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;
use XML::LibXML;
use Digest::SHA  qw(sha1 sha1_hex sha1_base64);

require 'functions.pl';

#print "Content-type: text/html\n\n";




sub printContenuto{

	my $page=new CGI;
	my $session=CGI::Session->new($page);
	#print $session->header();
	
	if($page->param("submit")){
		my $username = $page->param("username");
		my $password = $page->param("password");
		if($password){
			&login($session,$password);
			my $log=&logged($session);
			if($log){ print "<META HTTP-EQUIV=refresh CONTENT='1;URL=../cgi_bin/index.cgi'>\n";} 
			else {print "<h1>errore</h1>";} 
			}
	}

	
	if($page->param("submitR")){
		#REGISTRAZIONE
		my $nome = $page->param("nome");
		my $cognome = $page->param("cogome");
		my $nascita = $page->param("nascita");
		my $usernameR = $page->param("usernameR");
		my $emailUtente = $page->param("emailUtente");
		my $passwordR = $page->param("passwordR");
		my $confermaPassword = $page->param("confermaPassword");
		
		
		
	}
	
	
	if($page->param("logout") eq "logout"){&logout($session);}

	my $log=&logged($session);


	if(!$log){
	#pagina di login
	my $err="";
	if($digitata){$err="class=\"invalid\"";}
	&loginForm($err);
	}else{}

	print"<h2>Entra o registrati per accedere a più funzionalità</h2>
		<form class='formLogin' method='post' action='login.cgi'>
			<fieldset>
				<legend>Login</legend>
				<label for='username'>Inserisci username</label><input type='text' id='username'  name='username' />
				<label for='password'>Inserisci password</label><input type='password' id='password'  name='password' />
				<input type='submit' name='submit' class='submit' value='Entra'/>
			</fieldset>
		</form>
		<form class='formLogin' method='post' action='login.cgi'>
			<fieldset>
				<legend>Registrazione</legend>
				<label for='nome'>Inserisci Nome</label><input type='text' id='nome'  name='nome' />
				<label for='cognome'>Inserisci Cognome</label><input type='text' id='cognome'  name='cognome' />
				<label for='nascita'>Inserisci anno di nascita</label><input type='text' id='nascita'  name='nascita' />
				<label for='usernameR'>Inserisci username</label><input type='text' id='usernameR'  name='usernameR' />
				<label for='emailUtente'>Inserisci Email</label><input type='text' id='emailUtente'  name='emailUtente' />
				<label for='passwordR'>Inserisci password</label><input type='password' id='passwordR'  name='passwordR' />
				<label for='confermaPassword'>Conferma password</label><input type='password' id='confermaPassword'  name='confermaPassword' />
				<input type='submit' name='submitR' id='submitR' value='Registrati'/>
			</fieldset>
		</form>";
	
	
}


#need $title $description $keywords
printHead('Login - Biblioteca di Portobuffolè','Login del sito della biblioteca comunale di Portobuffolè','login biblioteca Portobuffolè');

printBody("Login");



	
