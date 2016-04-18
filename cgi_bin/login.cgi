#!/usr/bin/perl

use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

print "Content-type: text/html\n\n";

print<<EOF;

	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<title>Login - Libronline</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
		<meta http-equiv="Content-Script-Type" content="text/javascript"/>
		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
		<meta name="title" content="" />
		<meta name="description" content="Home page del sito del progetto" />
		<meta name="keywords" content="libraria Padova" />
		<meta name="language" content="italian it" />
		<meta name="author" content="root" />
		<link href="style.css" rel="stylesheet" type="text/css" media="screen"/>
		<link rel="stylesheet" href="printstyle.css" type="text/css" media="print"/>	
		<link rel="stylesheet" href="mobilestyle.css" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)"/>
		<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
		<link href="https://fonts.googleapis.com/css?family=Fredoka+One%7cShadows+Into+Light+Two%7cCherry+Cream+Soda%7cCinzel+Decorative" rel="stylesheet" type="text/css" />
		<script type="text/javascript" src="javascript/check_login.js"></script>
	</head>
	<body>

		<div id="header">
			<span id="logo"></span>
			<h1> Libronline</h1>
			<h2> il tuo libro a portata di mano ovunque sei</h2>
		</div>
		<div id="main">
			<div id="menu">
				<ul>
					<li><a href="index.html" tabindex="0">Home</a></li>
					<li><a href="libri.html" tabindex="1">Libri</a></li>
					<li><a href="contatti.html" tabindex="2">Contatti</a></li>	
					<li><a href="registrazione.html" tabindex="3">Registrati</a></li>
					<li>Entra</li>
				</ul>
			</div>
			<div id="contenuto">
			<div id="path">
				Ti trovi in: <a href="index.html" xml:lang="en">Home</a> » Entra
			</div>
EOF
			
sub createSession() {
		$session = new CGI::Session();
		$session->param('pwd', $password);
}


sub getPwd() {
	$session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
		}	
 	else {
		my $pwd = $session->param('pwd');
		return $pwd;
		}
}

sub destroySession() {
$session = CGI::Session->load() or die $!;
$SID = $session->id();
$session->close();
$session->delete();
$session->flush();
}		

# modifica

$page = new CGI;
createSession();
$password=getPwd();

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

<div id="login">
				<h1>Accedi:</h1>
					<form action="" method="post" onsubmit="check_login()">
						<p><span class="capo"> Username: <input name="username" title="username" type="text" id="username"/></span>
						<span class="capo"> Password: <input name="password" title="password" type="password" id="password"/></span>
						<input type="submit" title="login" value="Login" name="Login"/>
						<input type="reset" title="annulla" value="annulla" name="annulla"/></p>
					</form>
			</div>
			</div>
		</div>
		<div id="footer">
		via ugo bassi libreria libronline
		</div>
	</body>
	</html>
EOF
	
