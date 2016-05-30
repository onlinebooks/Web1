#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

require 'functions.pl';

print "Content-type: text/html\n\n";

print<<EOF;
 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">


<head>
	<title>Progetto - admin</title>
	<meta http-equiv="Content-Type"content="text/html; charset=utf-8"/>
	<meta name="title" content="" />
	<meta name="description" content="accesso admin" />
	<meta name="keywords" content="LibreriaOnline" />
	<meta name="language" content="italian it" />
	<meta name="author" content="stefano" />
	<link rel="stylesheet" href="style.css" type="text/css" media="screen"/>
	<link rel="stylesheet" href="printstyle.css" type="text/css" media="print"/>	
	<link rel="stylesheet" href="mobilestyle.css" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)"/>		
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
</head>
<body>

EOF

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

# modifica

my $page = new CGI;
createSession();
my $password=getPwd();

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

	<form id="form-admin" action="admin.cgi" method="post">
	<!-- dentro tag form c'era onSubmit="" rimosso perchè non valido -->
	<fieldset>
		<legend>Effettua il Login</legend>
			<label id="label-pwd">Inserisci la password</label>
			<input type="password" name="pwd" id="pwd" value="$password"/><br />
			<input type="submit" name="submit" class="submit" value="Login"/>
	</fieldset>
	</form>


EOF
	
	}
}

else{

	print "<h1>LOGGED</h1>";

}

print<<EOF;

</body>
</html>

EOF
