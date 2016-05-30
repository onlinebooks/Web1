#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

print "Content-type: text/html\n\n";


sub createSession() {
   my	$session = new CGI::Session();
		$session->param('pwd',my $password);
}


sub getPwd() {
	my $session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
		}	
 	else {
		my $pwd = $session->param('pwd');
		return $pwd;
		}
}

sub destroySession() {
my $session = CGI::Session->load() or die $!;
my $SID = $session->id();
$session->close();
$session->delete();
$session->flush();
}

sub printContenuto(){
	
	print<<EOF;

	<form id="form-admin" action="admin.cgi" method="post">
	<!-- dentro tag form c'era onSubmit="" rimosso perchè non valido -->
	<fieldset>
		<legend>Effettua il Login</legend>
			<label id="label-pwd">Inserisci la password</label>
			<!-- rimosso variabile password da campo value(perchè era li?) -->
			<input type="password" name="pwd" id="pwd" value="password"/><br />
			<input type="submit" name="submit" class="submit" value="Login"/>
	</fieldset>
	</form>


EOF
	
	}		

# modifica

my $page = new CGI;
createSession();
my $password=getPwd();

#need $title $description $keywords
printHead('Accesso Admin - Biblioteca di Portobuffolè','Pagina accesso amministratore della biblioteca comunale di Portobuffolè','biblioteca Portobuffolè');

printBody("Admin");

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
	printContenuto();
	
	}
}

else{

	print "<h1>LOGGED</h1>";

}

